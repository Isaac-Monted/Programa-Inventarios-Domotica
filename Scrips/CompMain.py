import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox, QAbstractItemView, QFileDialog, QMenu, QActionGroup, QAction, QSystemTrayIcon
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt, QByteArray, QBuffer, QIODevice, QAbstractAnimation
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from  InterfazPrincipal import *
import time

from IngresarProductos import *
from IngresarEntradas import *
from IngresarSalidas import *
from IngresarListas import *

import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class VentanaSecundaria(QMainWindow):
    def __init__(self, clase):
        super(VentanaSecundaria, self).__init__()
        self.Inter = uic.loadUi('InterfazSecundariaInt.ui', self)
        self.Inter.setWindowTitle('Edicion de Datos')
        self.Inter.setWindowIcon(QIcon('IconoEsfera.png'))
        #self.Inter = arranque() 
        self.Base = Pagina1()
        self.Entradas = Pagina4()
        self.Salidas = Pagina5()
        self.Listas = Pagina6()
        
        #Ocultar los Botones#
        self.Inter.BTMax2.hide()
        #self.Inter.BTMax.hide()
        #Ocultar los botones#

        #Eliminar barra y titulo -opacidad#
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #Eliminar barra y titulo -opacidad#

        #===========================Botones=============================#
        self.Inter.BTSalir.clicked.connect(self.FBTSalir)
        self.Inter.BTGuardar.clicked.connect(self.FBTGuardar)
        self.Inter.BTLimpiar.clicked.connect(self.FBTLimpiar)
        self.Inter.BTLimpiarObs.clicked.connect(self.FBTLimpiarObs)

            #tabla 1#
        self.Inter.TWRegistro.setEditTriggers(QAbstractItemView.NoEditTriggers) #No Modificar#
        self.Inter.TWRegistro.setDragDropOverwriteMode(False) #No Arrastrar y Soltar#
        self.Inter.TWRegistro.setSelectionBehavior(QAbstractItemView.SelectRows) #Seleccionar Toda la Fila#
        self.Inter.TWRegistro.setSelectionMode(QAbstractItemView.SingleSelection) #Seleccionar solo Una Fila#
        self.Inter.TWRegistro.setTextElideMode(Qt.ElideRight) #Texto largo aparece asi: . . . #
        self.Inter.TWRegistro.setWordWrap(False) #Deshabilitar autoajuste#
        self.Inter.TWRegistro.setSortingEnabled(False) #Desgabilitar la clasificacion#
        self.Inter.TWRegistro.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) #Aliciacion del encabezado#
        self.Inter.TWRegistro.horizontalHeader().setHighlightSections(False) #Deshabilitar Sombreado Encabezado#
        self.Inter.TWRegistro.horizontalHeader().setStretchLastSection(True) #Estirar la tabla a todo el espacio que tenga#
        self.Inter.TWRegistro.verticalHeader().setVisible(False) #Quitar encabezado vertical#
        self.Inter.TWRegistro.setAlternatingRowColors(True)#una fila de un color y otra de otro#
        self.Inter.TWRegistro.clicked.connect(self.TabMostRegistroSeleccionado)
            #tabla 1#

        #===========================Botones=============================#

        #===========================FUNCIONES INICIALES=============================#
        #llenar Informacion#
        self.TTitulo(clase)
        self.Refrescar(clase)
        #llenar Informacion#
        #===========================FUNCIONES INICIALES=============================#

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
    def TTitulo(self, Clase):
        self.Inter.Titulo.setText("REGISTRO DE {}".format(Clase.upper()))
        #print(Clase)

    def FBTSalir(self):
        pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Eliminar el Producto de la Lista?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if pregunta == QMessageBox.Yes:
            self.Inter.close()
        else:
            pass

    def FBTGuardar(self):
        FilaSewleccionada = self.Inter.TWRegistro.selectedItems()
        fila = [dato.text() for dato in FilaSewleccionada]
        #fila = fila[0]

        if  fila == []:
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Seleccione un Registro para Editar")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            if self.Inter.TXObra.text() == "":
                    dialogo = QMessageBox()
                    dialogo.setText("Por Favor LLene Correctamente Los Campos del Formulario")
                    dialogo.setWindowTitle("DesinGlass Smart Windows")
                    dialogo.setWindowIcon(QIcon('DG.png'))
                    dialogo.setIcon(QMessageBox.Warning)
                    dialogo.exec_()
            else:
                fila = fila[0]
                clave = fila
                
                clase = self.Inter.Titulo.text()
                clase = clase[12: ]
                
                if clase == "ENTRADAS":
                    busc = self.Entradas.BuscarEntradas(fila)[0]
                elif clase == "SALIDAS":
                    busc = self.Salidas.BuscarSalidas(fila)[0]
                else:
                    busc = self.Listas.BuscarListas(fila)[0]

                Obra = self.Inter.TXObra.text() #Obra
                OrComp = self.Inter.TXOrComp.text() #Orden de Compra
                FolFact = self.Inter.TXOrComp.text() #Folio Factura
                Observaciones = self.Inter.TXObservaciones.toPlainText() #Observaciones

                lista = []

                #print(busc)
                contador = 0
                for i in busc:
                    contador += 1
                    #print(contador, ":", i)
                    if contador == 1:
                        #print(contador, ":", i)
                        ID = i
                    elif contador == 3:
                        lista.append(Obra)
                        #print(contador, ":", i)
                    elif contador == 168:
                        lista.append(OrComp)
                       # print(contador, ":", i)
                    elif contador == 169:
                        lista.append(FolFact)
                        #print(contador, ":", i)
                    elif contador == 170:
                        lista.append(Observaciones)
                        #print(contador, ":", i)
                    else:
                        lista.append(i)
                        #print(contador, ":", i)

                #print(lista, len(lista))

                if clase == "ENTRADAS":
                    self.Entradas.ActualizarEntradasL(ID, lista)
                    dialogoB = QMessageBox()
                    dialogoB.setText("Se Ha Guardado Correctamete")
                    dialogoB.setWindowTitle("DesinGlass Smart Windows")
                    dialogoB.setWindowIcon(QIcon('DG.png'))
                    dialogoB.setIcon(QMessageBox.Information)
                    dialogoB.exec_()

                    #REFRESCAR INFORMACION#
                    self.Refrescar(clase.capitalize())
                    self.FBTLimpiar()
                    #REFRESCAR INFORMACION#
                elif clase == "SALIDAS":
                    self.Salidas.ActualizarSalidasL(ID, lista)
                    dialogoB = QMessageBox()
                    dialogoB.setText("Se Ha Guardado Correctamete")
                    dialogoB.setWindowTitle("DesinGlass Smart Windows")
                    dialogoB.setWindowIcon(QIcon('DG.png'))
                    dialogoB.setIcon(QMessageBox.Information)
                    dialogoB.exec_()

                    #REFRESCAR INFORMACION#
                    self.Refrescar(clase.capitalize())
                    self.FBTLimpiar()
                    #REFRESCAR INFORMACION#
                else:
                    self.Listas.ActualizarListasL(ID, lista)
                    dialogoB = QMessageBox()
                    dialogoB.setText("Se Ha Guardado Correctamete")
                    dialogoB.setWindowTitle("DesinGlass Smart Windows")
                    dialogoB.setWindowIcon(QIcon('DG.png'))
                    dialogoB.setIcon(QMessageBox.Information)
                    dialogoB.exec_()

                    #REFRESCAR INFORMACION#
                    self.Refrescar(clase.capitalize())
                    self.FBTLimpiar()
                    #REFRESCAR INFORMACION#              

    def FBTLimpiar(self):
        self.Inter.TXObra.clear() #Obra#
        self.Inter.TXOrComp.clear() #Orden de Compra#
        self.Inter.TXFolFact.clear() #Folio Factura#
        self.Inter.TXObservaciones.clear() #Observaciones#

    def FBTLimpiarObs(self):
        self.Inter.TXObservaciones.clear() #Observaciones#

    def TabMostRegistros(self, clase):
        if clase == 'Salidas':
            self.Inter.TWRegistro.setColumnCount(166) #Columnas
            self.Inter.TWRegistro.setRowCount(0)  #FIlas
            self.Inter.TWRegistro.clear()
            NombreColumnas = self.Base.NomColum()
            self.Inter.TWRegistro.setHorizontalHeaderLabels(NombreColumnas)

            entrada = self.Salidas.ConsultarSalidasR("ID")
            #print(datos)
            #row = 0
            i = len(entrada)
            self.Inter.TWRegistro.setRowCount(i)
            tableRow = 0
            for row in entrada:
                self.Id = row[0]
                z = iter(range(168)) #creamos el iterable
                for e,e2 in enumerate(z, start=0): #ciclo for con dos variables para llenar la tabla
                    e2 += 1
                    #print(e, e2)
                    self.Inter.TWRegistro.setItem(tableRow,e,QtWidgets.QTableWidgetItem(row[e2])) #llenado simultaneo
                tableRow += 1 #agregamos una fila
        elif clase == 'Entradas':
            self.Inter.TWRegistro.setColumnCount(166) #Columnas
            self.Inter.TWRegistro.setRowCount(0)  #FIlas
            self.Inter.TWRegistro.clear()
            NombreColumnas = self.Base.NomColum()
            self.Inter.TWRegistro.setHorizontalHeaderLabels(NombreColumnas)

            entrada = self.Entradas.ConsultarEntradasR("ID")
            #print(datos)
            #row = 0
            i = len(entrada)
            self.Inter.TWRegistro.setRowCount(i)
            tableRow = 0
            for row in entrada:
                self.Id = row[0]
                z = iter(range(168)) #creamos el iterable
                for e,e2 in enumerate(z, start=0): #ciclo for con dos variables para llenar la tabla
                    e2 += 1
                    #print(e, e2)
                    self.Inter.TWRegistro.setItem(tableRow,e,QtWidgets.QTableWidgetItem(row[e2])) #llenado simultaneo
                tableRow += 1 #agregamos una fila
        elif clase == 'Listas':
            self.Inter.TWRegistro.setColumnCount(166) #Columnas
            self.Inter.TWRegistro.setRowCount(0)  #FIlas
            self.Inter.TWRegistro.clear()
            NombreColumnas = self.Base.NomColum()
            self.Inter.TWRegistro.setHorizontalHeaderLabels(NombreColumnas)

            entrada = self.Listas.ConsultarListasR("ID")
            #print(datos)
            #row = 0
            i = len(entrada)
            self.Inter.TWRegistro.setRowCount(i)
            tableRow = 0
            for row in entrada:
                self.Id = row[0]
                z = iter(range(168)) #creamos el iterable
                for e,e2 in enumerate(z, start=0): #ciclo for con dos variables para llenar la tabla
                    e2 += 1
                    #print(e, e2)
                    self.Inter.TWRegistro.setItem(tableRow,e,QtWidgets.QTableWidgetItem(row[e2])) #llenado simultaneo
                tableRow += 1 #agregamos una fila
        else:
            self.Inter.TWRegistro.setColumnCount(166) #Columnas
            self.Inter.TWRegistro.setRowCount(0)  #FIlas
            self.Inter.TWRegistro.clear()
            NombreColumnas = self.Base.NomColum()
            self.Inter.TWRegistro.setHorizontalHeaderLabels(NombreColumnas)

    def TabMostRegistroSeleccionado(self):
        FilaSewleccionada = self.Inter.TWRegistro.selectedItems()
        fila = [dato.text() for dato in FilaSewleccionada]
        fila = fila[0]
        #print(fila)

        clase = self.Inter.Titulo.text()
        clase = clase[12: ]
        
        if clase == "ENTRADAS":
            busc = self.Entradas.BuscarEntradas(fila)
        elif clase == "SALIDAS":
            busc = self.Salidas.BuscarSalidas(fila)
        else:
            busc = self.Listas.BuscarListas(fila)

        if busc == []:
            dialogo = QMessageBox()
            dialogo.setText('No se Encontro Ningun Registro con Ese Folio')
            dialogo.setWindowTitle('DesinGlass Smart Windows')
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()
        else:
            busc = busc[0]
            #print(busc)
            self.Inter.TXObra.setText(busc[2]) #Obra#
            self.Inter.TXOrComp.setText(busc[167]) #Orden de Compra#
            self.Inter.TXFolFact.setText(busc[168]) #Folio Factura#
            self.Inter.TXObservaciones.setText(busc[169]) #Observaciones#

            self.Inter.TWRegistro.viewport().setCursor(Qt.ClosedHandCursor) #Hacer que la manita se cierre
            cronometroI = time.time()
            while True:
                cronometroF = time.time()
                if cronometroF - cronometroI >= 0.2:
                    self.Inter .TWRegistro.viewport().setCursor(Qt.OpenHandCursor) #Hacer que la manita se abra
                    break
                else:
                    #print(cronometroF - cronometroI)
                    pass

    def Refrescar(self, clase):
        self.TabMostRegistros(clase)

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
    #myApp = VentanaSecundaria('Salidas')
    #myApp = arranque()
    #myApp.show()
    sys.exit(app.exec_())
