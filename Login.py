import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox, QInputDialog
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator, QPainter
import sqlite3
from sqlite3 import *
import time
import os
import keyboard
from LoginInt import Ui_Inicio

from ConstructorBases import *
from main import VentanaPrincipal
from Permiso import *

import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class VentanaLoginn(QMainWindow):
    def __init__(self):
        super(VentanaLoginn, self).__init__()
        self.Inter = uic.loadUi('LoginInt.ui', self)
        self.Inter.setWindowTitle('Inicio de Sesion')
        self.Inter.setWindowIcon(QIcon('IconoEsfera.png'))
        self.KeyMaster = 'BAVI751018HDFRRG06'
        #self.Inter = Ui_Inicio()

        #Verificar Base de Datos#
        self.bd = ""
        Archivo = "UsuariosDG.db"
        Validar = os.path.isfile(Archivo)
        

        if Validar == True:
            self.bd = True
        else:
            self.bd = False

        #self.bd = False
        #verificar Base de Datos#

        #Ocultar los Botones#
        self.Inter.BTMax2.hide()
        self.Inter.BTMax.hide()
        #Ocultar los botones#
        
        #Eliminar barra y titulo -opacidad#
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        #Eliminar barra y titulo -opacidad#

        #===========================Botones=============================#
            #Pestaña 1#
        self.Inter.BTIngresar.clicked.connect(self.FBTIngresar) #Buscar# 
        self.Inter.BTSalir.clicked.connect(self.close)#Salir#

        self.Inter.CHBMostrar.clicked.connect(self.FCHBMostrar) #Mostra#
            #Pestaña 1#

            #Pestaña 2#
        self.Inter.Informacion #Cargando Recursos . . .#
        self.Inter.BarProgress #Progress Barr#
        self.Inter.Terminado #Terminado#

            #Pestaña 2#
        
            #Pestaña 3#
        self.Inter.BTAgregar.clicked.connect(self.FBTAgregar) #Agregar#
        self.Inter.CHBMostrar_2.clicked.connect(self.FCHBMostrar_2) #Mostrar 1#
        self.Inter.CHBMostrar_3.clicked.connect(self.FCHBMostrar_3) #Mostrar 2#
            #Pestaña 3#

            #Pestaña 4#
        self.Inter.BTBuscar.clicked.connect(self.FBTBuscar) #Buscar#
        self.Inter.BTActualizar.clicked.connect(self.FBTActualizar) #Actualizar#
        self.Inter.CHBMostrar_4.clicked.connect(self.FCHBMostrar_4) #Mostrar 1#
        self.Inter.CHBMostrar_5.clicked.connect(self.FCHBMostrar_5) #Mostrar 2#
            #Pestaña 4#

        #===========================Botones=============================#

        #===========================TECLADO=============================#
        try:
           self.Inter.BTNUs.clicked.connect(self.IngresarUsuario) #Arriba# Para Ingresar Usuarios
           self.Inter.BTCUs.clicked.connect(self.CambiarUsuario) #Abajo# Para Cambiar Usuarios
           self.Inter.BTBorrar.clicked.connect(self.FBTBorrar) #Abajo# Para Borrar Usuarios
        except:
            print('ERORR')
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
        self.FrameControles.mouseMoveEvent = self.MoverVentana
        #Mover Ventana#
    
    #=========================================FUNCIONES BOTONES==========================================#
    def FBTIngresar(self):
        if self.Inter.TXUsuario.text() == "" or self.Inter.TXContrasena.text() == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Llene Corecctamente Los Campos del Formulario")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Warning)
            dialogo.exec_()
        else:
            #print(self.bd)
            if self.bd == False:
                self.Inter.Terminado.hide()
                self.Inter.Paginas.setCurrentWidget(self.Inter.Pag2)
               
                time.sleep(1)
                print('Cambio de pestaña')
                time.sleep(0)

                self.ProgresBarr()

                #Informar que ya se crearon las bases de datos#
                self.Inter.Paginas.setCurrentWidget(self.Inter.Pag1)

                self.Inter.Informacion.show() #Cargando Recursos . . .#
                self.Inter.BarProgress.show() #Progress Barr#
                self.Inter.Terminado.hide() #Terminado#

                dialogo = QMessageBox()
                dialogo.setText("Se Han Cargado Los Recusrsos Correctamente")
                dialogo.setWindowTitle("DesinGlass Smart Windows")
                dialogo.setWindowIcon(QIcon('DG.png'))
                dialogo.setIcon(QMessageBox.Information)
                dialogo.exec_()

                self.Inter.TXUsuario.clear()
                self.Inter.TXContrasena.clear()

                self.Inter.close()
                #self.Inter.show()
            else:
                Usuario = self.Inter.TXUsuario.text()
                contrasena = self.Inter.TXContrasena.text()
                Usuario = Usuario.upper()

                #Consultar la base de datos#
                conn = sqlite3.connect("UsuariosDG.db")
                c = conn.cursor()
                buscar = "SELECT * FROM Usuarios WHERE Usuario= '{}'".format(str(Usuario))
                c.execute(buscar)

                buscado = c.fetchall()
                UsuarioBD = ""
                contrasenaBD = ""

                #Asignar valores#
                for i in buscado:
                    UsuarioBD = i[1]
                    contrasenaBD = i[2]

                conn.commit()
                #Consultar la base de datos#
                #print(UsuarioBD)

                if Usuario == UsuarioBD:
                    if contrasena == contrasenaBD:
                        self.Inter.hide()
                        dialogoB = QMessageBox()
                        dialogoB.setText("Bienvenido: "+ str(Usuario.capitalize()))
                        dialogoB.setWindowTitle("DesinGlass Smart Windows")
                        dialogoB.setWindowIcon(QIcon('DG.png'))
                        dialogoB.setIcon(QMessageBox.Information)
                        dialogoB.exec_()
                        myApp = VentanaPrincipal()
                        myApp.show()
                    else:
                        dialogoC = QMessageBox()
                        dialogoC.setText("La Contraseña Esta Mal Escrita")
                        dialogoC.setWindowTitle("DesinGlass Smart Windows")
                        dialogoC.setWindowIcon(QIcon('DG.png'))
                        dialogoC.setIcon(QMessageBox.Critical)
                        dialogoC.exec_()
                else:
                    dialogoU = QMessageBox()
                    dialogoU.setText("El Usuario Esta Mal Escrito o no Esta Registrado")
                    dialogoU.setWindowTitle("DesinGlass Smart Windows")
                    dialogoU.setWindowIcon(QIcon('DG.png'))
                    dialogoU.setIcon(QMessageBox.Critical)
                    dialogoU.exec_()  

    def FCHBMostrar(self):
        if self.Inter.CHBMostrar.isChecked() == True:
            self.Inter.TXContrasena.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.Inter.TXContrasena.setEchoMode(QtWidgets.QLineEdit.Password)

    def ProgresBarr(self):
        base = inevntario()     
        print('creando las cosas ...')
        base.Lista()
        base.Encabezado()
        self.Inter.BarProgress.setValue(0)

        #Primera Base#
        self.login()
        self.Inter.BarProgress.setValue(14) #Progress Barr#
        #Primera Base#

        #Segunda Base#
        base.Inventario()
        self.Inter.BarProgress.setValue(28) #Progress Barr#
        #Segunda Base#

        #Tercera Base#
        base.Movimientos()
        self.Inter.BarProgress.setValue(42) #Progress Barr#
        #Tercera Base#

        #Cuarta Base#
        base.Proveedores()
        self.Inter.BarProgress.setValue(56) #Progress Barr#
        #Cuarta Base#

        #Quinta Base#
        base.RegistroSalidas()
        self.Inter.BarProgress.setValue(70) #Progress Barr#
        #Quinta Base#

        #Sexta Base#
        base.RegistroEntradas()
        self.Inter.BarProgress.setValue(84) #Progress Barr#
        #Sexta Base#

        #Septima Base#
        base.ListasDeSalidas()
        self.Inter.BarProgress.setValue(100) #Progress Barr#
        #Septima Base#

        time.sleep(0.5)
        self.Inter.Informacion.hide() #Cargando Recursos . . .#
        self.Inter.BarProgress.hide() #Progress Barr#
        self.Inter.Terminado.show() #Terminado#
        time.sleep(0)
    
    def FBTAgregar(self):
        if self.Inter.TXNuevoUsuario.text() == "" or self.Inter.TXContrasena_2.text() == "" or self.Inter.TXCOnfContrasena.text() == "":
            #dialogo = QMessageBox.question(self,"DesinGlass Smart Windows", "Por Favor Llene Corecctamente Los Campos del Formulario\n ¿Quiere Intentarlo De Nuevo?", QMessageBox.Cancel | QMessageBox.Retry)
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Llene Corecctamente Los Campos del Formulario\n ¿Quiere Intentarlo De Nuevo?")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Question)
            dialogo.setStandardButtons(QMessageBox.Cancel | QMessageBox.Retry)
            dialogo.setInformativeText('Al cancelar se enviara al menu principal')
            dialogo.buttonClicked.connect(self.FinPregunta)
            dialogo.exec_()
        else:
            if self.bd == False:
                dialogo1 = QMessageBox()
                dialogo1.setText("No Se Han Cargado Los Recursos, ERROR:404")
                dialogo1.setWindowTitle("DesinGlass Smart Windows")
                dialogo1.setWindowIcon(QIcon('DG.png'))
                dialogo1.setIcon(QMessageBox.Critical)
                dialogo1.exec_()
            else:
                Usuario = self.Inter.TXNuevoUsuario.text()
                Usuario = Usuario.upper()
                contrasena = self.Inter.TXContrasena_2.text()
                contrasena2 = self.Inter.TXCOnfContrasena.text()

                if contrasena != contrasena2:
                    dialogo2 = QMessageBox()
                    dialogo2.setText("Las Contraseñas Son Diferentes")
                    dialogo2.setWindowTitle("DesinGlass Smart Windows")
                    dialogo2.setWindowIcon(QIcon('DG.png'))
                    dialogo2.setIcon(QMessageBox.Warning)
                    dialogo2.exec_()
                else:
                    #Consultar la base de datos#
                    conn = sqlite3.connect("UsuariosDG.db")
                    c = conn.cursor()
                    buscar = "SELECT * FROM Usuarios WHERE Usuario= '{}'".format(str(Usuario))
                    c.execute(buscar)

                    buscado = c.fetchall()
                    UsuarioBD = ""

                    #Asignar valores#
                    for i in buscado:
                        UsuarioBD = i[1]

                    conn.commit()
                    #Consultar la base de datos#
                    #print(UsuarioBD)

                    if Usuario == UsuarioBD:
                        dialogo = QMessageBox()
                        dialogo.setText("Ya Existe Un Usuario Registrado Con Este Nombre")
                        dialogo.setWindowTitle("DesinGlass Smart Windows")
                        dialogo.setWindowIcon(QIcon('DG.png'))
                        dialogo.setIcon(QMessageBox.Warning)
                        dialogo.exec_()
                    else:
                        Ingreso = "INSERT INTO Usuarios VALUES(NULL,'{}','{}')".format(str(Usuario), str(contrasena))
                        c.execute(Ingreso)

                        conn.commit()
                        self.Inter.Paginas.setCurrentWidget(self.Inter.Pag1)

                        dialogoB = QMessageBox()
                        dialogoB.setText("Se Ha Creado Un Nuevo Usuario, Bienvenido: "+ str(Usuario.capitalize()))
                        dialogoB.setWindowTitle("DesinGlass Smart Windows")
                        dialogoB.setWindowIcon(QIcon('DG.png'))
                        dialogoB.setIcon(QMessageBox.Information)
                        dialogoB.exec_()
    def FinPregunta(self, i):
        respuesta = i.text()
        if respuesta == 'Retry':
            pass
        else:
            self.Inter.Paginas.setCurrentWidget(self.Inter.Pag1)

    def FCHBMostrar_2(self):
        if self.Inter.CHBMostrar_2.isChecked() == True:
            self.Inter.TXContrasena_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.Inter.TXContrasena_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def FCHBMostrar_3(self):
        if self.Inter.CHBMostrar_3.isChecked() == True:
            self.Inter.TXCOnfContrasena.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.Inter.TXCOnfContrasena.setEchoMode(QtWidgets.QLineEdit.Password)

    def FBTBuscar(self):
        BusUsu =self.Inter.TXUsuario_2.text()
        BusUsu = BusUsu.upper()
        #Consultar la base de datos#
        conn = sqlite3.connect("UsuariosDG.db")
        c = conn.cursor()
        buscar = "SELECT * FROM Usuarios WHERE Usuario= '{}'".format(str(BusUsu))
        c.execute(buscar)

        buscado = c.fetchall()

        Usuario = ""
        Contrasena = ""

        #Asignar valores#
        for i in buscado:
            Usuario = i[1]
            Contrasena = i[2]

        conn.commit()
        #Consultar la base de datos#

        if Usuario == "":
            dialogoB = QMessageBox()
            dialogoB.setText("No se a Podido Encontrar al Usuario: "+ str(Usuario.capitalize()))
            dialogoB.setWindowTitle("DesinGlass Smart Windows")
            dialogoB.setWindowIcon(QIcon('DG.png'))
            dialogoB.setIcon(QMessageBox.Information)
            dialogoB.exec_()
        else:
            self.Usuario = Usuario
            self.Inter.TXUsuario_2.setText(Usuario.capitalize())
            self.Inter.TXNuevaContrasena.setText(Contrasena)



    def FBTActualizar(self):
        usuario1 =self.Usuario
        #usuario1 = usuario1.upper()
        usuario2 = self.Inter.TXUsuario_2.text()
        usuario2 = usuario2.upper()
        contrasena1 = self.Inter.TXNuevaContrasena.text()
        contrasena2 = self.Inter.TXConfirmarContrasena.text()

        if usuario2 == "" or contrasena1 == "" or contrasena2 == "":
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Llene Corecctamente Los Campos del Formulario\n ¿Quiere Intentarlo De Nuevo?")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Question)
            dialogo.setStandardButtons(QMessageBox.Cancel | QMessageBox.Retry)
            dialogo.setInformativeText('Al cancelar se enviara al menu principal')
            dialogo.buttonClicked.connect(self.FinPregunta)
            dialogo.exec_()
        else:
            #Consultar la base de datos#
            conn = sqlite3.connect("UsuariosDG.db")
            c = conn.cursor()
            buscar = "SELECT * FROM Usuarios WHERE Usuario= '{}'".format(str(usuario1))
            c.execute(buscar)

            buscado = c.fetchall()

            validar = ""

            #Asignar valores#
            for e in buscado:
                validar = e[1]

            conn.commit()
            #Consultar la base de datos#
            print(validar)
            print(usuario2)

            if validar != usuario1:
                dialogo2 = QMessageBox()
                dialogo2.setText("No Esta Registrado el Usuario Que Solicita")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()
            else:
                if usuario1 != usuario2:
                    pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Cambiar El Nombre de Usuario?", QMessageBox.Yes | QMessageBox.No)
                    if pregunta == QMessageBox.Yes:
                        pregunta2 = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
                        if pregunta2 == QMessageBox.Yes:
                            Actuali = "UPDATE Usuarios SET Usuario='{}', Contraseña='{}' WHERE Usuario='{}'".format(str(usuario2), str(contrasena1), str(usuario1))
                            c.execute(Actuali)

                            conn.commit()

                            dialogoB = QMessageBox()
                            dialogoB.setText("Se Ha Actualizado Correctamete")
                            dialogoB.setWindowTitle("DesinGlass Smart Windows")
                            dialogoB.setWindowIcon(QIcon('DG.png'))
                            dialogoB.setIcon(QMessageBox.Information)
                            dialogoB.exec_()

                            self.Inter.TXUsuario_2.clear()
                            self.Inter.TXNuevaContrasena.clear()
                            self.Inter.TXConfirmarContrasena.clear()
                        else:
                            dialogo3 = QMessageBox()
                            dialogo3.setText("Operacion Cancelada")
                            dialogo3.setWindowTitle("DesinGlass Smart Windows")
                            dialogo3.setWindowIcon(QIcon('DG.png'))
                            dialogo3.setIcon(QMessageBox.Warning)
                            dialogo3.exec_()
                    else:
                        pregunta3 = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
                        if pregunta3 == QMessageBox.Yes:
                            Actuali1 = "UPDATE Usuarios SET Usuario='{}', Contraseña='{}' WHERE Usuario='{}'".format(str(usuario1), str(contrasena1), str(usuario1))
                            c.execute(Actuali1)

                            conn.commit()

                            dialogoB1 = QMessageBox()
                            dialogoB1.setText("Se Ha Actualizado Correctamete")
                            dialogoB1.setWindowTitle("DesinGlass Smart Windows")
                            dialogoB1.setWindowIcon(QIcon('DG.png'))
                            dialogoB1.setIcon(QMessageBox.Information)
                            dialogoB1.exec_()

                            self.Inter.TXUsuario_2.clear()
                            self.Inter.TXNuevaContrasena.clear()
                            self.Inter.TXConfirmarContrasena.clear()
                else:
                    pregunta4 = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
                    if pregunta4 == QMessageBox.Yes:
                        Actuali2 = "UPDATE Usuarios SET Usuario='{}', Contraseña='{}' WHERE Usuario='{}'".format(str(usuario1), str(contrasena1), str(usuario1))
                        c.execute(Actuali2)

                        conn.commit()

                        dialogoB12 = QMessageBox()
                        dialogoB12.setText("Se Ha Actualizado Correctamete")
                        dialogoB12.setWindowTitle("DesinGlass Smart Windows")
                        dialogoB12.setWindowIcon(QIcon('DG.png'))
                        dialogoB12.setIcon(QMessageBox.Information)
                        dialogoB12.exec_()

                        self.Inter.TXUsuario_2.clear()
                        self.Inter.TXNuevaContrasena.clear()
                        self.Inter.TXConfirmarContrasena.clear()
        #Eliminar Usuario#
    def FBTBorrar(self):
        self.Solicitud = Permiso()
        self.Solicitud.show()
        self.Solicitud.Contrase.clear()
        self.Solicitud.Titulo.setText('Ingrese Nombre de Usuario: ')
        self.Solicitud.setWindowTitle('Eliminar Usuario')

        self.Solicitud.BTOk.clicked.connect(self.EliminarUsuario)
        self.Solicitud.BTCans.clicked.connect(self.EliminarUsuario1)
    def EliminarUsuario(self):
        usuario = self.Solicitud.Contrase.text()
        usuario = usuario.upper()
        #Consultar la base de datos#
        conn = sqlite3.connect("UsuariosDG.db")
        c = conn.cursor()
        buscar = "SELECT * FROM Usuarios WHERE Usuario= '{}'".format(str(usuario))
        c.execute(buscar)

        buscado = c.fetchall()
        usuarioBD = ""

        #Asignar valores#
        for i in buscado:
            usuarioBD = i[1]

        conn.commit()
        #Consultar la base de datos#
        if usuario  == usuarioBD:
            print('correcto')
            pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Eliminar El Nombre de Usuario?", QMessageBox.Yes | QMessageBox.No)
            if pregunta == QMessageBox.Yes:
                Borrar = "DELETE FROM Usuarios WHERE Usuario='{}'".format(str(usuario))

                c.execute(Borrar)
                conn.commit()

                dialogoB12 = QMessageBox()
                dialogoB12.setText("Se Ha Eliminado Correctamete")
                dialogoB12.setWindowTitle("DesinGlass Smart Windows")
                dialogoB12.setWindowIcon(QIcon('DG.png'))
                dialogoB12.setIcon(QMessageBox.Information)
                dialogoB12.exec_()

                self.Solicitud1.close()
            else:
                dialogo2 = QMessageBox()
                dialogo2.setText("Operacion Cancelada")
                dialogo2.setWindowTitle("DesinGlass Smart Windows")
                dialogo2.setWindowIcon(QIcon('DG.png'))
                dialogo2.setIcon(QMessageBox.Warning)
                dialogo2.exec_()

                self.Solicitud.close()
        else:
            print('Incorrecto')
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Escriba un Nombre Ya Registrado")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()
            self.Solicitud.Contrase.clear()
    def EliminarUsuario1(self):
        self.Solicitud.close()
        #Eliminar Usuario#

    def FCHBMostrar_4(self):
        if self.Inter.CHBMostrar_4.isChecked() == True:
            self.Inter.TXNuevaContrasena.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.Inter.TXNuevaContrasena.setEchoMode(QtWidgets.QLineEdit.Password)

    def FCHBMostrar_5(self):
        if self.Inter.CHBMostrar_5.isChecked() == True:
            self.Inter.TXConfirmarContrasena.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.Inter.TXConfirmarContrasena.setEchoMode(QtWidgets.QLineEdit.Password)

        #Verificar Dialogo 1#
    def IngresarUsuario(self):
        #print('comando')
        #contrasena = QInputDialog.getText(self, 'Permisos del Administrador', 'Ingrese la Contraseña: ')
        #print(contrasena)
        self.Solicitud = Permiso()
        self.Solicitud.show()
        self.Solicitud.setWindowTitle('Ingresar Nuevo Usuario')

        self.Solicitud.BTOk.clicked.connect(self.FBTIngresarUsuario1)
        self.Solicitud.BTCans.clicked.connect(self.FBTIngresarUsuario12)
    def FBTIngresarUsuario1(self):
        if self.Solicitud.Contrase.text() == self.KeyMaster:
            print('correcto')
            self.Solicitud.close()
            self.Inter.Paginas.setCurrentWidget(self.Inter.Pag3)
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
        #Verificar Dialogo 1#

        #Verificar Dialogo 2#
    def CambiarUsuario(self):
        #print('comando')
        #contrasena = QInputDialog.getText(self, 'Permisos del Administrador', 'Ingrese la Contraseña: ')
        #print(contrasena)
        self.Solicitud = Permiso()
        self.Solicitud.show()
        self.Solicitud.setWindowTitle('Cambiar Datos del Usuario')

        self.Solicitud.BTOk.clicked.connect(self.FBTIngresarUsuario2)
        self.Solicitud.BTCans.clicked.connect(self.FBTIngresarUsuario22)

    def FBTIngresarUsuario2(self):
        if self.Solicitud.Contrase.text() == self.KeyMaster:
            print('correcto')
            self.Solicitud.close()
            self.Inter.Paginas.setCurrentWidget(self.Inter.Pag4)
        else:
            print('Incorrecto')
            dialogo = QMessageBox()
            dialogo.setText("Por Favor Solicite el Acceso Al Administrador")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()
            self.Solicitud.Contrase.clear()
    def FBTIngresarUsuario22(self):
        self.Solicitud.close()
        #Verificar Dialogo 2#

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
            #self.Inter.BTMax.hide()
            #self.Inter.BTMax2.show()
        else:
            self.showNormal()
            #self.Inter.BTMax.show()
            #self.Inter.BTMax2.hide()
    #=========================================BOTONES DE LA BARRA PRINCIPAL==========================================#
        

    def login(self):
        if self.bd == True: 
            pass
        else:
            conn = sqlite3.connect("UsuariosDG.db")
            c = conn.cursor()
            try:
                c.execute('''
                    CREATE TABLE IF NOT EXISTS Usuarios (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Usuario VARCHAR(20) NOT NULL UNIQUE,
                    Contraseña VARCHAR(20) NOT NULL)
                ''')

                Administradores = [
                    ('DesinGlass0119', 'BAVI751018HDFRRG06'),
                    ('IGNACIO', 'Karlita2682'),
                    ('ISAAC', 'Qwerty1379'),
                ]

                c.executemany("INSERT INTO Usuarios VALUES (NULL, ?, ?)", Administradores)
                conn.commit()
                conn.close()
            except:
                dialogo = QMessageBox()
                dialogo.setText("Error Al Crear la Base de Datos")
                dialogo.setWindowTitle("DesinGlass Smart Windows")
                dialogo.setWindowIcon(QIcon('DG.png'))
                dialogo.setIcon(QMessageBox.Critical)
                dialogo.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = VentanaLoginn()
    #myApp = arranque()
    myApp.show()
    sys.exit(app.exec_())
    

