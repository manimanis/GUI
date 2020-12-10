from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from ihm import Ui_MainWindow
import sys
import os
import datetime
import shutil


def files_to_move(directory):
    files = []
    for file in os.listdir(directory):
        if not file.endswith('.lnk'):
            files.append(os.path.join(directory, file))
    return files


def select_folder():
    global directory
    directory = QtWidgets.QFileDialog.getExistingDirectory(
        MainWindow, "Select Directory")
    ui.txt_folder.setText(directory)


def clean_folder():
    global directory
    if (directory == ""
        or not os.path.exists(directory)
            or not os.path.isdir(directory)):
        QMessageBox.warning(MainWindow,
                            MainWindow.windowTitle(),
                            "Veuillez sélectionner le "
                            "bureau de Windows d'abord")
        return
    now = datetime.datetime.now()
    files = files_to_move(directory)
    
    garbage_folder = os.path.join(directory, 'Garbage_' + now.strftime("%Y-%m-%d_%H-%M-%S"))
    os.makedirs(garbage_folder)
    moved = []
    for file in files:
        try:
            shutil.move(file, garbage_folder)    
            moved.append(file)
        except Exception:
            pass
    
    with open(os.path.join(garbage_folder, 'fl.txt'), 'w', encoding='utf-8') as f:
        for file in moved:
            f.write(file + "\n")


# Main Program
directory = ""

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.btn_select_folder.clicked.connect(select_folder)
ui.btn_clean.clicked.connect(clean_folder)
MainWindow.show()
sys.exit(app.exec_())
