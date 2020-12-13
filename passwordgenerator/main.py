from window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from generator import generate_password
from PyQt5.QtCore import QTimer
import sys


def generate():
    pwd = generate_password()
    ui.lbl_passwd.setText(pwd)


def copy_to_clipboard():
    global timer
    if timer is None:
        timer = QTimer()
        timer.timeout.connect(timeout)
    timer.start(1000)
    ui.lbl_copied.setVisible(True)
    cp = QtWidgets.QApplication.clipboard()
    cp.clear(mode=cp.Clipboard)
    cp.setText(ui.lbl_passwd.text(), mode=cp.Clipboard)


def timeout():
    ui.lbl_copied.setVisible(False)
    timer.stop()


# PP
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.lbl_copied.setVisible(False)
ui.btn_generate.clicked.connect(generate)
ui.btn_copy.clicked.connect(copy_to_clipboard)
timer = None
generate()
MainWindow.show()
sys.exit(app.exec_())