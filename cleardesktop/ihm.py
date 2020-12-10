# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ihm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 230)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_select_folder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_select_folder.setStyleSheet("font-size: 14pt;")
        self.btn_select_folder.setObjectName("btn_select_folder")
        self.gridLayout_2.addWidget(self.btn_select_folder, 0, 2, 1, 1)
        self.lbl_folder = QtWidgets.QLabel(self.centralwidget)
        self.lbl_folder.setStyleSheet("font-weight: bolder;\n"
                                      "font-size: 14pt;")
        self.lbl_folder.setObjectName("lbl_folder")
        self.gridLayout_2.addWidget(self.lbl_folder, 0, 0, 1, 1)
        self.txt_folder = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_folder.setStyleSheet("font-size: 14pt;")
        self.txt_folder.setObjectName("txt_folder")
        self.gridLayout_2.addWidget(self.txt_folder, 0, 1, 1, 1)
        self.btn_clean = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clean.setStyleSheet("font-size: 36pt;\n"
                                     "border-radius: 0.25em;\n"
                                     "background-color: rgb(170, 0, 0);\n"
                                     "color: #fff;\n"
                                     "padding: 0.25em;")
        self.btn_clean.setObjectName("btn_clean")
        self.gridLayout_2.addWidget(self.btn_clean, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Desktop Cleaner"))
        self.btn_select_folder.setText(
            _translate("MainWindow", "Sélectionner..."))
        self.lbl_folder.setText(_translate("MainWindow", "Dossier"))
        self.btn_clean.setText(_translate("MainWindow", "Clean..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
