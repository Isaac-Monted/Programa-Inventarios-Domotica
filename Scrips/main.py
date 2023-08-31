import datetime
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox, QAbstractItemView, QFileDialog, QMenu, QActionGroup, QAction, QSystemTrayIcon
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt, QByteArray, QBuffer, QIODevice, QAbstractAnimation
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap, QIcon
import cv2
import imutils
import os
import time
from datetime import datetime 
from  InterfazPrincipal import *
from Calculadora import *
from Divisas import *

from IngresarProductos import *
from IngresarMovimientos import *
from IngresarProveedores import *
from IngresarEntradas import *
from IngresarSalidas import *
from IngresarListas import *
from IngresarLista import *
from IngresarEncabezado import *
from CreacionPDF import *
from Permiso import *
from CompMain import *

import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class VentanaPrincipal(QMainWindow):
    time.sleep(0)
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.Inter = uic.loadUi('InterfazPrincipal.ui', self)
        self.Inter.setWindowTitle('Inventario DesinGlass Smart Windows')
        self.Inter.setWindowIcon(QIcon('IconoEsfera.png'))
        self.Imagen = ""
        self.Contrasenas()
        #self.Inter = arranque()  
        #self.Cursor = QtGui.QCursor()

        self.Inter.BTMenu.clicked.connect(self.MoverMenu)

        #Conexion Base de Datos#       
        self.Base = Pagina1()
        self.Movimientoss = Pagina2()
        self.Proveedoress = Pagina3()
        self.Entradas = Pagina4()
        self.Salidas = Pagina5()
        self.Listas = Pagina6()
        self.Lista = Pagina7()
        self.Encabezado = Pagina8()
        #Conexion Base de Datos# 

        #llenar datos#
            #Hoja2
        self.Refrescar2()
        self.LLenarCBBuscar()
            #Hoja 2

            #Hoja5
        self.Refrescar5()
        self.LLenarCBBuscar1()
            #Hoja5
        
            #Hoja6
        self.Refrescar6()
        self.LLenarCBBuscar_3()
        self.LLenarCBBuscar_4()
            #Hoja6

            #Hoja7
        self.Refrescar7()
        self.LLenarCBBuscar_5()
            #Hoja7
        
            #Hoja8
        self.Refrescar8()
        self.LLenarCBBuscar_2()
            #Hoja8
        #llenar datos# 

        #Ocultar los Botones#
        self.Inter.BTMax2.hide()
        #Ocultar los botones#

        #============================Botones=============================#
        #Primera Pagina#        Ingresos
            #Menu#
        self.Inter.Calculadora.clicked.connect(self.Calc) #Calculadora#
        self.Inter.Divisa.clicked.connect(self.DiviIVA)   #Divisa#
        #self.Inter.Divisa_2.clicked.connect() #Refrescar#
        self.Inter.Divisa_3.clicked.connect(self.licencia) #Licencia#
        self.Inter.Divisa_4.clicked.connect(self.AcercaDe) #Acerca de#
        self.Inter.Divisa_5.clicked.connect(self.Salir) #Salir#
            #Menu#
        
        #menu contextual#
        self.Inter.Ingresos.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Inter.Ingresos.customContextMenuRequested.connect(self.menuContextual)
        #menu contextual#

        self.Inter.TXStock.cursorPositionChanged.connect(self.Validacion1)
        self.Inter.TXPCompra.cursorPositionChanged.connect(self.Validacion12)
        self.Inter.TXPVenta.cursorPositionChanged.connect(self.Validacion13)
        
        self.Inter.BTImagen.clicked.connect(self.FBTImagen) #Cargar Imagen#
        self.Inter.BTGuardar.clicked.connect(self.FBTGuardar) #Guardar#
        self.Inter.BTLimpiar.clicked.connect(self.FBTLimpiar) #Limpiar#
        self.Inter.BTActualizar.clicked.connect(self.FBTActualizar) #Actualizar#
        self.Inter.BTSalir.clicked.connect(lambda: self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)) #Salir#
        #Primer Pagina#

        #Segunda Pagina#        Productos
            #Menu#
        self.Inter.Calculadora_2.clicked.connect(self.Calc) #Calculadora#
        self.Inter.Divisa_6.clicked.connect(self.DiviIVA) #Divisa#
        self.Inter.Divisa_9.clicked.connect(self.Refrescar2) #Refrescar#
        self.Inter.Divisa_8.clicked.connect(self.licencia) #Licencia#
        self.Inter.Divisa_10.clicked.connect(self.AcercaDe) #Acerca de#
        self.Inter.Divisa_7.clicked.connect(self.Salir) #Salir#
            #Menu#

        #tabla 1#
        self.Inter.TWProductos_4.setEditTriggers(QAbstractItemView.NoEditTriggers) #No Modificar#
        self.Inter.TWProductos_4.setDragDropOverwriteMode(False) #No Arrastrar y Soltar#
        self.Inter.TWProductos_4.setSelectionBehavior(QAbstractItemView.SelectRows) #Seleccionar Toda la Fila#
        self.Inter.TWProductos_4.setSelectionMode(QAbstractItemView.SingleSelection) #Seleccionar solo Una Fila#
        self.Inter.TWProductos_4.setTextElideMode(Qt.ElideRight) #Texto largo aparece asi: . . . #
        self.Inter.TWProductos_4.setWordWrap(False) #Deshabilitar autoajuste#
        self.Inter.TWProductos_4.setSortingEnabled(False) #Desgabilitar la clasificacion#
        self.Inter.TWProductos_4.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) #Aliciacion del encabezado#
        self.Inter.TWProductos_4.horizontalHeader().setHighlightSections(False) #Deshabilitar Sombreado Encabezado#
        self.Inter.TWProductos_4.horizontalHeader().setStretchLastSection(True) #Estirar la tabla a todo el espacio que tenga#
        self.Inter.TWProductos_4.verticalHeader().setVisible(False) #Quitar encabezado vertical#
        self.Inter.TWProductos_4.setAlternatingRowColors(True)#una fila de un color y otra de otro#
        self.Inter.TWProductos_4.clicked.connect(self.TabMostProductos)
        #tabla 1#

        self.Inter.BTBuscar2_4.clicked.connect(self.FBTBuscar2_4) #Buscar#
        self.Inter.BTImagen2_4.clicked.connect(self.FBTImagen2_4) #Imagen#
        self.Inter.BTAgregar2_4.clicked.connect(self.FBTAgregar2_4) #Agregar#
        self.Inter.BTActualizar2_4.clicked.connect(self.FBTActualizar2_4) #Actualizar#
        self.Inter.BTLimpiar2_4.clicked.connect(self.FBTLimpiar2_4) #Limpiar#
        self.Inter.BTSalir2_4.clicked.connect(lambda: self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)) #Salir#
        #Segunda Pagina#

        #Tercera Pagina#        Informacion
            #Menu#
        self.Inter.Calculadora_3.clicked.connect(self.Calc) #Calculadora#
        self.Inter.Divisa_13.clicked.connect(self.DiviIVA) #Divisa#
        self.Inter.Divisa_14.clicked.connect(self.Refrescar3) #Refrescar#
        self.Inter.Divisa_15.clicked.connect(self.licencia) #Licencia#
        self.Inter.Divisa_12.clicked.connect(self.AcercaDe) #Acerca de#
        self.Inter.Divisa_11.clicked.connect(self.Salir) #Salir#
            #menu#
        self.Inter.BTHojInv.clicked.connect(self.FBTHojInv) #Hoja para Inventario#
        self.Inter.BTReport.clicked.connect(self.FBTReport) #Reporte#
        #Tercera Pagina#

        #Cuarta Pagina#         Movimientos
            #Menu#
        self.Inter.Calculadora_4.clicked.connect(self.Calc) #Calculadora#
        self.Inter.Divisa_18.clicked.connect(self.DiviIVA) #Divisa#
        self.Inter.Divisa_19.clicked.connect(self.Refrescar4) #Refrescar#
        self.Inter.Divisa_20.clicked.connect(self.licencia) #Licencia#
        self.Inter.Divisa_17.clicked.connect(self.AcercaDe) #Acerca de#
        self.Inter.Divisa_16.clicked.connect(self.Salir) #Salir#
            #Menu#

            #Deshabilitar Botones#
        self.Inter.BTImprimir.hide()
        self.Inter.BTEditar.hide()
            #Deshabilitar Botones

        #tabla MOV#
        self.Inter.TWHistorial.setEditTriggers(QAbstractItemView.NoEditTriggers) #No Modificar#
        self.Inter.TWHistorial.setDragDropOverwriteMode(False) #No Arrastrar y Soltar#
        self.Inter.TWHistorial.setSelectionBehavior(QAbstractItemView.SelectRows) #Seleccionar Toda la Fila#
        self.Inter.TWHistorial.setSelectionMode(QAbstractItemView.SingleSelection) #Seleccionar solo Una Fila#
        self.Inter.TWHistorial.setTextElideMode(Qt.ElideRight) #Texto largo aparece asi: . . . #
        self.Inter.TWHistorial.setWordWrap(False) #Deshabilitar autoajuste#
        self.Inter.TWHistorial.setSortingEnabled(False) #Desgabilitar la clasificacion#
        self.Inter.TWHistorial.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) #Aliciacion del encabezado#
        self.Inter.TWHistorial.horizontalHeader().setHighlightSections(False) #Deshabilitar Sombreado Encabezado#
        self.Inter.TWHistorial.horizontalHeader().setStretchLastSection(True) #Estirar la tabla a todo el espacio que tenga#
        self.Inter.TWHistorial.verticalHeader().setVisible(False) #Quitar encabezado vertical#
        self.Inter.TWHistorial.setAlternatingRowColors(True)#una fila de un color y otra de otro#
        self.Inter.TWHistorial.clicked.connect(self.FTWHistorialSelecionado)
        #tabla MOV#

        self.Inter.BTListas.clicked.connect(self.FBTListas) #Listas#
        self.Inter.BTSalidas_2.clicked.connect(self.FBTSalidas_2) #Salidas#
        self.Inter.BTEntradas.clicked.connect(self.FBTEntradas) #Entradas#
        self.Inter.BTMovimientos.clicked.connect(self.FBTMovimientos) #Movimientos#
        self.Inter.BTSalir_2.clicked.connect(lambda: self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)) #Salir#
        self.Inter.BTImprimir.clicked.connect(self.FBTImprimir) #Imprimir#
        self.Inter.BTEditar.clicked.connect(self.FBTEditar) #Editar#
        #Cuarta Pagina#

        #Quinta pagina#         Proveedores
            #Menu#
        self.Inter.Calculadora_5.clicked.connect(self.Calc) #Calculadora#
        self.Inter.Divisa_23.clicked.connect(self.DiviIVA) #Divisa#
        self.Inter.Divisa_24.clicked.connect(self.Refrescar5) #Refrescar#
        self.Inter.Divisa_25.clicked.connect(self.licencia) #Licencia#
        self.Inter.Divisa_22.clicked.connect(self.AcercaDe) #Acerca de#
        self.Inter.Divisa_21.clicked.connect(self.Salir) #Salir#
            #menu#
        
        #tabla PROV#
        self.Inter.TWProveedores.setEditTriggers(QAbstractItemView.NoEditTriggers) #No Modificar#
        self.Inter.TWProveedores.setDragDropOverwriteMode(False) #No Arrastrar y Soltar#
        self.Inter.TWProveedores.setSelectionBehavior(QAbstractItemView.SelectRows) #Seleccionar Toda la Fila#
        self.Inter.TWProveedores.setSelectionMode(QAbstractItemView.SingleSelection) #Seleccionar solo Una Fila#
        self.Inter.TWProveedores.setTextElideMode(Qt.ElideRight) #Texto largo aparece asi: . . . #
        self.Inter.TWProveedores.setWordWrap(False) #Deshabilitar autoajuste#
        self.Inter.TWProveedores.setSortingEnabled(False) #Desgabilitar la clasificacion#
        self.Inter.TWProveedores.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) #Aliciacion del encabezado#
        self.Inter.TWProveedores.horizontalHeader().setHighlightSections(False) #Deshabilitar Sombreado Encabezado#
        self.Inter.TWProveedores.horizontalHeader().setStretchLastSection(True) #Estirar la tabla a todo el espacio que tenga#
        self.Inter.TWProveedores.verticalHeader().setVisible(False) #Quitar encabezado vertical#
        self.Inter.TWProveedores.setAlternatingRowColors(True)#una fila de un color y otra de otro#
        self.Inter.TWProveedores.clicked.connect(self.FTWProveedorSelecionado)
        #tabla PROB#

        self.Inter.BTBuscar.clicked.connect(self.FBTBuscar) #Buscar#
        self.Inter.BTIngresar.clicked.connect(self.FBTIngresar) #Ingresar#
        self.Inter.BTLimpiar_2.clicked.connect(self.FBTLimpiar_2) #Limpiar#
        self.Inter.BTActualizar_2.clicked.connect(self.FBTActualizar_2) #Actualizar#
        self.Inter.BTEliminar.clicked.connect(self.FBTEliminar) #Eliminar#
        self.Inter.BTSalir_3.clicked.connect(lambda: self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)) #Salir#
        #Quinta Pagina#

        #Sexta Pagina#      Entradas y Salidas
            #Menu#
        self.Inter.Calculadora_6.clicked.connect(self.Calc) #Calculadora#
        self.Inter.Divisa_28.clicked.connect(self.DiviIVA) #Divisa#
        self.Inter.Divisa_29.clicked.connect(self.Refrescar6) #Refrescar#
        self.Inter.Divisa_30.clicked.connect(self.licencia) #Licencia#
        self.Inter.Divisa_27.clicked.connect(self.AcercaDe) #Acerca de#
        self.Inter.Divisa_26.clicked.connect(self.Salir) #Salir#
            #Menu#'''
        self.Inter.BTEntradas_2.clicked.connect(self.EntradasBT) #Entradas#
        self.Inter.BTSalidas.clicked.connect(self.SalidasBT) #Salidas#
        self.Inter.BTListas_2.clicked.connect(self.ListasBT) #Listas#

        #=========Entradas==========#
        #tabla ENT#
        self.Inter.TWLista.setEditTriggers(QAbstractItemView.NoEditTriggers) #No Modificar#
        self.Inter.TWLista.setDragDropOverwriteMode(False) #No Arrastrar y Soltar#
        self.Inter.TWLista.setSelectionBehavior(QAbstractItemView.SelectRows) #Seleccionar Toda la Fila#
        self.Inter.TWLista.setSelectionMode(QAbstractItemView.SingleSelection) #Seleccionar solo Una Fila#
        self.Inter.TWLista.setTextElideMode(Qt.ElideRight) #Texto largo aparece asi: . . . #
        self.Inter.TWLista.setWordWrap(False) #Deshabilitar autoajuste#
        self.Inter.TWLista.setSortingEnabled(False) #Desgabilitar la clasificacion#
        self.Inter.TWLista.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) #Aliciacion del encabezado#
        self.Inter.TWLista.horizontalHeader().setHighlightSections(False) #Deshabilitar Sombreado Encabezado#
        self.Inter.TWLista.horizontalHeader().setStretchLastSection(True) #Estirar la tabla a todo el espacio que tenga#
        self.Inter.TWLista.verticalHeader().setVisible(False) #Quitar encabezado vertical#
        self.Inter.TWLista.setAlternatingRowColors(True)#una fila de un color y otra de otro#
        self.Inter.TWLista.clicked.connect(self.FTWListaSelecionado)
        #tabla ENT#
        #tabla ENTProd#
        self.Inter.TWProductos_2.setEditTriggers(QAbstractItemView.NoEditTriggers) #No Modificar#
        self.Inter.TWProductos_2.setDragDropOverwriteMode(False) #No Arrastrar y Soltar#
        self.Inter.TWProductos_2.setSelectionBehavior(QAbstractItemView.SelectRows) #Seleccionar Toda la Fila#
        self.Inter.TWProductos_2.setSelectionMode(QAbstractItemView.SingleSelection) #Seleccionar solo Una Fila#
        self.Inter.TWProductos_2.setTextElideMode(Qt.ElideRight) #Texto largo aparece asi: . . . #
        self.Inter.TWProductos_2.setWordWrap(False) #Deshabilitar autoajuste#
        self.Inter.TWProductos_2.setSortingEnabled(False) #Desgabilitar la clasificacion#
        self.Inter.TWProductos_2.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) #Aliciacion del encabezado#
        self.Inter.TWProductos_2.horizontalHeader().setHighlightSections(False) #Deshabilitar Sombreado Encabezado#
        self.Inter.TWProductos_2.horizontalHeader().setStretchLastSection(True) #Estirar la tabla a todo el espacio que tenga#
        self.Inter.TWProductos_2.verticalHeader().setVisible(False) #Quitar encabezado vertical#
        self.Inter.TWProductos_2.setAlternatingRowColors(True)#una fila de un color y otra de otro#
        self.Inter.TWProductos_2.clicked.connect(self.FTWProductos_2Selecionado)
        #tabla ENTProd#

        self.Inter.BTIngresar_2.clicked.connect(self.IngresosBT) #Ingresar# #self.FBTIngresar_2
        self.Inter.BTLimpiarTodo.clicked.connect(self.FBTLimpiarTodo) #Limpiar Todo#
        self.Inter.BTSalir_5.clicked.connect(lambda: self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)) #Salir#

        self.Inter.BTLimpiar_4.clicked.connect(self.FBTLimpiar_4) #Limpiar#
        self.Inter.BTAgregar.clicked.connect(self.FBTAgregar) #Agragar#

        self.Inter.BTBuscar_3.clicked.connect(self.FBTBuscar_3) #Buscar#

        self.Inter.BTGuardar_2.clicked.connect(self.FBTGuardar_2) #Guardar#
        self.Inter.BTEliminar_2.clicked.connect(self.FBTEliminar_2) #Eliminar#

        self.Inter.BTLimpObs_2.clicked.connect(self.FBTLimpObs_2) #Limpiar observaciones#
        #=========Entradas=========#

        #========Salidas========#
        #tabla SAL#
        self.Inter.TWLista_2.setEditTriggers(QAbstractItemView.NoEditTriggers) #No Modificar#
        self.Inter.TWLista_2.setDragDropOverwriteMode(False) #No Arrastrar y Soltar#
        self.Inter.TWLista_2.setSelectionBehavior(QAbstractItemView.SelectRows) #Seleccionar Toda la Fila#
        self.Inter.TWLista_2.setSelectionMode(QAbstractItemView.SingleSelection) #Seleccionar solo Una Fila#
        self.Inter.TWLista_2.setTextElideMode(Qt.ElideRight) #Texto largo aparece asi: . . . #
        self.Inter.TWLista_2.setWordWrap(False) #Deshabilitar autoajuste#
        self.Inter.TWLista_2.setSortingEnabled(False) #Desgabilitar la clasificacion#
        self.Inter.TWLista_2.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) #Aliciacion del encabezado#
        self.Inter.TWLista_2.horizontalHeader().setHighlightSections(False) #Deshabilitar Sombreado Encabezado#
        self.Inter.TWLista_2.horizontalHeader().setStretchLastSection(True) #Estirar la tabla a todo el espacio que tenga#
        self.Inter.TWLista_2.verticalHeader().setVisible(False) #Quitar encabezado vertical#
        self.Inter.TWLista_2.setAlternatingRowColors(True)#una fila de un color y otra de otro#
        self.Inter.TWLista_2.clicked.connect(self.FTWLista_2Selecionado)
        #tabla SAL#
        #tabla SALProd#
        self.Inter.TWProductos_3.setEditTriggers(QAbstractItemView.NoEditTriggers) #No Modificar#
        self.Inter.TWProductos_3.setDragDropOverwriteMode(False) #No Arrastrar y Soltar#
        self.Inter.TWProductos_3.setSelectionBehavior(QAbstractItemView.SelectRows) #Seleccionar Toda la Fila#
        self.Inter.TWProductos_3.setSelectionMode(QAbstractItemView.SingleSelection) #Seleccionar solo Una Fila#
        self.Inter.TWProductos_3.setTextElideMode(Qt.ElideRight) #Texto largo aparece asi: . . . #
        self.Inter.TWProductos_3.setWordWrap(False) #Deshabilitar autoajuste#
        self.Inter.TWProductos_3.setSortingEnabled(False) #Desgabilitar la clasificacion#
        self.Inter.TWProductos_3.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) #Aliciacion del encabezado#
        self.Inter.TWProductos_3.horizontalHeader().setHighlightSections(False) #Deshabilitar Sombreado Encabezado#
        self.Inter.TWProductos_3.horizontalHeader().setStretchLastSection(True) #Estirar la tabla a todo el espacio que tenga#
        self.Inter.TWProductos_3.verticalHeader().setVisible(False) #Quitar encabezado vertical#
        self.Inter.TWProductos_3.setAlternatingRowColors(True)#una fila de un color y otra de otro#
        self.Inter.TWProductos_3.clicked.connect(self.FTWProductos_3Selecionado)
        #tabla SALProd#
        
        self.Inter.BTIngresar_3.clicked.connect(self.IngresosBT) #ingrear# #self.FBTIngresar_3
        self.Inter.BTLimpiarTodo_2.clicked.connect(self.FBTLimpiarTodo_2) #Limpiar Todo#
        self.Inter.BTSalir_6.clicked.connect(lambda: self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)) #Salir#

        self.Inter.BTLimpiar_5.clicked.connect(self.FBTLimpiar_5) #Limpiar#
        self.Inter.BTAgregar_2.clicked.connect(self.FBTAgregar_2) #Agregar#

        self.Inter.BTBuscar_4.clicked.connect(self.FBTBuscar_4) #Buscar#

        self.Inter.BTGuardar_3.clicked.connect(self.FBTGuardar_3) #Guardar#
        self.Inter.BTEliminar_3.clicked.connect(self.FBTEliminar_3) #Eliminar#

        self.Inter.BTLimpObs.clicked.connect(self.FBTLimpObs) #Limpiar Observaciones#
        #=========Salidas=========#

        self.Inter.TXCantidad.cursorPositionChanged.connect(self.Validacion61) #Solo Numeros Cantidad Entrada
        self.Inter.TXCantidad_2.cursorPositionChanged.connect(self.Validacion62) #Solo Numeros Cantidad Salida

        #Sexta Pagina#

        #Septima Pagina#        Lista de Salidas
            #Menu#
        self.Inter.Calculadora_7.clicked.connect(self.Calc) #Calculadora#
        self.Inter.Divisa_33.clicked.connect(self.DiviIVA) #Divisa#
        self.Inter.Divisa_34.clicked.connect(self.Refrescar7) #Refrescar#
        self.Inter.Divisa_35.clicked.connect(self.licencia) #Licencia#
        self.Inter.Divisa_32.clicked.connect(self.AcercaDe) #Acerca de#
        self.Inter.Divisa_31.clicked.connect(self.Salir) #Salir#
            #Menu#

        #tabla LIST#
        self.Inter.TWLista_3.setEditTriggers(QAbstractItemView.NoEditTriggers) #No Modificar#
        self.Inter.TWLista_3.setDragDropOverwriteMode(False) #No Arrastrar y Soltar#
        self.Inter.TWLista_3.setSelectionBehavior(QAbstractItemView.SelectRows) #Seleccionar Toda la Fila#
        self.Inter.TWLista_3.setSelectionMode(QAbstractItemView.SingleSelection) #Seleccionar solo Una Fila#
        self.Inter.TWLista_3.setTextElideMode(Qt.ElideRight) #Texto largo aparece asi: . . . #
        self.Inter.TWLista_3.setWordWrap(False) #Deshabilitar autoajuste#
        self.Inter.TWLista_3.setSortingEnabled(False) #Desgabilitar la clasificacion#
        self.Inter.TWLista_3.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) #Aliciacion del encabezado#
        self.Inter.TWLista_3.horizontalHeader().setHighlightSections(False) #Deshabilitar Sombreado Encabezado#
        self.Inter.TWLista_3.horizontalHeader().setStretchLastSection(True) #Estirar la tabla a todo el espacio que tenga#
        self.Inter.TWLista_3.verticalHeader().setVisible(False) #Quitar encabezado vertical#
        self.Inter.TWLista_3.setAlternatingRowColors(True)#una fila de un color y otra de otro#
        self.Inter.TWLista_3.clicked.connect(self.FTWLista_3Selecionado)
        #tabla LIST#
        #tabla LISTProd#
        self.Inter.TWProductos_5.setEditTriggers(QAbstractItemView.NoEditTriggers) #No Modificar#
        self.Inter.TWProductos_5.setDragDropOverwriteMode(False) #No Arrastrar y Soltar#
        self.Inter.TWProductos_5.setSelectionBehavior(QAbstractItemView.SelectRows) #Seleccionar Toda la Fila#
        self.Inter.TWProductos_5.setSelectionMode(QAbstractItemView.SingleSelection) #Seleccionar solo Una Fila#
        self.Inter.TWProductos_5.setTextElideMode(Qt.ElideRight) #Texto largo aparece asi: . . . #
        self.Inter.TWProductos_5.setWordWrap(False) #Deshabilitar autoajuste#
        self.Inter.TWProductos_5.setSortingEnabled(False) #Desgabilitar la clasificacion#
        self.Inter.TWProductos_5.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) #Aliciacion del encabezado#
        self.Inter.TWProductos_5.horizontalHeader().setHighlightSections(False) #Deshabilitar Sombreado Encabezado#
        self.Inter.TWProductos_5.horizontalHeader().setStretchLastSection(True) #Estirar la tabla a todo el espacio que tenga#
        self.Inter.TWProductos_5.verticalHeader().setVisible(False) #Quitar encabezado vertical#
        self.Inter.TWProductos_5.setAlternatingRowColors(True)#una fila de un color y otra de otro#
        self.Inter.TWProductos_5.clicked.connect(self.FTWProductos_5Selecionado)
        #tabla LISTProd#

        self.Inter.TXCantidad_3.cursorPositionChanged.connect(self.Validacion71) #Solo Numeros Cantidad Entrada

        self.Inter.BTIngresar_4.clicked.connect(self.IngresosBT) #Ingresar# #self.Ingresar_4
        self.Inter.BTLimpiarTodo_3.clicked.connect(self.FBTLimpiarTodo_3) #Limpiar Todo#
        self.Inter.BTSalir_7.clicked.connect(lambda: self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)) #Salir#

        self.Inter.BTLimpiar_6.clicked.connect(self.FBTLimpiar_6) #Limpiar#
        self.Inter.BTAgregar_3.clicked.connect(self.FBTAgregar_3) #Agregar#

        self.Inter.BTBuscar_5.clicked.connect(self.FBTBuscar_5) #Buscar#

        self.Inter.BTGuardar_4.clicked.connect(self.FBTGuardar_4) #Guardar#
        self.Inter.BTEliminar_4.clicked.connect(self.FBTEliminar_4) #Eliminar#
        #Septima Pagina#

        #Octava Pagina#         Ajuste de Inventario
            #Menu#
        self.Inter.Calculadora_8.clicked.connect(self.Calc) #calculadora#
        self.Inter.Divisa_38.clicked.connect(self.DiviIVA) #Divisa#
        self.Inter.Divisa_39.clicked.connect(self.Refrescar8) #Refrescar#
        self.Inter.Divisa_40.clicked.connect(self.licencia) #Licencia#
        self.Inter.Divisa_37.clicked.connect(self.AcercaDe) #Acerca de#
        self.Inter.Divisa_36.clicked.connect(self.Salir) #Salir#
            #menu#
        
        #tabla 8#
        self.Inter.TWProductos.setEditTriggers(QAbstractItemView.NoEditTriggers) #No Modificar#
        self.Inter.TWProductos.setDragDropOverwriteMode(False) #No Arrastrar y Soltar#
        self.Inter.TWProductos.setSelectionBehavior(QAbstractItemView.SelectRows) #Seleccionar Toda la Fila#
        self.Inter.TWProductos.setSelectionMode(QAbstractItemView.SingleSelection) #Seleccionar solo Una Fila#
        self.Inter.TWProductos.setTextElideMode(Qt.ElideRight) #Texto largo aparece asi: . . . #
        self.Inter.TWProductos.setWordWrap(False) #Deshabilitar autoajuste#
        self.Inter.TWProductos.setSortingEnabled(False) #Desgabilitar la clasificacion#
        self.Inter.TWProductos.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter) #Aliciacion del encabezado#
        self.Inter.TWProductos.horizontalHeader().setHighlightSections(False) #Deshabilitar Sombreado Encabezado#
        self.Inter.TWProductos.horizontalHeader().setStretchLastSection(True) #Estirar la tabla a todo el espacio que tenga#
        self.Inter.TWProductos.verticalHeader().setVisible(False) #Quitar encabezado vertical#
        self.Inter.TWProductos.setAlternatingRowColors(True)#una fila de un color y otra de otro#
        self.Inter.TWProductos.clicked.connect(self.FTWProductosSelecionado)
        #tabla 8#

        self.Inter.TXNum_2.cursorPositionChanged.connect(self.Validacion8)

        self.Inter.BTBuscar_2.clicked.connect(self.FBTBuscar_2) #Buscar#
        self.Inter.BTLimpiar_3.clicked.connect(self.FBTLimpiar_3) #limpiar#
        self.Inter.BTSalir_4.clicked.connect(lambda: self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)) #Salir#
        self.Inter.BTRestar.clicked.connect(self.FBTRestar) #Restar#
        self.Inter.BTSumar.clicked.connect(self.FBTSumar) #Sumar#
        #Octava pagina#
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

        #Botones Menu Lateral#
        self.Inter.BTIngresarProd.clicked.connect(self.IngresosBT) #Ingresar Producto#
        self.Inter.BTProductoss.clicked.connect(lambda: self.Inter.Libro1.setCurrentWidget(self.Inter.Productos)) #Productos#
        self.Inter.BTInformacion.clicked.connect(lambda: self.Inter.Libro1.setCurrentWidget(self.Inter.Informacion)) #Informacion#
        self.Inter.BTMovimientoss.clicked.connect(lambda: self.Inter.Libro1.setCurrentWidget(self.Inter.Movimientos)) #Movimientos#
        self.Inter.BTProveedores.clicked.connect(lambda: self.Inter.Libro1.setCurrentWidget(self.Inter.Proveedores)) #Proveedores#
        self.Inter.BTEntradasSalidas.clicked.connect(self.EntradasSalidas) #Entradas y Salidas#
        self.Inter.BTLIstasSal.clicked.connect(self.ListasBT) #Listas de Salidas#
        self.Inter.BTAjusteInv.clicked.connect(self.AjusteInvBT) #Ajuste de Inventario#
        #Botones Menu lateral#

        #Ancho de Conumna Adaptable#
        #self.Inter.TWProductos_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Inter.TWProveedores.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #Proveedores
        self.Inter.TWProductos_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #Salidas Producto
        #self.Inter.TWLista_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #Salida Lista
        self.Inter.TWProductos_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #Entradas Producto
        #self.Inter.TWLista.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #Entrada Lista
        #Ancho de Columna Adaptable#
    
    #=========================================FUNCIONES BOTONES==========================================#
        #Primera Pagina#
    def FBTImagen(self):  #Cargar Imagen#
        fileName = QFileDialog.getOpenFileName(filter= "Todo (*.*);;Image JPG(*.jpg);;Image PNG (*.png)")[0]
        self.Imagen = fileName
        #print(fileName)
        if fileName == "":
            dialogo = QMessageBox()
            dialogo.setText("Se Ha Eliminado La Imagen")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Information)
            dialogo.exec_()
            fileName = os.getcwd() + "\DG.png"
            fileName = fileName.replace("/", chr(92))
            #print(fileName)
            pixmapImage = QPixmap(fileName).scaled(200,200,Qt.KeepAspectRatio,Qt.SmoothTransformation)
            self.Inter.label_13.setPixmap(pixmapImage)
        else:
            pixmapImage = QPixmap(fileName).scaled(200,200,Qt.KeepAspectRatio,Qt.SmoothTransformation)
            self.Inter.label_13.setPixmap(pixmapImage)

    def FBTGuardar(self):  #Guardar#
        from datetime import datetime
        if self.Inter.TXNombre.text() == "" or self.Inter.TXClave.text() == "" or self.Inter.TXStock.text() == "" or self.Inter.TXLugar.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor LLene Correctamente Los Campos del Formulario")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
            if pregunta == QMessageBox.Yes:
                buscar = self.Inter.TXClave.text()

                verificar = self.Base.BuscarProducto(buscar)
                #print(verificar)

                if verificar != []:
                    dialogo = QMessageBox()
                    dialogo.setText("La Clave ya esta Registrada en la Base de Datos")
                    dialogo.setWindowTitle("DesinGlass Smart Windows")
                    dialogo.setWindowIcon(QIcon('DG.png'))
                    dialogo.setIcon(QMessageBox.Critical)
                    dialogo.exec_()

                else:
                    #print('paso')
                    Nombre = self.Inter.TXNombre.text()
                    Clave = self.Inter.TXClave.text()
                    Numero = self.Inter.TXNumero.text()
                    Color = self.Inter.TXColor.text()
                    Marca = self.Inter.TXMarca.text()
                    Unidad = self.Inter.TXUnidad.text()
                    Stock = self.Inter.TXStock.text()
                    Proveedor = self.Inter.TXProveedor.text()
                    Lugar = self.Inter.TXLugar.text()
                    PCompra = self.Inter.TXPCompra.text()
                    PVenta = self.Inter.TXPVenta.text()
                    foto = self.Inter.label_13.pixmap()

                    #print(foto)
                    if foto == None:
                        Imagen = os.getcwd() + "\DG.png"
                        Imagen = Imagen.replace("/", chr(92))
                        
                        pixmapImage = QPixmap(foto).scaled(200,200,Qt.KeepAspectRatio,Qt.SmoothTransformation)
                        self.Inter.label_13.setPixmap(pixmapImage)
                        foto = self.Inter.label_13.pixmap()

                        #Convertir Imagen a Bytes#
                        bArray = QByteArray()
                        buff = QBuffer(bArray)
                        buff.open(QIODevice.WriteOnly)
                        foto.save(buff, "PNG")
                        #Convertir Imagen a Bytes#
                    else:
                        foto = self.Inter.label_13.pixmap()
                        #Convertir Imagen a Bytes#
                        bArray = QByteArray()
                        buff = QBuffer(bArray)
                        buff.open(QIODevice.WriteOnly)
                        foto.save(buff, "PNG")
                        #Convertir Imagen a Bytes#
                        #Imagen = bArray

                    self.Base.AgregarProducto(Nombre.capitalize(), Clave, Numero.capitalize(), Marca.capitalize(), Color.capitalize(), Unidad.capitalize(), Stock, Proveedor.capitalize(), Lugar.capitalize(), PCompra, PVenta, bArray)

                    dialogoB = QMessageBox()
                    dialogoB.setText("Se Ha Guardado Correctamete")
                    dialogoB.setWindowTitle("DesinGlass Smart Windows")
                    dialogoB.setWindowIcon(QIcon('DG.png'))
                    dialogoB.setIcon(QMessageBox.Information)
                    dialogoB.exec_()

                    #REFRESCAR INFORMACION#
                    self.Refrescar2()
                    self.LLenarCBBuscar()
                    self.FBTLimpiar()
                    self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
                    #REFRESCAR INFORMACION#

                    #========================CREAR REGISTRO EN MOVIMIENTOS========================#
                    TipMov = "Ingreso"
                    Fecha = str(datetime.now())
                    Fecha = Fecha[0: 19]
                    Fecha = Fecha.replace("-", "/")
                    Fecha = str(Fecha)

                    self.Movimientoss.AgregarMovimientos(TipMov.capitalize(), Nombre.capitalize(), Clave, Numero.capitalize(), Marca.capitalize(), Color.capitalize(), Unidad.capitalize(), Stock, Proveedor.capitalize(), Lugar.capitalize(), Fecha)
                    print('Movimiento Registrado')
                    #========================CREAR REGISTRO EN MOVIMIENTOS========================#
            else:
                dialogo2 = QMessageBox()
                dialogo2.setText("Operacion Cancelada")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()

    def FBTLimpiar(self):  #Limpiar#
        self.Inter.TXNombre.clear()
        self.Inter.TXClave.clear()
        self.Inter.TXNumero.clear()
        self.Inter.TXColor.clear()
        self.Inter.TXMarca.clear()
        self.Inter.TXUnidad.clear()
        self.Inter.TXStock.clear()
        self.Inter.TXProveedor.clear()
        self.Inter.TXLugar.clear()
        self.Inter.TXPCompra.clear()
        self.Inter.TXPVenta.clear()

        self.Inter.label_13.clear() #imagen#
        self.Inter.label_13.setText('Imagen') #Texto Imagen#


    def FBTActualizar(self):  #Actualizar#
        self.Inter.Libro1.setCurrentWidget(self.Inter.Productos)

    def Validacion1(self):
        x = QDoubleValidator()
        self.Inter.TXStock.setValidator(x)
    def Validacion12(self):
        x = QDoubleValidator()
        self.Inter.TXPCompra.setValidator(x)
    def Validacion13(self):
        x = QDoubleValidator()
        self.Inter.TXPVenta.setValidator(x)
        #Primera Pagina#

        #Segunda Pagina#
    def FBTBuscar2_4(self): #Buscar#
        buscar = self.Inter.CBListaProd_4.currentText()
        #print(buscar)
        if buscar == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Seleccione Un Producto")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            busc = self.Base.BuscarProductoN(buscar)[0]
            #print(busc)
            if busc == "":
                dialogo2 = QMessageBox()
                dialogo2.setText("El Producto Selecionado No Existe")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                self.Inter.TXProducto2_4.setText(busc[1]) #Producto#
                self.Inter.TXMarca2_4.setText(busc[4]) #Marca#
                self.Inter.TXNumero2_4.setText(busc[3]) #Numero#
                self.Inter.TXClave2_4.setText(busc[2]) #Clave#
                self.Inter.TXUnidad2_4.setText(busc[6]) #Unidad#
                self.Inter.TXProveedor2_4.setText(busc[8]) #Proveedor#
                self.Inter.TXColor2_4.setText(busc[5]) #Color#
                self.Inter.TXLugar2_4.setText(busc[9]) #Lugar#

                Imagen = busc[12]
                #print(Imagen)
                if Imagen == "" or Imagen == None or Imagen == b'':
                    Imagen = os.getcwd() + "\DG.png"
                    Imagen = Imagen.replace("/", chr(92))

                    pixmapImage = QPixmap(Imagen).scaled(200,200,Qt.KeepAspectRatio,Qt.SmoothTransformation)
                    self.Inter.label_17.setPixmap(pixmapImage)
                else:
                    foto = QPixmap()
                    foto.loadFromData(Imagen, "PNG", Qt.AutoColor)
                    self.Inter.label_17.setPixmap(foto)

                '''image = cv2.imread(Imagen)

                Imagenn = image
                Imagenn = imutils.resize(Imagenn, width=200)
                Imagenn2 = cv2.cvtColor(Imagenn, cv2.COLOR_RGB2BGR)
                Imagenn = QImage(Imagenn2, Imagenn2.shape[1], Imagenn2.shape[0], Imagenn2.strides[0], QImage.Format_RGB888)
                self.Inter.label_17.setPixmap(QtGui.QPixmap.fromImage(Imagenn))
                self.Imagen = ""'''

    def FBTImagen2_4(self): #Imagen#
        fileName = QFileDialog.getOpenFileName(filter= "Todo (*.*);;Image JPG(*.jpg);;Image PNG (*.png)")[0]
        self.Imagen = fileName
        #print(fileName)
        if fileName == "":
            dialogo = QMessageBox()
            dialogo.setText("Se Ha Eliminado La Imagen")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Information)
            dialogo.exec_()
            fileName = os.getcwd() + "\DG.png"
            fileName = fileName.replace("/", chr(92))
            #print(fileName)
            pixmapImage = QPixmap(fileName).scaled(200,200,Qt.KeepAspectRatio,Qt.SmoothTransformation)
            self.Inter.label_17.setPixmap(pixmapImage)
        else:
            pixmapImage = QPixmap(fileName).scaled(200,200,Qt.KeepAspectRatio,Qt.SmoothTransformation)
            self.Inter.label_17.setPixmap(pixmapImage)

        "image = cv2.imread(fileName)"
        #self.setImagen(image)

        """Imagen = image
        Imagen = imutils.resize(Imagen, width=200)
        Imagen2 = cv2.cvtColor(Imagen, cv2.COLOR_RGB2BGR)
        Imagen = QImage(Imagen2, Imagen2.shape[1], Imagen2.shape[0], Imagen2.strides[0], QImage.Format_RGB888)
        self.Inter.label_17.setPixmap(QtGui.QPixmap.fromImage(Imagen))"""

    def FBTAgregar2_4(self):  #Agregar#
        self.Inter.Libro1.setCurrentWidget(self.Inter.Ingresos)

    def TabMostProductos(self): #Tabla Mostrar Producto selecionado
        FilaSewleccionada = self.Inter.TWProductos_4.selectedItems()
        fila = [dato.text() for dato in FilaSewleccionada]
        #fila = fila[1]
        #print(fila)
        self.Inter.TXProducto2_4.setText(fila[0]) #Producto#
        self.Inter.TXMarca2_4.setText(fila[3]) #Marca#
        self.Inter.TXNumero2_4.setText(fila[2]) #Numero#
        self.Inter.TXClave2_4.setText(fila[1]) #Clave#
        self.Inter.TXUnidad2_4.setText(fila[5]) #Unidad#
        self.Inter.TXProveedor2_4.setText(fila[7]) #Proveedor#
        self.Inter.TXColor2_4.setText(fila[4]) #Color#
        self.Inter.TXLugar2_4.setText(fila[8]) #Lugar#

        busc = self.Base.BuscarProducto(fila[1])[0]

        #print(busc)
        if busc == "":
            print('Nada')
        else:
            Imagen = busc[12]
            if Imagen == "" or Imagen == None or Imagen == b'':
                Imagen = os.getcwd() + "\DG.png"
                Imagen = Imagen.replace("/", chr(92))

                '''image = cv2.imread(Imagen)

                Imagenn = image
                Imagenn = imutils.resize(Imagenn, width=200)
                Imagenn2 = cv2.cvtColor(Imagenn, cv2.COLOR_RGB2BGR)
                Imagenn = QImage(Imagenn2, Imagenn2.shape[1], Imagenn2.shape[0], Imagenn2.strides[0], QImage.Format_RGB888)
                self.Inter.label_17.setPixmap(QtGui.QPixmap.fromImage(Imagenn))
                self.Imagen = ""'''
                pixmapImage = QPixmap(Imagen).scaled(200,200,Qt.KeepAspectRatio,Qt.SmoothTransformation)
                self.Inter.label_17.setPixmap(pixmapImage)
            else:
                foto = QPixmap()
                foto.loadFromData(Imagen, "PNG", Qt.AutoColor)
                self.Inter.label_17.setPixmap(foto)

        self.Inter.TWProductos_4.viewport().setCursor(Qt.ClosedHandCursor) #Hacer que la manita se cierre
        cronometroI = time.time()
        while True:
            cronometroF = time.time()
            if cronometroF - cronometroI >= 0.2:
                self.Inter .TWProductos_4.viewport().setCursor(Qt.OpenHandCursor) #Hacer que la manita se abra
                break
            else:
                #print(cronometroF - cronometroI)
                pass

        self.Inter.CBListaProd_4.setCurrentText("")            

    def FBTActualizar2_4(self): #Actualizar#
        if self.Inter.TXProducto2_4.text() == "" or self.Inter.TXClave2_4.text() == ""  or self.Inter.TXLugar2_4.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor LLene Correctamente Los Campos del Formulario")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
            if pregunta == QMessageBox.Yes:
                buscar = self.Inter.TXClave2_4.text()
                #print(buscar)
                if buscar == "":
                    dialogo = QMessageBox()
                    dialogo.setText("Por Favor Seleccione Un Producto PAra Actualizar")
                    dialogo.setWindowTitle("DesinGlass Smart Windows")
                    dialogo.setWindowIcon(QIcon('DG.png'))
                    dialogo.setIcon(QMessageBox.Warning)
                    dialogo.exec_()
                else:
                    busc = self.Base.BuscarProducto(buscar)[0]
                    #print(busc)
                    if busc == "":
                        dialogo2 = QMessageBox()
                        dialogo2.setText("El Producto Selecionado No Existe")
                        dialogo2.setWindowTitle("DesinGlass Smart Windows")
                        dialogo2.setWindowIcon(QIcon('DG.png'))
                        dialogo2.setIcon(QMessageBox.Warning)
                        dialogo2.exec_()
                    else:
                        Nombre = self.Inter.TXProducto2_4.text() #Producto#
                        Clave = self.Inter.TXClave2_4.text() #Clave#
                        Numero = self.Inter.TXNumero2_4.text() #Numero#
                        Color = self.Inter.TXColor2_4.text() #Color#
                        Marca = self.Inter.TXMarca2_4.text() #Marca#
                        Unidad = self.Inter.TXUnidad2_4.text() #Unidad#
                        Proveedor = self.Inter.TXProveedor2_4.text() #Proveedor#
                        Lugar = self.Inter.TXLugar2_4.text() #Lugar#

                        ID = busc[0]
                        Stock = busc[7]
                        PCompra = busc[10]
                        PVenta = busc[11]

                        foto = self.Inter.label_17.pixmap()
                        if foto == "":
                            foto = busc[12]
                            
                        #else:
                            #Imagen = Imagen
                            #Imagen = self.Imagen
                            #Imagen = os.getcwd() + "\DG.jpg"
                            #Imagen = Imagen.replace("/", chr(92))
    
                        #Convertir Imagen a Bytes#
                        bArray = QByteArray()
                        buff = QBuffer(bArray)
                        buff.open(QIODevice.WriteOnly)
                        foto.save(buff, "PNG")
                        #Convertir Imagen a Bytes#
                            

                        self.Base.ActualizarProducto( ID, Nombre.capitalize(), Clave, Numero.capitalize(), Marca.capitalize(), Color.capitalize(), Unidad.capitalize(), Stock, Proveedor.capitalize(), Lugar.capitalize(), PCompra, PVenta, bArray)

                        #REFRESCAR INFORMACION#
                        self.Refrescar2()
                        self.LLenarCBBuscar()
                        self.FBTLimpiar2_4()
                        #self.Imagen = ""
                        self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
                        #REFRESCAR INFORMACION#

                        dialogoB = QMessageBox()
                        dialogoB.setText("Se Ha Guardado Correctamete")
                        dialogoB.setWindowTitle("DesinGlass Smart Windows")
                        dialogoB.setWindowIcon(QIcon('DG.png'))
                        dialogoB.setIcon(QMessageBox.Information)
                        dialogoB.exec_()
            else:
                dialogo2 = QMessageBox()
                dialogo2.setText("Operacion Cancelada")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()

    def FBTLimpiar2_4(self):  #Limpiar#
        self.Inter.CBListaProd_4.setCurrentText("") #Buscar#
        self.Inter.TXProducto2_4.clear() #Producto#
        self.Inter.TXMarca2_4.clear() #Marca#
        self.Inter.TXNumero2_4.clear() #Numero#
        self.Inter.TXClave2_4.clear() #Clave#
        self.Inter.TXUnidad2_4.clear() #Unidad#
        self.Inter.TXProveedor2_4.clear() #Proveedor#
        self.Inter.TXColor2_4.clear() #Color#
        self.Inter.TXLugar2_4.clear() #Lugar#
        self.Inter.label_17.clear() #imagen#
        self.Inter.label_17.setText('Imagen') #Texto Imagen#
        self.Imagen = ""

    def LLenarCBBuscar(self):
        self.Inter.CBListaProd_4.clear()
        datos = self.Base.ConsultarProductos()
        i = len(datos)
        self.Inter.TWProductos_4.setRowCount(i)
        self.Inter.CBListaProd_4.addItem("")
        for row in datos:
            self.Inter.CBListaProd_4.addItem(row[1])

        #Segunda Pagina#

        #Tercera Pagina#
    def FBTHojInv(self):
        HInv = HojaInventario()
        HInv.PDFInventario()
    def FBTReport(self):
        self.Fechador = Calendario()
        self.Fechador.Titulo.setText("Seleccione la Fecha de: Inicio")
        self.Fechador.show()
        self.Fechador.CWCalendario.selectedDate() 
        self.Fechador.CWCalendario.selectionChanged.connect(self.DateTimo1)

        self.Fechador.BTSelecionarFC.clicked.connect(self.FBTSelecionarFC)
    def DateTimo1(self):
        fecha = str(self.Fechador.CWCalendario.selectedDate().toPyDate())
        self.Fechador.TXFecha.setText(fecha)
    def DateTimo2(self):
        fecha = str(self.Fechador2.CWCalendario.selectedDate().toPyDate())
        self.Fechador2.TXFecha.setText(fecha)
    def FBTSelecionarFC(self):
        #print('seleccion uno')
        fecha = self.Fechador.TXFecha.text()
        #print(fecha)
        if fecha == "":
            dialogo = QMessageBox()
            dialogo.setText("Operacion Cancelada")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()
        else:
            fecha1 = fecha
            self.Fechador.close()
            self.Fechador2 = Calendario()
            self.Fechador2.Titulo.setText("Seleccione la Fecha de: Termino")
            self.Fechador2.show()
            self.Fechador2.CWCalendario.selectedDate() 
            self.Fechador2.CWCalendario.selectionChanged.connect(self.DateTimo2)
            self.fecha1 = fecha1
            #print(self.fecha1)

            self.Fechador2.BTSelecionarFC.clicked.connect(self.FBTSelecionarFC2)
    def FBTSelecionarFC2(self):
        #print('seleccion dos')
        fecha = self.Fechador2.TXFecha.text()
        #print(fecha)
        if fecha == "":
            dialogo = QMessageBox()
            dialogo.setText("Operacion Cancelada")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()
        else:
            fecha2 = fecha
            self.Fechador2.close()
            #print(fecha2)
            fecha1 = self.fecha1
            self.fecha1 = ""
            #print(fecha1, fecha2)

            if fecha1 != "" and fecha2 != "":
                self.REPORTE(fecha1, fecha2)
            else:
                dialogo2 = QMessageBox()
                dialogo2.setText("Operacion Cancelada")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Critical)
                dialogo2.exec_()
        #Tercera Pagina#

        #Cuarta Pagina#
    def FBTListas(self):
        self.Inter.Titulo41.setText('Historial de Movimientos: Listas')
        self.Inter.TWHistorial.setColumnCount(166) #Columnas
        self.Inter.TWHistorial.setRowCount(0)  #FIlas
        self.Inter.TWHistorial.clear()
        NombreColumnas = self.Base.NomColum()
        self.Inter.BTImprimir.show()
        self.Inter.BTEditar.show()
        self.Inter.TWHistorial.setHorizontalHeaderLabels(NombreColumnas)
        
        lista = self.Listas.ConsultarListasR("ID")
        #print(datos)
        #row = 0
        i = len(lista)
        self.Inter.TWHistorial.setRowCount(i)
        tableRow = 0
        for row in lista:
            self.Id = row[0]
            z = iter(range(168)) #creamos el iterable
            for e,e2 in enumerate(z, start=0): #ciclo for con dos variables para llenar la tabla
                e2 += 1
                #print(e, e2)
                self.Inter.TWHistorial.setItem(tableRow,e,QtWidgets.QTableWidgetItem(row[e2])) #llenado simultaneo
            tableRow += 1 #agregamos una fila
            tableRow += 1

    def FBTSalidas_2(self):
        self.Inter.Titulo41.setText('Historial de Movimientos: Salidas')
        self.Inter.TWHistorial.setColumnCount(166) #Columnas
        self.Inter.TWHistorial.setRowCount(0)  #FIlas
        self.Inter.TWHistorial.clear()
        NombreColumnas = self.Base.NomColum()
        self.Inter.BTImprimir.show()
        self.Inter.BTEditar.show()
        self.Inter.TWHistorial.setHorizontalHeaderLabels(NombreColumnas)

        salida = self.Salidas.ConsultarSalidasR("ID")
        #print(datos)
        #row = 0
        i = len(salida)
        self.Inter.TWHistorial.setRowCount(i)
        tableRow = 0
        for row in salida:
            self.Id = row[0]
            z = iter(range(168)) #creamos el iterable
            for e,e2 in enumerate(z, start=0): #ciclo for con dos variables para llenar la tabla
                e2 += 1
                #print(e, e2)
                self.Inter.TWHistorial.setItem(tableRow,e,QtWidgets.QTableWidgetItem(row[e2])) #llenado simultaneo
            tableRow += 1 #agregamos una fila

    def FBTEntradas(self):
        self.Inter.Titulo41.setText('Historial de Movimientos: Entradas')
        self.Inter.TWHistorial.setColumnCount(166) #Columnas
        self.Inter.TWHistorial.setRowCount(0)  #FIlas
        self.Inter.TWHistorial.clear()
        NombreColumnas = self.Base.NomColum()
        self.Inter.BTImprimir.show()
        self.Inter.BTEditar.show()
        self.Inter.TWHistorial.setHorizontalHeaderLabels(NombreColumnas)

        entrada = self.Entradas.ConsultarEntradasR("ID")
        #print(datos)
        #row = 0
        i = len(entrada)
        self.Inter.TWHistorial.setRowCount(i)
        tableRow = 0
        for row in entrada:
            self.Id = row[0]
            z = iter(range(168)) #creamos el iterable
            for e,e2 in enumerate(z, start=0): #ciclo for con dos variables para llenar la tabla
                e2 += 1
                #print(e, e2)
                self.Inter.TWHistorial.setItem(tableRow,e,QtWidgets.QTableWidgetItem(row[e2])) #llenado simultaneo
            tableRow += 1 #agregamos una fila

    def FBTMovimientos(self):
        self.Inter.Titulo41.setText('Historial de Movimientos: Movimientos')
        self.Inter.TWHistorial.setColumnCount(11) #Columnas
        self.Inter.TWHistorial.setRowCount(0)  #FIlas
        self.Inter.TWHistorial.clear()
        NombreColumnas = self.Base.NomColumMov()
        self.Inter.BTImprimir.hide()
        self.Inter.BTEditar.hide()
        self.Inter.TWHistorial.setHorizontalHeaderLabels(NombreColumnas)

        movimiento = self.Movimientoss.ConsultarMovimientos("ID")
        #print(movimiento)
        #print(datos)
        #row = 0
        i = len(movimiento)
        self.Inter.TWHistorial.setRowCount(i)
        tableRow = 0
        for row in movimiento:
            self.Id1 = row[0]
            self.Inter.TWHistorial.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[1]))
            self.Inter.TWHistorial.setItem(tableRow,1,QtWidgets.QTableWidgetItem(row[2]))
            self.Inter.TWHistorial.setItem(tableRow,2,QtWidgets.QTableWidgetItem(row[3]))
            self.Inter.TWHistorial.setItem(tableRow,3,QtWidgets.QTableWidgetItem(row[4]))
            self.Inter.TWHistorial.setItem(tableRow,4,QtWidgets.QTableWidgetItem(row[5]))
            self.Inter.TWHistorial.setItem(tableRow,5,QtWidgets.QTableWidgetItem(row[6]))
            self.Inter.TWHistorial.setItem(tableRow,6,QtWidgets.QTableWidgetItem(row[7]))
            self.Inter.TWHistorial.setItem(tableRow,7,QtWidgets.QTableWidgetItem(str(row[8])))
            self.Inter.TWHistorial.setItem(tableRow,8,QtWidgets.QTableWidgetItem(row[9]))
            self.Inter.TWHistorial.setItem(tableRow,9,QtWidgets.QTableWidgetItem(row[10]))
            self.Inter.TWHistorial.setItem(tableRow,10,QtWidgets.QTableWidgetItem(row[11]))
            #self.Inter.TWHistorial.setItem(tableRow,11,QtWidgets.QTableWidgetItem(row[12]))
            tableRow += 1
    
    def FTWHistorialSelecionado(self):
        self.Inter.TWHistorial.viewport().setCursor(Qt.ClosedHandCursor) #Hacer que la manita se cierre
        cronometroI = time.time()
        while True:
            cronometroF = time.time()
            if cronometroF - cronometroI >= 0.2:
                self.Inter .TWHistorial.viewport().setCursor(Qt.OpenHandCursor) #Hacer que la manita se abra
                break
            else:
                #print(cronometroF - cronometroI)
                pass

    def FBTImprimir(self):
        FilaSewleccionada = self.Inter.TWHistorial.selectedItems()
        fila = [dato.text() for dato in FilaSewleccionada]
        #fila = fila[0]
        #print(fila)
        if fila == []:
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Seleccione Un elemento")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            fila = fila[0]
            mov = len(self.Inter.Titulo41.text())
            #print(mov)
            ubicacion = ""
            #print(ubicacion, "+", fila)
            if mov == 32:
                ubicacion = "Listas"
                self.IMPRIMIR(fila, ubicacion)
            elif mov == 33:
                ubicacion = "Salidas"
                self.IMPRIMIR(fila, ubicacion)
            elif mov == 34:
                ubicacion = "Entradas"
                self.IMPRIMIR(fila, ubicacion)
            else:
                print('ERROR')

    def FBTEditar(self):
        FilaSewleccionada = self.Inter.TWHistorial.selectedItems()
        fila = [dato.text() for dato in FilaSewleccionada]
        #fila = fila[0]
        #print(fila)
        if fila == []:
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Seleccione Un elemento")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            fila = fila[0]
            mov = len(self.Inter.Titulo41.text())
            #print(mov)
            ubicacion = ""
            #print(ubicacion, "+", fila)
            if mov == 32:
                ubicacion = "Listas"
                self.EDITAR(fila, ubicacion)
            elif mov == 33:
                ubicacion = "Salidas"
                self.EDITAR(fila, ubicacion)
            elif mov == 34:
                ubicacion = "Entradas"
                self.EDITAR(fila, ubicacion)
            else:
                print('ERROR')
        #Cuarta Pagina#

        #Quinta Pagina#
    def FBTBuscar(self):
        buscar = self.Inter.CBBuscar.currentText()
        #print(buscar)
        if buscar == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Seleccione Un Producto")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            busc = self.Proveedoress.BuscarProveedoresN(buscar)[0]
            #print(busc)
            if busc == "":
                dialogo2 = QMessageBox()
                dialogo2.setText("El Producto Selecionado No Existe")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                self.Inter.TXProveedor_2.setText(busc[1]) #Proveedor#
                self.Inter.TXCorreo.setText(busc[3]) #Correo#
                self.Inter.TXNum.setText(busc[2]) #Numero#
                self.Inter.TXTelefono.setText(busc[4]) #Telefono#


    def FBTIngresar(self):
        if self.Inter.TXProveedor_2.text() == "" or self.Inter.TXNum.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor LLene Correctamente Los Campos del Formulario")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
            if pregunta == QMessageBox.Yes:
                buscar = self.Inter.TXNum.text()

                verificar = self.Proveedoress.BuscarProveedores(buscar)
                #print(verificar)

                if verificar != []:
                    dialogo = QMessageBox()
                    dialogo.setText("La Clave ya esta Registrada en la Base de Datos")
                    dialogo.setWindowTitle("DesinGlass Smart Windows")
                    dialogo.setWindowIcon(QIcon('DG.png'))
                    dialogo.setIcon(QMessageBox.Critical)
                    dialogo.exec_()

                else:
                    #print('paso')
                    Proveedor = self.Inter.TXProveedor_2.text()
                    Numero = self.Inter.TXNum.text()
                    Correo = self.Inter.TXCorreo.text()
                    Telefono = self.Inter.TXTelefono.text()

                    self.Proveedoress.AgregarProveedores(Proveedor.capitalize(), Numero, Correo, Telefono)

                    dialogoB = QMessageBox()
                    dialogoB.setText("Se Ha Guardado Correctamete")
                    dialogoB.setWindowTitle("DesinGlass Smart Windows")
                    dialogoB.setWindowIcon(QIcon('DG.png'))
                    dialogoB.setIcon(QMessageBox.Information)
                    dialogoB.exec_()

                    #REFRESCAR INFORMACION#
                    self.Refrescar5()
                    self.LLenarCBBuscar1()
                    self.FBTLimpiar_2()
                    self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
                    #REFRESCAR INFORMACION#
            else:
                dialogo2 = QMessageBox()
                dialogo2.setText("Operacion Cancelada")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()

    def FBTLimpiar_2(self):
        self.Inter.CBBuscar.setCurrentText("") #Buscar#
        self.Inter.TXProveedor_2.clear() #Proveedor#
        self.Inter.TXNum.clear() #Numero#
        self.Inter.TXCorreo.clear() #Correo#
        self.Inter.TXTelefono.clear() #Telefono#

    def FBTActualizar_2(self):
        if self.Inter.TXProveedor_2.text() == "" or self.Inter.TXNum.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor LLene Correctamente Los Campos del Formulario")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
            if pregunta == QMessageBox.Yes:
                buscar = self.Inter.TXNum.text()
                #print(buscar)
                if buscar == "":
                    dialogo = QMessageBox()
                    dialogo.setText("Por Favor Seleccione Un Proveedor Para Actualizar")
                    dialogo.setWindowTitle("DesinGlass Smart Windows")
                    dialogo.setWindowIcon(QIcon('DG.png'))
                    dialogo.setIcon(QMessageBox.Warning)
                    dialogo.exec_()
                else:
                    busc = self.Proveedoress.BuscarProveedores(buscar)[0]
                    #print(busc)
                    if busc == "":
                        dialogo2 = QMessageBox()
                        dialogo2.setText("El Proveedor Selecionado No Existe")
                        dialogo2.setWindowTitle("DesinGlass Smart Windows")
                        dialogo2.setWindowIcon(QIcon('DG.png'))
                        dialogo2.setIcon(QMessageBox.Warning)
                        dialogo2.exec_()
                    else:
                        Proveedor = self.Inter.TXProveedor_2.text() #Proveedor#
                        Numero = self.Inter.TXNum.text() #Numero#
                        Correo = self.Inter.TXCorreo.text() #Correo#
                        Telefono = self.Inter.TXTelefono.text() #Telefono#

                        ID = busc[0]

                        self.Proveedoress.ActualizarProveedores( ID, Proveedor.capitalize(), Numero, Correo, Telefono)

                        #REFRESCAR INFORMACION#
                        self.Refrescar5()
                        self.LLenarCBBuscar1()
                        self.FBTLimpiar_2()
                        self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
                        #REFRESCAR INFORMACION#

                        dialogoB = QMessageBox()
                        dialogoB.setText("Se Ha Guardado Correctamete")
                        dialogoB.setWindowTitle("DesinGlass Smart Windows")
                        dialogoB.setWindowIcon(QIcon('DG.png'))
                        dialogoB.setIcon(QMessageBox.Information)
                        dialogoB.exec_()
            else:
                dialogo2 = QMessageBox()
                dialogo2.setText("Operacion Cancelada")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()

    def FBTEliminar(self):
        eliminar = self.Inter.TXNum.text() #Numero#

        if eliminar == "" or self.Inter.TXProveedor_2.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor LLene Correctamente Los Campos del Formulario")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
            if pregunta == QMessageBox.Yes:
                buscar = self.Inter.TXNum.text()
                #print(buscar)
                if buscar == "":
                    dialogo = QMessageBox()
                    dialogo.setText("Por Favor Seleccione Un Proveedor Para Actualizar")
                    dialogo.setWindowTitle("DesinGlass Smart Windows")
                    dialogo.setWindowIcon(QIcon('DG.png'))
                    dialogo.setIcon(QMessageBox.Warning)
                    dialogo.exec_()
                else:
                    busc = self.Proveedoress.BuscarProveedores(buscar)[0]
                    #print(busc)
                    if busc == "":
                        dialogo2 = QMessageBox()
                        dialogo2.setText("El Proveedor Selecionado No Existe")
                        dialogo2.setWindowTitle("DesinGlass Smart Windows")
                        dialogo2.setWindowIcon(QIcon('DG.png'))
                        dialogo2.setIcon(QMessageBox.Warning)
                        dialogo2.exec_()
                    else:
                        Numero = busc[2]

                        self.Proveedoress.EliminarProveedores(Numero)

                        #REFRESCAR INFORMACION#
                        self.Refrescar5()
                        self.LLenarCBBuscar1()
                        self.FBTLimpiar_2()
                        self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
                        #REFRESCAR INFORMACION#

                        dialogoB = QMessageBox()
                        dialogoB.setText("Se Ha Eliminado Correctamete")
                        dialogoB.setWindowTitle("DesinGlass Smart Windows")
                        dialogoB.setWindowIcon(QIcon('DG.png'))
                        dialogoB.setIcon(QMessageBox.Information)
                        dialogoB.exec_()
            else:
                dialogo2 = QMessageBox()
                dialogo2.setText("Operacion Cancelada")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()

    def LLenarCBBuscar1(self):
        self.Inter.CBBuscar.clear()
        datos = self.Proveedoress.ConsultarProveedores()
        i = len(datos)
        self.Inter.TWProveedores.setRowCount(i)
        self.Inter.CBBuscar.addItem("")
        for row in datos:
            self.Inter.CBBuscar.addItem(row[1])

    def MostarTWProveedores(self):
        datos = self.Proveedoress.ConsultarProveedores()
        #print(datos)
        #row = 0
        i = len(datos)
        self.Inter.TWProveedores.setRowCount(i)
        tableRow = 0
        for row in datos:
            self.Id = row[0]
            #print(row[7])
            self.Inter.TWProveedores.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[1])) #Producto
            self.Inter.TWProveedores.setItem(tableRow,1,QtWidgets.QTableWidgetItem(row[2])) #Clave
            self.Inter.TWProveedores.setItem(tableRow,2,QtWidgets.QTableWidgetItem(row[3])) #Numero
            self.Inter.TWProveedores.setItem(tableRow,3,QtWidgets.QTableWidgetItem(row[4])) #Telefono

            tableRow += 1

    def FTWProveedorSelecionado(self):
        FilaSewleccionada = self.Inter.TWProveedores.selectedItems()
        fila = [dato.text() for dato in FilaSewleccionada]
        #fila = fila[1]
        #print(fila)
        self.Inter.TXProveedor_2.setText(fila[0]) #Proveedor#
        self.Inter.TXCorreo.setText(fila[2]) #Correo#
        self.Inter.TXNum.setText(fila[1]) #Numero#
        self.Inter.TXTelefono.setText(fila[3]) #Telefono#

        self.Inter.CBBuscar.setCurrentText("")

        self.Inter.TWProveedores.viewport().setCursor(Qt.ClosedHandCursor) #Hacer que la manita se cierre
        cronometroI = time.time()
        while True:
            cronometroF = time.time()
            if cronometroF - cronometroI >= 0.2:
                self.Inter .TWProveedores.viewport().setCursor(Qt.OpenHandCursor) #Hacer que la manita se abra
                break
            else:
                #print(cronometroF - cronometroI)
                pass

    def LimpiarTWProveedores(self):
        self.Inter.TWProveedores.clearContents()
        self.Inter.TWProveedores.setRowCount(0)
        #Quinta Pagina#

        #Sexta Pagina#
    #=========Entradas==========#
    def FBTIngresar_2(self):
        self.Inter.Libro1.setCurrentWidget(self.Inter.Ingresos)
    
    def Validacion61(self):
        x = QDoubleValidator()
        self.Inter.TXCantidad.setValidator(x)

    def FBTLimpiarTodo(self):
        self.Inter.TXFolio.clear()
        self.Inter.TXObra.clear()
        self.Inter.TXAlmacen.clear()
        self.Inter.TXSolicita.clear()
        self.Inter.TXAutoriza.clear()
        self.Inter.TXOrdComp.clear()
        self.Inter.TXFolFact.clear()

        #===========LIMPIAR LISTA===========#
        lipL = self.Lista.ConsultarLista()
        if lipL == []:
            pass
        else:
            #print(lipL)
            for i in lipL:
                eliminar = i[0]
                self.Lista.EliminarLista(eliminar)
                #print(eliminar, " Eliminado")
        #===========LIMPIAR LISTA===========#

        #===========LIMPIAR ENCABEZADO===========#
        lipE = self.Encabezado.ConsultarEncabezado()
        if lipE == []:
            pass
        else:
            #print(lipE)
            for i2 in lipE:
                eliminar2 = i2[0]
                self.Encabezado.EliminarEncabezado(eliminar2)
                #print(eliminar2, " Eliminado")
        #===========LIMPIAR ENCABEZADO===========#
                
        #===========REFRESCAR INFORMACION===========#
        self.Refrescar5()
        self.LimpiarTWLista()
        self.MostarTWLista()
        self.LLenarCBBuscar_3()
        self.FBTLimpiar_4()
        self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
        #===========REFRESCAR INFORMACION===========#

    def FBTLimpiar_4(self):
        self.Inter.TXProducto_2.clear() #Producto
        self.Inter.TXStock_3.clear() #Stock Actual
        self.Inter.TXUnidad_2.clear() #Unidad
        self.Inter.TXCantidad.clear() #Cantidad
        self.Inter.TXAncho.clear() #Ancho
        self.Inter.TXClave_3.clear() #Clave
        self.Inter.TXLugar_2.clear() #Lugar
        self.Inter.TXLargo.clear() #Largo
        self.Inter.TXFolioReq.clear() #Folio REQ
        self.Inter.Imagen_1.clear() #Limpiar _1
        self.Inter.CBBuscar_3.setCurrentText("") #Lipiar Buscar
        self.Inter.Imagen_1.setText('Imagen') #Poner Texto Imagen
        #self.Inter.TXSetProducto.clear()
        #self.Inter.TXUltFol

    def FBTAgregar(self):
        if self.Inter.TXProducto_2.text() == "" and self.Inter.TXStock_3.text() == "" and self.Inter.TXUnidad_2.text() == "" and self.Inter.TXCantidad.text() == "" and self.Inter.TXAncho.text() == "" and self.Inter.TXClave_3.text() == "" and self.Inter.TXLugar_2.text() == "" and self.Inter.TXLargo.text() == "" and self.Inter.TXFolioReq.text() == "":
            pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Quiere Guardar el Encabezado?", QMessageBox.Yes | QMessageBox.No)
            if pregunta == QMessageBox.Yes:
                #Actualizar Encabezado#
                Folio1 = self.Inter.TXFolio.text() #Folio
                Obra1 = self.Inter.TXObra.text() #Obra
                Solicita1 =self.Inter.TXSolicita.text() #Solicita
                Autoriza1 = self.Inter.TXAutoriza.text() #Autoriza
                Almacen1 = self.Inter.TXAlmacen.text() #Almacen
                OrComp1 = self.Inter.TXOrdComp.text() #Orden de Compra
                FolFact1 = self.Inter.TXFolFact.text() #Folio Factura
                Observaciones1 = self.Inter.TXObservaciones_2.toPlainText() #Observaciones
                TPMov1 = "Entrada"

                enc1 = self.Encabezado.ConsultarEncabezado()
                if enc1 == []:
                    self.Encabezado.AgregarEncabezado(Folio1,Obra1.capitalize(),Solicita1.capitalize(),Autoriza1.capitalize(),Almacen1.capitalize(),OrComp1,FolFact1, Observaciones1, TPMov1)
                else:
                    ref1 = enc1[0]
                    if ref1[0] == Folio1:
                        self.Encabezado.ActualizarEncabezado(Folio1, Folio1, Obra1.capitalize(), Solicita1.capitalize(), Autoriza1.capitalize(), Almacen1.capitalize(), OrComp1, FolFact1, Observaciones1, TPMov1)
                    else:
                        self.Encabezado.ActualizarEncabezado(ref1[0], Folio1, Obra1.capitalize(), Solicita1.capitalize(), Autoriza1.capitalize(), Almacen1.capitalize(), OrComp1, FolFact1, Observaciones1, TPMov1)
                #Actualizar Encabezado#
            else:
                pass
        else:
            if self.Inter.TXProducto_2.text() == "" or self.Inter.TXStock_3.text() == "" or self.Inter.TXUnidad_2.text() == "" or self.Inter.TXCantidad.text() == "" or self.Inter.TXClave_3.text() == "" or self.Inter.TXLugar_2.text() == "":
                dialogo = QMessageBox()
                dialogo.setText("Por Favor LLene Correctamente Los Campos del Formulario")
                dialogo.setWindowTitle("DesinGlass Smart Windows")
                dialogo.setWindowIcon(QIcon('DG.png'))
                dialogo.setIcon(QMessageBox.Warning)
                dialogo.exec_()
            else:
                clave = self.Inter.TXClave_3.text()
                nomenclatura = clave[0:3]
                #print(nomenclatura)
                if nomenclatura != "VD-":
                    #print('no es vidrio')
                    datos = self.Lista.ConsultarLista()
                    e = len(datos)
                    #print(datos)
                    #print(i)
                    duplicado = ""
                    for i in datos: #Validar que no haya productos repetidos#
                        if i[1] == clave: 
                            duplicado = True
                            break
                        else:
                            duplicado = False

                    if duplicado == True:
                        dialogo1 = QMessageBox()
                        dialogo1.setText("El Producto Ya Esta Ingresado en La Lista")
                        dialogo1.setWindowTitle("DesinGlass Smart Windows")
                        dialogo1.setWindowIcon(QIcon('DG.png'))
                        dialogo1.setIcon(QMessageBox.Critical)
                        dialogo1.exec_()
                    else:
                        #print('lalalal')
                        busc = self.Base.BuscarProducto(clave)[0]
                        #print(busc)
                        if busc == []:
                            dialogo2 = QMessageBox()
                            dialogo2.setText("El Producto Selecionado No Existe")
                            dialogo2.setWindowTitle("DesinGlass Smart Windows")
                            dialogo2.setWindowIcon(QIcon('DG.png'))
                            dialogo2.setIcon(QMessageBox.Warning)
                            dialogo2.exec_()
                        else:
                            Numero = busc[3] #Numero
                            Marca = busc[4] #Marca
                            Color = busc[5] #Color
                            Proveedor = busc[8] #Proveedor
                            Stock =  busc[7] #Stock
                            TPMov = "Entrada" #Tipo de Movimiento

                        ID = e + 1

                        for i2 in datos: #Validar que no haya ID repetido#
                            if int(i2[0]) == ID: 
                                ID += 1
                            else:
                                ID = ID

                        #print(ID)
                        Referencia = self.Inter.TXClave_3.text() #CLave
                        Descripcion = self.Inter.TXProducto_2.text() #Producto
                        Unidad = self.Inter.TXUnidad_2.text() #Unidad
                        Cantidad = self.Inter.TXCantidad.text() #Cantidad
                        Ancho = self.Inter.TXAncho.text() #Ancho
                        Largo = self.Inter.TXLargo.text() #Largo
                        Lugar = self.Inter.TXLugar_2.text() #Lugar
                        FolioREQ = self.Inter.TXFolioReq.text() #Folio REQ

                        if int(Cantidad) <= 0:
                            dialogo3 = QMessageBox()
                            dialogo3.setText("La Cantidad Ingresada es Mayor al Stock Actual")
                            dialogo3.setWindowTitle("DesinGlass Smart Windows")
                            dialogo3.setWindowIcon(QIcon('DG.png'))
                            dialogo3.setIcon(QMessageBox.Warning)
                            dialogo3.exec_()
                        else:
                            if len(datos) < 20:
                                self.Lista.AgregarLista(ID, Referencia, Descripcion.capitalize(),Unidad.capitalize(),Cantidad,Ancho,Largo,Lugar.capitalize(),FolioREQ,Numero.capitalize(),Marca.capitalize(),Color.capitalize(),Proveedor.capitalize(),Stock,TPMov)

                                #Actualizar Encabezado#
                                Folio = self.Inter.TXFolio.text() #Folio
                                Obra = self.Inter.TXObra.text() #Obra
                                Solicita =self.Inter.TXSolicita.text() #Solicita
                                Autoriza = self.Inter.TXAutoriza.text() #Autoriza
                                Almacen = self.Inter.TXAlmacen.text() #Almacen
                                OrComp = self.Inter.TXOrdComp.text() #Orden de Compra
                                FolFact = self.Inter.TXFolFact.text() #Folio Factura
                                Observaciones = self.Inter.TXObservaciones_2.toPlainText() #Observaciones

                                enc = self.Encabezado.ConsultarEncabezado()
                                if enc == []:
                                    self.Encabezado.AgregarEncabezado(Folio,Obra.capitalize(),Solicita.capitalize(),Autoriza.capitalize(),Almacen.capitalize(),OrComp,FolFact, Observaciones, TPMov)
                                else:
                                    ref = enc[0]
                                    if ref[0] == Folio:
                                        self.Encabezado.ActualizarEncabezado(Folio, Folio, Obra.capitalize(), Solicita.capitalize(), Autoriza.capitalize(), Almacen.capitalize(), OrComp, FolFact, Observaciones, TPMov)
                                    else:
                                        self.Encabezado.ActualizarEncabezado(ref[0], Folio, Obra.capitalize(), Solicita.capitalize(), Autoriza.capitalize(), Almacen.capitalize(), OrComp, FolFact, Observaciones, TPMov)
                                #Actualizar Encabezado#

                                dialogoB = QMessageBox()
                                dialogoB.setText("Se Ha Guardado Correctamete")
                                dialogoB.setWindowTitle("DesinGlass Smart Windows")
                                dialogoB.setWindowIcon(QIcon('DG.png'))
                                dialogoB.setIcon(QMessageBox.Information)
                                dialogoB.exec_()

                                #REFRESCAR INFORMACION#
                                self.Refrescar6()
                                self.LimpiarTWLista()
                                self.MostarTWLista()
                                self.LLenarCBBuscar_3()
                                self.FBTLimpiar_4()
                                #REFRESCAR INFORMACION#
                            else:
                                dialogoE = QMessageBox()
                                dialogoE.setText("La Lista Ya Esta LLena")
                                dialogoE.setWindowTitle("DesinGlass Smart Windows")
                                dialogoE.setWindowIcon(QIcon('DG.png'))
                                dialogoE.setIcon(QMessageBox.Critical)
                                dialogoE.exec_()
                else:
                    datos = self.Lista.ConsultarLista()
                    e = len(datos)
                    #print('es vidrio')
                    busc = self.Base.BuscarProducto(clave)[0]
                    #print(busc)
                    if busc == "":
                        dialogo2 = QMessageBox()
                        dialogo2.setText("El Producto Selecionado No Existe")
                        dialogo2.setWindowTitle("DesinGlass Smart Windows")
                        dialogo2.setWindowIcon(QIcon('DG.png'))
                        dialogo2.setIcon(QMessageBox.Warning)
                        dialogo2.exec_()
                    else:
                        Numero = busc[3] #Numero
                        Marca = busc[4] #Marca
                        Color = busc[5] #Color
                        Proveedor = busc[8] #Proveedor
                        Stock =  busc[7] #Stock
                        TPMov = "Entrada" #Tipo de Movimiento

                        ID = e + 1

                        for i2 in datos: #Validar que no haya ID repetido#
                            if int(i2[0]) == ID: 
                                ID += 1
                            else:
                                ID = ID

                        #print(ID)
                        Referencia = self.Inter.TXClave_3.text() #CLave
                        Descripcion = self.Inter.TXProducto_2.text() #Producto
                        Unidad = self.Inter.TXUnidad_2.text() #Unidad
                        Cantidad = self.Inter.TXCantidad.text() #Cantidad
                        Ancho = self.Inter.TXAncho.text() #Ancho
                        Largo = self.Inter.TXLargo.text() #Largo
                        Lugar = self.Inter.TXLugar_2.text() #Lugar
                        FolioREQ = self.Inter.TXFolioReq.text() #Folio REQ

                        if int(Cantidad) <= 0:
                            dialogo3 = QMessageBox()
                            dialogo3.setText("La Cantidad Ingresada es Mayor al Stock Actual")
                            dialogo3.setWindowTitle("DesinGlass Smart Windows")
                            dialogo3.setWindowIcon(QIcon('DG.png'))
                            dialogo3.setIcon(QMessageBox.Warning)
                            dialogo3.exec_()
                        else:
                            if len(datos) <20:
                                self.Lista.AgregarLista(ID, Referencia, Descripcion.capitalize(),Unidad.capitalize(),Cantidad,Ancho,Largo,Lugar.capitalize(),FolioREQ,Numero.capitalize(),Marca.capitalize(),Color.capitalize(),Proveedor.capitalize(),Stock,TPMov)

                                #Actualizar Encabezado#
                                Folio = self.Inter.TXFolio.text() #Folio
                                Obra = self.Inter.TXObra.text() #Obra
                                Solicita =self.Inter.TXSolicita.text() #Solicita
                                Autoriza = self.Inter.TXAutoriza.text() #Autoriza
                                Almacen = self.Inter.TXAlmacen.text() #Almacen
                                OrComp = self.Inter.TXOrdComp.text() #Orden de Compra
                                FolFact = self.Inter.TXFolFact.text() #Folio Factura
                                Observaciones = self.Inter.TXObservaciones_2.toPlainText() #Observaciones

                                enc = self.Encabezado.ConsultarEncabezado()
                                if enc == []:
                                    self.Encabezado.AgregarEncabezado(Folio,Obra.capitalize(),Solicita.capitalize(),Autoriza.capitalize(),Almacen.capitalize(),OrComp,FolFact, Observaciones, TPMov)
                                else:
                                    ref = enc[0]
                                    if ref[0] == Folio:
                                        self.Encabezado.ActualizarEncabezado(Folio, Folio, Obra.capitalize(), Solicita.capitalize(), Autoriza.capitalize(), Almacen.capitalize(), OrComp, FolFact, Observaciones, TPMov)
                                    else:
                                        self.Encabezado.ActualizarEncabezado(ref[0], Folio, Obra.capitalize(), Solicita.capitalize(), Autoriza.capitalize(), Almacen.capitalize(), OrComp, FolFact, Observaciones, TPMov)
                                #Actualizar Encabezado#

                                dialogoB = QMessageBox()
                                dialogoB.setText("Se Ha Guardado Correctamete")
                                dialogoB.setWindowTitle("DesinGlass Smart Windows")
                                dialogoB.setWindowIcon(QIcon('DG.png'))
                                dialogoB.setIcon(QMessageBox.Information)
                                dialogoB.exec_()

                                #REFRESCAR INFORMACION#
                                self.Refrescar6()
                                self.LimpiarTWLista()
                                self.MostarTWLista()
                                self.LLenarCBBuscar_3()
                                self.FBTLimpiar_4()
                                #REFRESCAR INFORMACION#
                            else:
                                    dialogoE = QMessageBox()
                                    dialogoE.setText("La Lista Ya Esta LLena")
                                    dialogoE.setWindowTitle("DesinGlass Smart Windows")
                                    dialogoE.setWindowIcon(QIcon('DG.png'))
                                    dialogoE.setIcon(QMessageBox.Critical)
                                    dialogoE.exec_()

    def FBTBuscar_3(self):
        buscar = self.Inter.CBBuscar_3.currentText()
        #print(buscar)
        if buscar == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Seleccione Un Producto")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            busc = self.Base.BuscarProductoN(buscar)[0]
            #print(busc)
            if busc == "":
                dialogo2 = QMessageBox()
                dialogo2.setText("El Producto Selecionado No Existe")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                self.Inter.TXProducto_2.setText(busc[1]) #Producto#
                self.Inter.TXStock_3.setText(str(busc[7])) #Stock Actual#
                self.Inter.TXUnidad_2.setText(busc[6]) #Unidad#
                self.Inter.TXClave_3.setText(busc[2]) #Clave#
                
                Imagen = busc[12]
                #print(Imagen)
                if Imagen == "" or Imagen == None or Imagen == b'':
                    Imagen = os.getcwd() + "\DG.png"
                    Imagen = Imagen.replace("/", chr(92))

                    pixmapImage = QPixmap(Imagen).scaled(200,200,Qt.KeepAspectRatio,Qt.SmoothTransformation)
                    self.Inter.Imagen_1.setPixmap(pixmapImage)
                else:
                    foto = QPixmap()
                    foto.loadFromData(Imagen, "PNG", Qt.AutoColor)
                    self.Inter.Imagen_1.setPixmap(foto)

    def FBTGuardar_2(self):
        lista = self.Lista.ConsultarLista()
        if lista == []:
            dialogo = QMessageBox()
            dialogo.setText("La Lista Actualmente se Encuentra en Blanco")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            if self.Inter.TXFolio.text() == "" or self.Inter.TXObra.text() == "" or self.Inter.TXAlmacen.text() == "" or self.Inter.TXSolicita.text() == "" or self.Inter.TXAutoriza.text() == "":
                dialogo2 = QMessageBox()
                dialogo2.setText("Por Favor LLene Correctamente El Encabezado")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
                if pregunta == QMessageBox.Yes:
                    verificar = self.Entradas.BuscarEntradas(self.Inter.TXFolio.text())
                    if verificar == []:
                        #print(len(lista))
                        entrada = [] #Esta lista dara todos los parametros para registrar la entrada del producto
                        entrada.append(self.Inter.TXFolio.text()) #Folio
                        entrada.append(self.Inter.TXObra.text()) #Obra

                        fecha = self.Base.FechaLetra() #Mandamos a llamar a la fucion Fechador para que retorne la fecha actual
                        fechaa = fecha[6]
        
                        entrada.append(fechaa) #Feha
                        entrada.append(self.Inter.TXSolicita.text()) #Solicita
                        entrada.append(self.Inter.TXAutoriza.text()) #Autoriza
                        entrada.append(self.Inter.TXAlmacen.text()) #Almacen
                        
                        #========================CICLO PARA DESCONTEO, REGISTRO Y CREACION DE LISTA========================#
                        for i in lista:
                            #entrada.append(i[0]) #ID
                            entrada.append(i[1]) #Referencia
                            entrada.append(i[2]) #Descripcion
                            entrada.append(i[3]) #Unidad
                            entrada.append(i[4]) #Cantidad
                            entrada.append(i[5]) #Ancho
                            entrada.append(i[6]) #Largo
                            entrada.append(i[7]) #Lugar
                            entrada.append(i[8]) #FolioREQ
                            #entrada.append(i[9]) #Numero
                            #entrada.append(i[10]) #Marca
                            #entrada.append(i[11]) #Color
                            #entrada.append(i[12]) #Proveedor
                            #entrada.append(i[13]) #Stock
                            #entrada.append(i[14]) #Tipo de Movimiento

                            #========================CREAR REGISTRO EN MOVIMIENTOS========================#
                            buscar = i[1]
                            busc = self.Base.BuscarProducto(buscar)
                            #print(busc)
                            if busc == []:
                                dialogo2 = QMessageBox()
                                dialogo2.setText("El Producto: '{}' No Existe \n No se Desconto del Inventario".format(i[2]))
                                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                                dialogo2.setWindowIcon(QIcon('DG.png'))
                                dialogo2.setIcon(QMessageBox.Critical)
                                dialogo2.exec_()
                            else:
                                busc = busc[0] #se selecciona el unico valor de la lista
                                Nombre = busc[1] #Producto#
                                Clave = busc[2] #Clave#
                                Numero = busc[3] #Numero#
                                Color = busc[5] #Color#
                                Marca = busc[4] #Marca#
                                Unidad = busc[6] #Unidad#
                                Proveedor = busc[8] #Proveedor#
                                Lugar = busc[9] #Lugar#

                                ID = busc[0]
                                Stock = busc[7] + i[4]
                                PCompra = busc[10]
                                PVenta = busc[11]

                                foto = busc[12]

                                self.Base.ActualizarProducto( ID, Nombre, Clave, Numero, Marca, Color, Unidad, Stock, Proveedor, Lugar, PCompra, PVenta, foto)
                                #print('Desconteo Registrado')

                            #========================CREAR REGISTRO EN MOVIMIENTOS========================#

                            #========================CREAR REGISTRO EN MOVIMIENTOS========================#
                            TipMov = "Entrada"
                            Nombre = i[2]
                            Clave = i[1]
                            Numero = i[9]
                            Marca = i[10]
                            Color = i[11]
                            Unidad = i[3]
                            Cantidad = i[4]
                            Proveedor = i[12]
                            Lugar = i[7]
                            Fecha = str(fecha[0])

                            self.Movimientoss.AgregarMovimientos(TipMov.capitalize(), Nombre, Clave, Numero, Marca, Color, Unidad, Cantidad, Proveedor, Lugar, Fecha)
                            #print('Movimiento Registrado')
                            #========================CREAR REGISTRO EN MOVIMIENTOS========================#

                        #========================CICLO PARA DESCONTEO, REGISTRO Y CREACION DE LISTA========================#
                            
                        Faltante = len(entrada)
                        #print(Faltante)
                        for i2 in range(0, 166-Faltante):
                            entrada.append("")

                        entrada.append(self.Inter.TXOrdComp.text()) #Orden de Compra
                        entrada.append(self.Inter.TXFolFact.text()) #Folio Factura
                        entrada.append(self.Inter.TXObservaciones_2.toPlainText()) #Observaciones
                        #print(entrada)
                        #print(len(entrada)) #Verificamos que nos arroje 169 datos para el correcto registro

                        self.Entradas.AgregarEntradasL(entrada) #Creamos el registro

                        #========================LIMPIAR Y REFRESCAR========================#
                        self.FBTLimpiarTodo()

                        self.Refrescar6()
                        self.LimpiarTWLista()
                        self.MostarTWLista()
                        self.LLenarCBBuscar_3()
                        self.FBTLimpiar_4()
                        self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
                        #========================LIMPIAR Y REFRESCAR========================#

                        dialogo3 = QMessageBox()
                        dialogo3.setText("Se Ha Guardado Correctamete")
                        dialogo3.setWindowTitle("DesinGlass Smart Windows")
                        dialogo3.setWindowIcon(QIcon('DG.png'))
                        dialogo3.setIcon(QMessageBox.Information)
                        dialogo3.exec_()
                    else:
                        dialogo4 = QMessageBox()
                        dialogo4.setText("El Folio Ya Esta Registrado")
                        dialogo4.setWindowTitle("DesinGlass Smart Windows")
                        dialogo4.setWindowIcon(QIcon('DG.png'))
                        dialogo4.setIcon(QMessageBox.Warning)
                        dialogo4.exec_()
                else:
                    dialogo2 = QMessageBox()
                    dialogo2.setText("Operacion Cancelada")
                    dialogo2.setWindowTitle("DesinGlass Smart Windows")
                    dialogo2.setWindowIcon(QIcon('DG.png'))
                    dialogo2.setIcon(QMessageBox.Warning)
                    dialogo2.exec_()

    def FBTEliminar_2(self):
        if self.Inter.TXSetProducto.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Seleccione un Producto Para Eliminar")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            eliminar = self.Inter.TXSetProducto.text()
            busc = self.Lista.BuscarLista(eliminar)[0]
            #busc = self.Base.BuscarProducto(eliminar)
            #print(busc)
            if busc == []:
                dialogo2 = QMessageBox()
                dialogo2.setText("El Producto Selecionado No Existe")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Eliminar el Producto de la Lista?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if pregunta == QMessageBox.Yes:
                    ID = busc[0]
                    self.Lista.EliminarLista(ID)

                    dialogoB = QMessageBox()
                    dialogoB.setText("Se Ha Eliminado Correctamete")
                    dialogoB.setWindowTitle("DesinGlass Smart Windows")
                    dialogoB.setWindowIcon(QIcon('DG.png'))
                    dialogoB.setIcon(QMessageBox.Information)
                    dialogoB.exec_()

                    #REFRESCAR INFORMACION#
                    self.Refrescar5()
                    self.LimpiarTWLista()
                    self.MostarTWLista()
                    self.LLenarCBBuscar_3()
                    self.FBTLimpiar_4()
                    #REFRESCAR INFORMACION#
                else:
                    dialogoC = QMessageBox()
                    dialogoC.setText("Operacion Cancelada")
                    dialogoC.setWindowTitle("DesinGlass Smart Windows")
                    dialogoC.setWindowIcon(QIcon('DG.png'))
                    dialogoC.setIcon(QMessageBox.Warning)
                    dialogoC.exec_()

    def FBTLimpObs_2(self):
        self.Inter.TXObservaciones_2.clear()

    def LLenarCBBuscar_3(self):
        self.Inter.CBBuscar_3.clear()
        datos = self.Base.ConsultarProductos()
        i = len(datos)
        self.Inter.TWProductos.setRowCount(i)
        self.Inter.CBBuscar_3.addItem("")
        for row in datos:
            self.Inter.CBBuscar_3.addItem(row[1])

    def FTWListaSelecionado(self):
        FilaSewleccionada = self.Inter.TWLista.selectedItems()
        fila = [dato.text() for dato in FilaSewleccionada]
        #fila = fila[1]
        #print(fila)
        self.Inter.TXSetProducto.setText(fila[0]) #Producto Seleccionado#

        self.Inter.TWLista.viewport().setCursor(Qt.ClosedHandCursor) #Hacer que la manita se cierre
        cronometroI = time.time()
        while True:
            cronometroF = time.time()
            if cronometroF - cronometroI >= 0.2:
                self.Inter .TWLista.viewport().setCursor(Qt.OpenHandCursor) #Hacer que la manita se abra
                break
            else:
                #print(cronometroF - cronometroI)
                pass

    def FTWProductos_2Selecionado(self):
        FilaSewleccionada = self.Inter.TWProductos_2.selectedItems()
        fila = [dato.text() for dato in FilaSewleccionada]
        fila = fila[0]
        #print(fila)
        
        busc = self.Base.BuscarProductoN(fila)[0]
        #print(busc)
        if busc == "":
            dialogo2 = QMessageBox()
            dialogo2.setText("El Producto Selecionado No Existe")
            dialogo2.setWindowTitle("DesinGlass Smart Windows")
            dialogo2.setWindowIcon(QIcon('DG.png'))
            dialogo2.setIcon(QMessageBox.Warning)
            dialogo2.exec_()
        else:
            #print(busc)
            self.Inter.TXProducto_2.setText(busc[1]) #Producto#
            self.Inter.TXStock_3.setText(str(busc[7])) #Stock Actual#
            self.Inter.TXUnidad_2.setText(busc[6]) #Unidad#
            self.Inter.TXClave_3.setText(busc[2]) #Clave#

            Image = busc[12]
            #print(Image)
            if Image == "" or Image == None or Image == b'':
                Image = os.getcwd() + "\DG.png"
                Image = Image.replace("/", chr(92))

                pixmapImage = QPixmap(Image).scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation)
                self.Inter.Imagen_1.setPixmap(pixmapImage)
            else:
                foto = QPixmap()
                foto.loadFromData(Image, "PNG", Qt.AutoColor)
                self.Inter.Imagen_1.setPixmap(foto)

        self.Inter.CBBuscar_3.setCurrentText("")

    def MostarTWProductos_2(self):
        datos = self.Base.ConsultarProductos()
        #print(datos)
        #row = 0
        i = len(datos)
        self.Inter.TWProductos_2.setRowCount(i)
        tableRow = 0
        for row in datos:
            self.Id = row[0]
            #print(row[7])
            self.Inter.TWProductos_2.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[1])) #Producto

            tableRow += 1
    def LimpiarTWProductos_2(self):
        self.Inter.TWProductos_2.clearContents()
        self.Inter.TWProductos_2.setRowCount(0)

    def MostarTWLista(self):
        datos = self.Lista.ConsultarLista()
        #print(datos)
        #row = 0
        i = len(datos)
        self.Inter.TWLista.setRowCount(i)
        tableRow = 0
        for row in datos:
            self.Id = row[0]
            #print(row)
            self.Inter.TWLista.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[1])) #Referencia
            self.Inter.TWLista.setItem(tableRow,1,QtWidgets.QTableWidgetItem(row[2])) #Descripcion
            self.Inter.TWLista.setItem(tableRow,2,QtWidgets.QTableWidgetItem(row[3])) #Unidad
            self.Inter.TWLista.setItem(tableRow,3,QtWidgets.QTableWidgetItem(str(row[4]))) #Cantidad
            self.Inter.TWLista.setItem(tableRow,4,QtWidgets.QTableWidgetItem(row[5])) #Ancho
            self.Inter.TWLista.setItem(tableRow,5,QtWidgets.QTableWidgetItem(row[6])) #Largo
            self.Inter.TWLista.setItem(tableRow,6,QtWidgets.QTableWidgetItem(row[7])) #Lugar
            self.Inter.TWLista.setItem(tableRow,7,QtWidgets.QTableWidgetItem(row[8])) #FolioREQ

            tableRow += 1
    def LimpiarTWLista(self):
        self.Inter.TWLista.clearContents()
        self.Inter.TWLista.setRowCount(0)

    def MostrarEncabezadoENT(self):
        datos = self.Encabezado.ConsultarEncabezado()
        #print(datos)
        Enc = len(datos)
        if Enc == 0:
            pass
        else:
            info = datos[0]
            if info[8] == "Entrada":
                self.Inter.TXFolio.setText(info[0]) #Folio
                self.Inter.TXObra.setText(info[1]) #Obra
                self.Inter.TXSolicita.setText(info[2]) #Solicita
                self.Inter.TXAutoriza.setText(info[3]) #Autoriza
                self.Inter.TXAlmacen.setText(info[4]) #Almacen
                self.Inter.TXOrdComp.setText(info[5]) #Orden De Compra
                self.Inter.TXFolFact.setText(info[6]) #Folio Factura
                self.Inter.TXObservaciones_2.setText(info[7]) #Observaciones
            else:
                dialogo = QMessageBox()
                dialogo.setText("Error: El Encabezado no coincide con el Movimiento a Realizar\n ¿Quiere Borrar el Encabezado?")
                dialogo.setWindowTitle("DesinGlass Smart Windows")
                dialogo.setWindowIcon(QIcon('DG.png'))
                dialogo.setIcon(QMessageBox.Critical)
                dialogo.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                dialogo.setDefaultButton(QMessageBox.No)
                dialogo.setInformativeText('El Encabezado Pertenece a: {}'.format(info[8]))
                respuesta = dialogo.exec_()
                 
                if respuesta == 65536: #NO
                    print('no')
                    ID = info[0]
                    Folio = info[0]
                    Obra = info[1]
                    Solicita = info[2]
                    Autoriza = info[3]
                    Almacen = info[4]
                    OrCom = info[5]
                    FolFact = info[6]
                    Observaciones = info[7]
                    Type = "Entrada"

                    self.Encabezado.ActualizarEncabezado(ID, Folio, Obra, Solicita, Autoriza, Almacen, OrCom, FolFact, Observaciones, Type)

                    self.Inter.TXFolio.setText(info[0]) #Folio
                    self.Inter.TXObra.setText(info[1]) #Obra
                    self.Inter.TXSolicita.setText(info[2]) #Solicita
                    self.Inter.TXAutoriza.setText(info[3]) #Autoriza
                    self.Inter.TXAlmacen.setText(info[4]) #Almacen
                    self.Inter.TXOrdComp.setText(info[5]) #Orden De Compra
                    self.Inter.TXFolFact.setText(info[6]) #Folio Factura
                    self.Inter.TXObservaciones_2.setText(info[7]) #Observaciones

                    dialogo2 = QMessageBox()
                    dialogo2.setText("Se Recuperara la Maxima Informacion Posible")
                    dialogo2.setWindowTitle("DesinGlass Smart Windows")
                    dialogo2.setWindowIcon(QIcon('DG.png'))
                    dialogo2.setIcon(QMessageBox.Warning)
                    dialogo2.exec_()
                else: #SI
                    print('si')
                    ID = info[0]

                    self.Encabezado.EliminarEncabezado(ID)

                    self.Inter.TXFolio.clear() #Folio
                    self.Inter.TXObra.clear() #Obra
                    self.Inter.TXSolicita.clear() #Solicita
                    self.Inter.TXAutoriza.clear() #Autoriza
                    self.Inter.TXAlmacen.clear() #Almacen
                    self.Inter.TXOrdComp.clear() #Orden De Compra
                    self.Inter.TXFolFact.clear() #Folio Factura
                    self.Inter.TXObservaciones_2.clear() #Observaciones

                    dialogo2 = QMessageBox()
                    dialogo2.setText("Se Ha Eliminado la Informacion del Encabezado")
                    dialogo2.setWindowTitle("DesinGlass Smart Windows")
                    dialogo2.setWindowIcon(QIcon('DG.png'))
                    dialogo2.setIcon(QMessageBox.Warning)
                    dialogo2.exec_()

    #=========Entradas=========#

    #========Salidas========#
    def FBTIngresar_3(self):
        self.Inter.Libro1.setCurrentWidget(self.Inter.Ingresos)

    def Validacion62(self):
        x = QDoubleValidator()
        self.Inter.TXCantidad_2.setValidator(x)

    def FBTLimpiarTodo_2(self):
        self.Inter.TXFolio_2.clear()
        self.Inter.TXObra_2.clear()
        self.Inter.TXAlmacen_2.clear()
        self.Inter.TXSolicita_2.clear()
        self.Inter.TXAutoriza_2.clear()
        self.Inter.TXOrdComp_2.clear()
        self.Inter.TXFolFact_2.clear()
        self.Inter.TXSetProducto_2.clear()
        #===========LIMPIAR LISTA===========#
        lipL = self.Lista.ConsultarLista()
        if lipL == []:
            pass
        else:
            #print(lipL)
            for i in lipL:
                eliminar = i[0]
                self.Lista.EliminarLista(eliminar)
                #print(eliminar, " Eliminado")
        #===========LIMPIAR LISTA===========#

        #===========LIMPIAR ENCABEZADO===========#
        lipE = self.Encabezado.ConsultarEncabezado()
        if lipE == []:
            pass
        else:
            #print(lipE)
            for i2 in lipE:
                eliminar2 = i2[0]
                self.Encabezado.EliminarEncabezado(eliminar2)
                #print(eliminar2, " Eliminado")
        #===========LIMPIAR ENCABEZADO===========#
                
        #===========REFRESCAR INFORMACION===========#
        self.Refrescar6()
        self.LimpiarTWLista_2()
        self.MostarTWLista_2()
        self.LLenarCBBuscar_4()
        self.FBTLimpiar_5()
        self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
        #===========REFRESCAR INFORMACION===========#

    def FBTLimpiar_5(self):
        self.Inter.TXProducto_3.clear() #Producto
        self.Inter.TXStock_4.clear() #Sock Actual
        self.Inter.TXUnidad_3.clear() #Unidad
        self.Inter.TXCantidad_2.clear() #Cantidad
        self.Inter.TXAncho_2.clear() #Ancho
        self.Inter.TXClave_4.clear() #CLave
        self.Inter.TXLugar_3.clear() #Lugar
        self.Inter.TXLargo_2.clear() #Largo
        self.Inter.TXFolioReq_2.clear() #Folio REQ
        self.Inter.Imagen_2.clear() #Limpiar Imagen
        self.Inter.CBBuscar_4.setCurrentText("") #Limpiar Buscar
        self.Inter.Imagen_2.setText('Imagen') #Poner Texto Imagen
        #self.Inter.TXSetProducto_2.clear()
        #self.Inter.TXUltFol_2

    def FBTAgregar_2(self):
        if self.Inter.TXProducto_3.text() == "" and self.Inter.TXStock_4.text() == "" and self.Inter.TXUnidad_3.text() == "" and self.Inter.TXCantidad_2.text() == "" and self.Inter.TXAncho_2.text() == "" and self.Inter.TXClave_4.text() == "" and self.Inter.TXLugar_3.text() == "" and self.Inter.TXLargo_2.text() == "" and self.Inter.TXFolioReq_2.text() == "":
            pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Quiere Guardar el Encabezado?", QMessageBox.Yes | QMessageBox.No)
            if pregunta == QMessageBox.Yes:
                #Actualizar Encabezado#
                Folio1 = self.Inter.TXFolio_2.text() #Folio
                Obra1 = self.Inter.TXObra_2.text() #Obra
                Solicita1 =self.Inter.TXSolicita_2.text() #Solicita
                Autoriza1 = self.Inter.TXAutoriza_2.text() #Autoriza
                Almacen1 = self.Inter.TXAlmacen_2.text() #Almacen
                OrComp1 = self.Inter.TXOrdComp_2.text() #Orden de Compra
                FolFact1 = self.Inter.TXFolFact_2.text() #Folio Factura
                Observaciones1 = self.Inter.TXObservaciones.toPlainText() #Observaciones
                TPMov1 = "Salida"

                enc1 = self.Encabezado.ConsultarEncabezado()
                if enc1 == []:
                    self.Encabezado.AgregarEncabezado(Folio1,Obra1.capitalize(),Solicita1.capitalize(),Autoriza1.capitalize(),Almacen1.capitalize(),OrComp1,FolFact1, Observaciones1, TPMov1)
                else:
                    ref1 = enc1[0]
                    if ref1[0] == Folio1:
                        self.Encabezado.ActualizarEncabezado(Folio1, Folio1, Obra1.capitalize(), Solicita1.capitalize(), Autoriza1.capitalize(), Almacen1.capitalize(), OrComp1, FolFact1, Observaciones1, TPMov1)
                    else:
                        self.Encabezado.ActualizarEncabezado(ref1[0], Folio1, Obra1.capitalize(), Solicita1.capitalize(), Autoriza1.capitalize(), Almacen1.capitalize(), OrComp1, FolFact1, Observaciones1, TPMov1)
                #Actualizar Encabezado#
            else:
                pass
        else:
            if self.Inter.TXProducto_3.text() == "" or self.Inter.TXStock_4.text() == "" or self.Inter.TXUnidad_3.text() == "" or self.Inter.       TXCantidad_2.text() == "" or self.Inter.TXClave_4.text() == "" or self.Inter.TXLugar_3.text() == "":
                dialogo = QMessageBox()
                dialogo.setText("Por Favor LLene Correctamente Los Campos del Formulario")
                dialogo.setWindowTitle("DesinGlass Smart Windows")
                dialogo.setWindowIcon(QIcon('DG.png'))
                dialogo.setIcon(QMessageBox.Warning)
                dialogo.exec_()
            else:
                clave = self.Inter.TXClave_4.text()
                nomenclatura = clave[0:3]
                if nomenclatura != "VD-":
                    #print('no es vidrio')
                    datos = self.Lista.ConsultarLista()
                    e = len(datos)
                    #print(datos)
                    #print(i)
                    duplicado = ""
                    for i in datos: #Validar que no haya productos repetidos#
                        if i[1] == clave: 
                            duplicado = True
                            break
                        else:
                            duplicado = False

                    if duplicado == True:
                        dialogo1 = QMessageBox()
                        dialogo1.setText("El Producto Ya Esta Ingresado en La Lista")
                        dialogo1.setWindowTitle("DesinGlass Smart Windows")
                        dialogo1.setWindowIcon(QIcon('DG.png'))
                        dialogo1.setIcon(QMessageBox.Critical)
                        dialogo1.exec_()
                    else:
                        #print('lalalal')
                        busc = self.Base.BuscarProducto(clave)[0]
                        #print(busc)
                        if busc == "":
                            dialogo2 = QMessageBox()
                            dialogo2.setText("El Producto Selecionado No Existe")
                            dialogo2.setWindowTitle("DesinGlass Smart Windows")
                            dialogo2.setWindowIcon(QIcon('DG.png'))
                            dialogo2.setIcon(QMessageBox.Warning)
                            dialogo2.exec_()
                        else:
                            Numero = busc[3] #Numero
                            Marca = busc[4] #Marca
                            Color = busc[5] #Color
                            Proveedor = busc[8] #Proveedor
                            Stock =  busc[7] #Stock
                            TPMov = "Salida" #Tipo de Movimiento

                        ID = e + 1

                        for i2 in datos: #Validar que no haya ID repetido#
                            if int(i2[0]) == ID: 
                                ID += 1
                            else:
                                ID = ID

                        #print(ID)
                        Referencia = self.Inter.TXClave_4.text() #CLave
                        Descripcion = self.Inter.TXProducto_3.text() #Producto
                        Unidad = self.Inter.TXUnidad_3.text() #Unidad
                        Cantidad = self.Inter.TXCantidad_2.text() #Cantidad
                        Ancho = self.Inter.TXAncho_2.text() #Ancho
                        Largo = self.Inter.TXLargo_2.text() #Largo
                        Lugar = self.Inter.TXLugar_3.text() #Lugar
                        FolioREQ = self.Inter.TXFolioReq_2.text() #Folio REQ

                        if int(Cantidad) <= 0:
                            dialogo3 = QMessageBox()
                            dialogo3.setText("La Cantidad Ingresada es Mayor al Stock Actual")
                            dialogo3.setWindowTitle("DesinGlass Smart Windows")
                            dialogo3.setWindowIcon(QIcon('DG.png'))
                            dialogo3.setIcon(QMessageBox.Warning)
                            dialogo3.exec_()
                        else:
                            if len(datos) < 20:
                                self.Lista.AgregarLista(ID, Referencia, Descripcion.capitalize(),Unidad.capitalize(),Cantidad,Ancho,Largo,Lugar.capitalize(),FolioREQ,Numero.capitalize(),Marca.capitalize(),Color.capitalize(),Proveedor.capitalize(),Stock,TPMov)

                                #Actualizar Encabezado#
                                Folio = self.Inter.TXFolio_2.text() #Folio
                                Obra = self.Inter.TXObra_2.text() #Obra
                                Solicita =self.Inter.TXSolicita_2.text() #Solicita
                                Autoriza = self.Inter.TXAutoriza_2.text() #Autoriza
                                Almacen = self.Inter.TXAlmacen_2.text() #Almacen
                                OrComp = self.Inter.TXOrdComp_2.text() #Orden de Compra
                                FolFact = self.Inter.TXFolFact_2.text() #Folio Factura
                                Observaciones = self.Inter.TXObservaciones.toPlainText() #Observaciones

                                enc = self.Encabezado.ConsultarEncabezado()
                                if enc == []:
                                    self.Encabezado.AgregarEncabezado(Folio,Obra.capitalize(),Solicita.capitalize(),Autoriza.capitalize(),Almacen.capitalize(),OrComp,FolFact, Observaciones, TPMov)
                                else:
                                    ref = enc[0]
                                    if ref[0] == Folio:
                                        self.Encabezado.ActualizarEncabezado(Folio, Folio, Obra.capitalize(), Solicita.capitalize(), Autoriza.capitalize(), Almacen.capitalize(), OrComp, FolFact, Observaciones, TPMov)
                                    else:
                                        self.Encabezado.ActualizarEncabezado(ref[0], Folio, Obra.capitalize(), Solicita.capitalize(), Autoriza.capitalize(), Almacen.capitalize(), OrComp, FolFact, Observaciones, TPMov)
                                #Actualizar Encabezado#

                                dialogoB = QMessageBox()
                                dialogoB.setText("Se Ha Guardado Correctamete")
                                dialogoB.setWindowTitle("DesinGlass Smart Windows")
                                dialogoB.setWindowIcon(QIcon('DG.png'))
                                dialogoB.setIcon(QMessageBox.Information)
                                dialogoB.exec_()

                                #REFRESCAR INFORMACION#
                                self.Refrescar6()
                                self.LimpiarTWLista_2()
                                self.MostarTWLista_2()
                                self.LLenarCBBuscar_4()
                                self.FBTLimpiar_5()
                                #REFRESCAR INFORMACION#
                            else:
                                dialogoE = QMessageBox()
                                dialogoE.setText("La Lista Ya Esta LLena")
                                dialogoE.setWindowTitle("DesinGlass Smart Windows")
                                dialogoE.setIcon(QMessageBox.Critical)
                                dialogoE.exec_()
                else:
                    datos = self.Lista.ConsultarLista()
                    e = len(datos)
                    #print('es vidrio')
                    busc = self.Base.BuscarProducto(clave)[0]
                    #print(busc)
                    if busc == "":
                        dialogo2 = QMessageBox()
                        dialogo2.setText("El Producto Selecionado No Existe")
                        dialogo2.setWindowTitle("DesinGlass Smart Windows")
                        dialogo2.setWindowIcon(QIcon('DG.png'))
                        dialogo2.setIcon(QMessageBox.Warning)
                        dialogo2.exec_()
                    else:
                        Numero = busc[3] #Numero
                        Marca = busc[4] #Marca
                        Color = busc[5] #Color
                        Proveedor = busc[8] #Proveedor
                        Stock =  busc[7] #Stock
                        TPMov = "Salida" #Tipo de Movimiento

                    ID = e + 1

                    for i2 in datos: #Validar que no haya ID repetido#
                        if int(i2[0]) == ID: 
                            ID += 1
                        else:
                            ID = ID

                    #print(ID)
                    Referencia = self.Inter.TXClave_4.text() #CLave
                    Descripcion = self.Inter.TXProducto_3.text() #Producto
                    Unidad = self.Inter.TXUnidad_3.text() #Unidad
                    Cantidad = self.Inter.TXCantidad_2.text() #Cantidad
                    Ancho = self.Inter.TXAncho_2.text() #Ancho
                    Largo = self.Inter.TXLargo_2.text() #Largo
                    Lugar = self.Inter.TXLugar_3.text() #Lugar
                    FolioREQ = self.Inter.TXFolioReq_2.text() #Folio REQ

                    if int(Cantidad) <= 0:
                        dialogo3 = QMessageBox()
                        dialogo3.setText("La Cantidad Ingresada es Mayor al Stock Actual")
                        dialogo3.setWindowTitle("DesinGlass Smart Windows")
                        dialogo3.setWindowIcon(QIcon('DG.png'))
                        dialogo3.setIcon(QMessageBox.Warning)
                        dialogo3.exec_()
                    else:
                        if len(datos) < 20:
                            self.Lista.AgregarLista(ID, Referencia, Descripcion.capitalize(),Unidad.capitalize(),Cantidad,Ancho,Largo,Lugar.capitalize(),FolioREQ,Numero.capitalize(),Marca.capitalize(),Color.capitalize(),Proveedor.capitalize(),Stock,TPMov)

                            #Actualizar Encabezado#
                            Folio = self.Inter.TXFolio_2.text() #Folio
                            Obra = self.Inter.TXObra_2.text() #Obra
                            Solicita =self.Inter.TXSolicita_2.text() #Solicita
                            Autoriza = self.Inter.TXAutoriza_2.text() #Autoriza
                            Almacen = self.Inter.TXAlmacen_2.text() #Almacen
                            OrComp = self.Inter.TXOrdComp_2.text() #Orden de Compra
                            FolFact = self.Inter.TXFolFact_2.text() #Folio Factura
                            Observaciones = self.Inter.TXObservaciones.toPlainText() #Observaciones

                            enc = self.Encabezado.ConsultarEncabezado()
                            if enc == []:
                                self.Encabezado.AgregarEncabezado(Folio,Obra.capitalize(),Solicita.capitalize(),Autoriza.capitalize(),Almacen.capitalize(),OrComp,FolFact, Observaciones, TPMov)
                            else:
                                ref = enc[0]
                                if ref[0] == Folio:
                                    self.Encabezado.ActualizarEncabezado(Folio, Folio, Obra.capitalize(), Solicita.capitalize(), Autoriza.capitalize(), Almacen.capitalize(), OrComp, FolFact, Observaciones, TPMov)
                                else:
                                    self.Encabezado.ActualizarEncabezado(ref[0], Folio, Obra.capitalize(), Solicita.capitalize(), Autoriza.capitalize(), Almacen.capitalize(), OrComp, FolFact, Observaciones, TPMov)
                            #Actualizar Encabezado#

                            dialogoB = QMessageBox()
                            dialogoB.setText("Se Ha Guardado Correctamete")
                            dialogoB.setWindowTitle("DesinGlass Smart Windows")
                            dialogoB.setWindowIcon(QIcon('DG.png'))
                            dialogoB.setIcon(QMessageBox.Information)
                            dialogoB.exec_()

                            #REFRESCAR INFORMACION#
                            self.Refrescar6()
                            self.LimpiarTWLista_2()
                            self.MostarTWLista_2()
                            self.LLenarCBBuscar_4()
                            self.FBTLimpiar_5()
                            #REFRESCAR INFORMACION#
                        else:
                            dialogoE = QMessageBox()
                            dialogoE.setText("La Lista Ya Esta LLena")
                            dialogoE.setWindowTitle("DesinGlass Smart Windows")
                            dialogoE.setWindowIcon(QIcon('DG.png'))
                            dialogoE.setIcon(QMessageBox.Critical)
                            dialogoE.exec_()
                        
    def FBTBuscar_4(self):
        buscar = self.Inter.CBBuscar_4.currentText()
        #print(buscar)
        if buscar == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Seleccione Un Producto")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            busc = self.Base.BuscarProductoN(buscar)[0]
            #print(busc)
            if busc == "":
                dialogo2 = QMessageBox()
                dialogo2.setText("El Producto Selecionado No Existe")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                self.Inter.TXProducto_3.setText(busc[1]) #Producto#
                self.Inter.TXStock_4.setText(str(busc[7])) #Stock Actual#
                self.Inter.TXUnidad_3.setText(busc[6]) #Unidad#
                self.Inter.TXClave_4.setText(busc[2]) #Clave#
                
                Imagen = busc[12]
                #print(Imagen)
                if Imagen == "" or Imagen == None or Imagen == b'':
                    Imagen = os.getcwd() + "\DG.png"
                    Imagen = Imagen.replace("/", chr(92))

                    pixmapImage = QPixmap(Imagen).scaled(200,200,Qt.KeepAspectRatio,Qt.SmoothTransformation)
                    self.Inter.Imagen_2.setPixmap(pixmapImage)
                else:
                    foto = QPixmap()
                    foto.loadFromData(Imagen, "PNG", Qt.AutoColor)
                    self.Inter.Imagen_2.setPixmap(foto)

    def FBTGuardar_3(self):
        lista = self.Lista.ConsultarLista()
        if lista == []:
            dialogo = QMessageBox()
            dialogo.setText("La Lista Actualmente se Encuentra en Blanco")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            if self.Inter.TXFolio_2.text() == "" or self.Inter.TXObra_2.text() == "" or self.Inter.TXAlmacen_2.text() == "" or self.Inter.TXSolicita_2.text() == "" or self.Inter.TXAutoriza_2.text() == "":
                dialogo2 = QMessageBox()
                dialogo2.setText("Por Favor LLene Correctamente El Encabezado")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
                if pregunta == QMessageBox.Yes:
                    verificar = self.Salidas.BuscarSalidas(self.Inter.TXFolio_2.text())
                    if verificar == []:
                        #print(len(lista))
                        salida = [] #Esta lista dara todos los parametros para registrar la salida del producto
                        salida.append(self.Inter.TXFolio_2.text()) #Folio
                        salida.append(self.Inter.TXObra_2.text()) #Obra

                        fecha = self.Base.FechaLetra() #Mandamos a llamar a la fucion Fechador para que retorne la fecha actual
                        fechaa = fecha[6]
        
                        salida.append(fechaa) #Fecha
                        salida.append(self.Inter.TXSolicita_2.text()) #Solicita
                        salida.append(self.Inter.TXAutoriza_2.text()) #Autoriza
                        salida.append(self.Inter.TXAlmacen_2.text()) #Almacen
                        
                        #========================CICLO PARA DESCONTEO, REGISTRO Y CREACION DE LISTA========================#
                        for i in lista:
                            #salida.append(i[0]) #ID
                            salida.append(i[1]) #Referencia
                            salida.append(i[2]) #Descripcion
                            salida.append(i[3]) #Unidad
                            salida.append(i[4]) #Cantidad
                            salida.append(i[5]) #Ancho
                            salida.append(i[6]) #Largo
                            salida.append(i[7]) #Lugar
                            salida.append(i[8]) #FolioREQ
                            #salida.append(i[9]) #Numero
                            #salida.append(i[10]) #Marca
                            #salida.append(i[11]) #Color
                            #salida.append(i[12]) #Proveedor
                            #salida.append(i[13]) #Stock
                            #salida.append(i[14]) #Tipo de Movimiento

                            #========================CREAR REGISTRO EN MOVIMIENTOS========================#
                            buscar = i[1]
                            busc = self.Base.BuscarProducto(buscar)
                            #print(busc)
                            if busc == []:
                                dialogo2 = QMessageBox()
                                dialogo2.setText("El Producto: '{}' No Existe \n No se Desconto del Inventario".format(i[2]))
                                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                                dialogo2.setWindowIcon(QIcon('DG.png'))
                                dialogo2.setIcon(QMessageBox.Critical)
                                dialogo2.exec_()
                            else:
                                busc = busc[0] #se selecciona el unico valor de la lista
                                Nombre = busc[1] #Producto#
                                Clave = busc[2] #Clave#
                                Numero = busc[3] #Numero#
                                Color = busc[5] #Color#
                                Marca = busc[4] #Marca#
                                Unidad = busc[6] #Unidad#
                                Proveedor = busc[8] #Proveedor#
                                Lugar = busc[9] #Lugar#

                                ID = busc[0]
                                Stock = busc[7] - i[4]
                                PCompra = busc[10]
                                PVenta = busc[11]

                                foto = busc[12]

                                self.Base.ActualizarProducto( ID, Nombre, Clave, Numero, Marca, Color, Unidad, Stock, Proveedor, Lugar, PCompra, PVenta, foto)
                                #print('Desconteo Registrado')

                            #========================CREAR REGISTRO EN MOVIMIENTOS========================#

                            #========================CREAR REGISTRO EN MOVIMIENTOS========================#
                            TipMov = "Salida"
                            Nombre = i[2]
                            Clave = i[1]
                            Numero = i[9]
                            Marca = i[10]
                            Color = i[11]
                            Unidad = i[3]
                            Cantidad = i[4]
                            Proveedor = i[12]
                            Lugar = i[7]
                            Fecha = str(fecha[0])

                            self.Movimientoss.AgregarMovimientos(TipMov.capitalize(), Nombre, Clave, Numero, Marca, Color, Unidad, Cantidad, Proveedor, Lugar, Fecha)
                            #print('Movimiento Registrado')
                            #========================CREAR REGISTRO EN MOVIMIENTOS========================#

                        #========================CICLO PARA DESCONTEO, REGISTRO Y CREACION DE LISTA========================#

                        Faltante = len(salida)
                        #print(Faltante)
                        for i2 in range(0, 166-Faltante):
                            salida.append("")

                        salida.append(self.Inter.TXOrdComp_2.text()) #Orden de Compra
                        salida.append(self.Inter.TXFolFact_2.text()) #Folio Factura
                        salida.append(self.Inter.TXObservaciones.toPlainText()) #Observaciones
                        #print(salida)
                        #print(len(salida)) #Verificamos que nos arroje 169 datos para el correcto registro

                        self.Salidas.AgregarSalidasL(salida) #Creamos el registro

                        #========================LIMPIAR Y REFRESCAR========================#
                        self.FBTLimpiarTodo_2()

                        self.Refrescar6()
                        self.LimpiarTWLista_2()
                        self.MostarTWLista_2()
                        self.LLenarCBBuscar_4()
                        self.FBTLimpiar_5()
                        self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
                        #========================LIMPIAR Y REFRESCAR========================#

                        dialogo3 = QMessageBox()
                        dialogo3.setText("Se Ha Guardado Correctamete")
                        dialogo3.setWindowTitle("DesinGlass Smart Windows")
                        dialogo3.setWindowIcon(QIcon('DG.png'))
                        dialogo3.setIcon(QMessageBox.Information)
                        dialogo3.exec_()
                    else:
                        dialogo4 = QMessageBox()
                        dialogo4.setText("El Folio Ya Esta Registrado")
                        dialogo4.setWindowTitle("DesinGlass Smart Windows")
                        dialogo4.setWindowIcon(QIcon('DG.png'))
                        dialogo4.setIcon(QMessageBox.Warning)
                        dialogo4.exec_()
                else:
                    dialogo2 = QMessageBox()
                    dialogo2.setText("Operacion Cancelada")
                    dialogo2.setWindowTitle("DesinGlass Smart Windows")
                    dialogo2.setWindowIcon(QIcon('DG.png'))
                    dialogo2.setIcon(QMessageBox.Warning)
                    dialogo2.exec_()

    def FBTEliminar_3(self):
        if self.Inter.TXSetProducto_2.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Seleccione un Producto Para Eliminar")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            eliminar = self.Inter.TXSetProducto_2.text()
            busc = self.Lista.BuscarLista(eliminar)[0]
            #busc = self.Base.BuscarProducto(eliminar)
            #print(busc)
            if busc == []:
                dialogo2 = QMessageBox()
                dialogo2.setText("El Producto Selecionado No Existe")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Eliminar el Producto de la Lista?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if pregunta == QMessageBox.Yes:
                    ID = busc[0]
                    self.Lista.EliminarLista(ID)

                    dialogoB = QMessageBox()
                    dialogoB.setText("Se Ha Eliminado Correctamete")
                    dialogoB.setWindowTitle("DesinGlass Smart Windows")
                    dialogoB.setWindowIcon(QIcon('DG.png'))
                    dialogoB.setIcon(QMessageBox.Information)
                    dialogoB.exec_()

                    #REFRESCAR INFORMACION#
                    self.Refrescar6()
                    self.LimpiarTWLista_2()
                    self.MostarTWLista_2()
                    self.LLenarCBBuscar_4()
                    self.FBTLimpiar_5()
                    #REFRESCAR INFORMACION#
                else:
                    dialogoC = QMessageBox()
                    dialogoC.setText("Operacion Cancelada")
                    dialogoC.setWindowTitle("DesinGlass Smart Windows")
                    dialogoC.setWindowIcon(QIcon('DG.png'))
                    dialogoC.setIcon(QMessageBox.Warning)
                    dialogoC.exec_()

    def FBTLimpObs(self):
        self.Inter.TXObservaciones.clear()

    def LLenarCBBuscar_4(self):
        self.Inter.CBBuscar_4.clear()
        datos = self.Base.ConsultarProductos()
        i = len(datos)
        self.Inter.TWProductos.setRowCount(i)
        self.Inter.CBBuscar_4.addItem("")
        for row in datos:
            self.Inter.CBBuscar_4.addItem(row[1])

    def FTWLista_2Selecionado(self):
        FilaSewleccionada = self.Inter.TWLista_2.selectedItems()
        fila = [dato.text() for dato in FilaSewleccionada]
        #fila = fila[1]
        #print(fila)
        self.Inter.TXSetProducto_2.setText(fila[0]) #Producto Seleccionado#

        self.Inter.TWLista_2.viewport().setCursor(Qt.ClosedHandCursor) #Hacer que la manita se cierre
        cronometroI = time.time()
        while True:
            cronometroF = time.time()
            if cronometroF - cronometroI >= 0.2:
                self.Inter .TWLista_2.viewport().setCursor(Qt.OpenHandCursor) #Hacer que la manita se abra
                break
            else:
                #print(cronometroF - cronometroI)
                pass

    def FTWProductos_3Selecionado(self):
        FilaSewleccionada = self.Inter.TWProductos_3.selectedItems()
        fila = [dato.text() for dato in FilaSewleccionada]
        fila = fila[0]
        #print(fila)
        
        busc = self.Base.BuscarProductoN(fila)[0]
        #print(busc)
        if busc == []:
            dialogo2 = QMessageBox()
            dialogo2.setText("El Producto Selecionado No Existe")
            dialogo2.setWindowTitle("DesinGlass Smart Windows")
            dialogo2.setWindowIcon(QIcon('DG.png'))
            dialogo2.setIcon(QMessageBox.Warning)
            dialogo2.exec_()
        else:
            self.Inter.TXProducto_3.setText(busc[1]) #Producto#
            self.Inter.TXStock_4.setText(str(busc[7])) #Stock Actual#
            self.Inter.TXUnidad_3.setText(busc[6]) #Unidad#
            self.Inter.TXClave_4.setText(busc[2]) #Clave#

            Imagen = busc[12]
            #print(Imagen)
            if Imagen == "" or Imagen == None or Imagen == b'':
                Imagen = os.getcwd() + "\DG.png"
                Imagen = Imagen.replace("/", chr(92))

                pixmapImage = QPixmap(Imagen).scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation)
                self.Inter.Imagen_2.setPixmap(pixmapImage)
            else:
                foto = QPixmap()
                foto.loadFromData(Imagen, "PNG", Qt.AutoColor)
                self.Inter.Imagen_2.setPixmap(foto)

        self.Inter.CBBuscar_4.setCurrentText("")

    def MostarTWProductos_3(self):
        datos = self.Base.ConsultarProductos()
        #print(datos)
        #row = 0
        i = len(datos)
        self.Inter.TWProductos_3.setRowCount(i)
        tableRow = 0
        for row in datos:
            self.Id = row[0]
            #print(row[7])
            self.Inter.TWProductos_3.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[1])) #Producto

            tableRow += 1
    def LimpiarTWProductos_3(self):
        self.Inter.TWProductos_3.clearContents()
        self.Inter.TWProductos_3.setRowCount(0)

    def MostarTWLista_2(self):
        datos = self.Lista.ConsultarLista()
        #print(datos)
        #row = 0
        i = len(datos)
        self.Inter.TWLista_2.setRowCount(i)
        tableRow = 0
        for row in datos:
            self.Id = row[0]
            #print(row)
            self.Inter.TWLista_2.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[1])) #Referencia
            self.Inter.TWLista_2.setItem(tableRow,1,QtWidgets.QTableWidgetItem(row[2])) #Descripcion
            self.Inter.TWLista_2.setItem(tableRow,2,QtWidgets.QTableWidgetItem(row[3])) #Unidad
            self.Inter.TWLista_2.setItem(tableRow,3,QtWidgets.QTableWidgetItem(str(row[4]))) #Cantidad
            self.Inter.TWLista_2.setItem(tableRow,4,QtWidgets.QTableWidgetItem(row[5])) #Ancho
            self.Inter.TWLista_2.setItem(tableRow,5,QtWidgets.QTableWidgetItem(row[6])) #Largo
            self.Inter.TWLista_2.setItem(tableRow,6,QtWidgets.QTableWidgetItem(row[7])) #Lugar
            self.Inter.TWLista_2.setItem(tableRow,7,QtWidgets.QTableWidgetItem(row[8])) #FolioREQ

            tableRow += 1
    def LimpiarTWLista_2(self):
        self.Inter.TWLista_2.clearContents()
        self.Inter.TWLista_2.setRowCount(0)

    def MostrarEncabezadoSAL(self):
        datos = self.Encabezado.ConsultarEncabezado()
        #print(datos)
        if datos == []:
            pass
        else:
            info = datos[0]
            #print(info)
            if info[8] == "Salida":
                self.Inter.TXFolio_2.setText(info[0]) #Folio
                self.Inter.TXObra_2.setText(info[1]) #Obra
                self.Inter.TXSolicita_2.setText(info[2]) #Solicita
                self.Inter.TXAutoriza_2.setText(info[3]) #Autoriza
                self.Inter.TXAlmacen_2.setText(info[4]) #Almacen
                self.Inter.TXOrdComp_2.setText(info[5]) #Orden De Compra
                self.Inter.TXFolFact_2.setText(info[6]) #Folio Factura
                self.Inter.TXObservaciones.setText(info[7]) #Observaciones
            else:
                dialogo = QMessageBox()
                dialogo.setText("Error: El Encabezado no coincide con el Movimiento a Realizar\n ¿Quiere Borrar el Encabezado?")
                dialogo.setWindowTitle("DesinGlass Smart Windows")
                dialogo.setWindowIcon(QIcon('DG.png'))
                dialogo.setIcon(QMessageBox.Critical)
                dialogo.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                dialogo.setDefaultButton(QMessageBox.No)
                dialogo.setInformativeText('El Encabezado Pertenece a: {}'.format(info[8]))
                respuesta = dialogo.exec_()
                 
                if respuesta == 65536: #NO
                    print('no')
                    ID = info[0]
                    Folio = info[0]
                    Obra = info[1]
                    Solicita = info[2]
                    Autoriza = info[3]
                    Almacen = info[4]
                    OrCom = info[5]
                    FolFact = info[6]
                    Observaciones = info[7]
                    Type = "Salida"

                    self.Encabezado.ActualizarEncabezado(ID, Folio, Obra, Solicita, Autoriza, Almacen, OrCom, FolFact, Observaciones, Type)

                    self.Inter.TXFolio_2.setText(info[0]) #Folio
                    self.Inter.TXObra_2.setText(info[1]) #Obra
                    self.Inter.TXSolicita_2.setText(info[2]) #Solicita
                    self.Inter.TXAutoriza_2.setText(info[3]) #Autoriza
                    self.Inter.TXAlmacen_2.setText(info[4]) #Almacen
                    self.Inter.TXOrdComp_2.setText(info[5]) #Orden De Compra
                    self.Inter.TXFolFact_2.setText(info[6]) #Folio Factura
                    self.Inter.TXObservaciones.setText(info[7]) #Observaciones

                    dialogo2 = QMessageBox()
                    dialogo2.setText("Se Recuperara la Maxima Informacion Posible")
                    dialogo2.setWindowTitle("DesinGlass Smart Windows")
                    dialogo2.setWindowIcon(QIcon('DG.png'))
                    dialogo2.setIcon(QMessageBox.Warning)
                    dialogo2.exec_()
                else: #SI
                    print('si')
                    ID = info[0]

                    self.Encabezado.EliminarEncabezado(ID)

                    self.Inter.TXFolio_2.clear() #Folio
                    self.Inter.TXObra_2.clear() #Obra
                    self.Inter.TXSolicita_2.clear() #Solicita
                    self.Inter.TXAutoriza_2.clear() #Autoriza
                    self.Inter.TXAlmacen_2.clear() #Almacen
                    self.Inter.TXOrdComp_2.clear() #Orden De Compra
                    self.Inter.TXFolFact_2.clear() #Folio Factura
                    self.Inter.TXObservaciones.clear() #Observaciones

                    dialogo2 = QMessageBox()
                    dialogo2.setText("Se Ha Eliminado la Informacion del Encabezado")
                    dialogo2.setWindowTitle("DesinGlass Smart Windows")
                    dialogo2.setWindowIcon(QIcon('DG.png'))
                    dialogo2.setIcon(QMessageBox.Warning)
                    dialogo2.exec_()

    #=========Salidas=========#
        #Sexta Pagina#

        #Septima Pagina#
    def FBTIngresar_4(self):
        self.Inter.Libro1.setCurrentWidget(self.Inter.Ingresos)

    def Validacion71(self):
        x = QDoubleValidator()
        self.Inter.TXCantidad_3.setValidator(x)

    def FBTLimpiarTodo_3(self):
        self.Inter.TXFolio_3.clear()
        self.Inter.TXObra_3.clear()
        self.Inter.TXAlmacen_3.clear()
        self.Inter.TXSolicita_3.clear()
        self.Inter.TXAutoriza_3.clear()
        self.Inter.TXOrdComp_3.clear()
        self.Inter.TXFolFact_3.clear()
        self.Inter.TXSetProducto_3.clear()
        #===========LIMPIAR LISTA===========#
        lipL = self.Lista.ConsultarLista()
        if lipL == []:
            pass
        else:
            #print(lipL)
            for i in lipL:
                eliminar = i[0]
                self.Lista.EliminarLista(eliminar)
                #print(eliminar, " Eliminado")
        #===========LIMPIAR LISTA===========#

        #===========LIMPIAR ENCABEZADO===========#
        lipE = self.Encabezado.ConsultarEncabezado()
        if lipE == []:
            pass
        else:
            #print(lipE)
            for i2 in lipE:
                eliminar2 = i2[0]
                self.Encabezado.EliminarEncabezado(eliminar2)
                #print(eliminar2, " Eliminado")
        #===========LIMPIAR ENCABEZADO===========#
                
        #===========REFRESCAR INFORMACION===========#
        self.Refrescar7()
        self.LimpiarTWLista_3()
        self.MostarTWLista_3()
        self.LLenarCBBuscar_5()
        self.FBTLimpiar_6()
        self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
        #===========REFRESCAR INFORMACION===========#

    def FBTLimpiar_6(self):
        self.Inter.TXProducto_4.clear() #Producto
        self.Inter.TXStock_5.clear() #Sock Actual
        self.Inter.TXUnidad_4.clear() #Unidad
        self.Inter.TXCantidad_3.clear() #Cantidad
        self.Inter.TXAncho_3.clear() #Ancho
        self.Inter.TXClave_5.clear() #CLave
        self.Inter.TXLugar_4.clear() #Lugar
        self.Inter.TXLargo_3.clear() #Largo
        self.Inter.TXFolioReq_3.clear() #Folio REQ
        self.Inter.Imagen_3.clear() #Limpiar Imagen
        self.Inter.CBBuscar_5.setCurrentText("") #Limpiar Buscar
        self.Inter.Imagen_3.setText('Imagen') #Poner Texto Imagen
        #self.Inter.TXSetProducto_3.clear()
        #self.Inter.TXUltFol_3

    def FBTAgregar_3(self):
        if self.Inter.TXProducto_4.text() == "" and self.Inter.TXStock_5.text() == "" and self.Inter.TXUnidad_4.text() == "" and self.Inter.TXCantidad_3.text() == "" and self.Inter.TXAncho_3.text() == "" and self.Inter.TXClave_5.text() == "" and self.Inter.TXLugar_4.text() == "" and self.Inter.TXLargo_3.text() == "" and self.Inter.TXFolioReq_3.text() == "":
            pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Quiere Guardar el Encabezado?", QMessageBox.Yes | QMessageBox.No)
            if pregunta == QMessageBox.Yes:
                #Actualizar Encabezado#
                Folio1 = self.Inter.TXFolio_3.text() #Folio
                Obra1 = self.Inter.TXObra_3.text() #Obra
                Almacen1 = self.Inter.TXAlmacen_3.text() #Almacen
                Solicita1 =self.Inter.TXSolicita_3.text() #Solicita
                Autoriza1 = self.Inter.TXAutoriza_3.text() #Autoriza
                OrComp1 = self.Inter.TXOrdComp_3.text() #Orden de Compra
                FolFact1 = self.Inter.TXFolFact_3.text() #Folio Factura
                Observaciones1 = self.Inter.TXObservaciones_3.toPlainText() #Observaciones
                TPMov1 = "Lista"

                enc1 = self.Encabezado.ConsultarEncabezado()
                if enc1 == []:
                    self.Encabezado.AgregarEncabezado(Folio1,Obra1.capitalize(),Solicita1.capitalize(),Autoriza1.capitalize(),Almacen1.capitalize(),OrComp1,FolFact1, Observaciones1, TPMov1)
                else:
                    ref1 = enc1[0]
                    if ref1[0] == Folio1:
                        self.Encabezado.ActualizarEncabezado(Folio1, Folio1, Obra1.capitalize(), Solicita1.capitalize(), Autoriza1.capitalize(), Almacen1.capitalize(), OrComp1, FolFact1, Observaciones1, TPMov1)
                    else:
                        self.Encabezado.ActualizarEncabezado(ref1[0], Folio1, Obra1.capitalize(), Solicita1.capitalize(), Autoriza1.capitalize(), Almacen1.capitalize(), OrComp1, FolFact1, Observaciones1, TPMov1)
                #Actualizar Encabezado#
            else:
                pass
        else:
            if self.Inter.TXProducto_4.text() == "" or self.Inter.TXStock_5.text() == "" or self.Inter.TXUnidad_4.text() == "" or self.Inter.TXCantidad_3.text() == "" or self.Inter.TXClave_5.text() == "" or self.Inter.TXLugar_4.text() == "":
                dialogo = QMessageBox()
                dialogo.setText("Por Favor LLene Correctamente Los Campos del Formulario")
                dialogo.setWindowTitle("DesinGlass Smart Windows")
                dialogo.setWindowIcon(QIcon('DG.png'))
                dialogo.setIcon(QMessageBox.Warning)
                dialogo.exec_()
            else:
                clave = self.Inter.TXClave_5.text()
                nomenclatura = clave[0:2]
                if nomenclatura != "VD-":
                    #print('no es vidrio')
                    datos = self.Lista.ConsultarLista()
                    e = len(datos)
                    #print(datos)
                    #print(i)
                    duplicado = ""
                    for i in datos: #Validar que no haya productos repetidos#
                        if i[1] == clave: 
                            duplicado = True
                            break
                        else:
                            duplicado = False

                    #duplicado = False #Desactivamos la validacion de productos 

                    if duplicado == True:
                        dialogo1 = QMessageBox()
                        dialogo1.setText("El Producto Ya Esta Ingresado en La Lista")
                        dialogo1.setWindowTitle("DesinGlass Smart Windows")
                        dialogo1.setWindowIcon(QIcon('DG.png'))
                        dialogo1.setIcon(QMessageBox.Critical)
                        dialogo1.exec_()
                    else:
                        #print('lalalal')
                        busc = self.Base.BuscarProducto(clave)[0]
                        #print(busc)
                        if busc == "":
                            dialogo2 = QMessageBox()
                            dialogo2.setText("El Producto Selecionado No Existe")
                            dialogo2.setWindowTitle("DesinGlass Smart Windows")
                            dialogo2.setWindowIcon(QIcon('DG.png'))
                            dialogo2.setIcon(QMessageBox.Warning)
                            dialogo2.exec_()
                        else:
                            Numero = busc[3] #Numero
                            Marca = busc[4] #Marca
                            Color = busc[5] #Color
                            Proveedor = busc[8] #Proveedor
                            Stock =  busc[7] #Stock
                            TPMov = "Lista" #Tipo de Movimiento

                        ID = e + 1

                        for i2 in datos: #Validar que no haya ID repetido#
                            if int(i2[0]) == ID: 
                                ID += 1
                            else:
                                ID = ID

                        #print(ID)
                        Referencia = self.Inter.TXClave_5.text() #CLave
                        Descripcion = self.Inter.TXProducto_4.text() #Producto
                        Unidad = self.Inter.TXUnidad_4.text() #Unidad
                        Cantidad = self.Inter.TXCantidad_3.text() #Cantidad
                        Ancho = self.Inter.TXAncho_3.text() #Ancho
                        Largo = self.Inter.TXLargo_3.text() #Largo
                        Lugar = self.Inter.TXLugar_4.text() #Lugar
                        FolioREQ = self.Inter.TXFolioReq_3.text() #Folio REQ

                        if int(Cantidad) <= 0: #int(Cantidad) > Stock or int(Cantidad) <= 0
                            dialogo3 = QMessageBox()
                            dialogo3.setText("Por Favor Ingrese una Cantidad Valida")
                            dialogo3.setWindowTitle("DesinGlass Smart Windows")
                            dialogo3.setWindowIcon(QIcon('DG.png'))
                            dialogo3.setIcon(QMessageBox.Warning)
                            dialogo3.exec_()
                        else:
                            if len(datos) < 20:
                                self.Lista.AgregarLista(ID, Referencia, Descripcion.capitalize(),Unidad.capitalize(),Cantidad,Ancho,Largo,Lugar.capitalize(),FolioREQ,Numero.capitalize(),Marca.capitalize(),Color.capitalize(),Proveedor.capitalize(),Stock,TPMov)

                                #Actualizar Encabezado#
                                Folio = self.Inter.TXFolio_3.text() #Folio
                                Obra = self.Inter.TXObra_3.text() #Obra
                                Almacen = self.Inter.TXAlmacen_3.text() #Almacen
                                Solicita =self.Inter.TXSolicita_3.text() #Solicita
                                Autoriza = self.Inter.TXAutoriza_3.text() #Autoriza
                                OrComp = self.Inter.TXOrdComp_3.text() #Orden de Compra
                                FolFact = self.Inter.TXFolFact_3.text() #Folio Factura
                                Observaciones = self.Inter.TXObservaciones_3.toPlainText() #Observaciones

                                enc = self.Encabezado.ConsultarEncabezado()
                                if enc == []:
                                    self.Encabezado.AgregarEncabezado(Folio,Obra.capitalize(),Solicita.capitalize(),Autoriza.capitalize(),Almacen.capitalize(),OrComp,FolFact, Observaciones, TPMov)
                                else:
                                    ref = enc[0]
                                    if ref[0] == Folio:
                                        self.Encabezado.ActualizarEncabezado(Folio, Folio, Obra.capitalize(), Solicita.capitalize(), Autoriza.capitalize(), Almacen.capitalize(), OrComp, FolFact, Observaciones, TPMov)
                                    else:
                                        self.Encabezado.ActualizarEncabezado(ref[0], Folio, Obra.capitalize(), Solicita.capitalize(), Autoriza.capitalize(), Almacen.capitalize(), OrComp, FolFact, Observaciones, TPMov)
                                #Actualizar Encabezado#

                                dialogoB = QMessageBox()
                                dialogoB.setText("Se Ha Guardado Correctamete")
                                dialogoB.setWindowTitle("DesinGlass Smart Windows")
                                dialogoB.setWindowIcon(QIcon('DG.png'))
                                dialogoB.setIcon(QMessageBox.Information)
                                dialogoB.exec_()

                                #REFRESCAR INFORMACION#
                                self.Refrescar7()
                                self.LimpiarTWLista_3()
                                self.MostarTWLista_3()
                                self.LLenarCBBuscar_5()
                                self.FBTLimpiar_6()
                                #REFRESCAR INFORMACION#
                            else:
                                dialogoE = QMessageBox()
                                dialogoE.setText("La Lista Ya Esta LLena")
                                dialogoE.setWindowTitle("DesinGlass Smart Windows")
                                dialogoE.setWindowIcon(QIcon('DG.png'))
                                dialogoE.setIcon(QMessageBox.Critical)
                                dialogoE.exec_()
                else:
                    #print('es vidrio')
                    busc = self.Base.BuscarProducto(clave)[0]
                    #print(busc)
                    if busc == "":
                        dialogo2 = QMessageBox()
                        dialogo2.setText("El Producto Selecionado No Existe")
                        dialogo2.setWindowTitle("DesinGlass Smart Windows")
                        dialogo2.setWindowIcon(QIcon('DG.png'))
                        dialogo2.setIcon(QMessageBox.Warning)
                        dialogo2.exec_()
                    else:
                        Numero = busc[3] #Numero
                        Marca = busc[4] #Marca
                        Color = busc[5] #Color
                        Proveedor = busc[8] #Proveedor
                        Stock =  busc[7] #Stock
                        TPMov = "Lista" #Tipo de Movimiento

                    ID = e + 1

                    for i2 in datos: #Validar que no haya ID repetido#
                        if int(i2[0]) == ID: 
                            ID += 1
                        else:
                            ID = ID

                    #print(ID)
                    Referencia = self.Inter.TXClave_5.text() #CLave
                    Descripcion = self.Inter.TXProducto_4.text() #Producto
                    Unidad = self.Inter.TXUnidad_4.text() #Unidad
                    Cantidad = self.Inter.TXCantidad_3.text() #Cantidad
                    Ancho = self.Inter.TXAncho_3.text() #Ancho
                    Largo = self.Inter.TXLargo_3.text() #Largo
                    Lugar = self.Inter.TXLugar_4.text() #Lugar
                    FolioREQ = self.Inter.TXFolioReq_3.text() #Folio REQ

                    if int(Cantidad) > Stock or int(Cantidad) <= 0:
                        dialogo3 = QMessageBox()
                        dialogo3.setText("La Cantidad Ingresada es Mayor al Stock Actual")
                        dialogo3.setWindowTitle("DesinGlass Smart Windows")
                        dialogo3.setWindowIcon(QIcon('DG.png'))
                        dialogo3.setIcon(QMessageBox.Warning)
                        dialogo3.exec_()
                    else:
                        if len(datos) < 20:
                            self.Lista.AgregarLista(ID, Referencia, Descripcion.capitalize(),Unidad.capitalize(),Cantidad,Ancho,Largo,Lugar.capitalize(),FolioREQ,Numero.capitalize(),Marca.capitalize(),Color.capitalize(),Proveedor.capitalize(),Stock,TPMov)

                            #Actualizar Encabezado#
                            Folio = self.Inter.TXFolio_3.text() #Folio
                            Obra = self.Inter.TXObra_3.text() #Obra
                            Almacen = self.Inter.TXAlmacen_3.text() #Almacen
                            Solicita =self.Inter.TXSolicita_3.text() #Solicita
                            Autoriza = self.Inter.TXAutoriza_3.text() #Autoriza
                            OrComp = self.Inter.TXOrdComp_3.text() #Orden de Compra
                            FolFact = self.Inter.TXFolFact_3.text() #Folio Factura
                            Observaciones = self.Inter.TXObservaciones_3.toPlainText() #Observaciones

                            enc = self.Encabezado.ConsultarEncabezado()
                            if enc == []:
                                self.Encabezado.AgregarEncabezado(Folio,Obra.capitalize(),Solicita.capitalize(),Autoriza.capitalize(),Almacen.capitalize(),OrComp,FolFact, Observaciones, TPMov)
                            else:
                                ref = enc[0]
                                if ref[0] == Folio:
                                    self.Encabezado.ActualizarEncabezado(Folio, Folio, Obra.capitalize(), Solicita.capitalize(), Autoriza.capitalize(), Almacen.capitalize(), OrComp, FolFact, Observaciones, TPMov)
                                else:
                                    self.Encabezado.ActualizarEncabezado(ref[0], Folio, Obra.capitalize(), Solicita.capitalize(), Autoriza.capitalize(), Almacen.capitalize(), OrComp, FolFact, Observaciones, TPMov)
                            #Actualizar Encabezado#

                            dialogoB = QMessageBox()
                            dialogoB.setText("Se Ha Guardado Correctamete")
                            dialogoB.setWindowTitle("DesinGlass Smart Windows")
                            dialogoB.setWindowIcon(QIcon('DG.png'))
                            dialogoB.setIcon(QMessageBox.Information)
                            dialogoB.exec_()

                            #REFRESCAR INFORMACION#
                            self.Refrescar7()
                            self.LimpiarTWLista_3()
                            self.MostarTWLista_3()
                            self.LLenarCBBuscar_5()
                            self.FBTLimpiar_6()
                            #REFRESCAR INFORMACION#
                        else:
                            dialogoE = QMessageBox()
                            dialogoE.setText("La Lista Ya Esta LLena")
                            dialogoE.setWindowTitle("DesinGlass Smart Windows")
                            dialogoE.setWindowIcon(QIcon('DG.png'))
                            dialogoE.setIcon(QMessageBox.Critical)
                            dialogoE.exec_()

    def FBTBuscar_5(self):
        buscar = self.Inter.CBBuscar_5.currentText()
        #print(buscar)
        if buscar == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Seleccione Un Producto")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            busc = self.Base.BuscarProductoN(buscar)[0]
            #print(busc)
            if busc == "":
                dialogo2 = QMessageBox()
                dialogo2.setText("El Producto Selecionado No Existe")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                self.Inter.TXProducto_4.setText(busc[1]) #Producto#
                self.Inter.TXStock_5.setText(str(busc[7])) #Stock Actual#
                self.Inter.TXUnidad_4.setText(busc[6]) #Unidad#
                self.Inter.TXClave_5.setText(busc[2]) #Clave#
                
                Imagen = busc[12]
                #print(Imagen)
                if Imagen == "" or Imagen == None or Imagen == b'':
                    Imagen = os.getcwd() + "\DG.png"
                    Imagen = Imagen.replace("/", chr(92))

                    pixmapImage = QPixmap(Imagen).scaled(200,200,Qt.KeepAspectRatio,Qt.SmoothTransformation)
                    self.Inter.Imagen_3.setPixmap(pixmapImage)
                else:
                    foto = QPixmap()
                    foto.loadFromData(Imagen, "PNG", Qt.AutoColor)
                    self.Inter.Imagen_3.setPixmap(foto)

    def FBTGuardar_4(self):
        lista = self.Lista.ConsultarLista()
        if lista == []:
            dialogo = QMessageBox()
            dialogo.setText("La Lista Actualmente se Encuentra en Blanco")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            if self.Inter.TXFolio_3.text() == "" or self.Inter.TXObra_3.text() == "" or self.Inter.TXAlmacen_3.text() == "" or self.Inter.TXSolicita_3.text() == "" or self.Inter.TXAutoriza_3.text() == "":
                dialogo2 = QMessageBox()
                dialogo2.setText("Por Favor LLene Correctamente El Encabezado")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
                if pregunta == QMessageBox.Yes:
                    verificar = self.Listas.BuscarListas(self.Inter.TXFolio_3.text())
                    #print(verificar)
                    if verificar == []:
                        #print(len(lista))
                        Lista = [] #Esta lista dara todos los parametros para registrar la Lista del producto
                        Lista.append(self.Inter.TXFolio_3.text()) #Folio
                        Lista.append(self.Inter.TXObra_3.text()) #Obra

                        fecha = self.Base.FechaLetra() #Mandamos a llamar a la fucion Fechador para que retorne la fecha actual
                        fechaa = fecha[6]
        
                        Lista.append(fechaa) #Feha
                        Lista.append(self.Inter.TXAlmacen_3.text()) #Almacen
                        Lista.append(self.Inter.TXSolicita_3.text()) #Solicita
                        Lista.append(self.Inter.TXAutoriza_3.text()) #Autoriza
                        
                        #========================CICLO PARA DESCONTEO, REGISTRO Y CREACION DE LISTA========================#
                        for i in lista:
                            #Lista.append(i[0]) #ID
                            Lista.append(i[1]) #Referencia
                            Lista.append(i[2]) #Descripcion
                            Lista.append(i[3]) #Unidad
                            Lista.append(i[4]) #Cantidad
                            Lista.append(i[5]) #Ancho
                            Lista.append(i[6]) #Largo
                            Lista.append(i[7]) #Lugar
                            Lista.append(i[8]) #FolioREQ
                            #Lista.append(i[9]) #Numero
                            #Lista.append(i[10]) #Marca
                            #Lista.append(i[11]) #Color
                            #Lista.append(i[12]) #Proveedor
                            #Lista.append(i[13]) #Stock
                            #Lista.append(i[14]) #Tipo de Movimiento

                            '''#========================CREAR REGISTRO EN MOVIMIENTOS========================#
                            buscar = i[1]
                            busc = self.Base.BuscarProducto(buscar)
                            #print(busc)
                            if busc == []:
                                dialogo2 = QMessageBox()
                                dialogo2.setText("El Producto: '{}' No Existe \n No se Desconto del Inventario".format(i[2]))
                                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                                dialogo2.setWindowIcon(QIcon('DG.png'))
                                dialogo2.setIcon(QMessageBox.Critical)
                                dialogo2.exec_()
                            else:
                                busc = busc[0] #se selecciona el unico valor de la lista
                                Nombre = busc[1] #Producto#
                                Clave = busc[2] #Clave#
                                Numero = busc[3] #Numero#
                                Color = busc[5] #Color#
                                Marca = busc[4] #Marca#
                                Unidad = busc[6] #Unidad#
                                Proveedor = busc[8] #Proveedor#
                                Lugar = busc[9] #Lugar#

                                ID = busc[0]
                                Stock = busc[7] - i[4]
                                PCompra = busc[10]
                                PVenta = busc[11]

                                foto = busc[12]

                                self.Base.ActualizarProducto( ID, Nombre, Clave, Numero, Marca, Color, Unidad, Stock, Proveedor, Lugar, PCompra, PVenta, foto)
                                #print('Desconteo Registrado')

                            #========================CREAR REGISTRO EN MOVIMIENTOS========================#

                            #========================CREAR REGISTRO EN MOVIMIENTOS========================#
                            TipMov = "Lista"
                            Nombre = i[2]
                            Clave = i[1]
                            Numero = i[9]
                            Marca = i[10]
                            Color = i[11]
                            Unidad = i[3]
                            Cantidad = i[4]
                            Proveedor = i[12]
                            Lugar = i[7]
                            Fecha = str(fecha[0])

                            self.Movimientoss.AgregarMovimientos(TipMov.capitalize(), Nombre, Clave, Numero, Marca, Color, Unidad, Cantidad, Proveedor, Lugar, Fecha)
                            #print('Movimiento Registrado')
                            #========================CREAR REGISTRO EN MOVIMIENTOS========================#'''

                        #========================CICLO PARA DESCONTEO, REGISTRO Y CREACION DE LISTA========================#

                        Faltante = len(Lista)
                        #print(Faltante)
                        for i2 in range(0, 166-Faltante):
                            Lista.append("")

                        Lista.append(self.Inter.TXOrdComp_3.text()) #Orden de Compra
                        Lista.append(self.Inter.TXFolFact_3.text()) #Folio Factura
                        Lista.append(self.Inter.TXObservaciones_3.toPlainText()) #Observaciones
                        #print(Lista)
                        #print(len(Lista)) #Verificamos que nos arroje 169 datos para el correcto registro

                        self.Listas.AgregarListasL(Lista) #Creamos el registro

                        #========================LIMPIAR Y REFRESCAR========================#
                        self.FBTLimpiarTodo_3()

                        self.Refrescar7()
                        self.LimpiarTWLista_3()
                        self.MostarTWLista_3()
                        self.LLenarCBBuscar_5()
                        self.FBTLimpiar_6()
                        self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
                        #========================LIMPIAR Y REFRESCAR========================#

                        dialogo3 = QMessageBox()
                        dialogo3.setText("Se Ha Guardado Correctamete")
                        dialogo3.setWindowTitle("DesinGlass Smart Windows")
                        dialogo3.setWindowIcon(QIcon('DG.png'))
                        dialogo3.setIcon(QMessageBox.Information)
                        dialogo3.exec_()
                    else:
                        dialogo4 = QMessageBox()
                        dialogo4.setText("El Folio Ya Esta Registrado")
                        dialogo4.setWindowTitle("DesinGlass Smart Windows")
                        dialogo4.setWindowIcon(QIcon('DG.png'))
                        dialogo4.setIcon(QMessageBox.Warning)
                        dialogo4.exec_()
                else:
                    dialogo2 = QMessageBox()
                    dialogo2.setText("Operacion Cancelada")
                    dialogo2.setWindowTitle("DesinGlass Smart Windows")
                    dialogo2.setWindowIcon(QIcon('DG.png'))
                    dialogo2.setIcon(QMessageBox.Warning)
                    dialogo2.exec_()

    def FBTEliminar_4(self):
        if self.Inter.TXSetProducto_3.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Seleccione un Producto Para Eliminar")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            eliminar = self.Inter.TXSetProducto_3.text()
            busc = self.Lista.BuscarLista(eliminar)[0]
            #busc = self.Base.BuscarProducto(eliminar)
            #print(busc)
            if busc == []:
                dialogo2 = QMessageBox()
                dialogo2.setText("El Producto Selecionado No Existe")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Eliminar el Producto de la Lista?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if pregunta == QMessageBox.Yes:
                    ID = busc[0]
                    self.Lista.EliminarLista(ID)

                    dialogoB = QMessageBox()
                    dialogoB.setText("Se Ha Eliminado Correctamete")
                    dialogoB.setWindowTitle("DesinGlass Smart Windows")
                    dialogoB.setWindowIcon(QIcon('DG.png'))
                    dialogoB.setIcon(QMessageBox.Information)
                    dialogoB.exec_()

                    #REFRESCAR INFORMACION#
                    self.Refrescar7()
                    self.LimpiarTWLista_3()
                    self.MostarTWLista_3()
                    self.LLenarCBBuscar_5()
                    self.FBTLimpiar_6()
                    #REFRESCAR INFORMACION#
                else:
                    dialogoC = QMessageBox()
                    dialogoC.setText("Operacion Cancelada")
                    dialogoC.setWindowTitle("DesinGlass Smart Windows")
                    dialogoC.setWindowIcon(QIcon('DG.png'))
                    dialogoC.setIcon(QMessageBox.Warning)
                    dialogoC.exec_()

    def FBTLimpObsLIST(self):
        self.Inter.TXObservaciones_3.clear()

    def LLenarCBBuscar_5(self):
        self.Inter.CBBuscar_5.clear()
        datos = self.Base.ConsultarProductos()
        i = len(datos)
        self.Inter.TWProductos.setRowCount(i)
        self.Inter.CBBuscar_5.addItem("")
        for row in datos:
            self.Inter.CBBuscar_5.addItem(row[1])

    def FTWLista_3Selecionado(self):
        FilaSewleccionada = self.Inter.TWLista_3.selectedItems()
        fila = [dato.text() for dato in FilaSewleccionada]
        #fila = fila[1]
        #print(fila)
        self.Inter.TXSetProducto_3.setText(fila[0]) #Producto Seleccionado#

        self.Inter.TWLista_3.viewport().setCursor(Qt.ClosedHandCursor) #Hacer que la manita se cierre
        cronometroI = time.time()
        while True:
            cronometroF = time.time()
            if cronometroF - cronometroI >= 0.2:
                self.Inter .TWLista_3.viewport().setCursor(Qt.OpenHandCursor) #Hacer que la manita se abra
                break
            else:
                #print(cronometroF - cronometroI)
                pass

    def FTWProductos_5Selecionado(self):
        FilaSewleccionada = self.Inter.TWProductos_5.selectedItems()
        fila = [dato.text() for dato in FilaSewleccionada]
        fila = fila[0]
        #print(fila)
        
        busc = self.Base.BuscarProductoN(fila)[0]
        #print(busc)
        if busc == "":
            dialogo2 = QMessageBox()
            dialogo2.setText("El Producto Selecionado No Existe")
            dialogo2.setWindowTitle("DesinGlass Smart Windows")
            dialogo2.setWindowIcon(QIcon('DG.png'))
            dialogo2.setIcon(QMessageBox.Warning)
            dialogo2.exec_()
        else:
            self.Inter.TXProducto_4.setText(busc[1]) #Producto#
            self.Inter.TXStock_5.setText(str(busc[7])) #Stock Actual#
            self.Inter.TXUnidad_4.setText(busc[6]) #Unidad#
            self.Inter.TXClave_5.setText(busc[2]) #Clave#

            Imagen = busc[12]
            #print(Imagen)
            if Imagen == "" or Imagen == None or Imagen == b'':
                Imagen = os.getcwd() + "\DG.png"
                Imagen = Imagen.replace("/", chr(92))

                pixmapImage = QPixmap(Imagen).scaled(100,100,Qt.KeepAspectRatio,Qt.SmoothTransformation)
                self.Inter.Imagen_3.setPixmap(pixmapImage)
            else:
                foto = QPixmap()
                foto.loadFromData(Imagen, "PNG", Qt.AutoColor)
                self.Inter.Imagen_3.setPixmap(foto)

        self.Inter.CBBuscar_5.setCurrentText("")

    def MostarTWProductos_5(self):
        datos = self.Base.ConsultarProductos()
        #print(datos)
        #row = 0
        i = len(datos)
        self.Inter.TWProductos_5.setRowCount(i)
        tableRow = 0
        for row in datos:
            self.Id = row[0]
            #print(row[7])
            self.Inter.TWProductos_5.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[1])) #Producto

            tableRow += 1
    def LimpiarTWProductos_5(self):
        self.Inter.TWProductos_5.clearContents()
        self.Inter.TWProductos_5.setRowCount(0)

    def MostarTWLista_3(self):
        datos = self.Lista.ConsultarLista()
        #print(datos)
        #row = 0
        i = len(datos)
        self.Inter.TWLista_3.setRowCount(i)
        tableRow = 0
        for row in datos:
            self.Id = row[0]
            #print(row)
            self.Inter.TWLista_3.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[1])) #Referencia
            self.Inter.TWLista_3.setItem(tableRow,1,QtWidgets.QTableWidgetItem(row[2])) #Descripcion
            self.Inter.TWLista_3.setItem(tableRow,2,QtWidgets.QTableWidgetItem(row[3])) #Unidad
            self.Inter.TWLista_3.setItem(tableRow,3,QtWidgets.QTableWidgetItem(str(row[4]))) #Cantidad
            self.Inter.TWLista_3.setItem(tableRow,4,QtWidgets.QTableWidgetItem(row[5])) #Ancho
            self.Inter.TWLista_3.setItem(tableRow,5,QtWidgets.QTableWidgetItem(row[6])) #Largo
            self.Inter.TWLista_3.setItem(tableRow,6,QtWidgets.QTableWidgetItem(row[7])) #Lugar
            self.Inter.TWLista_3.setItem(tableRow,7,QtWidgets.QTableWidgetItem(row[8])) #FolioREQ

            tableRow += 1
    def LimpiarTWLista_3(self):
        self.Inter.TWLista_3.clearContents()
        self.Inter.TWLista_3.setRowCount(0)

    def MostrarEncabezadoLIST(self):
        datos = self.Encabezado.ConsultarEncabezado()
        #print(datos)
        if datos == []:
            pass
        else:
            info = datos[0]
            #print(info)
            if info[8] == "Lista":
                self.Inter.TXFolio_3.setText(info[0]) #Folio
                self.Inter.TXObra_3.setText(info[1]) #Obra
                self.Inter.TXAlmacen_3.setText(info[4]) #Almacen
                self.Inter.TXSolicita_3.setText(info[2]) #Solicita
                self.Inter.TXAutoriza_3.setText(info[3]) #Autoriza
                self.Inter.TXOrdComp_3.setText(info[5]) #Orden De Compra
                self.Inter.TXFolFact_3.setText(info[6]) #Folio Factura
                self.Inter.TXObservaciones_3.setText(info[7]) #Observaciones
            else:
                dialogo = QMessageBox()
                dialogo.setText("Error: El Encabezado no coincide con el Movimiento a Realizar\n ¿Quiere Borrar el Encabezado?")
                dialogo.setWindowTitle("DesinGlass Smart Windows")
                dialogo.setWindowIcon(QIcon('DG.png'))
                dialogo.setIcon(QMessageBox.Critical)
                dialogo.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
                dialogo.setDefaultButton(QMessageBox.No)
                dialogo.setInformativeText('El Encabezado Pertenece a: {}'.format(info[8]))
                respuesta = dialogo.exec_()
                 
                if respuesta == 65536: #NO
                    print('no')
                    ID = info[0]
                    Folio = info[0]
                    Obra = info[1]
                    Solicita = info[2]
                    Autoriza = info[3]
                    Almacen = info[4]
                    OrCom = info[5]
                    FolFact = info[6]
                    Observaciones = info[7]
                    Type = "Lista"

                    self.Encabezado.ActualizarEncabezado(ID, Folio, Obra, Solicita, Autoriza, Almacen, OrCom, FolFact, Observaciones, Type)

                    self.Inter.TXFolio_3.setText(info[0]) #Folio
                    self.Inter.TXObra_3.setText(info[1]) #Obra
                    self.Inter.TXAlmacen_3.setText(info[4]) #Almacen
                    self.Inter.TXSolicita_3.setText(info[2]) #Solicita
                    self.Inter.TXAutoriza_3.setText(info[3]) #Autoriza
                    self.Inter.TXOrdComp_3.setText(info[5]) #Orden De Compra
                    self.Inter.TXFolFact_3.setText(info[6]) #Folio Factura
                    self.Inter.TXObservaciones_3.setText(info[7]) #Observaciones

                    dialogo2 = QMessageBox()
                    dialogo2.setText("Se Recuperara la Maxima Informacion Posible")
                    dialogo2.setWindowTitle("DesinGlass Smart Windows")
                    dialogo2.setWindowIcon(QIcon('DG.png'))
                    dialogo2.setIcon(QMessageBox.Warning)
                    dialogo2.exec_()
                else: #SI
                    print('si')
                    ID = info[0]

                    self.Encabezado.EliminarEncabezado(ID)

                    self.Inter.TXFolio_3.clear() #Folio
                    self.Inter.TXObra_3.clear() #Obra
                    self.Inter.TXAlmacen_3.clear() #Almacen
                    self.Inter.TXSolicita_3.clear() #Solicita
                    self.Inter.TXAutoriza_3.clear() #Autoriza
                    self.Inter.TXOrdComp_3.clear() #Orden De Compra
                    self.Inter.TXFolFact_3.clear() #Folio Factura
                    self.Inter.TXObservaciones_3.clear() #Observaciones

                    dialogo2 = QMessageBox()
                    dialogo2.setText("Se Ha Eliminado la Informacion del Encabezado")
                    dialogo2.setWindowTitle("DesinGlass Smart Windows")
                    dialogo2.setWindowIcon(QIcon('DG.png'))
                    dialogo2.setIcon(QMessageBox.Warning)
                    dialogo2.exec_()
        #Septima Pagina#

        #Octava Pagina#
    def Validacion8(self):
        x = QDoubleValidator()
        self.Inter.TXNum_2.setValidator(x)

    def FBTBuscar_2(self):
        buscar = self.Inter.CBBuscar_2.currentText()
        #print(buscar)
        if buscar == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Seleccione Un Producto")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            busc = self.Base.BuscarProductoN(buscar)[0]
            #print(busc)
            if busc == "":
                dialogo2 = QMessageBox()
                dialogo2.setText("El Producto Selecionado No Existe")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                self.Inter.TXProducto.setText(busc[1]) #Producto#
                self.Inter.TXStock_2.setText(str(busc[7])) #Stock#
                self.Inter.TXClave_2.setText(busc[2]) #Clave#

    def FBTLimpiar_3(self):
        self.Inter.CBBuscar_2.setCurrentText("") #Buscar#
        self.Inter.TXProducto.clear() #Producto#
        self.Inter.TXClave_2.clear() #Clave#
        self.Inter.TXStock_2.clear() #Stock#
        self.Inter.TXNum_2.clear() #Cantidad#

    def FBTRestar(self):
        from datetime import datetime
        Valor = self.Inter.TXNum_2.text()
        if Valor == "":
            Valor = 0
        Valor = int(Valor)
        #print(type(Valor), Valor)

        if self.Inter.TXProducto.text() == "" or self.Inter.TXClave_2.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor LLene Correctamente Los Campos del Formulario")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
            if pregunta == QMessageBox.Yes:
                buscar = self.Inter.TXClave_2.text()
                #print(buscar)
                if buscar == "":
                    dialogo = QMessageBox()
                    dialogo.setText("Por Favor Seleccione Un Producto Para Actualizar")
                    dialogo.setWindowTitle("DesinGlass Smart Windows")
                    dialogo.setWindowIcon(QIcon('DG.png'))
                    dialogo.setIcon(QMessageBox.Warning)
                    dialogo.exec_()
                else:
                    busc = self.Base.BuscarProducto(buscar)[0]
                    #print(busc)
                    if busc == "":
                        dialogo2 = QMessageBox()
                        dialogo2.setText("El Producto Selecionado No Existe")
                        dialogo2.setWindowTitle("DesinGlass Smart Windows")
                        dialogo2.setWindowIcon(QIcon('DG.png'))
                        dialogo2.setIcon(QMessageBox.Warning)
                        dialogo2.exec_()
                    else:
                        if Valor == 0 or Valor < 0: 
                            dialogo3 = QMessageBox()
                            dialogo3.setText("Ingrese Una Cantidad Para Completar La Operacion")
                            dialogo3.setWindowTitle("DesinGlass Smart Windows")
                            dialogo3.setWindowIcon(QIcon('DG.png'))
                            dialogo3.setIcon(QMessageBox.Warning)
                            dialogo3.exec_()
                        else:
                            Nombre = busc[1] #Producto#
                            Clave = busc[2] #Clave#
                            Numero = busc[3] #Numero#
                            Color = busc[5] #Color#
                            Marca = busc[4] #Marca#
                            Unidad = busc[6] #Unidad#
                            Proveedor = busc[8] #Proveedor#
                            Lugar = busc[9] #Lugar#
                            ID = busc[0]

                            Stock = busc[7] - Valor

                            PCompra = busc[10]
                            PVenta = busc[11]
                            foto = busc[12]
                            
                            if Stock < 0:
                                dialogo3 = QMessageBox()
                                dialogo3.setText("La Cantidad Ingresada es Mayor al Stock Actual")
                                dialogo3.setWindowTitle("DesinGlass Smart Windows")
                                dialogo3.setWindowIcon(QIcon('DG.png'))
                                dialogo3.setIcon(QMessageBox.Critical)
                                dialogo3.exec_()
                            else:
                                self.Base.ActualizarProducto( ID, Nombre.capitalize(), Clave, Numero.capitalize(), Marca.capitalize(), Color.capitalize(), Unidad.capitalize(), Stock, Proveedor.capitalize(), Lugar.capitalize(), PCompra, PVenta, foto)

                                #REFRESCAR INFORMACION#
                                self.Refrescar8()
                                self.LLenarCBBuscar_2()
                                self.FBTLimpiar_3()
                                self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
                                #REFRESCAR INFORMACION#

                                #========================CREAR REGISTRO EN MOVIMIENTOS========================#
                                TipMov = "Ajuste Salida"
                                Fecha = str(datetime.now())
                                Fecha = Fecha[0: 19]
                                Fecha = Fecha.replace("-", "/")
                                Fecha = str(Fecha)

                                self.Movimientoss.AgregarMovimientos(TipMov.capitalize(), Nombre.capitalize(), Clave, Numero.capitalize(), Marca.capitalize(), Color.capitalize(), Unidad.capitalize(), Valor, Proveedor.capitalize(), Lugar.capitalize(), Fecha)
                                print('Movimiento Registrado')
                                #========================CREAR REGISTRO EN MOVIMIENTOS========================#

                                dialogoB = QMessageBox()
                                dialogoB.setText("Se Ha Guardado Correctamete")
                                dialogoB.setWindowTitle("DesinGlass Smart Windows")
                                dialogoB.setWindowIcon(QIcon('DG.png'))
                                dialogoB.setIcon(QMessageBox.Information)
                                dialogoB.exec_()
            else:
                dialogo2 = QMessageBox()
                dialogo2.setText("Operacion Cancelada")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()

    def FBTSumar(self):
        from datetime import datetime
        Valor = self.Inter.TXNum_2.text()
        if Valor == "":
            Valor = 0
        Valor = int(Valor)
        #print(type(Valor), Valor)

        if self.Inter.TXProducto.text() == "" or self.Inter.TXClave_2.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor LLene Correctamente Los Campos del Formulario")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
            if pregunta == QMessageBox.Yes:
                buscar = self.Inter.TXClave_2.text()
                #print(buscar)
                if buscar == "":
                    dialogo = QMessageBox()
                    dialogo.setText("Por Favor Seleccione Un Producto Para Actualizar")
                    dialogo.setWindowTitle("DesinGlass Smart Windows")
                    dialogo.setWindowIcon(QIcon('DG.png'))
                    dialogo.setIcon(QMessageBox.Warning)
                    dialogo.exec_()
                else:
                    busc = self.Base.BuscarProducto(buscar)[0]
                    #print(busc)
                    if busc == "":
                        dialogo2 = QMessageBox()
                        dialogo2.setText("El Producto Selecionado No Existe")
                        dialogo2.setWindowTitle("DesinGlass Smart Windows")
                        dialogo2.setWindowIcon(QIcon('DG.png'))
                        dialogo2.setIcon(QMessageBox.Warning)
                        dialogo2.exec_()
                    else:
                        if Valor == 0 or Valor < 0: 
                            dialogo3 = QMessageBox()
                            dialogo3.setText("Ingrese Una Cantidad Para Completar La Operacion")
                            dialogo3.setWindowTitle("DesinGlass Smart Windows")
                            dialogo3.setWindowIcon(QIcon('DG.png'))
                            dialogo3.setIcon(QMessageBox.Warning)
                            dialogo3.exec_()
                        else:
                            Nombre = busc[1] #Producto#
                            Clave = busc[2] #Clave#
                            Numero = busc[3] #Numero#
                            Color = busc[5] #Color#
                            Marca = busc[4] #Marca#
                            Unidad = busc[6] #Unidad#
                            Proveedor = busc[8] #Proveedor#
                            Lugar = busc[9] #Lugar#
                            ID = busc[0]

                            Stock = busc[7] + Valor

                            PCompra = busc[10]
                            PVenta = busc[11]
                            foto = busc[12]
                            
                            if Stock < 0:
                                dialogo3 = QMessageBox()
                                dialogo3.setText("La Cantidad Ingresada es Mayor al Stock Actual")
                                dialogo3.setWindowTitle("DesinGlass Smart Windows")
                                dialogo3.setWindowIcon(QIcon('DG.png'))
                                dialogo3.setIcon(QMessageBox.Critical)
                                dialogo3.exec_()
                            else:
                                self.Base.ActualizarProducto( ID, Nombre.capitalize(), Clave, Numero.capitalize(), Marca.capitalize(), Color.capitalize(), Unidad.capitalize(), Stock, Proveedor.capitalize(), Lugar.capitalize(), PCompra, PVenta, foto)

                                #REFRESCAR INFORMACION#
                                self.Refrescar8()
                                self.LLenarCBBuscar_2()
                                self.FBTLimpiar_3()
                                self.RefescarTooodo() #REFRESCA LA INFORMACION DE ToDO EL PROGRAMA#
                                #REFRESCAR INFORMACION#

                                #========================CREAR REGISTRO EN MOVIMIENTOS========================#
                                TipMov = "Ajuste Entrada"
                                Fecha = str(datetime.now())
                                Fecha = Fecha[0: 19]
                                Fecha = Fecha.replace("-", "/")
                                Fecha = str(Fecha)

                                self.Movimientoss.AgregarMovimientos(TipMov.capitalize(), Nombre.capitalize(), Clave, Numero.capitalize(), Marca.capitalize(), Color.capitalize(), Unidad.capitalize(), Valor, Proveedor.capitalize(), Lugar.capitalize(), Fecha)
                                print('Movimiento Registrado')
                                #========================CREAR REGISTRO EN MOVIMIENTOS========================#

                                dialogoB = QMessageBox()
                                dialogoB.setText("Se Ha Guardado Correctamete")
                                dialogoB.setWindowTitle("DesinGlass Smart Windows")
                                dialogoB.setWindowIcon(QIcon('DG.png'))
                                dialogoB.setIcon(QMessageBox.Information)
                                dialogoB.exec_()
            else:
                dialogo2 = QMessageBox()
                dialogo2.setText("Operacion Cancelada")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()

    def LLenarCBBuscar_2(self):
        self.Inter.CBBuscar_2.clear()
        datos = self.Base.ConsultarProductos()
        i = len(datos)
        self.Inter.TWProductos.setRowCount(i)
        self.Inter.CBBuscar_2.addItem("")
        for row in datos:
            self.Inter.CBBuscar_2.addItem(row[1])

    def MostarTWProductos(self):
        datos = self.Base.ConsultarProductos()
        #print(datos)
        #row = 0
        i = len(datos)
        self.Inter.TWProductos.setRowCount(i)
        tableRow = 0
        for row in datos:
            self.Id = row[0]
            #print(row[7])
            self.Inter.TWProductos.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[1])) #Producto
            self.Inter.TWProductos.setItem(tableRow,1,QtWidgets.QTableWidgetItem(row[2])) #Clave
            self.Inter.TWProductos.setItem(tableRow,2,QtWidgets.QTableWidgetItem(row[3])) #Numero
            self.Inter.TWProductos.setItem(tableRow,3,QtWidgets.QTableWidgetItem(row[4])) #Marca
            self.Inter.TWProductos.setItem(tableRow,4,QtWidgets.QTableWidgetItem(row[5])) #Color
            self.Inter.TWProductos.setItem(tableRow,5,QtWidgets.QTableWidgetItem(row[6])) #Unidad
            self.Inter.TWProductos.setItem(tableRow,6,QtWidgets.QTableWidgetItem(str(row[7]))) #Stock
            self.Inter.TWProductos.setItem(tableRow,7,QtWidgets.QTableWidgetItem(row[8])) #Proveedor
            self.Inter.TWProductos.setItem(tableRow,8,QtWidgets.QTableWidgetItem(row[9])) #Lugar
            self.Inter.TWProductos.setItem(tableRow,9,QtWidgets.QTableWidgetItem(row[10])) #$Compra
            self.Inter.TWProductos.setItem(tableRow,10,QtWidgets.QTableWidgetItem(row[11])) #$Venta
            #self.Inter.TWProductos.setItem(tableRow,11,QtWidgets.QTableWidgetItem(row[12]))

            tableRow += 1

    def FTWProductosSelecionado(self):
        FilaSewleccionada = self.Inter.TWProductos.selectedItems()
        #print(FilaSewleccionada)
        fila = [dato.text() for dato in FilaSewleccionada]
        #fila = fila[1]
        #print(fila)
        self.Inter.TXProducto.setText(fila[0]) #Producto#
        self.Inter.TXClave_2.setText(fila[1]) #Clave#
        self.Inter.TXStock_2.setText(fila[6]) #Stock#

        self.Inter.CBBuscar_2.setCurrentText("")

        self.Inter.TWProductos.viewport().setCursor(Qt.ClosedHandCursor) #Hacer que la manita se cierre
        cronometroI = time.time()
        while True:
            cronometroF = time.time()
            if cronometroF - cronometroI >= 0.2:
                self.Inter .TWProductos.viewport().setCursor(Qt.OpenHandCursor) #Hacer que la manita se abra
                break
            else:
                #print(cronometroF - cronometroI)
                pass

    def LimpiarTWProductos(self):
        self.Inter.TWProductos.clearContents()
        self.Inter.TWProductos.setRowCount(0)
        #Octava Pagina#
    #=========================================FUNCIONES BOTONES==========================================#


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
            self.Inter.BTMax.hide()
            self.Inter.BTMax2.show()
        else:
            self.showNormal()
            self.Inter.BTMax.show()
            self.Inter.BTMax2.hide()

    def MoverMenu(self):
        if True:
            width = self.Inter.FrameBotones.width()
            normal = 0
            if width  == 0:
                extender = 200
                self.animacion = QPropertyAnimation(self.Inter.FrameBotones, b'minimumWidth')
                self.animacion.setDuration(300)
                self.animacion.setStartValue(width)
                self.animacion.setEndValue(extender)
                self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.animacion.start()
            else:
                extender = 0
                self.animacion = QPropertyAnimation(self.Inter.FrameBotones, b'minimumWidth')
                self.animacion.setDuration(300)
                self.animacion.setStartValue(width)
                self.animacion.setEndValue(extender)
                self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.animacion.start()
        
    def MostarProductos(self):
        datos = self.Base.ConsultarProductos()
        #print(datos)
        #row = 0
        i = len(datos)
        self.Inter.TWProductos_4.setRowCount(i)
        tableRow = 0
        for row in datos:
            self.Id = row[0]
            #print(row[7])
            self.Inter.TWProductos_4.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[1])) #Producto
            self.Inter.TWProductos_4.setItem(tableRow,1,QtWidgets.QTableWidgetItem(row[2])) #Clave
            self.Inter.TWProductos_4.setItem(tableRow,2,QtWidgets.QTableWidgetItem(row[3])) #Numero
            self.Inter.TWProductos_4.setItem(tableRow,3,QtWidgets.QTableWidgetItem(row[4])) #Marca
            self.Inter.TWProductos_4.setItem(tableRow,4,QtWidgets.QTableWidgetItem(row[5])) #Color
            self.Inter.TWProductos_4.setItem(tableRow,5,QtWidgets.QTableWidgetItem(row[6])) #Unidad
            self.Inter.TWProductos_4.setItem(tableRow,6,QtWidgets.QTableWidgetItem(str(row[7]))) #Stock
            self.Inter.TWProductos_4.setItem(tableRow,7,QtWidgets.QTableWidgetItem(row[8])) #Proveedor
            self.Inter.TWProductos_4.setItem(tableRow,8,QtWidgets.QTableWidgetItem(row[9])) #Lugar
            #self.Inter.TWProductos_4.setItem(tableRow,9,QtWidgets.QTableWidgetItem(row[10]))
            #self.Inter.TWProductos_4.setItem(tableRow,10,QtWidgets.QTableWidgetItem(row[11]))
            #self.Inter.TWProductos_4.setItem(tableRow,11,QtWidgets.QTableWidgetItem(row[12]))
            tableRow += 1
            #self.FBTLimpiar2_4

    def LimpiarTabla21(self):
        self.Inter.TWProductos_4.clearContents()
        self.Inter.TWProductos_4.setRowCount(0)

    def listasDeSalidas(self):
        try:
            lista = self.Lista.ConsultarLista()
            #print(lista)
            if lista == []:
                tipo = self.Encabezado.ConsultarEncabezado()
                if tipo == []:
                    pass
                else:
                    tipo = tipo[0]
                    if tipo[8] == "Salida":
                        #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPSalidas) #Salidas#
                        #self.MostrarEncabezadoSAL()
                        self.Inter.TXFolio_2.setText(tipo[0]) #Folio
                        self.Inter.TXObra_2.setText(tipo[1]) #Obra
                        self.Inter.TXAlmacen_2.setText(tipo[4]) #Almacen
                        self.Inter.TXSolicita_2.setText(tipo[2]) #Solicita
                        self.Inter.TXAutoriza_2.setText(tipo[3]) #Autoriza
                        self.Inter.TXOrdComp_2.setText(tipo[5]) #Orden De Compra
                        self.Inter.TXFolFact_2.setText(tipo[6]) #Folio Factura
                        self.Inter.TXObservaciones.setText(tipo[7]) #Observaciones
                    elif tipo[8] == "Entrada":
                        #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPEntradas) #Entradas#
                        #self.MostrarEncabezadoENT()
                        self.Inter.TXFolio.setText(tipo[0]) #Folio
                        self.Inter.TXObra.setText(tipo[1]) #Obra
                        self.Inter.TXAlmacen.setText(tipo[4]) #Almacen
                        self.Inter.TXSolicita.setText(tipo[2]) #Solicita
                        self.Inter.TXAutoriza.setText(tipo[3]) #Autoriza
                        self.Inter.TXOrdComp.setText(tipo[5]) #Orden De Compra
                        self.Inter.TXFolFact.setText(tipo[6]) #Folio Factura
                        self.Inter.TXObservaciones.setText(tipo[7]) #Observaciones
                    else:
                        #self.Inter.Libro1.setCurrentWidget(self.Inter.ListaSal) #Listas#
                        #self.MostrarEncabezadoLISTA()
                        self.Inter.TXFolio_3.setText(tipo[0]) #Folio
                        self.Inter.TXObra_3.setText(tipo[1]) #Obra
                        self.Inter.TXAlmacen_3.setText(tipo[4]) #Almacen
                        self.Inter.TXSolicita_3.setText(tipo[2]) #Solicita
                        self.Inter.TXAutoriza_3.setText(tipo[3]) #Autoriza
                        self.Inter.TXOrdComp_3.setText(tipo[5]) #Orden De Compra
                        self.Inter.TXFolFact_3.setText(tipo[6]) #Folio Factura
                        self.Inter.TXObservaciones_3.setText(tipo[7]) #Observaciones
            else:
                lista = lista[0]
                #print(lista[14])
                if lista[14] == "Lista":
                    #print('bien')
                    self.LimpiarTWLista_3()
                    self.MostarTWLista_3()
                    Encabezado = self.Encabezado.ConsultarEncabezado()
                    if Encabezado == []:
                        pass
                    else:
                        self.MostrarEncabezadoLIST()
                elif lista[14] == "Entrada":
                    dialogo = QMessageBox()
                    dialogo.setText("Actualmente Estas Realizando una: {}. Finalice la {} de lo Contrario la Informacion se Perdera".format(lista[14],lista[14]))
                    dialogo.setWindowTitle("DesinGlass Smart Windows")
                    dialogo.setWindowIcon(QIcon('DG.png'))
                    dialogo.setIcon(QMessageBox.Warning)
                    dialogo.exec_()
                    if lista[14] == "Entrada":
                        #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPSalidas) #Salidas#
                        #self.SalidasBT() #Funcion Salidas#
                        #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPEntradas) #Entradas#
                        self.EntradasBT() #Funcion Entradas#
                    elif lista[14] == "Salida":
                        #self.Inter.Libro1.setCurrentWidget(self.Inter.ListaSal) #Listas#
                        #self.ListasBT() #Funcion Listas#
                        self.SalidasBT() #Funcion Salidas#
                    else:
                        self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)   
                else:
                    dialogo2 = QMessageBox()
                    dialogo2.setText("Actualmente Estas Realizando una: {}. Finalice la {} de lo Contrario la Informacion se Perdera".format(lista[14],lista[14]))
                    dialogo2.setWindowTitle("DesinGlass Smart Windows")
                    dialogo2.setWindowIcon(QIcon('DG.png'))
                    dialogo2.setIcon(QMessageBox.Warning)
                    dialogo2.exec_()
                    if lista[14] == "Entrada":
                        #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPSalidas) #Salidas#
                        #self.SalidasBT() #Funcion Salidas#
                        #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPEntradas) #Entradas#
                        self.EntradasBT() #Funcion Entradas#
                    elif lista[14] == "Salida":
                        #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPEntradas) #Entradas#
                        #self.EntradasBT() #Funcion Entradas#
                        self.SalidasBT() #Funcion Salidas#
                    else:
                        self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)
        except:
            pass
           
    def EntradasSalidas(self):
        self.Inter.Libro1.setCurrentWidget(self.Inter.EntrYSal)
        cosa = self.Inter.PPEntSal.currentWidget()
        try:
            lista = self.Lista.ConsultarLista()
            Salida = self.Inter.PPSalidas
            #Entrada = self.Inter.PPEntradas
            #print(lista)
            if lista == []:
                tipo = self.Encabezado.ConsultarEncabezado()
                if tipo == []:
                    pass
                else:
                    tipo = tipo[0]
                    if tipo[8] == "Salida":
                        #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPSalidas) #Salidas#
                        #self.MostrarEncabezadoSAL()
                        self.Inter.TXFolio_2.setText(tipo[0]) #Folio
                        self.Inter.TXObra_2.setText(tipo[1]) #Obra
                        self.Inter.TXAlmacen_2.setText(tipo[4]) #Almacen
                        self.Inter.TXSolicita_2.setText(tipo[2]) #Solicita
                        self.Inter.TXAutoriza_2.setText(tipo[3]) #Autoriza
                        self.Inter.TXOrdComp_2.setText(tipo[5]) #Orden De Compra
                        self.Inter.TXFolFact_2.setText(tipo[6]) #Folio Factura
                        self.Inter.TXObservaciones.setText(tipo[7]) #Observaciones
                    elif tipo[8] == "Entrada":
                        #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPEntradas) #Entradas#
                        #self.MostrarEncabezadoENT()
                        self.Inter.TXFolio.setText(tipo[0]) #Folio
                        self.Inter.TXObra.setText(tipo[1]) #Obra
                        self.Inter.TXAlmacen.setText(tipo[4]) #Almacen
                        self.Inter.TXSolicita.setText(tipo[2]) #Solicita
                        self.Inter.TXAutoriza.setText(tipo[3]) #Autoriza
                        self.Inter.TXOrdComp.setText(tipo[5]) #Orden De Compra
                        self.Inter.TXFolFact.setText(tipo[6]) #Folio Factura
                        self.Inter.TXObservaciones.setText(tipo[7]) #Observaciones
                    else:
                        #self.Inter.Libro1.setCurrentWidget(self.Inter.ListaSal) #Listas#
                        #self.MostrarEncabezadoLISTA()
                        self.Inter.TXFolio_3.setText(tipo[0]) #Folio
                        self.Inter.TXObra_3.setText(tipo[1]) #Obra
                        self.Inter.TXAlmacen_3.setText(tipo[4]) #Almacen
                        self.Inter.TXSolicita_3.setText(tipo[2]) #Solicita
                        self.Inter.TXAutoriza_3.setText(tipo[3]) #Autoriza
                        self.Inter.TXOrdComp_3.setText(tipo[5]) #Orden De Compra
                        self.Inter.TXFolFact_3.setText(tipo[6]) #Folio Factura
                        self.Inter.TXObservaciones_3.setText(tipo[7]) #Observaciones
            else:
                lista = lista[0]
                if cosa == Salida: 
                    #print('Salidas')
                    #print(lista[14])
                    if lista[14] == "Salida":
                        #print('bien')
                        self.LimpiarTWLista_2()
                        self.MostarTWLista_2()
                        Encabezado = self.Encabezado.ConsultarEncabezado()
                        if Encabezado == []:
                            pass
                        else:
                            self.MostrarEncabezadoSAL()
                    elif lista[14] == "Entrada":
                        dialogo = QMessageBox()
                        dialogo.setText("Actualmente Estas Realizando una: {}. Finalice la {} de lo Contrario la Informacion se Perdera".format(lista[14],lista[14]))
                        dialogo.setWindowTitle("DesinGlass Smart Windows")
                        dialogo.setWindowIcon(QIcon('DG.png'))
                        dialogo.setIcon(QMessageBox.Warning)
                        dialogo.exec_()
                        if lista[14] == "Entrada":
                            #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPSalidas) #Salidas#
                            #self.SalidasBT() #Funcion Salidas#
                            #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPEntradas) #Entradas#
                            self.EntradasBT() #Funcion Entradas#
                        elif lista[14] == "Lista":
                            #self.Inter.Libro1.setCurrentWidget(self.Inter.ListaSal) #Listas#
                            self.ListasBT() #Funcion Listas#
                        else:
                            self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)   
                    else:
                        dialogo2 = QMessageBox()
                        dialogo2.setText("Actualmente Estas Realizando una: {}. Finalice la {} de lo Contrario la Informacion se Perdera".format(lista[14],lista[14]))
                        dialogo2.setWindowTitle("DesinGlass Smart Windows")
                        dialogo2.setWindowIcon(QIcon('DG.png'))
                        dialogo2.setIcon(QMessageBox.Warning)
                        dialogo2.exec_()
                        if lista[14] == "Entrada":
                            #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPSalidas) #Salidas#
                            #self.SalidasBT() #Funcion Salidas#
                            #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPEntradas) #Entradas#
                            self.EntradasBT() #Funcion Entradas#
                        elif lista[14] == "Lista":
                            #self.Inter.Libro1.setCurrentWidget(self.Inter.ListaSal) #Listas#
                            self.ListasBT() #Funcion Listas#
                        else:
                            self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)
                else:
                    #print('Entrada')
                    #print(lista[14])
                    if lista[14] == "Entrada":
                        #print('bien')
                        self.LimpiarTWLista()
                        self.MostarTWLista()
                        Encabezado = self.Encabezado.ConsultarEncabezado()
                        if Encabezado == []:
                            pass
                        else:
                            self.MostrarEncabezadoENT()
                    elif lista[14] == "Salida":
                        dialogo3 = QMessageBox()
                        dialogo3.setText("Actualmente Estas Realizando una: {}. Finalice la {} de lo Contrario la Informacion se Perdera".format(lista[14],lista[14]))
                        dialogo3.setWindowTitle("DesinGlass Smart Windows")
                        dialogo3.setWindowIcon(QIcon('DG.png'))
                        dialogo3.setIcon(QMessageBox.Warning)
                        dialogo3.exec_()
                        if lista[14] == "Salida":
                            #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPSalidas) #Salidas#
                            self.SalidasBT() #Funcion Salidas#
                            #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPEntradas) #Entradas#
                            #self.EntradasBT() #Funcion Entradas#
                        elif lista[14] == "Lista":
                            #self.Inter.Libro1.setCurrentWidget(self.Inter.ListaSal) #Listas#
                            self.ListasBT() #Funcion Listas#
                        else:
                            self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)
                    else:
                        dialogo4 = QMessageBox()
                        dialogo4.setText("Actualmente Estas Realizando una: {}. Finalice la {} de lo Contrario la Informacion se Perdera".format(lista[14],lista[14]))
                        dialogo4.setWindowTitle("DesinGlass Smart Windows")
                        dialogo4.setWindowIcon(QIcon('DG.png'))
                        dialogo4.setIcon(QMessageBox.Warning)
                        dialogo4.exec_()
                        if lista[14] == "Entrada":
                            #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPSalidas) #Salidas#
                            #self.SalidasBT() #Funcion Salidas#
                            #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPEntradas) #Entradas#
                            self.EntradasBT() #Funcion Entradas#
                        elif lista[14] == "Salida":
                            #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPSalidas) #Salidas#
                            self.SalidasBT() #Funcion Salidas#
                            #self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPEntradas) #Entradas#
                            #self.EntradasBT() #Funcion Entradas#
                        else:
                            self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)
        except:
            pass

    def EntradasBT(self):
        self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPEntradas) #Entradas#
        self.EntradasSalidas()
    def SalidasBT(self):
        self.Inter.PPEntSal.setCurrentWidget(self.Inter.PPSalidas) #Salidas#
        self.EntradasSalidas()
    def ListasBT(self):
        self.Inter.Libro1.setCurrentWidget(self.Inter.ListaSal) #Listas#
        self.listasDeSalidas()
          

    def menuContextual(self, posicion):
        #indices = self.Inter.selectedIndexes()

        menu = QMenu()
        itemsGrupo = QActionGroup(self)
        itemsGrupo.setExclusive(True)

        lista = [
            "Herraje",
            "Perfil",
            "Vidrio",
            "Silicon",
            "General",
            "Peliculas",
            "Liquidos",
            "Cintas"
            ]
        
        Mmenu = menu.addMenu("Nomenclaturas")
        for i,Item in enumerate (lista, start=0):
            Accion = QAction(Item, itemsGrupo)
            Accion.setData(i)

            Mmenu.addAction(Accion)

        menu.addSeparator()
        menu.addAction(QAction("salir", itemsGrupo))
        itemsGrupo.triggered.connect(self.FMenuContextual)
        menu.exec(self.Inter.Ingresos.mapToGlobal(posicion)) #Ingresos.viewport().
    def FMenuContextual(self, accion):
        #indices = self.Inter.selectedIndexes()

        if accion.text() == "Herraje":
            #print('Herraje')
            txhr = self.Inter.TXClave.text()
            txhr = "HR-" + txhr
            self.Inter.TXClave.setText(txhr)
        elif accion.text() == "Perfil":
            #print('Perfil')
            txpf = self.Inter.TXClave.text()
            txpf = "PF-" + txpf
            self.Inter.TXClave.setText(txpf)
        elif accion.text() == "Vidrio":
            #print('Vidrio')
            txvd = self.Inter.TXClave.text()
            txvd = "VD-" + txvd
            self.Inter.TXClave.setText(txvd)
        elif accion.text() == "Silicon":
            #print('Silicon')
            txsl = self.Inter.TXClave.text()
            txsl = "SL-" + txsl
            self.Inter.TXClave.setText(txsl)
        elif accion.text() == "General":
            #print('General')
            txgn = self.Inter.TXClave.text()
            txgn = "GN-" + txgn
            self.Inter.TXClave.setText(txgn)
        elif accion.text() == "Peliculas":
            #print('Peliculas')
            txpc = self.Inter.TXClave.text()
            txpc = "PC-" + txpc
            self.Inter.TXClave.setText(txpc)
        elif accion.text() == "Liquidos":
            #print('Liquidos')
            txli = self.Inter.TXClave.text()
            txli = "LI-" + txli
            self.Inter.TXClave.setText(txli)
        elif accion.text() == "Cintas":
            #print('Cintas')
            txct = self.Inter.TXClave.text()
            txct = "CT-" + txct
            self.Inter.TXClave.setText(txct)
        else:
            pass
    
    def IngresosBT(self):
        self.Solicitud = Permiso()
        self.Solicitud.show()
        self.Solicitud.setWindowTitle('Ingresar Producto al Inventario')

        self.Solicitud.BTOk.clicked.connect(self.FBTIngresarUsuario1)
        self.Solicitud.BTCans.clicked.connect(self.FBTIngresarUsuario12)
    def FBTIngresarUsuario1(self):
        if self.Solicitud.Contrase.text() == self.Keyy:
            print('correcto')
            self.Solicitud.close()
            self.Inter.Libro1.setCurrentWidget(self.Inter.Ingresos)
        else:
            print('Incorrecto')
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Solicite el Acceso Al Administrador")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()
            self.Solicitud.Contrase.clear()
    def FBTIngresarUsuario12(self):
        self.Solicitud.close()
        self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)

    def AjusteInvBT(self):
        self.Solicitud2 = Permiso()
        self.Solicitud2.show()
        self.Solicitud2.setWindowTitle('Ingresar Producto al Inventario')

        self.Solicitud2.BTOk.clicked.connect(self.FBTIngresarUsuario2)
        self.Solicitud2.BTCans.clicked.connect(self.FBTIngresarUsuario22)
    def FBTIngresarUsuario2(self):
        if self.Solicitud2.Contrase.text() == self.KeyMaster:
            print('correcto')
            self.Solicitud2.close()
            self.Inter.Libro1.setCurrentWidget(self.Inter.AjusteInv)
        else:
            print('Incorrecto')
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Solicite el Acceso Al Administrador")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()
            self.Solicitud2.Contrase.clear()
    def FBTIngresarUsuario22(self):
        self.Solicitud2.close()
        self.Inter.Libro1.setCurrentWidget(self.Inter.Inicio)

    def RefescarTooodo(self):
            #Hoja2
        self.Refrescar2()
        self.LLenarCBBuscar()
            #Hoja 2

            #Hoja5
        self.Refrescar5()
        self.LLenarCBBuscar1()
            #Hoja5
        
            #Hoja6
        self.Refrescar6()
        self.LLenarCBBuscar_3()
        self.LLenarCBBuscar_4()
            #Hoja6

            #Hoja7
        self.Refrescar7()
        self.LLenarCBBuscar_5()
            #Hoja7
        
            #Hoja8
        self.Refrescar8()
        self.LLenarCBBuscar_2()
            #Hoja8
         
    #=========================================BOTONES DE LA BARRA PRINCIPAL==========================================#

    #=========================================VENTANAS DE LOS BOTONES DEL MENU==========================================#            
    def DiviIVA(self):
        #self.Calcu
        #app2 = QDialog(self)
        myApp2 = VentanaDivisas()
        myApp2.show()
        #app2.exec_()
     
    def Calc(self):
        #self.Calcu
        #app1 = QDialog(self)
        myApp1 = VentanaCalculadora()
        myApp1.show()
        #app1.exec_()
        #pass

    def licencia(self):
        dialogo = QMessageBox()
        dialogo.setText("Programa De Inventarios con Base de Datos Integrada \n                                  Version: 3.2 \n       Derechos Reservados - DesinGlass Company ©")
        dialogo.setWindowTitle("DesinGlass Smart Windows")
        dialogo.setWindowIcon(QIcon('DG.png'))
        dialogo.exec_()

    def AcercaDe(self):
        dialogo = QMessageBox()
        dialogo.setText("Desarrollado en Pyton 3.10.6 \n          By: Isaac Montes")
        dialogo.setWindowTitle("DesinGlass Smart Windows")
        dialogo.setWindowIcon(QIcon('DG.png'))
        dialogo.setIcon(QMessageBox.Information)
        dialogo.exec_()

    def Salir(self):
        mensaje = QMessageBox.question(self, "DesinGlass Smart Windows", "¿Esta seguro de Salir del Programa?", QMessageBox.Yes | QMessageBox.No)
        if mensaje == QMessageBox.Yes:
            self.close()
        else:
            pass

    def Refrescar2(self):
        self.LimpiarTabla21()
        self.MostarProductos()

    def Refrescar3(self):
        pass

    def Refrescar4(self):
        self.Inter.Titulo41.setText('Historial de Movimientos') #Resetear el titulo
        self.Inter.TWHistorial.clear() #Limpiar Contenido
        self.Inter.TWHistorial.setColumnCount(0) #Columnas
        self.Inter.TWHistorial.setRowCount(0)  #FIlas
        self.Inter.BTImprimir.hide() #Quitar Boton
        self.Inter.BTEditar.hide()  #Quitar Boton

    def Refrescar5(self):
        self.LimpiarTWProveedores()
        self.MostarTWProveedores()

    def Refrescar6(self):
        #===========SALIDAS==========#
        self.LimpiarTWProductos_3() #Producto Salida
        self.MostarTWProductos_3() #Producto Salinas
        #self.LimpiarTWLista_2()
        #self.MostarTWLista_2()
        #self.MostrarEncabezadoSAL()   
        fsal = self.Salidas.ConsultarSalidasR("ID")
        #print(fsal)
        if fsal == []:
            self.Inter.TXUltFol_2.setText("S/R")
        else:
            fsal = fsal[0]
            #print(fsal[1])
            self.Inter.TXUltFol_2.setText(fsal[1])
        #===========SALIDAS==========#
             
        #===========ENTRADAS==========#
        self.LimpiarTWProductos_2() #Producto Entrada
        self.MostarTWProductos_2() #Producto Entrada
        #self.LimpiarTWLista()
        #self.MostarTWLista()
        #self.MostrarEncabezadoENT()
        fent = self.Entradas.ConsultarEntradasR("ID")
        #print(fent)
        if fent == []:
            self.Inter.TXUltFol.setText("S/R")
        else:
            fent = fent[0]
            #print(fent[1])
            self.Inter.TXUltFol.setText(fent[1])
        #===========ENTRADAS==========#

    def Refrescar7(self):
        self.LimpiarTWProductos_5() #Producto Lista
        self.MostarTWProductos_5() #Producto Lista

        fent = self.Listas.ConsultarListasR("ID")
        #print(fent)
        if fent == []:
            self.Inter.TXUltFol_3.setText("S/R")
        else:
            fent = fent[0]
            #print(fent[1])
            self.Inter.TXUltFol_3.setText(fent[1])

    def Refrescar8(self):
        self.LimpiarTWProductos()
        self.MostarTWProductos()

    def IMPRIMIR(self, Folio, Ubicacion):
        if Ubicacion == "Listas":
            #print(1)
            ImpList = CrearPDF()
            ImpList.PDFListas(Folio)
        elif Ubicacion == "Salidas":
            #print(2)
            ImpSalidas = CrearPDF()
            ImpSalidas.PDFSalidas(Folio)
        elif Ubicacion == "Entradas":
            #print(3)
            ImpEntradas = CrearPDF()
            ImpEntradas.PDFEntradas(Folio)
        else:
            dialogo = QMessageBox()
            dialogo.setText("No se Encontro el Folio Ingresado En la Base de Datos")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMainWindow.Critical)
            dialogo.exec_()

    def REPORTE(self, Fecha1, Fecha2):
        from datetime import datetime
        FCH11 = str(Fecha1)
        FCH21 = str(Fecha2)
        #print(FCH11)
        #print(FCH21)

        Fecha1 = str(Fecha1.replace("-","/"))
        Fecha2 = str(Fecha2.replace("-","/"))

        FCH1 = datetime.strptime(Fecha1, '%Y/%m/%d')
        FCH2 = datetime.strptime(Fecha2, '%Y/%m/%d')
        #print(type(FCH2))
        #print(FCH2)

        #print(type(Fecha2))
        #print(Fecha2)
        lista = []

        if FCH1 < FCH2:
            Fecha1 = str(Fecha1 + " 00:00:00")
            Fecha2 = str(Fecha2 + " 23:59:59")

            Fecha1 = datetime.strptime(Fecha1, '%Y/%m/%d %H:%M:%S')
            Fecha2 = datetime.strptime(Fecha2, '%Y/%m/%d %H:%M:%S')

            print('es menor')
            movimientos = self.Movimientoss.ConsultarMovimientos("ID")
            for i in movimientos:
                Valor = datetime.strptime(i[11], '%Y/%m/%d %H:%M:%S')
                if Valor >= Fecha1 and Valor <= Fecha2:
                    agregar = [
                        i[1],
                        i[2],
                        i[3],
                        i[4],
                        i[5],
                        i[6],
                        i[7],
                        i[8],
                        i[9],
                        i[10],
                        i[11]
                    ]
                    lista.append(agregar)
        elif FCH1 > FCH2:
            Fecha2 = str(Fecha2 + " 00:00:00")
            Fecha1 = str(Fecha1 + " 23:59:59")

            Fecha1 = datetime.strptime(Fecha1, '%Y/%m/%d %H:%M:%S')
            Fecha2 = datetime.strptime(Fecha2, '%Y/%m/%d %H:%M:%S')
        
            print('es mayor')
            movimientos = self.Movimientoss.ConsultarMovimientosR("ID")
            for i in movimientos:
                Valor = datetime.strptime(i[11], '%Y/%m/%d %H:%M:%S')
                if Valor >= Fecha2 and Valor <= Fecha1:
                    agregar = [
                        i[1],
                        i[2],
                        i[3],
                        i[4],
                        i[5],
                        i[6],
                        i[7],
                        i[8],
                        i[9],
                        i[10],
                        i[11]
                    ]
                    lista.append(agregar)
        else:
            Fecha1 = str(Fecha1 + " 00:00:00")
            Fecha2 = str(Fecha2 + " 23:59:59")

            Fecha1 = datetime.strptime(Fecha1, '%Y/%m/%d %H:%M:%S')
            Fecha2 = datetime.strptime(Fecha2, '%Y/%m/%d %H:%M:%S')

            print('es igual')
            movimientos = self.Movimientoss.ConsultarMovimientos("ID")
            for i in movimientos:
                Valor = datetime.strptime(i[11], '%Y/%m/%d %H:%M:%S')
                if Valor >= Fecha1 and Valor <= Fecha2:
                    agregar = [
                        i[1],
                        i[2],
                        i[3],
                        i[4],
                        i[5],
                        i[6],
                        i[7],
                        i[8],
                        i[9],
                        i[10],
                        i[11]
                    ]
                    lista.append(agregar)

        #print(lista)
        #FCH11 = Fecha1.replace("/","-")
        #FCH21 = Fecha2.replace("/","-")
        Imprimir = HojaReporte()
        Imprimir.PDFReporte(FCH11, FCH21, lista)

    def EDITAR(self, Folio, Ubicacion):
        segunda = VentanaSecundaria(Ubicacion)
        segunda.show()

    def Contrasenas(self):
        conn = sqlite3.connect("UsuariosDG.db")
        c = conn.cursor()
        buscar = "SELECT * FROM Usuarios WHERE ID= 1"
        c.execute(buscar)
        buscado = c.fetchall()
        c.close()
        key = buscado[0]
        #print(key[1], key[2])
        self.Keyy = str(key[1])
        self.KeyMaster = str(key[2])
    
    #=========================================VENTANAS DE LOS BOTONES DEL MENU==========================================#   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = VentanaPrincipal()
    #myApp = arranque()
    myApp.show()
    #sys.exit(app.exec_())
    app.exec_()

