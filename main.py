import sys
import re as regex

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

selectedFiles = None

def select_function_file():
    global selectedFiles
    selected_function_file = QFileDialog.getOpenFileNames(filter="Minecraft Function Files (*.mcfunction)")
    selectedFiles = selected_function_file[:-1][0]
    window.function_path_text.setText(' '.join(selectedFiles))

def modify_function():
    for file in selectedFiles:
        # Get the lines in the file
        with open(file, "r") as function:
            lines = function.readlines()

        with open(file, "w") as function:
            whole_file = []
            # Iterate through each line in the file
            for line in lines:
                modified_line = []  # Used for rebuilding the line

                # Split the line up and iterate through each element
                split_line = line.split()
                for index, value in enumerate(split_line):
                    if value == "positioned":
                        if split_line[index + 1] == "~":
                            modified_line.append(value)
                        else:
                            x_value = float(split_line[index + 1])
                            y_value = float(split_line[index + 2])
                            z_value = float(split_line[index + 3])
                            if x_value.is_integer():
                                x_value = int(x_value)
                            if y_value.is_integer():
                                y_value = int(y_value)
                            if z_value.is_integer():
                                z_value = int(z_value)

                            x_value += window.XOffset.value()
                            y_value += window.YOffset.value()
                            z_value += window.ZOffset.value()

                            del split_line[index:index + 3]
                            modified_line.append(f"positioned {x_value} {y_value} {z_value}")
                
                    elif value == "if":
                        if split_line[index + 1] == "block":
                            if split_line[index + 2] == "~":
                                modified_line.append(value)
                            else:
                                x_value = float(split_line[index + 2])
                                y_value = float(split_line[index + 3])
                                z_value = float(split_line[index + 4])
                                if x_value.is_integer():
                                    x_value = int(x_value)
                                if y_value.is_integer():
                                    y_value = int(y_value)
                                if z_value.is_integer():
                                    z_value = int(z_value)

                                x_value += window.XOffset.value()
                                y_value += window.YOffset.value()
                                z_value += window.ZOffset.value()

                                del split_line[index:index + 4]
                                modified_line.append(f"if block {x_value} {y_value} {z_value}")
                        else:
                            modified_line.append(value)
     
                    elif value == "unless":
                        if split_line[index + 1] == "block":
                            if split_line[index + 2] == "~":
                                modified_line.append(value)
                            else:
                                x_value = float(split_line[index + 2])
                                y_value = float(split_line[index + 3])
                                z_value = float(split_line[index + 4])
                                if x_value.is_integer():
                                    x_value = int(x_value)
                                if y_value.is_integer():
                                    y_value = int(y_value)
                                if z_value.is_integer():
                                    z_value = int(z_value)

                                x_value += window.XOffset.value()
                                y_value += window.YOffset.value()
                                z_value += window.ZOffset.value()

                                del split_line[index:index + 4]
                                modified_line.append(f"unless block {x_value} {y_value} {z_value}")
                        else:
                            modified_line.append(value)
                    elif value == "summon":
                        if split_line[index + 2] == "~":
                            modified_line.append(value)
                        else:
                            id = split_line[index + 1]
                            x_value = float(split_line[index + 2])
                            y_value = float(split_line[index + 3])
                            z_value = float(split_line[index + 4])
                            if x_value.is_integer():
                                x_value = int(x_value)
                            if y_value.is_integer():
                                y_value = int(y_value)
                            if z_value.is_integer():
                                z_value = int(z_value)

                            x_value += window.XOffset.value()
                            y_value += window.YOffset.value()
                            z_value += window.ZOffset.value()

                            del split_line[index:index + 4]
                            modified_line.append(f"summon {id} {x_value} {y_value} {z_value}")

                    elif value == "teleport":
                        if split_line[index + 2] == "~":
                            modified_line.append(value)
                        else:
                            entity = split_line[index + 1]
                            x_value = float(split_line[index + 2])
                            y_value = float(split_line[index + 3])
                            z_value = float(split_line[index + 4])
                            if x_value.is_integer():
                                x_value = int(x_value)
                            if y_value.is_integer():
                                y_value = int(y_value)
                            if z_value.is_integer():
                                z_value = int(z_value)

                            x_value += window.XOffset.value()
                            y_value += window.YOffset.value()
                            z_value += window.ZOffset.value()

                            del split_line[index:index + 4]
                            modified_line.append(f"teleport {entity} {x_value} {y_value} {z_value}")

                    elif value == "setblock":
                        if split_line[index + 1] == "~":
                            modified_line.append(value)
                        else:
                            x_value = float(split_line[index + 1])
                            y_value = float(split_line[index + 2])
                            z_value = float(split_line[index + 3])
                            if x_value.is_integer():
                                x_value = int(x_value)
                            if y_value.is_integer():
                                y_value = int(y_value)
                            if z_value.is_integer():
                                z_value = int(z_value)

                            x_value += window.XOffset.value()
                            y_value += window.YOffset.value()
                            z_value += window.ZOffset.value()

                            del split_line[index:index + 3]
                            modified_line.append(f"setblock {x_value} {y_value} {z_value}")

                    elif value == "data":
                        if split_line[index + 2] == "block":
                            if split_line[index + 3] == "~":
                                modified_line.append(value)
                            else:
                                action = split_line[index + 1]
                                x_value = float(split_line[index + 3])
                                y_value = float(split_line[index + 4])
                                z_value = float(split_line[index + 5])
                                if x_value.is_integer():
                                    x_value = int(x_value)
                                if y_value.is_integer():
                                    y_value = int(y_value)
                                if z_value.is_integer():
                                    z_value = int(z_value)

                                x_value += window.XOffset.value()
                                y_value += window.YOffset.value()
                                z_value += window.ZOffset.value()

                                del split_line[index:index + 5]
                                modified_line.append(f"data {action} block {x_value} {y_value} {z_value}")
                        else: 
                            modified_line.append(value)
                    else: 
                        modified_line.append(value)
                whole_file.append(' '.join(modified_line))
                function.write('\n'.join(whole_file))
        
        offset_dict = {
            'x': window.XOffset.value(),
            'y': window.YOffset.value(),
            'z': window.ZOffset.value()
        }

        def add_offset(match):
            start, dim, mid, value = match.group(1, 2, 3, 4)
            value = float(value)
            if value.is_integer():
                value = int(value)
            return f'{start}{dim}{mid}{value + offset_dict[dim]}'

        pattern = r'([\[,]\s*)(x|y|z)(\s*\=\s*)(-?(\d*\.?\d+))'
        function = regex.sub(pattern, add_offset, open(file, "r").read())

        with open(file, "w") as _:
            _.write(function)
    print("Finished building")
    
window.XOffset.setRange(-2147483648, 2147483647)
window.YOffset.setRange(-2147483648, 2147483647)
window.ZOffset.setRange(-2147483648, 2147483647)
window.change_function_path.clicked.connect(select_function_file)
window.modify_function.clicked.connect(modify_function)

# Show the window
window.show()

# Exit the program if the GUI is closed
sys.exit(app.exec_())
