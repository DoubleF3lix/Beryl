import sys
import subprocess

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import QFile

uiFile = QFile("interface.ui")
app = QApplication(sys.argv)
uiFile.open(QFile.ReadOnly)
loader = QUiLoader()
window = loader.load(uiFile)
uiFile.close()


def select_function_file():
    selected_function_file = QFileDialog.getOpenFileNames(filter="Minecraft Function Files (*.mcfunction)")
    function_path = ' '.join(selected_function_file[0])
    window.function_path_text.setText(function_path)


def modify_function():
    # Get the lines in the file
    with open(window.function_path_text.text(), "r") as function:
        lines = function.readlines()

    with open(window.function_path_text.text(), "w") as function:
        whole_file = []
        # Iterate through each line in the file
        for line in lines:
            modified_line = []  # Used for rebuilding the line

            # Split the line up and iterate through each element
            split_line = line.split()
            for index, value in enumerate(split_line):
                if value == "positioned":
                    x_value = int(split_line[index + 1])
                    y_value = int(split_line[index + 2])
                    z_value = int(split_line[index + 3])

                    x_value += window.XOffset.value()
                    y_value += window.YOffset.value()
                    z_value += window.ZOffset.value()

                    del split_line[index:index + 3]
                    modified_line.append(f"positioned {x_value} {y_value} {z_value}")
                else:
                    modified_line.append(value)
            whole_file.append(' '.join(modified_line))
        function.write('\n'.join(whole_file))

    print("Finished building")


subprocess.check_call([sys.executable, "-m", "pip", "install", "PySide2"])
window.XOffset.setRange(-2147483648, 2147483647)
window.YOffset.setRange(-2147483648, 2147483647)
window.ZOffset.setRange(-2147483648, 2147483647)
window.change_function_path.clicked.connect(select_function_file)
window.modify_function.clicked.connect(modify_function)

# Show the window
window.show()

# Exit the program if the GUI is closed
sys.exit(app.exec_())
