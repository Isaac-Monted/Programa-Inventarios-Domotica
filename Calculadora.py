import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QSystemTrayIcon
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from  InterfazPrincipal import *

import math
import keyboard

import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class VentanaCalculadora(QMainWindow):
    def __init__(self):
        super(VentanaCalculadora, self).__init__()
        self.Inter = uic.loadUi('CalculadoraInt.ui', self)
        self.Inter.setWindowTitle('Calculadora')
        self.Inter.setWindowIcon(QIcon('IconoEsfera.png'))
        #self.Inter = arranque() 
        
        #Ocultar los Botones#
        self.Inter.BTMax2.hide()
        self.Inter.BTMax.hide()
        #Ocultar los botones#

        #Eliminar barra y titulo -opacidad#
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #Eliminar barra y titulo -opacidad#

        #===========================Botones=============================#
        self.Inter.Resultado.setEnabled(False) #Pantalla Resultado#
        self.Inter.Edicion.setEnabled(False) #Pantalla Edicion#

        self.Inter.BTPar1.clicked.connect(self.FBTPar1) #(#
        self.Inter.BTPar2.clicked.connect(self.FBTPar2) #)#
        self.Inter.BTC.clicked.connect(self.FBTC) #C#
        self.Inter.BTDelete.clicked.connect(self.FBTDelete) #⌫#

        self.Inter.BT7.clicked.connect(self.FBT7) #7#
        self.Inter.BT8.clicked.connect(self.FBT8) #8#
        self.Inter.BT9.clicked.connect(self.FBT9) #9#
        self.Inter.BTDiv.clicked.connect(self.FBTDiv) #÷#

        self.Inter.BT4.clicked.connect(self.FBT4) #4#
        self.Inter.BT5.clicked.connect(self.FBT5) #5#
        self.Inter.BT6.clicked.connect(self.FBT6) #6#
        self.Inter.BTMult.clicked.connect(self.FBTMult) #X#

        self.Inter.BT1.clicked.connect(self.FBT1) #1#
        self.Inter.BT2.clicked.connect(self.FBT2) #2#
        self.Inter.BT3.clicked.connect(self.FBT3) #3#
        self.Inter.BTSum.clicked.connect(self.FBTSum) #+#

        self.Inter.BT0.clicked.connect(self.FBT0) #0#
        self.Inter.BTPunto.clicked.connect(self.FBTPunto) #.#
        self.Inter.BTRest.clicked.connect(self.FBTRest) #-#

        self.Inter.BTIgual.clicked.connect(self.FBTIgual) #=#
        self.Inter.BTRaiz.clicked.connect(self.FBTRaiz) #√#
        #===========================Botones=============================#

        #===========================TECLADO=============================#
        try:
            keyboard.add_hotkey('1', self.FBT1) #1#
            keyboard.add_hotkey('2', self.FBT2) #2#
            keyboard.add_hotkey('3', self.FBT3) #3#
            keyboard.add_hotkey('4', self.FBT4) #4#
            keyboard.add_hotkey('5', self.FBT5) #5#
            keyboard.add_hotkey('6', self.FBT6) #6#
            keyboard.add_hotkey('7', self.FBT7) #7#
            keyboard.add_hotkey('8', self.FBT8) #8#
            keyboard.add_hotkey('9', self.FBT9) #9
            keyboard.add_hotkey('0', self.FBT0) #0#

            keyboard.add_hotkey('c', self.FBTPar1) #(#
            keyboard.add_hotkey('v', self.FBTPar2) #)#

            keyboard.add_hotkey('BACKSPACE', self.FBTDelete) #⌫#
            keyboard.add_hotkey('DELETE', self.FBTC) #C#

            keyboard.add_hotkey('/', self.FBTDiv) #÷#
            keyboard.add_hotkey('*', self.FBTMult) #x#
            keyboard.add_hotkey('-', self.FBTRest) #-#
            keyboard.add_hotkey('+', self.FBTSum) #+#
            keyboard.add_hotkey('Enter', self.FBTIgual) #=#
            keyboard.add_hotkey('.', self.FBTPunto) #.#
            keyboard.add_hotkey('R', self.FBTRaiz) #√#
        except:
            print('ERROR')
        #===========================TECLADO=============================#

        #Controles barra de Titulo#
        self.Inter.BTMin.clicked.connect(self.FBTMin)
        self.Inter.BTMax.clicked.connect(self.FBTMax)
        self.Inter.BTMax2.clicked.connect(self.FBTMax2)
        self.Inter.BTCerar.clicked.connect(lambda: self.close())
        #Controles Barra de Titulo"               

        #Eliminar barra y titulo -opacidad#
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #Eliminar barra y titulo -opacidad#

        #Sise Grip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        #Size Grip

        #Mover Ventana#
        self.FrameSuperior.mouseMoveEvent = self.MoverVentana
        #Mover Ventana#
    #=========================================FUNCIONES CALCULOS==========================================#
    def FBTPar1(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("(")
        self.Inter.Edicion.setText(str(entrada))

    def FBTPar2(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str(")")
        self.Inter.Edicion.setText(str(entrada))

    def FBTC(self):
        entrada = self.Inter.Edicion.text()
        largo = len(entrada)
        #print(largo)
        if largo >0:
            self.Inter.Edicion.clear()
            self.Inter.Resultado.clear()
        else:
            'nada'

    def FBTDelete(self):
        entrada = self.Inter.Edicion.text()
        largo = len(entrada)
        #print(largo)
        if largo >0:
            self.Inter.Edicion.setText(entrada[:len(entrada)-1])
        else:
            'nada'

    def FBT7(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("7")
        self.Inter.Edicion.setText(str(entrada))

    def FBT8(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("8")
        self.Inter.Edicion.setText(str(entrada))

    def FBT9(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("9")
        self.Inter.Edicion.setText(str(entrada))

    def FBTDiv(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("/")
        self.Inter.Edicion.setText(str(entrada))

    def FBT4(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("4")
        self.Inter.Edicion.setText(str(entrada))

    def FBT5(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("5")
        self.Inter.Edicion.setText(str(entrada))

    def FBT6(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("6")
        self.Inter.Edicion.setText(str(entrada))

    def FBTMult(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("*")
        self.Inter.Edicion.setText(str(entrada))

    def FBT1(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("1")
        self.Inter.Edicion.setText(str(entrada))
    
    def FBT2(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("2")
        self.Inter.Edicion.setText(str(entrada))

    def FBT3(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("3")
        self.Inter.Edicion.setText(str(entrada))

    def FBTSum(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("+")
        self.Inter.Edicion.setText(str(entrada))

    def FBT0(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("0")
        self.Inter.Edicion.setText(str(entrada))

    def FBTPunto(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str(".")
        self.Inter.Edicion.setText(str(entrada))

    def FBTRest(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("-")
        self.Inter.Edicion.setText(str(entrada))

    def FBTIgual(self):
        entrada = self.Inter.Edicion.text()
        try:
            ans = eval(entrada)
            self.Inter.Edicion.setText(str(ans))
            self.Inter.Resultado.setText(str(ans))
        except:
            self.Inter.Edicion.clear()
            self.Inter.Resultado.setText('ERROR')
    
    def FBTRaiz(self):
        entrada = self.Inter.Edicion.text()
        entrada = str(entrada) + str("**(1/2)")
        self.Inter.Edicion.setText(str(entrada))
    
    #=========================================FUNCIONES CALCULOS==========================================#
        

    #=========================================BOTONES DE LA BARRA PRINCIPAL==========================================#
    def FBTMin(self):
        self.showMinimized()

    def FBTMax(self):
        self.showMaximized()
        self.Inter.BTMax.hide()
        self.Inter.BTMax2.show()
    
    def FBTMax2(self):
        self.showNormal()
        self.Inter.BTMax2.hide()
        self.Inter.BTMax.show()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def MoverVentana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=10:
            self.showMaximized()
        else:
            self.showNormal()
    #=========================================BOTONES DE LA BARRA PRINCIPAL==========================================#

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = VentanaCalculadora()
    #myApp = arranque()
    myApp.show()
    sys.exit(app.exec_())
