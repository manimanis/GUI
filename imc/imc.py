# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imc.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_hauteur = QtWidgets.QLabel(self.centralwidget)
        self.lbl_hauteur.setObjectName("lbl_hauteur")
        self.gridLayout_2.addWidget(self.lbl_hauteur, 2, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 4)
        self.lbl_imc_intro = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imc_intro.setTextFormat(QtCore.Qt.RichText)
        self.lbl_imc_intro.setWordWrap(True)
        self.lbl_imc_intro.setObjectName("lbl_imc_intro")
        self.gridLayout_2.addWidget(self.lbl_imc_intro, 5, 0, 1, 4)
        self.txt_masse = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_masse.setObjectName("txt_masse")
        self.gridLayout_2.addWidget(self.txt_masse, 2, 1, 1, 1)
        self.lbl_imc_val = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lbl_imc_val.setFont(font)
        self.lbl_imc_val.setStyleSheet("color: rgb(164, 0, 0);")
        self.lbl_imc_val.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_imc_val.setObjectName("lbl_imc_val")
        self.gridLayout_2.addWidget(self.lbl_imc_val, 3, 0, 1, 4)
        self.txt_hauteur = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_hauteur.setObjectName("txt_hauteur")
        self.gridLayout_2.addWidget(self.txt_hauteur, 2, 3, 1, 1)
        self.lbl_titre = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_titre.setFont(font)
        self.lbl_titre.setStyleSheet("color: rgb(78, 154, 6);")
        self.lbl_titre.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titre.setObjectName("lbl_titre")
        self.gridLayout_2.addWidget(self.lbl_titre, 0, 0, 1, 4)
        self.lbl_imc_image = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imc_image.setText("")
        self.lbl_imc_image.setPixmap(QtGui.QPixmap(":/imc/imc.jpg"))
        self.lbl_imc_image.setObjectName("lbl_imc_image")
        self.gridLayout_2.addWidget(self.lbl_imc_image, 6, 0, 1, 4)
        self.lbl_masse = QtWidgets.QLabel(self.centralwidget)
        self.lbl_masse.setObjectName("lbl_masse")
        self.gridLayout_2.addWidget(self.lbl_masse, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_ob_maigreur = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ob_maigreur.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.lbl_ob_maigreur.setText("")
        self.lbl_ob_maigreur.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ob_maigreur.setObjectName("lbl_ob_maigreur")
        self.horizontalLayout.addWidget(self.lbl_ob_maigreur)
        self.lbl_ob_normale = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ob_normale.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.lbl_ob_normale.setText("")
        self.lbl_ob_normale.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ob_normale.setObjectName("lbl_ob_normale")
        self.horizontalLayout.addWidget(self.lbl_ob_normale)
        self.lbl_ob_surpoids = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ob_surpoids.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.lbl_ob_surpoids.setText("")
        self.lbl_ob_surpoids.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ob_surpoids.setObjectName("lbl_ob_surpoids")
        self.horizontalLayout.addWidget(self.lbl_ob_surpoids)
        self.lbl_ob_modree = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ob_modree.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.lbl_ob_modree.setText("")
        self.lbl_ob_modree.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ob_modree.setObjectName("lbl_ob_modree")
        self.horizontalLayout.addWidget(self.lbl_ob_modree)
        self.lbl_ob_severe = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ob_severe.setStyleSheet("background-color: rgb(206, 92, 0);")
        self.lbl_ob_severe.setText("")
        self.lbl_ob_severe.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ob_severe.setObjectName("lbl_ob_severe")
        self.horizontalLayout.addWidget(self.lbl_ob_severe)
        self.lbl_ob_morbide = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ob_morbide.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.lbl_ob_morbide.setText("")
        self.lbl_ob_morbide.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ob_morbide.setObjectName("lbl_ob_morbide")
        self.horizontalLayout.addWidget(self.lbl_ob_morbide)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 7, 0, 1, 4)
        self.gridLayout_2.setColumnStretch(1, 100)
        self.gridLayout_2.setColumnStretch(3, 100)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Indice de masse corporelle"))
        self.lbl_hauteur.setText(_translate("MainWindow", "Hauteur (m)"))
        self.lbl_imc_intro.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#204a87;\">L\'indice de masse corporelle ou IMC permet de connaître son poids idéal, autrement dit, s\'il est adapté à votre taille. </span></p></body></html>"))
        self.lbl_imc_val.setText(_translate("MainWindow", "..."))
        self.lbl_titre.setText(_translate("MainWindow", "Calcul de l\'indice de masse corporelle"))
        self.lbl_masse.setText(_translate("MainWindow", "Masse (kg)"))
import ressources_rc


if __name__ == "__main__":
    def get_masse():
        try:
            return int(ui.txt_masse.text())
        except Exception:
            return 0

    def get_hauteur():
        try:
            return float(ui.txt_hauteur.text())
        except Exception:
            return 0
    
    def calc_imc():
        m, h = get_masse(), get_hauteur()
        if m == 0 or h == 0:
            imc = 0
        else:
            imc = m / (h*h)
        display_imc(imc)

    def calc_categorie(imc):
        for i in range(5, -1, -1):
            if imc >= ob_cat_val[i]:
                print(ob_cat_val[i])
                return i
        return -1

    def display_imc(imc):
        if imc == 0:
            imc_txt = "..."
        else:
            imc_txt = f"{imc:3.1f}"
        cat_ob = calc_categorie(imc)
        ui.lbl_imc_val.setText(imc_txt)
        for i in range(6):
            if cat_ob == i:
                ob_cat_lbl[i].setStyleSheet(ob_cat_style[i])
            else:
                ob_cat_lbl[i].setStyleSheet(None)

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.txt_masse.textChanged.connect(calc_imc)
    ui.txt_hauteur.textChanged.connect(calc_imc)
    ob_cat_lbl = [ui.lbl_ob_maigreur, ui.lbl_ob_normale, ui.lbl_ob_surpoids, ui.lbl_ob_modree, ui.lbl_ob_severe, ui.lbl_ob_morbide]
    ob_cat_val = [0.1, 18.5, 25.0, 30.0, 35.0, 40.0]
    ob_cat_style = [label.styleSheet() for label in ob_cat_lbl]
    MainWindow.show()
    sys.exit(app.exec_())