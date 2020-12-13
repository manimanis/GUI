# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_image = QtWidgets.QLabel(self.centralwidget)
        self.lbl_image.setText("")
        self.lbl_image.setPixmap(QtGui.QPixmap(":/images/password.png"))
        self.lbl_image.setScaledContents(False)
        self.lbl_image.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_image.setObjectName("lbl_image")
        self.verticalLayout_2.addWidget(self.lbl_image)
        self.lbl_passwd = QtWidgets.QLabel(self.centralwidget)
        self.lbl_passwd.setStyleSheet("text-align: center;\n"
"font-size: 40px;")
        self.lbl_passwd.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_passwd.setObjectName("lbl_passwd")
        self.verticalLayout_2.addWidget(self.lbl_passwd)
        self.lbl_copied = QtWidgets.QLabel(self.centralwidget)
        self.lbl_copied.setStyleSheet("color: rgb(78, 154, 6);")
        self.lbl_copied.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_copied.setObjectName("lbl_copied")
        self.verticalLayout_2.addWidget(self.lbl_copied)
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setStyleSheet("font-size: 20pt;\n"
"color: rgb(32, 74, 135);\n"
"padding: 10px;")
        self.btn_generate.setObjectName("btn_generate")
        self.verticalLayout_2.addWidget(self.btn_generate)
        self.btn_copy = QtWidgets.QPushButton(self.centralwidget)
        self.btn_copy.setStyleSheet("color: rgb(164, 0, 0);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(204, 0, 0);\n"
"background-color: rgb(238, 238, 236);\n"
"padding: 5px;")
        self.btn_copy.setObjectName("btn_copy")
        self.verticalLayout_2.addWidget(self.btn_copy)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.lbl_passwd.setText(_translate("MainWindow", "..."))
        self.lbl_copied.setText(_translate("MainWindow", "copied"))
        self.btn_generate.setText(_translate("MainWindow", "Générer un mot de passe"))
        self.btn_copy.setText(_translate("MainWindow", "Copier"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
