# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resistor.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_marron4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_marron4.setStyleSheet("background-color: rgb(143, 89, 2);\n"
"color: rgb(255, 255, 255);")
        self.btn_marron4.setObjectName("btn_marron4")
        self.gridLayout_2.addWidget(self.btn_marron4, 8, 4, 1, 1)
        self.lbl_leg2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_leg2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_leg2.setObjectName("lbl_leg2")
        self.gridLayout_2.addWidget(self.lbl_leg2, 4, 1, 1, 1)
        self.lbl_resistor_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_resistor_val.setStyleSheet("font-size: 32pt;\n"
"color: rgb(32, 74, 135);")
        self.lbl_resistor_val.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_resistor_val.setObjectName("lbl_resistor_val")
        self.gridLayout_2.addWidget(self.lbl_resistor_val, 0, 0, 1, 5)
        self.btn_violet4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_violet4.setStyleSheet("background-color: violet;\n"
"color: #333;")
        self.btn_violet4.setObjectName("btn_violet4")
        self.gridLayout_2.addWidget(self.btn_violet4, 15, 4, 1, 1)
        self.btn_argent4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_argent4.setStyleSheet("background-color: silver;\n"
"color: #333;")
        self.btn_argent4.setObjectName("btn_argent4")
        self.gridLayout_2.addWidget(self.btn_argent4, 20, 4, 1, 1)
        self.btn_orange1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_orange1.setStyleSheet("background-color: orange;\n"
"color: rgb(255, 255, 255);")
        self.btn_orange1.setObjectName("btn_orange1")
        self.gridLayout_2.addWidget(self.btn_orange1, 10, 1, 1, 1)
        self.btn_or3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_or3.setStyleSheet("background-color: gold;\n"
"color: #333;")
        self.btn_or3.setObjectName("btn_or3")
        self.gridLayout_2.addWidget(self.btn_or3, 19, 3, 1, 1)
        self.btn_blanc1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_blanc1.setStyleSheet("background-color: #fff;\n"
"color: #333;")
        self.btn_blanc1.setObjectName("btn_blanc1")
        self.gridLayout_2.addWidget(self.btn_blanc1, 17, 1, 1, 1)
        self.lbl_tolerance = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tolerance.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tolerance.setObjectName("lbl_tolerance")
        self.gridLayout_2.addWidget(self.lbl_tolerance, 3, 4, 2, 1)
        self.btn_bleu1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bleu1.setStyleSheet("background-color: blue;\n"
"color: #fff;")
        self.btn_bleu1.setObjectName("btn_bleu1")
        self.gridLayout_2.addWidget(self.btn_bleu1, 14, 1, 1, 1)
        self.btn_orange2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_orange2.setStyleSheet("background-color: orange;\n"
"color: rgb(255, 255, 255);")
        self.btn_orange2.setObjectName("btn_orange2")
        self.gridLayout_2.addWidget(self.btn_orange2, 10, 2, 1, 1)
        self.btn_noir2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_noir2.setStyleSheet("background-color: #000;\n"
"color: #fff;")
        self.btn_noir2.setObjectName("btn_noir2")
        self.gridLayout_2.addWidget(self.btn_noir2, 7, 2, 1, 1)
        self.btn_noir0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_noir0.setStyleSheet("background-color: #000;\n"
"color: #fff;")
        self.btn_noir0.setObjectName("btn_noir0")
        self.gridLayout_2.addWidget(self.btn_noir0, 7, 0, 1, 1)
        self.btn_gris1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gris1.setStyleSheet("background-color: lightgray;\n"
"color: #333;")
        self.btn_gris1.setObjectName("btn_gris1")
        self.gridLayout_2.addWidget(self.btn_gris1, 16, 1, 1, 1)
        self.lbl_leg1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_leg1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_leg1.setObjectName("lbl_leg1")
        self.gridLayout_2.addWidget(self.lbl_leg1, 4, 0, 1, 1)
        self.btn_violet3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_violet3.setStyleSheet("background-color: violet;\n"
"color: #333;")
        self.btn_violet3.setObjectName("btn_violet3")
        self.gridLayout_2.addWidget(self.btn_violet3, 15, 3, 1, 1)
        self.lbl_band1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_band1.setStyleSheet("font-size: 16pt;\n"
"color: rgb(164, 0, 0);")
        self.lbl_band1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_band1.setObjectName("lbl_band1")
        self.gridLayout_2.addWidget(self.lbl_band1, 5, 1, 1, 1)
        self.btn_violet2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_violet2.setStyleSheet("background-color: violet;\n"
"color: #333;")
        self.btn_violet2.setObjectName("btn_violet2")
        self.gridLayout_2.addWidget(self.btn_violet2, 15, 2, 1, 1)
        self.lbl_nbre_bands = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nbre_bands.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_nbre_bands.setObjectName("lbl_nbre_bands")
        self.gridLayout_2.addWidget(self.lbl_nbre_bands, 1, 0, 1, 2)
        self.btn_vert4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vert4.setStyleSheet("background-color: green;\n"
"color: #fff;")
        self.btn_vert4.setObjectName("btn_vert4")
        self.gridLayout_2.addWidget(self.btn_vert4, 13, 4, 1, 1)
        self.btn_vert2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vert2.setStyleSheet("background-color: green;\n"
"color: #fff;")
        self.btn_vert2.setObjectName("btn_vert2")
        self.gridLayout_2.addWidget(self.btn_vert2, 13, 2, 1, 1)
        self.btn_blanc2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_blanc2.setStyleSheet("background-color: #fff;\n"
"color: #333;")
        self.btn_blanc2.setObjectName("btn_blanc2")
        self.gridLayout_2.addWidget(self.btn_blanc2, 17, 2, 1, 1)
        self.btn_vert1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vert1.setStyleSheet("background-color: green;\n"
"color: #fff;")
        self.btn_vert1.setObjectName("btn_vert1")
        self.gridLayout_2.addWidget(self.btn_vert1, 13, 1, 1, 1)
        self.btn_vert0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vert0.setStyleSheet("background-color: green;\n"
"color: #fff;")
        self.btn_vert0.setObjectName("btn_vert0")
        self.gridLayout_2.addWidget(self.btn_vert0, 13, 0, 1, 1)
        self.btn_bleu2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bleu2.setStyleSheet("background-color: blue;\n"
"color: #fff;")
        self.btn_bleu2.setObjectName("btn_bleu2")
        self.gridLayout_2.addWidget(self.btn_bleu2, 14, 2, 1, 1)
        self.btn_gris3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gris3.setStyleSheet("background-color: lightgray;\n"
"color: #333;")
        self.btn_gris3.setObjectName("btn_gris3")
        self.gridLayout_2.addWidget(self.btn_gris3, 16, 3, 1, 1)
        self.btn_rouge0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rouge0.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_rouge0.setObjectName("btn_rouge0")
        self.gridLayout_2.addWidget(self.btn_rouge0, 9, 0, 1, 1)
        self.lbl_band4 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_band4.setStyleSheet("font-size: 16pt;\n"
"color: rgb(164, 0, 0);")
        self.lbl_band4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_band4.setObjectName("lbl_band4")
        self.gridLayout_2.addWidget(self.lbl_band4, 5, 4, 1, 1)
        self.btn_blanc0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_blanc0.setStyleSheet("background-color: #fff;\n"
"color: #333;")
        self.btn_blanc0.setObjectName("btn_blanc0")
        self.gridLayout_2.addWidget(self.btn_blanc0, 17, 0, 1, 1)
        self.btn_bleu4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bleu4.setStyleSheet("background-color: blue;\n"
"color: #fff;")
        self.btn_bleu4.setObjectName("btn_bleu4")
        self.gridLayout_2.addWidget(self.btn_bleu4, 14, 4, 1, 1)
        self.btn_jaune0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_jaune0.setStyleSheet("background-color: yellow;\n"
"color: #333;")
        self.btn_jaune0.setObjectName("btn_jaune0")
        self.gridLayout_2.addWidget(self.btn_jaune0, 12, 0, 1, 1)
        self.lbl_mul = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mul.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mul.setObjectName("lbl_mul")
        self.gridLayout_2.addWidget(self.lbl_mul, 3, 3, 2, 1)
        self.btn_jaune2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_jaune2.setStyleSheet("background-color: yellow;\n"
"color: #333;")
        self.btn_jaune2.setObjectName("btn_jaune2")
        self.gridLayout_2.addWidget(self.btn_jaune2, 12, 2, 1, 1)
        self.btn_rouge1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rouge1.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_rouge1.setObjectName("btn_rouge1")
        self.gridLayout_2.addWidget(self.btn_rouge1, 9, 1, 1, 1)
        self.btn_bleu3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bleu3.setStyleSheet("background-color: blue;\n"
"color: #fff;")
        self.btn_bleu3.setObjectName("btn_bleu3")
        self.gridLayout_2.addWidget(self.btn_bleu3, 14, 3, 1, 1)
        self.btn_noir1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_noir1.setStyleSheet("background-color: #000;\n"
"color: #fff;")
        self.btn_noir1.setObjectName("btn_noir1")
        self.gridLayout_2.addWidget(self.btn_noir1, 7, 1, 1, 1)
        self.btn_marron1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_marron1.setStyleSheet("background-color: rgb(143, 89, 2);\n"
"color: rgb(255, 255, 255);")
        self.btn_marron1.setObjectName("btn_marron1")
        self.gridLayout_2.addWidget(self.btn_marron1, 8, 1, 1, 1)
        self.btn_or4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_or4.setStyleSheet("background-color: gold;\n"
"color: #333;")
        self.btn_or4.setObjectName("btn_or4")
        self.gridLayout_2.addWidget(self.btn_or4, 19, 4, 1, 1)
        self.btn_marron0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_marron0.setStyleSheet("background-color: rgb(143, 89, 2);\n"
"color: rgb(255, 255, 255);")
        self.btn_marron0.setObjectName("btn_marron0")
        self.gridLayout_2.addWidget(self.btn_marron0, 8, 0, 1, 1)
        self.lbl_band2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_band2.setStyleSheet("font-size: 16pt;\n"
"color: rgb(164, 0, 0);")
        self.lbl_band2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_band2.setObjectName("lbl_band2")
        self.gridLayout_2.addWidget(self.lbl_band2, 5, 2, 1, 1)
        self.btn_gris2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gris2.setStyleSheet("background-color: lightgray;\n"
"color: #333;")
        self.btn_gris2.setObjectName("btn_gris2")
        self.gridLayout_2.addWidget(self.btn_gris2, 16, 2, 1, 1)
        self.btn_orange3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_orange3.setStyleSheet("background-color: orange;\n"
"color: rgb(255, 255, 255);")
        self.btn_orange3.setObjectName("btn_orange3")
        self.gridLayout_2.addWidget(self.btn_orange3, 10, 3, 1, 1)
        self.btn_violet1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_violet1.setStyleSheet("background-color: violet;\n"
"color: #333;")
        self.btn_violet1.setObjectName("btn_violet1")
        self.gridLayout_2.addWidget(self.btn_violet1, 15, 1, 1, 1)
        self.btn_noir3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_noir3.setStyleSheet("background-color: #000;\n"
"color: #fff;")
        self.btn_noir3.setObjectName("btn_noir3")
        self.gridLayout_2.addWidget(self.btn_noir3, 7, 3, 1, 1)
        self.btn_jaune3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_jaune3.setStyleSheet("background-color: yellow;\n"
"color: #333;")
        self.btn_jaune3.setObjectName("btn_jaune3")
        self.gridLayout_2.addWidget(self.btn_jaune3, 12, 3, 1, 1)
        self.btn_violet0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_violet0.setStyleSheet("background-color: violet;\n"
"color: #333;")
        self.btn_violet0.setObjectName("btn_violet0")
        self.gridLayout_2.addWidget(self.btn_violet0, 15, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rd_four_bands = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_four_bands.setChecked(True)
        self.rd_four_bands.setObjectName("rd_four_bands")
        self.horizontalLayout.addWidget(self.rd_four_bands)
        self.rd_five_bands = QtWidgets.QRadioButton(self.centralwidget)
        self.rd_five_bands.setObjectName("rd_five_bands")
        self.horizontalLayout.addWidget(self.rd_five_bands)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 2, 1, 2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 5)
        self.btn_gris0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gris0.setStyleSheet("background-color: lightgray;\n"
"color: #333;")
        self.btn_gris0.setObjectName("btn_gris0")
        self.gridLayout_2.addWidget(self.btn_gris0, 16, 0, 1, 1)
        self.lbl_chiffres_sig = QtWidgets.QLabel(self.centralwidget)
        self.lbl_chiffres_sig.setStyleSheet("border-bottom: #333 solid 2px;\n"
"")
        self.lbl_chiffres_sig.setMidLineWidth(2)
        self.lbl_chiffres_sig.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_chiffres_sig.setObjectName("lbl_chiffres_sig")
        self.gridLayout_2.addWidget(self.lbl_chiffres_sig, 3, 0, 1, 3)
        self.btn_orange0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_orange0.setStyleSheet("background-color: orange;\n"
"color: rgb(255, 255, 255);")
        self.btn_orange0.setObjectName("btn_orange0")
        self.gridLayout_2.addWidget(self.btn_orange0, 10, 0, 1, 1)
        self.btn_vert3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vert3.setStyleSheet("background-color: green;\n"
"color: #fff;")
        self.btn_vert3.setObjectName("btn_vert3")
        self.gridLayout_2.addWidget(self.btn_vert3, 13, 3, 1, 1)
        self.btn_rouge4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rouge4.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_rouge4.setObjectName("btn_rouge4")
        self.gridLayout_2.addWidget(self.btn_rouge4, 9, 4, 1, 1)
        self.lbl_band0 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_band0.setStyleSheet("font-size: 16pt;\n"
"color: rgb(164, 0, 0);")
        self.lbl_band0.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_band0.setObjectName("lbl_band0")
        self.gridLayout_2.addWidget(self.lbl_band0, 5, 0, 1, 1)
        self.btn_bleu0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bleu0.setStyleSheet("background-color: blue;\n"
"color: #fff;")
        self.btn_bleu0.setObjectName("btn_bleu0")
        self.gridLayout_2.addWidget(self.btn_bleu0, 14, 0, 1, 1)
        self.btn_rouge3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rouge3.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_rouge3.setObjectName("btn_rouge3")
        self.gridLayout_2.addWidget(self.btn_rouge3, 9, 3, 1, 1)
        self.lbl_band3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_band3.setStyleSheet("font-size: 16pt;\n"
"color: rgb(164, 0, 0);")
        self.lbl_band3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_band3.setObjectName("lbl_band3")
        self.gridLayout_2.addWidget(self.lbl_band3, 5, 3, 1, 1)
        self.lbl_leg3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_leg3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_leg3.setObjectName("lbl_leg3")
        self.gridLayout_2.addWidget(self.lbl_leg3, 4, 2, 1, 1)
        self.btn_jaune1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_jaune1.setStyleSheet("background-color: yellow;\n"
"color: #333;")
        self.btn_jaune1.setObjectName("btn_jaune1")
        self.gridLayout_2.addWidget(self.btn_jaune1, 12, 1, 1, 1)
        self.btn_blanc3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_blanc3.setStyleSheet("background-color: #fff;\n"
"color: #333;")
        self.btn_blanc3.setObjectName("btn_blanc3")
        self.gridLayout_2.addWidget(self.btn_blanc3, 17, 3, 1, 1)
        self.btn_marron2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_marron2.setStyleSheet("background-color: rgb(143, 89, 2);\n"
"color: rgb(255, 255, 255);")
        self.btn_marron2.setObjectName("btn_marron2")
        self.gridLayout_2.addWidget(self.btn_marron2, 8, 2, 1, 1)
        self.btn_rouge2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rouge2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_rouge2.setObjectName("btn_rouge2")
        self.gridLayout_2.addWidget(self.btn_rouge2, 9, 2, 1, 1)
        self.btn_argent3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_argent3.setStyleSheet("background-color: silver;\n"
"color: #333;")
        self.btn_argent3.setObjectName("btn_argent3")
        self.gridLayout_2.addWidget(self.btn_argent3, 20, 3, 1, 1)
        self.btn_marron3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_marron3.setStyleSheet("background-color: rgb(143, 89, 2);\n"
"color: rgb(255, 255, 255);")
        self.btn_marron3.setObjectName("btn_marron3")
        self.gridLayout_2.addWidget(self.btn_marron3, 8, 3, 1, 1)
        self.btn_gris4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gris4.setStyleSheet("background-color: lightgray;\n"
"color: #333;")
        self.btn_gris4.setObjectName("btn_gris4")
        self.gridLayout_2.addWidget(self.btn_gris4, 16, 4, 1, 1)
        self.lbl_col_band0 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_col_band0.setText("")
        self.lbl_col_band0.setObjectName("lbl_col_band0")
        self.gridLayout_2.addWidget(self.lbl_col_band0, 6, 0, 1, 1)
        self.lbl_col_band1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_col_band1.setText("")
        self.lbl_col_band1.setObjectName("lbl_col_band1")
        self.gridLayout_2.addWidget(self.lbl_col_band1, 6, 1, 1, 1)
        self.lbl_col_band2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_col_band2.setText("")
        self.lbl_col_band2.setObjectName("lbl_col_band2")
        self.gridLayout_2.addWidget(self.lbl_col_band2, 6, 2, 1, 1)
        self.lbl_col_band3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_col_band3.setText("")
        self.lbl_col_band3.setObjectName("lbl_col_band3")
        self.gridLayout_2.addWidget(self.lbl_col_band3, 6, 3, 1, 1)
        self.lbl_col_band4 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_col_band4.setText("")
        self.lbl_col_band4.setObjectName("lbl_col_band4")
        self.gridLayout_2.addWidget(self.lbl_col_band4, 6, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resistor"))
        self.btn_marron4.setText(_translate("MainWindow", "Marron"))
        self.lbl_leg2.setText(_translate("MainWindow", "<html><head/><body><p>2<span style=\" vertical-align:super;\">ème</span> Bande</p></body></html>"))
        self.lbl_resistor_val.setText(_translate("MainWindow", "Valeur du résistor"))
        self.btn_violet4.setText(_translate("MainWindow", "Violet"))
        self.btn_argent4.setText(_translate("MainWindow", "Argent"))
        self.btn_orange1.setText(_translate("MainWindow", "Orange"))
        self.btn_or3.setText(_translate("MainWindow", "Or"))
        self.btn_blanc1.setText(_translate("MainWindow", "Blanc"))
        self.lbl_tolerance.setText(_translate("MainWindow", "Tolérance"))
        self.btn_bleu1.setText(_translate("MainWindow", "Bleu"))
        self.btn_orange2.setText(_translate("MainWindow", "Orange"))
        self.btn_noir2.setText(_translate("MainWindow", "Noir"))
        self.btn_noir0.setText(_translate("MainWindow", "Noir"))
        self.btn_gris1.setText(_translate("MainWindow", "Gris"))
        self.lbl_leg1.setText(_translate("MainWindow", "1<sup>ère</sup> Bande"))
        self.btn_violet3.setText(_translate("MainWindow", "Violet"))
        self.lbl_band1.setText(_translate("MainWindow", "..."))
        self.btn_violet2.setText(_translate("MainWindow", "Violet"))
        self.lbl_nbre_bands.setText(_translate("MainWindow", "Nombre de bandes"))
        self.btn_vert4.setText(_translate("MainWindow", "Vert"))
        self.btn_vert2.setText(_translate("MainWindow", "Vert"))
        self.btn_blanc2.setText(_translate("MainWindow", "Blanc"))
        self.btn_vert1.setText(_translate("MainWindow", "Vert"))
        self.btn_vert0.setText(_translate("MainWindow", "Vert"))
        self.btn_bleu2.setText(_translate("MainWindow", "Bleu"))
        self.btn_gris3.setText(_translate("MainWindow", "Gris"))
        self.btn_rouge0.setText(_translate("MainWindow", "Rouge"))
        self.lbl_band4.setText(_translate("MainWindow", "..."))
        self.btn_blanc0.setText(_translate("MainWindow", "Blanc"))
        self.btn_bleu4.setText(_translate("MainWindow", "Bleu"))
        self.btn_jaune0.setText(_translate("MainWindow", "Jaune"))
        self.lbl_mul.setText(_translate("MainWindow", "Multiplicateur"))
        self.btn_jaune2.setText(_translate("MainWindow", "Jaune"))
        self.btn_rouge1.setText(_translate("MainWindow", "Rouge"))
        self.btn_bleu3.setText(_translate("MainWindow", "Bleu"))
        self.btn_noir1.setText(_translate("MainWindow", "Noir"))
        self.btn_marron1.setText(_translate("MainWindow", "Marron"))
        self.btn_or4.setText(_translate("MainWindow", "Or"))
        self.btn_marron0.setText(_translate("MainWindow", "Marron"))
        self.lbl_band2.setText(_translate("MainWindow", "..."))
        self.btn_gris2.setText(_translate("MainWindow", "Gris"))
        self.btn_orange3.setText(_translate("MainWindow", "Orange"))
        self.btn_violet1.setText(_translate("MainWindow", "Violet"))
        self.btn_noir3.setText(_translate("MainWindow", "Noir"))
        self.btn_jaune3.setText(_translate("MainWindow", "Jaune"))
        self.btn_violet0.setText(_translate("MainWindow", "Violet"))
        self.rd_four_bands.setText(_translate("MainWindow", "4 Bandes"))
        self.rd_five_bands.setText(_translate("MainWindow", "5 Bandes"))
        self.btn_gris0.setText(_translate("MainWindow", "Gris"))
        self.lbl_chiffres_sig.setText(_translate("MainWindow", "Chiffres significatifs"))
        self.btn_orange0.setText(_translate("MainWindow", "Orange"))
        self.btn_vert3.setText(_translate("MainWindow", "Vert"))
        self.btn_rouge4.setText(_translate("MainWindow", "Rouge"))
        self.lbl_band0.setText(_translate("MainWindow", "..."))
        self.btn_bleu0.setText(_translate("MainWindow", "Bleu"))
        self.btn_rouge3.setText(_translate("MainWindow", "Rouge"))
        self.lbl_band3.setText(_translate("MainWindow", "..."))
        self.lbl_leg3.setText(_translate("MainWindow", "3<sup>ème</sup> Bande"))
        self.btn_jaune1.setText(_translate("MainWindow", "Jaune"))
        self.btn_blanc3.setText(_translate("MainWindow", "Blanc"))
        self.btn_marron2.setText(_translate("MainWindow", "Marron"))
        self.btn_rouge2.setText(_translate("MainWindow", "Rouge"))
        self.btn_argent3.setText(_translate("MainWindow", "Argent"))
        self.btn_marron3.setText(_translate("MainWindow", "Marron"))
        self.btn_gris4.setText(_translate("MainWindow", "Gris"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
