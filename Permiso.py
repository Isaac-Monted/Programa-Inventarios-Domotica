import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox, QSystemTrayIcon
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5 import QtCore, QtWidgets, uic 
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator, QIcon
from  InterfazPrincipal import *
from BolsaValores import *

import math
import keyboard

import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Permiso(QDialog):
    def __init__(self):
        super(Permiso, self).__init__()
        self.Inter = uic.loadUi('Permiso.ui', self)
        self.Inter.setWindowIcon(QIcon('DG.png'))

class Calendario(QDialog):
    def __init__(self):
        super(Calendario,self).__init__()
        self.Inter = uic.loadUi('Fechador.ui', self)
        self.Inter.setWindowTitle('Calendario DesinGlass Smart Windows')
        self.Inter.setWindowIcon(QIcon('DG.png'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #myApp = Permiso()
    #myApp = arranque()
    #myApp.show()
    myapp = Calendario()
    myapp.show()
    sys.exit(app.exec_())