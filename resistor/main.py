from PyQt5 import QtCore, QtGui, QtWidgets
from resistor import Ui_MainWindow
import sys

couleurs = {
    'argent': -2,
    'or': -1,
    'noir': 0,
    'marron': 1,
    'rouge': 2,
    'orange': 3,
    'jaune': 4,
    'vert': 5,
    'bleu': 6,
    'violet': 7,
    'gris': 8,
    'blanc': 9
}

tolerance = {
    'argent': 10,
    'or': 5,
    'noir': 0,
    'marron': 1,
    'rouge': 2,
    'vert': 0.5,
    'bleu': 0.25,
    'violet': 0.10,
    'gris': 0.05,
}


def handler(bouton, b_idx, b_color):
    global selection
    def set_digit():
        if b_idx <= 2:
            lbl_bands[b_idx].setText(str(couleurs[b_color]))
            selection[b_idx] = couleurs[b_color]
        elif b_idx == 3:
            lbl_bands[b_idx].setText(f"10<sup>{couleurs[b_color]}</sup>")
            selection[b_idx] = couleurs[b_color]
        elif b_idx == 4:
            lbl_bands[b_idx].setText(f"±{tolerance[b_color]}%")
        col_bands[b_idx].setStyleSheet(bouton.styleSheet())
        show_resistor_value()
        
    return set_digit


def set_bands(nbands):
    global resistor_bands, selection
    resistor_bands = nbands
    if nbands == 4:
        selection[2] = 0
    else:
        selection[2] = -10
    for band in band2.values():
        band.setVisible(nbands == 5)
    ui.lbl_leg3.setVisible(nbands == 5)
    ui.lbl_band2.setVisible(nbands == 5)
    show_resistor_value()


def calc_resistor_value():
    global resistor_bands, selection
    if -10 in selection:
        return -10
    val = selection[0] * 10 + selection[1]
    if resistor_bands == 5:
        val = val * 10 +selection[2]
    val = val * 10**selection[3]
    return val


def show_resistor_value():
    res = calc_resistor_value()
    if res != -10:
        ui.lbl_resistor_val.setText(f"{res} Ω")
    else:
        ui.lbl_resistor_val.setText('Valeur du résistor')

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
band0 = {
    'noir': ui.btn_noir0, 
    'marron': ui.btn_marron0,
    'rouge': ui.btn_rouge0,
    'orange': ui.btn_orange0,
    'jaune': ui.btn_jaune0,
    'vert': ui.btn_vert0,
    'bleu': ui.btn_bleu0,
    'violet': ui.btn_violet0,
    'gris': ui.btn_gris0,
    'blanc': ui.btn_blanc0
}
band1 = {
    'noir': ui.btn_noir1, 
    'marron': ui.btn_marron1,
    'rouge': ui.btn_rouge1,
    'orange': ui.btn_orange1,
    'jaune': ui.btn_jaune1,
    'vert': ui.btn_vert1,
    'bleu': ui.btn_bleu1,
    'violet': ui.btn_violet1,
    'gris': ui.btn_gris1,
    'blanc': ui.btn_blanc1
}
band2 = {
    'noir': ui.btn_noir2, 
    'marron': ui.btn_marron2,
    'rouge': ui.btn_rouge2,
    'orange': ui.btn_orange2,
    'jaune': ui.btn_jaune2,
    'vert': ui.btn_vert2,
    'bleu': ui.btn_bleu2,
    'violet': ui.btn_violet2,
    'gris': ui.btn_gris2,
    'blanc': ui.btn_blanc2
}
band3 = {
    'noir': ui.btn_noir3, 
    'marron': ui.btn_marron3,
    'rouge': ui.btn_rouge3,
    'orange': ui.btn_orange3,
    'jaune': ui.btn_jaune3,
    'vert': ui.btn_vert3,
    'bleu': ui.btn_bleu3,
    'violet': ui.btn_violet3,
    'gris': ui.btn_gris3,
    'blanc': ui.btn_blanc3,
    'or': ui.btn_or3,
    'argent': ui.btn_argent3
}
band4 = {
    'marron': ui.btn_marron4,
    'rouge': ui.btn_rouge4,
    'vert': ui.btn_vert4,
    'bleu': ui.btn_bleu4,
    'violet': ui.btn_violet4,
    'gris': ui.btn_gris4,
    'or': ui.btn_or4,
    'argent': ui.btn_argent4
}
bands = [band0, band1, band2, band3, band4]
lbl_bands = [ui.lbl_band0, ui.lbl_band1, ui.lbl_band2, ui.lbl_band3, ui.lbl_band4]
col_bands = [ui.lbl_col_band0, ui.lbl_col_band1, ui.lbl_col_band2, ui.lbl_col_band3, ui.lbl_col_band4]
selection = [-10] * 4
resistor_bands = 4
for index, band in enumerate(bands):
    for color, button in band.items():
        button.clicked.connect(handler(button, index, color))
ui.rd_four_bands.clicked.connect(lambda: set_bands(4))
ui.rd_five_bands.clicked.connect(lambda: set_bands(5))
set_bands(resistor_bands)
MainWindow.show()
sys.exit(app.exec_())