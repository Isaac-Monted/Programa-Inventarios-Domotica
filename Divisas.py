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

class VentanaDivisas(QMainWindow):
    def __init__(self):
        super(VentanaDivisas, self).__init__()
        self.Inter = uic.loadUi('DivisasInt.ui', self)
        self.Inter.setWindowTitle('Calculo de Divisas')
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
            #Conexion#
        self.Inter.CBDivisas.currentIndexChanged.connect(self.Valor)
        self.Inter.BTNacional.clicked.connect(self.FBTNacional)
        self.Inter.BTExtranjera.clicked.connect(self.FBTExtranjera)
        self.Inter.BTRestar.clicked.connect(self.FBTRestar)
        self.Inter.BTAgregar.clicked.connect(self.FBTAgregar)
        self.Inter.BTConvertir.clicked.connect(self.FBTConvertir)
        self.Inter.BTCalcular.clicked.connect(self.FBTCalcular)

        self.Inter.TXCantidad.cursorPositionChanged.connect(self.Validacion1)
        self.Inter.TXCantidad_2.cursorPositionChanged.connect(self.Validacion3)
        self.Inter.Inter.TXIva.cursorPositionChanged.connect(self.Validacion2)
            #Conexion#
        
        self.Inter.Cantidad.setText("Cantidad INT")

        self.MarIzq = True
        self.MarDer = True

        self.Inter.TXCambio.setEnabled(False)
        self.Inter.TXResultado.setEnabled(False)

        self.Inter.BTNacional.setEnabled(False)
        self.Inter.BTNacional.setStyleSheet("QPushButton{\n"
                                            "background-color:#AEAEAE;\n"
                                            "border-radius:10px;\n"
                                            "color:Black;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "background-color:#FFFFFF;\n"
                                            "border-radius:10px;\n"
                                            "color:Black;\n"
                                            "}\n")
        self.Inter.BTAgregar.setEnabled(False)
        self.Inter.BTAgregar.setStyleSheet("QPushButton{\n"
                                            "background-color:#AEAEAE;\n"
                                            "border-radius:10px;\n"
                                            "color:Black;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "background-color:#FFFFFF;\n"
                                            "border-radius:10px;\n"
                                            "color:Black;\n"
                                            "}\n")

        #===========================Botones=============================#

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
    def FBTNacional(self):
        self.MarIzq = True
        self.Inter.Cantidad.setText("Cantidad INT")
        self.Inter.BTNacional.setEnabled(False)
        self.Inter.BTExtranjera.setEnabled(True)
        self.Inter.BTExtranjera.setStyleSheet("QPushButton{\n"
                                                "background-color:#A4D6DC;\n"
                                                "border-radius:10px;\n"
                                                "color:Black;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "background-color:#DCD8A4;\n"
                                                "border-radius:10px;\n"
                                                "color:Black;\n"
                                                "}\n")
        self.Inter.BTNacional.setStyleSheet("QPushButton{\n"
                                            "background-color:#AEAEAE;\n"
                                            "border-radius:10px;\n"
                                            "color:Black;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "background-color:#FFFFFF;\n"
                                            "border-radius:10px;\n"
                                            "color:Black;\n"
                                            "}\n")
    
    def FBTExtranjera(self):
        self.MarIzq = False
        self.Inter.Cantidad.setText("Cantidad MXN")
        self.Inter.BTNacional.setEnabled(True)
        self.Inter.BTExtranjera.setEnabled(False)
        self.Inter.BTNacional.setStyleSheet("QPushButton{\n"
                                                "background-color:#A4D6DC;\n"
                                                "border-radius:10px;\n"
                                                "color:Black;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "background-color:#DCD8A4;\n"
                                                "border-radius:10px;\n"
                                                "color:Black;\n"
                                                "}\n")
        self.Inter.BTExtranjera.setStyleSheet("QPushButton{\n"
                                            "background-color:#AEAEAE;\n"
                                            "border-radius:10px;\n"
                                            "color:Black;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "background-color:#FFFFFF;\n"
                                            "border-radius:10px;\n"
                                            "color:Black;\n"
                                            "}\n")

    def FBTAgregar(self):
        self.MarDer = True
        self.Inter.BTRestar.setEnabled(True)
        self.Inter.BTAgregar.setEnabled(False)
        self.Inter.BTRestar.setStyleSheet("QPushButton{\n"
                                                "background-color:#A4D6DC;\n"
                                                "border-radius:10px;\n"
                                                "color:Black;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "background-color:#DCD8A4;\n"
                                                "border-radius:10px;\n"
                                                "color:Black;\n"
                                                "}\n")
        self.Inter.BTAgregar.setStyleSheet("QPushButton{\n"
                                            "background-color:#AEAEAE;\n"
                                            "border-radius:10px;\n"
                                            "color:Black;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "background-color:#FFFFFF;\n"
                                            "border-radius:10px;\n"
                                            "color:Black;\n"
                                            "}\n")

    def FBTRestar(self):
        self.MarDer = False
        self.Inter.BTRestar.setEnabled(False)
        self.Inter.BTAgregar.setEnabled(True)
        self.Inter.BTAgregar.setStyleSheet("QPushButton{\n"
                                                "background-color:#A4D6DC;\n"
                                                "border-radius:10px;\n"
                                                "color:Black;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "background-color:#DCD8A4;\n"
                                                "border-radius:10px;\n"
                                                "color:Black;\n"
                                                "}\n")
        self.Inter.BTRestar.setStyleSheet("QPushButton{\n"
                                            "background-color:#AEAEAE;\n"
                                            "border-radius:10px;\n"
                                            "color:Black;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "background-color:#FFFFFF;\n"
                                            "border-radius:10px;\n"
                                            "color:Black;\n"
                                            "}\n")
    def Validacion1(self):
        #print('cambio')
        x = QDoubleValidator()
        self.Inter.TXCantidad.setValidator(x)
        

    def Validacion2(self):
        x = QDoubleValidator()
        self.Inter.TXIva.setValidator(x)

    def Validacion3(self):
        x = QDoubleValidator()
        self.Inter.TXCantidad_2.setValidator(x)
        
    def FBTConvertir(self):
        #print(self.MarIzq)
        Cantidad = self.Inter.TXCantidad.text()

        if self.Inter.CBDivisas.itemText(self.Inter.CBDivisas.currentIndex()) == "" or self.Inter.TXCantidad.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Llene Correctamente Los campos del Formulario")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Information)
            dialogo.exec_()
        else:
            if self.MarIzq == True:
                #print(self.valor, Cantidad)
                valor = float(self.valor)
                Cantidad = float(Cantidad)
                Resultado = valor * Cantidad
                #print(Resultado)
                self.Inter.TXCambio.setText(str("%.2f"%Resultado))
            else:
                #print(self.valor, Cantidad)
                valor = float(self.valor)
                Cantidad = float(Cantidad)
                Resultado = Cantidad / valor
                #print(Resultado)
                self.Inter.TXCambio.setText(str("%.2f"%Resultado))
    def FBTCalcular(self):
        #print(self.MarDer)
        IVA = self.Inter.TXIva.text()
        if self.Inter.TXIva.text() == "" or self.Inter.TXCantidad_2.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Llene Correctamente Los campos del Formulario")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Information)
            dialogo.exec_()
        else:
            if self.MarDer == True:
                #print(self.valor, Cantidad)
                iva = float(self.Inter.TXIva.text())
                Cantidad = float(self.Inter.TXCantidad_2.text())
                Resultado =  (Cantidad * (iva / 100)) + Cantidad
                #print(Resultado)
                self.Inter.TXResultado.setText(str("%.2f"%Resultado))
            else:
                #print(self.valor, Cantidad)
                iva = float(self.Inter.TXIva.text())
                Cantidad = float(self.Inter.TXCantidad_2.text())
                Resultado = ((Cantidad * (iva / 100)) * -1) + Cantidad
                #print(Resultado)
                self.Inter.TXResultado.setText(str("%.2f"%Resultado))

    #=========================================FUNCIONES CALCULOS==========================================#

    #=========================================BUSCAR DIVISAS==========================================#
    def Valor(self,  **kwargs):
        Constante = CalcularDiv()
        Divisa = self.Inter.CBDivisas.currentIndex()
        if Divisa == 0:
            self.valor = None
        if Divisa == 1:
            self.valor = Constante.Dolar()
        if Divisa == 2:
            self.valor = Constante.Euro()
        if Divisa == 3:
            self.valor = Constante.Yuan()
        if Divisa == 4:
            self.valor = Constante.Libra()

        #print(valor)

    #=========================================BUSCAR DIVISAS==========================================#

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
    myApp = VentanaDivisas()
    #myApp = arranque()
    myApp.show()
    sys.exit(app.exec_())
