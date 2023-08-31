import fpdf
from fpdf import FPDF
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox, QFileDialog, QSystemTrayIcon
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5 import QtCore, QtWidgets, uic 
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator, QIcon

from IngresarProductos import *
from IngresarEntradas import *
from IngresarSalidas import *
from IngresarListas import *

#P: Portrait (Vertical)
#L: Landscape (Horizontal)

#A4: 210 x 297 mm

class CrearPDF(QMainWindow):
    def __init__(self):
        super(CrearPDF,self).__init__()
        self.fechador =  Pagina1() #Creamos un fechador
        self.Entradas = Pagina4()
        self.Salidas = Pagina5()
        self.Listas = Pagina6()

    def LISTA(self, Folio, Movimiento):
        if Movimiento == "Listas":
            Buscar = self.Listas.BuscarListas(Folio)
        elif Movimiento == "Salidas":
            Buscar = self.Salidas.BuscarSalidas(Folio)
        else:
            Buscar = self.Entradas.BuscarEntradas(Folio)

        if Buscar == []:
            dialogo = QMessageBox()
            dialogo.setText("No Existe El Folio en la Base de Datos")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()
        else:
            Buscar = Buscar[0]
            contador = 0
            Encabezado = []
            Contenido = []
            Extras = []
            for i in Buscar:
                if contador > 0 and contador < 7:
                    Encabezado.append(i)
                    #print(contador, ":" , i, " Encabezado")
                elif contador > 6 and contador < 167:
                    #print(contador, ":" , i, " Contenido")
                    lista = []
                    if contador == 7:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    if contador == 15:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 23:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 31:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 39:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 47:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 55:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 63:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 71:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 79:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 87:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 95:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 103:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 111:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 119:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 127:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 135:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 143:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 151:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                    elif contador == 159:
                        for i2 in range(8):
                           lista.append(Buscar[contador + i2])
                           #print(Buscar[contador + i2])

                        Contenido.append(lista)
                elif contador > 166 and contador <170:
                    Extras.append(i)
                    #print(contador, ":" , i, " Extras")
                else:
                    print('se hizo la exepcion de: ', i)

                contador += 1

            Retorno = [
                Encabezado,
                Contenido,
                Extras
            ]

            return Retorno

    def Ruta(self):
        #========== BUSCAR NOMBRE DE USUARIO DE LA COMPUTADORA  ==========#
        ruta = "C:" + chr(92)+ "Users"+ chr(92)  #especificamos la ruta inicial en: "C:\Users\"
        carpetas = os.listdir(ruta) #revizamos cuantos directorios hay en la ruta
        #carpetas = ['User', 'User', 'User', 'User', 'User', 'User','user']
        #print(carpetas)
        usuario = "" #preparamos la variable que almacenara el nombre de usuario
        if len(carpetas) == 6:
            for i in carpetas: #revisamos cada elemento de la lista para encontrar el nombre de usuario
                if str(i) != 'All Users':
                    #print('Fallo')
                    pass
                    if str(i) != 'Default':
                        #print('Fallo')
                        pass
                        if str(i) != 'Default User':
                            #print('Fallo')
                            pass
                            if str(i) != 'desktop.ini':
                                #print('Fallo')
                                pass
                                if str(i) == 'Public':
                                    #print('Fallo')
                                    pass
                                else: #Aqui nos arroja el unico elemento que es el nombre de usuario de la maquina
                                    usuario = str(i)
                                    #print(i,conta)
            #print(usuario)
        else:
            usuario = ""
        return usuario

    def PDFListas(self, nom):
        #========== CREACION DEL GUARDADOR ==========#
        fecha = self.fechador.FechaLetra() #Fecha de año
        usuario = self.Ruta() #usuario de la PC
        #print(usuario)
        nombre = "Lista_de_Salida-" + nom + "-" + fecha[4] #Nombre del archivo por defecto
        Root = "C:" + chr(92)+ "Users"+ chr(92) + usuario + chr(92) + "Desktop" + chr(92) + nombre #Ruta para el buscador
        #Root = "Acceso rápido"
        #print(ruta)
        if usuario != "":
            fileName = QFileDialog.getSaveFileName(filter= "PDF(*.pdf);;Image JPG(*.jpg);;Image PNG (*.png)",directory=Root)[0] #Guardador
        else:
            fileName = QFileDialog.getSaveFileName(filter= "PDF(*.pdf);;Image JPG(*.jpg);;Image PNG (*.png)",directory="C:\\")[0] #Guardador
        #========== CREACION DEL GUARDADOR ==========#
        #fileName = "C:/Users/OFICINA/Desktop/Lista_de_Salida-Folio-2022.pdf"
        if fileName != "":
            #print(fileName)
            Datos = self.LISTA(nom, "Listas")
            
            Encabezado = Datos[0]
            Contenido = Datos[1]
            Extras = Datos[2]
            #========== CREACION DEL PDF ==========#
            pdf = FPDF(orientation='P', unit='mm', format='A4')
            pdf.add_page()

            pdf.set_font('Arial', '', 12)

            #MEDIDAS DE LAS COLUMNAS Y FILAS#
            Largo = 0
            Alto = 9

            Largo11 = 0
            Alto11 = 8

            Largo21 = 50
            Alto21 = 7

            Alto31 = 6
            Largo31 = 18
            Largo32 = 45
            Largo33 = 20
            Largo34 = 20
            Largo35 = 20
            Largo36 = 20
            Largo37 = 20

            Largo41 = 0
            Alto41 = 5
            #MEDIDAS DE LAS COLUMNAS Y FILAS#

            #contenido#
            #IMAGENES Y MARCAS DE AGUA#
            pdf.image('MarcaDeAgua.png', x=5, y=60, w=200, h=200)
            #pdf.rect(x=30, y= 250, w=40, h=40)
            pdf.image('DGlt ch.png', x=155, y=273, w=45, h=13)
            pdf.image('LogoEmp.png', x=75, y=5, w=65, h=48)
            #IMAGENES Y MARCAS DE AGUA#

            #pdf.set_fill_color(255,255,255)

            #ESPACIOS#
            pdf.cell(w=Largo, h=Alto, txt="", border=0, ln=1, align='C', fill=0)
            pdf.cell(w=Largo, h=Alto, txt="", border=0, ln=2, align='C', fill=0)
            pdf.cell(w=Largo, h=Alto, txt="", border=0, ln=3, align='C', fill=0)
            pdf.cell(w=Largo, h=Alto, txt="", border=0, ln=4, align='C', fill=0)
            #ESPACIOS#

            #TABLA#
            #fila 1#
            pdf.set_font('Arial', 'B', 12)
            TX1 = str("LISTA DE SALIDAS FOLIO: " + str(nom))
            pdf.set_fill_color(r=142,g=169,b=219)
            pdf.cell(w=Largo11, h=Alto11, txt=TX1, border=1, ln=2, align='C', fill=1)
            #fila 1#

            #fila 2#
            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="OBRA:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[1], border=1, align='C', fill=0)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="FECHA:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[2], border=1, align='C', fill=0)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="SOLICITA:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[3], border=1, align='C', fill=0)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="AUTORIZA:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[4], border=1, align='C', fill=0)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="ALMACEN:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[5], border=1, align='C', fill=0)
            #fila 2#

            #fila3#
            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo31, h=Alto31, txt="CLAVE", border=1, align='C', fill=0)
            pdf.cell(w=Largo32, h=Alto31, txt="DESCRIPCION", border=1, align='C', fill=0)
            pdf.cell(w=Largo33, h=Alto31, txt="UNIDAD", border=1, align='C', fill=0)
            pdf.cell(w=Largo34, h=Alto31, txt="CANTIDAD", border=1, align='C', fill=0)
            pdf.cell(w=Largo35, h=Alto31, txt="ANCHO", border=1, align='C', fill=0)
            pdf.cell(w=Largo36, h=Alto31, txt="LARGO", border=1, align='C', fill=0)
            pdf.cell(w=Largo37, h=Alto31, txt="STATUS", border=1, align='C', fill=0)
            pdf.multi_cell(w=Largo, h=Alto31, txt="FOLIO REQ", border=1, align='C', fill=0)
            for i in Contenido:
                #print(i)
                pdf.set_font('Arial', '', 8)
                #=====CLAVE=====
                if len(str(i[0])) > 12:
                    claveCH = str(i[0])
                    claveP = claveCH[0:9] + "..." #11
                    pdf.cell(w=Largo31,h=Alto31, txt=claveP, border=1,align='C',fill=0)
                else:
                    pdf.cell(w=Largo31, h=Alto31, txt=str(i[0]), border=1, align='C', fill=0)
                #=====CLAVE=====

                #=====PRODUCTO=====
                if len(str(i[1])) > 30:
                    ProductoCH = str(i[1])
                    ProductoP = ProductoCH[0:26] + "..." #29
                    pdf.cell(w=Largo32, h=Alto31, txt=ProductoP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo32, h=Alto31, txt=str(i[1]), border=1, align='C', fill=0)
                #=====PRODUCTO=====

                #=====UNIDAD=====
                if len(str(i[2])) > 14:
                    UnidadCH = str(i[2])
                    UnidadP = UnidadCH[0:10] + "..." #13
                    pdf.cell(w=Largo33, h=Alto31, txt=UnidadP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo33, h=Alto31, txt=str(i[2]), border=1, align='C', fill=0)
                #=====UNIDAD=====

                #=====CANTIDAD=====
                if len(str(i[3])) > 10:
                    CantidadCH = str(i[3])
                    CantidadP = CantidadCH[0:7] + "..." #10
                    pdf.cell(w=Largo34, h=Alto31, txt=CantidadP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo34, h=Alto31, txt=str(i[3]), border=1, align='C', fill=0)
                #=====CANTIDAD=====

                #=====ANCHO=====
                if len(str(i[4])) > 15:
                    AnchoCH = str(i[4])
                    AnchoP = AnchoCH[0:12] + "..." #15
                    pdf.cell(w=Largo35, h=Alto31, txt=AnchoP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo35, h=Alto31, txt=str(i[4]), border=1, align='C', fill=0)
                #=====ANCHO=====

                #=====LARGO=====
                if len(str(i[5])) > 15:
                    LargoCH = str(i[5])
                    LargoP = AnchoCH[0:12] + "..." #15
                    pdf.cell(w=Largo36, h=Alto31, txt=LargoP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo36, h=Alto31, txt=str(i[5]), border=1, align='C', fill=0)
                #=====LARGO=====

                #=====STATUS=====
                if len(str(i[6])) >14:
                    StatusCH = str(i[6])
                    StatusP = StatusCH[0:11] + "..." #14
                    pdf.cell(w=Largo37, h=Alto31, txt=StatusP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo37, h=Alto31, txt=str(i[6]), border=1, align='C', fill=0)
                #=====STATUS=====

                #======FOLIO REQ=====
                if len(str(i[7])) > 16:
                    FolioREQCH = str(i[7])
                    FolioREQP = FolioREQCH[0:13] + "..." #16
                    pdf.multi_cell(w=Largo, h=Alto31, txt=FolioREQP, border=1, align='C', fill=0)
                else:
                    pdf.multi_cell(w=Largo, h=Alto31, txt=str(i[7]), border=1, align='C', fill=0)
                #=====FOLIO REQ=====
            #fila3#
            #TABLA#

            #Observaciones#
            pdf.ln(5) 
            obs = "OBSERVACIONES: \n" + str(Extras[2]) 
            pdf.multi_cell(w=Largo, h=Alto41, txt=obs, border=1, align='L', fill=0)
            #Observaciones#

            #Firmas#
            alt = 262
            esp = 10
            lar = 40
            pdf.set_font('Arial', '', 12)
            pdf.ln(5)
            pdf.line(esp, alt, esp+lar, alt)
            pdf.text(x=esp+esp, y=alt+esp-5, txt="ALMACEN")

            pdf.line(esp+lar+esp, alt, esp+lar+esp+lar, alt)
            pdf.text(x=esp+lar+esp+esp, y=alt+esp-5, txt="ENTREGA")

            pdf.line(esp+lar+esp+lar+esp, alt, esp+lar+esp+lar+esp+lar, alt)
            pdf.text(x=esp+lar+esp+lar+esp+esp, y=alt+esp-5, txt="CHOFER")

            pdf.line(esp+lar+esp+lar+esp+lar+esp, alt, esp+lar+esp+lar+esp+lar+esp+lar, alt)
            pdf.text(x=esp+lar+esp+lar+esp+lar+esp+esp, y=alt+esp-5, txt="RECIBE")
            #Firmas#
            
            #contenido#

            #Metadatos#
            pdf.set_title(title=nombre)
            pdf.set_author(author="DesinGlass Company")
            pdf.set_creator(creator="DesinGlass Smart Windows")
            pdf.set_keywords(keywords=f"Hoja, {nombre}, DesinGlass")
            pdf.set_subject(subject="Comprobante de Movimiento")
            #Metadatos

            pdf.output(str(fileName))
            print('listo')
            #========== CREACION DEL PDF ==========#
        else:
            dialogo = QMessageBox()
            dialogo.setText("Operacion Cancelada")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()

    def PDFSalidas(self, nom):
        #========== CREACION DEL GUARDADOR ==========#
        fecha = self.fechador.FechaLetra() #Fecha de año
        usuario = self.Ruta() #usuario de la PC
        #print(usuario)
        nombre = "Hoja_de_Salida-" + nom + "-" + fecha[4] #Nombre del archivo por defecto
        Root = "C:" + chr(92)+ "Users"+ chr(92) + usuario + chr(92) + "Desktop" + chr(92) + nombre #Ruta para el buscador
        #Root = "Acceso rápido"
        #print(ruta)
        if usuario != "":
            fileName = QFileDialog.getSaveFileName(filter= "PDF(*.pdf);;Image JPG(*.jpg);;Image PNG (*.png)",directory=Root)[0] #Guardador
        else:
            fileName = QFileDialog.getSaveFileName(filter= "PDF(*.pdf);;Image JPG(*.jpg);;Image PNG (*.png)",directory="C:\\")[0] #Guardador
        #========== CREACION DEL GUARDADOR ==========#
        #fileName = "C:/Users/OFICINA/Desktop/Lista_de_Salida-Folio-2022.pdf"
        if fileName != "":
            #print(fileName)
            Datos = self.LISTA(nom, "Salidas")
            
            Encabezado = Datos[0]
            Contenido = Datos[1]
            Extras = Datos[2]
            #========== CREACION DEL PDF ==========#
            pdf = FPDF(orientation='P', unit='mm', format='A4')
            pdf.add_page()

            pdf.set_font('Arial', '', 12)

            #MEDIDAS DE LAS COLUMNAS Y FILAS#
            Largo = 0
            Alto = 9

            Largo11 = 0
            Alto11 = 8

            Largo21 = 50
            Alto21 = 7

            Alto31 = 6
            Largo31 = 18
            Largo32 = 45
            Largo33 = 20
            Largo34 = 20
            Largo35 = 20
            Largo36 = 20
            Largo37 = 20

            Largo41 = 0
            Alto41 = 5
            #MEDIDAS DE LAS COLUMNAS Y FILAS#

            #contenido#
            #IMAGENES Y MARCAS DE AGUA#
            pdf.image('MarcaDeAgua.png', x=5, y=60, w=200, h=200)
            #pdf.rect(x=30, y= 250, w=40, h=40)
            pdf.image('DGlt ch.png', x=155, y=273, w=45, h=13)
            pdf.image('LogoEmp.png', x=75, y=5, w=65, h=48)
            #IMAGENES Y MARCAS DE AGUA#

            #pdf.set_fill_color(255,255,255)

            #ESPACIOS#
            pdf.cell(w=Largo, h=Alto, txt="", border=0, ln=1, align='C', fill=0)
            pdf.cell(w=Largo, h=Alto, txt="", border=0, ln=2, align='C', fill=0)
            pdf.cell(w=Largo, h=Alto, txt="", border=0, ln=3, align='C', fill=0)
            pdf.cell(w=Largo, h=Alto, txt="", border=0, ln=4, align='C', fill=0)
            #ESPACIOS#

            #TABLA#
            #fila 1#
            pdf.set_font('Arial', 'B', 12)
            TX1 = str("HOJA DE SALIDAS FOLIO: " + str(nom))
            pdf.set_fill_color(r=142,g=169,b=219)
            pdf.cell(w=Largo11, h=Alto11, txt=TX1, border=1, ln=2, align='C', fill=1)
            #fila 1#

            #fila 2#
            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="OBRA:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[1], border=1, align='C', fill=0)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="FECHA:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[2], border=1, align='C', fill=0)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="SOLICITA:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[3], border=1, align='C', fill=0)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="AUTORIZA:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[4], border=1, align='C', fill=0)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="ALMACEN:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[5], border=1, align='C', fill=0)
            #fila 2#

            #fila3#
            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo31, h=Alto31, txt="CLAVE", border=1, align='C', fill=0)
            pdf.cell(w=Largo32, h=Alto31, txt="DESCRIPCION", border=1, align='C', fill=0)
            pdf.cell(w=Largo33, h=Alto31, txt="UNIDAD", border=1, align='C', fill=0)
            pdf.cell(w=Largo34, h=Alto31, txt="CANTIDAD", border=1, align='C', fill=0)
            pdf.cell(w=Largo35, h=Alto31, txt="ANCHO", border=1, align='C', fill=0)
            pdf.cell(w=Largo36, h=Alto31, txt="LARGO", border=1, align='C', fill=0)
            pdf.cell(w=Largo37, h=Alto31, txt="STATUS", border=1, align='C', fill=0)
            pdf.multi_cell(w=Largo, h=Alto31, txt="FOLIO REQ", border=1, align='C', fill=0)
            for i in Contenido:
                #print(i)
                pdf.set_font('Arial', '', 8)
                #=====CLAVE=====
                if len(str(i[0])) > 12:
                    claveCH = str(i[0])
                    claveP = claveCH[0:9] + "..." #11
                    pdf.cell(w=Largo31,h=Alto31, txt=claveP, border=1,align='C',fill=0)
                else:
                    pdf.cell(w=Largo31, h=Alto31, txt=str(i[0]), border=1, align='C', fill=0)
                #=====CLAVE=====

                #=====PRODUCTO=====
                if len(str(i[1])) > 30:
                    ProductoCH = str(i[1])
                    ProductoP = ProductoCH[0:26] + "..." #29
                    pdf.cell(w=Largo32, h=Alto31, txt=ProductoP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo32, h=Alto31, txt=str(i[1]), border=1, align='C', fill=0)
                #=====PRODUCTO=====

                #=====UNIDAD=====
                if len(str(i[2])) > 14:
                    UnidadCH = str(i[2])
                    UnidadP = UnidadCH[0:10] + "..." #13
                    pdf.cell(w=Largo33, h=Alto31, txt=UnidadP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo33, h=Alto31, txt=str(i[2]), border=1, align='C', fill=0)
                #=====UNIDAD=====

                #=====CANTIDAD=====
                if len(str(i[3])) > 10:
                    CantidadCH = str(i[3])
                    CantidadP = CantidadCH[0:7] + "..." #10
                    pdf.cell(w=Largo34, h=Alto31, txt=CantidadP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo34, h=Alto31, txt=str(i[3]), border=1, align='C', fill=0)
                #=====CANTIDAD=====

                #=====ANCHO=====
                if len(str(i[4])) > 15:
                    AnchoCH = str(i[4])
                    AnchoP = AnchoCH[0:12] + "..." #15
                    pdf.cell(w=Largo35, h=Alto31, txt=AnchoP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo35, h=Alto31, txt=str(i[4]), border=1, align='C', fill=0)
                #=====ANCHO=====

                #=====LARGO=====
                if len(str(i[5])) > 15:
                    LargoCH = str(i[5])
                    LargoP = AnchoCH[0:12] + "..." #15
                    pdf.cell(w=Largo36, h=Alto31, txt=LargoP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo36, h=Alto31, txt=str(i[5]), border=1, align='C', fill=0)
                #=====LARGO=====

                #=====STATUS=====
                if len(str(i[6])) >14:
                    StatusCH = str(i[6])
                    StatusP = StatusCH[0:11] + "..." #14
                    pdf.cell(w=Largo37, h=Alto31, txt=StatusP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo37, h=Alto31, txt=str(i[6]), border=1, align='C', fill=0)
                #=====STATUS=====

                #======FOLIO REQ=====
                if len(str(i[7])) > 16:
                    FolioREQCH = str(i[7])
                    FolioREQP = FolioREQCH[0:13] + "..." #16
                    pdf.multi_cell(w=Largo, h=Alto31, txt=FolioREQP, border=1, align='C', fill=0)
                else:
                    pdf.multi_cell(w=Largo, h=Alto31, txt=str(i[7]), border=1, align='C', fill=0)
                #=====FOLIO REQ=====
            #fila3#
            #TABLA#

            #Observaciones#
            pdf.ln(5) 
            obs = "OBSERVACIONES: \n" + str(Extras[2]) 
            pdf.multi_cell(w=Largo, h=Alto41, txt=obs, border=1, align='L', fill=0)
            #Observaciones#

            #Firmas#
            alt = 262
            esp = 10
            lar = 40
            pdf.set_font('Arial', '', 12)
            pdf.ln(5)
            pdf.line(esp, alt, esp+lar, alt)
            pdf.text(x=esp+esp, y=alt+esp-5, txt="ALMACEN")

            pdf.line(esp+lar+esp, alt, esp+lar+esp+lar, alt)
            pdf.text(x=esp+lar+esp+esp, y=alt+esp-5, txt="ENTREGA")

            pdf.line(esp+lar+esp+lar+esp, alt, esp+lar+esp+lar+esp+lar, alt)
            pdf.text(x=esp+lar+esp+lar+esp+esp, y=alt+esp-5, txt="CHOFER")

            pdf.line(esp+lar+esp+lar+esp+lar+esp, alt, esp+lar+esp+lar+esp+lar+esp+lar, alt)
            pdf.text(x=esp+lar+esp+lar+esp+lar+esp+esp, y=alt+esp-5, txt="RECIBE")
            #Firmas#
            
            #contenido#

            #Metadatos#
            pdf.set_title(title=nombre)
            pdf.set_author(author="DesinGlass Company")
            pdf.set_creator(creator="DesinGlass Smart Windows")
            pdf.set_keywords(keywords=f"Hoja, {nombre}, DesinGlass")
            pdf.set_subject(subject="Comprobante de Movimiento")
            #Metadatos

            pdf.output(str(fileName))
            print('listo')
            #========== CREACION DEL PDF ==========#
        else:
            dialogo = QMessageBox()
            dialogo.setText("Operacion Cancelada")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()

    def PDFEntradas(self, nom):
        #========== CREACION DEL GUARDADOR ==========#
        fecha = self.fechador.FechaLetra() #Fecha de año
        usuario = self.Ruta() #usuario de la PC
        #print(usuario)
        nombre = "Hoja_de_Entradas-" + nom + "-" + fecha[4] #Nombre del archivo por defecto
        Root = "C:" + chr(92)+ "Users"+ chr(92) + usuario + chr(92) + "Desktop" + chr(92) + nombre #Ruta para el buscador
        #Root = "Acceso rápido"
        #print(ruta)
        if usuario != "":
            fileName = QFileDialog.getSaveFileName(filter= "PDF(*.pdf);;Image JPG(*.jpg);;Image PNG (*.png)",directory=Root)[0] #Guardador
        else:
            fileName = QFileDialog.getSaveFileName(filter= "PDF(*.pdf);;Image JPG(*.jpg);;Image PNG (*.png)",directory="C:\\")[0] #Guardador
        #========== CREACION DEL GUARDADOR ==========#
        #fileName = "C:/Users/OFICINA/Desktop/Lista_de_Salida-Folio-2022.pdf"
        if fileName != "":
            #print(fileName)
            Datos = self.LISTA(nom, "Entadas")
            
            Encabezado = Datos[0]
            Contenido = Datos[1]
            Extras = Datos[2]
            #========== CREACION DEL PDF ==========#
            pdf = FPDF(orientation='P', unit='mm', format='A4')
            pdf.add_page()

            pdf.set_font('Arial', '', 12)

            #MEDIDAS DE LAS COLUMNAS Y FILAS#
            Largo = 0
            Alto = 9

            Largo11 = 0
            Alto11 = 8

            Largo21 = 50
            Alto21 = 7

            Alto31 = 6
            Largo31 = 18
            Largo32 = 45
            Largo33 = 20
            Largo34 = 20
            Largo35 = 20
            Largo36 = 20
            Largo37 = 20

            Largo41 = 0
            Alto41 = 5
            #MEDIDAS DE LAS COLUMNAS Y FILAS#

            #contenido#
            #IMAGENES Y MARCAS DE AGUA#
            pdf.image('MarcaDeAgua.png', x=5, y=60, w=200, h=200)
            #pdf.rect(x=30, y= 250, w=40, h=40)
            pdf.image('DGlt ch.png', x=155, y=273, w=45, h=13)
            pdf.image('LogoEmp.png', x=75, y=5, w=65, h=48)
            #IMAGENES Y MARCAS DE AGUA#

            #pdf.set_fill_color(255,255,255)

            #ESPACIOS#
            pdf.cell(w=Largo, h=Alto, txt="", border=0, ln=1, align='C', fill=0)
            pdf.cell(w=Largo, h=Alto, txt="", border=0, ln=2, align='C', fill=0)
            pdf.cell(w=Largo, h=Alto, txt="", border=0, ln=3, align='C', fill=0)
            pdf.cell(w=Largo, h=Alto, txt="", border=0, ln=4, align='C', fill=0)
            #ESPACIOS#

            #TABLA#
            #fila 1#
            pdf.set_font('Arial', 'B', 12)
            TX1 = str("HOJA DE ENTRADAS FOLIO: " + str(nom))
            pdf.set_fill_color(r=142,g=169,b=219)
            pdf.cell(w=Largo11, h=Alto11, txt=TX1, border=1, ln=2, align='C', fill=1)
            #fila 1#

            #fila 2#
            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="OBRA:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[1], border=1, align='C', fill=0)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="FECHA:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[2], border=1, align='C', fill=0)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="SOLICITA:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[3], border=1, align='C', fill=0)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="AUTORIZA:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[4], border=1, align='C', fill=0)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo21, h=Alto21, txt="ALMACEN:", border=1, align='C', fill=0)
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(w=Largo, h=Alto21, txt=Encabezado[5], border=1, align='C', fill=0)
            #fila 2#

            #fila3#
            pdf.set_font('Arial', 'B', 10)
            pdf.cell(w=Largo31, h=Alto31, txt="CLAVE", border=1, align='C', fill=0)
            pdf.cell(w=Largo32, h=Alto31, txt="DESCRIPCION", border=1, align='C', fill=0)
            pdf.cell(w=Largo33, h=Alto31, txt="UNIDAD", border=1, align='C', fill=0)
            pdf.cell(w=Largo34, h=Alto31, txt="CANTIDAD", border=1, align='C', fill=0)
            pdf.cell(w=Largo35, h=Alto31, txt="ANCHO", border=1, align='C', fill=0)
            pdf.cell(w=Largo36, h=Alto31, txt="LARGO", border=1, align='C', fill=0)
            pdf.cell(w=Largo37, h=Alto31, txt="STATUS", border=1, align='C', fill=0)
            pdf.multi_cell(w=Largo, h=Alto31, txt="FOLIO REQ", border=1, align='C', fill=0)
            for i in Contenido:
                #print(i)
                pdf.set_font('Arial', '', 8)
                #=====CLAVE=====
                if len(str(i[0])) > 12:
                    claveCH = str(i[0])
                    claveP = claveCH[0:9] + "..." #11
                    pdf.cell(w=Largo31,h=Alto31, txt=claveP, border=1,align='C',fill=0)
                else:
                    pdf.cell(w=Largo31, h=Alto31, txt=str(i[0]), border=1, align='C', fill=0)
                #=====CLAVE=====

                #=====PRODUCTO=====
                if len(str(i[1])) > 30:
                    ProductoCH = str(i[1])
                    ProductoP = ProductoCH[0:26] + "..." #29
                    pdf.cell(w=Largo32, h=Alto31, txt=ProductoP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo32, h=Alto31, txt=str(i[1]), border=1, align='C', fill=0)
                #=====PRODUCTO=====

                #=====UNIDAD=====
                if len(str(i[2])) > 14:
                    UnidadCH = str(i[2])
                    UnidadP = UnidadCH[0:10] + "..." #13
                    pdf.cell(w=Largo33, h=Alto31, txt=UnidadP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo33, h=Alto31, txt=str(i[2]), border=1, align='C', fill=0)
                #=====UNIDAD=====

                #=====CANTIDAD=====
                if len(str(i[3])) > 10:
                    CantidadCH = str(i[3])
                    CantidadP = CantidadCH[0:7] + "..." #10
                    pdf.cell(w=Largo34, h=Alto31, txt=CantidadP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo34, h=Alto31, txt=str(i[3]), border=1, align='C', fill=0)
                #=====CANTIDAD=====

                #=====ANCHO=====
                if len(str(i[4])) > 15:
                    AnchoCH = str(i[4])
                    AnchoP = AnchoCH[0:12] + "..." #15
                    pdf.cell(w=Largo35, h=Alto31, txt=AnchoP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo35, h=Alto31, txt=str(i[4]), border=1, align='C', fill=0)
                #=====ANCHO=====

                #=====LARGO=====
                if len(str(i[5])) > 15:
                    LargoCH = str(i[5])
                    LargoP = AnchoCH[0:12] + "..." #15
                    pdf.cell(w=Largo36, h=Alto31, txt=LargoP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo36, h=Alto31, txt=str(i[5]), border=1, align='C', fill=0)
                #=====LARGO=====

                #=====STATUS=====
                if len(str(i[6])) >14:
                    StatusCH = str(i[6])
                    StatusP = StatusCH[0:11] + "..." #14
                    pdf.cell(w=Largo37, h=Alto31, txt=StatusP, border=1, align='C', fill=0)
                else:
                    pdf.cell(w=Largo37, h=Alto31, txt=str(i[6]), border=1, align='C', fill=0)
                #=====STATUS=====

                #======FOLIO REQ=====
                if len(str(i[7])) > 16:
                    FolioREQCH = str(i[7])
                    FolioREQP = FolioREQCH[0:13] + "..." #16
                    pdf.multi_cell(w=Largo, h=Alto31, txt=FolioREQP, border=1, align='C', fill=0)
                else:
                    pdf.multi_cell(w=Largo, h=Alto31, txt=str(i[7]), border=1, align='C', fill=0)
                #=====FOLIO REQ=====
            #fila3#
            #TABLA#

            #Observaciones#
            pdf.ln(5) 
            obs = "OBSERVACIONES: \n" + str(Extras[2]) 
            pdf.multi_cell(w=Largo, h=Alto41, txt=obs, border=1, align='L', fill=0)
            #Observaciones#

            #Firmas#
            alt = 262
            esp = 10
            lar = 40
            pdf.set_font('Arial', '', 12)
            pdf.ln(5)
            pdf.line(esp, alt, esp+lar, alt)
            pdf.text(x=esp+esp, y=alt+esp-5, txt="ALMACEN")

            pdf.line(esp+lar+esp, alt, esp+lar+esp+lar, alt)
            pdf.text(x=esp+lar+esp+esp, y=alt+esp-5, txt="ENTREGA")

            pdf.line(esp+lar+esp+lar+esp, alt, esp+lar+esp+lar+esp+lar, alt)
            pdf.text(x=esp+lar+esp+lar+esp+esp, y=alt+esp-5, txt="CHOFER")

            pdf.line(esp+lar+esp+lar+esp+lar+esp, alt, esp+lar+esp+lar+esp+lar+esp+lar, alt)
            pdf.text(x=esp+lar+esp+lar+esp+lar+esp+esp, y=alt+esp-5, txt="RECIBE")
            #Firmas#
            
            #contenido#

            #Metadatos#
            pdf.set_title(title=nombre)
            pdf.set_author(author="DesinGlass Company")
            pdf.set_creator(creator="DesinGlass Smart Windows")
            pdf.set_keywords(keywords=f"Hoja, {nombre}, DesinGlass")
            pdf.set_subject(subject="Comprobante de Movimiento")
            #Metadatos

            pdf.output(str(fileName))
            print('listo')
            #========== CREACION DEL PDF ==========#
        else:
            dialogo = QMessageBox()
            dialogo.setText("Operacion Cancelada")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()

class PDFINV(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 18)
        self.text(x=64, y=20, txt="INVENTARIO DESINGLASS")
        self.ln(15)
        self.image('MarcaDeAgua.png', x=5, y=60, w=200, h=200)
    def footer(self):
        self.image('DGlt ch.png', x=160, y=273, w=40, h=11)
class HojaInventario(QMainWindow):
    def __init__(self):
        super(HojaInventario,self).__init__()
        self.Productos = Pagina1()

    def LISTA(self):
        Buscar = self.Productos.ConsultarProductos()

        if Buscar == []:
            dialogo = QMessageBox()
            dialogo.setText("No Existe El Folio en la Base de Datos")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()
        else:
            #Buscar = Buscar[0]
            return Buscar

    def Ruta(self):
        #========== BUSCAR NOMBRE DE USUARIO DE LA COMPUTADORA  ==========#
        ruta = "C:" + chr(92)+ "Users"+ chr(92)  #especificamos la ruta inicial en: "C:\Users\"
        carpetas = os.listdir(ruta) #revizamos cuantos directorios hay en la ruta
        #carpetas = ['User', 'User', 'User', 'User', 'User', 'User','user']
        #print(carpetas)
        usuario = "" #preparamos la variable que almacenara el nombre de usuario
        if len(carpetas) == 6:
            for i in carpetas: #revisamos cada elemento de la lista para encontrar el nombre de usuario
                if str(i) != 'All Users':
                    #print('Fallo')
                    pass
                    if str(i) != 'Default':
                        #print('Fallo')
                        pass
                        if str(i) != 'Default User':
                            #print('Fallo')
                            pass
                            if str(i) != 'desktop.ini':
                                #print('Fallo')
                                pass
                                if str(i) == 'Public':
                                    #print('Fallo')
                                    pass
                                else: #Aqui nos arroja el unico elemento que es el nombre de usuario de la maquina
                                    usuario = str(i)
                                    #print(i,conta)
            #print(usuario)
        else:
            usuario = ""
        return usuario

    def PDFInventario(self):
        #========== CREACION DEL GUARDADOR ==========#
        fecha = self.Productos.FechaLetra() #Fecha de año
        usuario = self.Ruta() #usuario de la PC
        #print(usuario)
        nombre = "Hoja_de_Inventario-" + fecha[3] + "-" + fecha[4] #Nombre del archivo por defecto
        Root = "C:" + chr(92)+ "Users"+ chr(92) + usuario + chr(92) + "Desktop" + chr(92) + nombre #Ruta para el buscador
        #Root = "Acceso rápido"
        #print(ruta)
        if usuario != "":
            fileName = QFileDialog.getSaveFileName(filter= "PDF(*.pdf);;Image JPG(*.jpg);;Image PNG (*.png)",directory=Root)[0] #Guardador
        else:
            fileName = QFileDialog.getSaveFileName(filter= "PDF(*.pdf);;Image JPG(*.jpg);;Image PNG (*.png)",directory="C:\\")[0] #Guardador
        #========== CREACION DEL GUARDADOR ==========#
        #fileName = "C:/Users/OFICINA/Desktop/Hoja_de_Inventario-Diciembre-2022.pdf"
        if fileName != "":
            #print(fileName)
            Datos = self.LISTA()
            
           
            #========== CREACION DEL PDF ==========#
            pdf = PDFINV(orientation='P', unit='mm', format='A4')
            pdf.add_page()

            pdf.set_font('Arial', '', 12)

            #MEDIDAS DE LAS COLUMNAS Y FILAS#
            Alto11 = 6
            Largo = 0
            Largo11 = 18
            Largo12 = 45
            Largo13 = 20
            Largo14 = 22
            #MEDIDAS DE LAS COLUMNAS Y FILAS#

            #contenido#
            pdf.set_font('Arial', 'B', 12)
            #TABLA#
            #fila 1#
            pdf.set_font('Arial', 'B', 10)
            pdf.set_text_color(r=255,g=255,b=255)
            pdf.set_fill_color(r=0,g=0,b=0)
            pdf.cell(w=Largo11, h=Alto11, txt="CLAVE", border=1, align='C', fill=1)
            pdf.cell(w=Largo12, h=Alto11, txt="PRODUCTO", border=1, align='C', fill=1)
            pdf.cell(w=Largo13, h=Alto11, txt="ACTUAL", border=1, align='C', fill=1)
            pdf.cell(w=Largo14, h=Alto11, txt="EXISTENTE", border=1, align='C', fill=1)
            pdf.multi_cell(w=Largo, h=Alto11, txt="OBSERVACIONES", border=1, align='C', fill=1)
            
            e = "si"
            pdf.set_text_color(r=0,g=0,b=0)
            for i in Datos:
                #print(i)
                if e == "no":
                    #print(e)
                    pdf.set_font('Arial', '', 8)
                    pdf.set_text_color(r=0,g=0,b=0)
                    pdf.cell(w=Largo11, h=Alto11, txt=str(i[2]), border=1, align='C', fill=0)
                    pdf.cell(w=Largo12, h=Alto11, txt=str(i[1]), border=1, align='C', fill=0)
                    pdf.cell(w=Largo13, h=Alto11, txt=str(i[7]), border=1, align='C', fill=0)
                    pdf.cell(w=Largo14, h=Alto11, txt="", border=1, align='C', fill=0)
                    pdf.multi_cell(w=Largo, h=Alto11, txt="", border=1, align='C', fill=0)
                    e = "si"
                else:
                    #print(e)
                    pdf.set_fill_color(r=222,g=222,b=222)
                    pdf.set_font('Arial', '', 8)
                    pdf.cell(w=Largo11, h=Alto11, txt=str(i[2]), border=1, align='C', fill=1)
                    pdf.cell(w=Largo12, h=Alto11, txt=str(i[1]), border=1, align='C', fill=1)
                    pdf.cell(w=Largo13, h=Alto11, txt=str(i[7]), border=1, align='C', fill=1)
                    pdf.cell(w=Largo14, h=Alto11, txt="", border=1, align='C', fill=1)
                    pdf.multi_cell(w=Largo, h=Alto11, txt="", border=1, align='C', fill=1)
                    e = "no"
            #contenido#

            #Metadatos#
            pdf.set_title(title=nombre)
            pdf.set_author(author="DesinGlass Company")
            pdf.set_creator(creator="DesinGlass Smart Windows")
            pdf.set_keywords(keywords=f"Hoja, {nombre}, DesinGlass")
            pdf.set_subject(subject="Hoja de Inventario")
            #Metadatos

            pdf.output(str(fileName))
            print('listo')
            #========== CREACION DEL PDF ==========#
        else:
            dialogo = QMessageBox()
            dialogo.setText("Operacion Cancelada")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()

class PDFREP(FPDF):
    def header(self):
        self.Productos = Pagina1()
        fecha = self.Productos.FechaLetra() #Fecha de año
        fch = fecha[0]

        self.set_font('Arial', 'B', 18)
        self.text(x=110, y=20, txt="REPORTE DESINGLASS")
        self.set_font('Arial', '', 13)
        self.text(x=260, y=20, txt=fch[0:10])
        self.ln(15)
        self.image('MarcaEmpresarial.png', x=10, y=20, w=275, h=180)
    def footer(self):
        self.image('DGlt ch.png', x=250, y=190, w=40, h=11)
class HojaReporte(QMainWindow):
    def __init__(self):
        super(HojaReporte,self).__init__()
        self.Productos = Pagina1()

    def Ruta(self):
        #========== BUSCAR NOMBRE DE USUARIO DE LA COMPUTADORA  ==========#
        ruta = "C:" + chr(92)+ "Users"+ chr(92)  #especificamos la ruta inicial en: "C:\Users\"
        carpetas = os.listdir(ruta) #revizamos cuantos directorios hay en la ruta
        #carpetas = ['User', 'User', 'User', 'User', 'User', 'User','user']
        #print(carpetas)
        usuario = "" #preparamos la variable que almacenara el nombre de usuario
        if len(carpetas) == 6:
            for i in carpetas: #revisamos cada elemento de la lista para encontrar el nombre de usuario
                if str(i) != 'All Users':
                    #print('Fallo')
                    pass
                    if str(i) != 'Default':
                        #print('Fallo')
                        pass
                        if str(i) != 'Default User':
                            #print('Fallo')
                            pass
                            if str(i) != 'desktop.ini':
                                #print('Fallo')
                                pass
                                if str(i) == 'Public':
                                    #print('Fallo')
                                    pass
                                else: #Aqui nos arroja el unico elemento que es el nombre de usuario de la maquina
                                    usuario = str(i)
                                    #print(i,conta)
            #print(usuario)
        else:
            usuario = ""
        return usuario

    def PDFReporte(self, Fecha1, Fecha2, Lista):
        #========== CREACION DEL GUARDADOR ==========#
        fecha = self.Productos.FechaLetra() #Fecha de año
        usuario = self.Ruta() #usuario de la PC
        #print(usuario)
        nombre = "REPORTE_" + str(Fecha1) + "_" + str(Fecha2) #Nombre del archivo por defecto
        Root = "C:" + chr(92)+ "Users"+ chr(92) + usuario + chr(92) + "Desktop" + chr(92) + nombre #Ruta para el buscador
        #Root = "Acceso rápido"
        #print(ruta)
        if usuario != "":
            fileName = QFileDialog.getSaveFileName(filter= "PDF(*.pdf);;Image JPG(*.jpg);;Image PNG (*.png)",directory=Root)[0] #Guardador
        else:
            fileName = QFileDialog.getSaveFileName(filter= "PDF(*.pdf);;Image JPG(*.jpg);;Image PNG (*.png)",directory="C:\\")[0] #Guardador
        #========== CREACION DEL GUARDADOR ==========#
        #fileName = "C:/Users/OFICINA/Desktop/REPORTE_2022-12-07_2022-12-07.pdf"
        if fileName != "":
            #print(fileName)
            Datos = Lista
            
           
            #========== CREACION DEL PDF ==========#
            pdf = PDFREP(orientation='L', unit='mm', format='A4')
            pdf.add_page()

            pdf.set_font('Arial', '', 12)

            #MEDIDAS DE LAS COLUMNAS Y FILAS#
            Alto11 = 6
            Largo = 0
            Largo11 = 18
            Largo12 = 45
            Largo13 = 20
            Largo14 = 20
            Largo15 = 22
            Largo16 = 22
            Largo17 = 22
            Largo18 = 22
            Largo19 = 24
            Largo20 = 22
            #MEDIDAS DE LAS COLUMNAS Y FILAS#

            #contenido#
            pdf.set_font('Arial', 'B', 12)
            #TABLA#
            #fila 1#
            pdf.set_font('Arial', 'B', 10)
            pdf.set_text_color(r=255,g=255,b=255)
            pdf.set_fill_color(r=0,g=32,b=96)
            pdf.cell(w=Largo11, h=Alto11, txt="TP MOV.", border=1, align='C', fill=1)
            pdf.cell(w=Largo12, h=Alto11, txt="NOMBRE DEL PRODUCTO", border=1, align='C', fill=1)
            pdf.cell(w=Largo13, h=Alto11, txt="CLAVE", border=1, align='C', fill=1)
            pdf.cell(w=Largo14, h=Alto11, txt="NUMERO", border=1, align='C', fill=1)
            pdf.cell(w=Largo15, h=Alto11, txt="MARCA", border=1, align='C', fill=1)
            pdf.cell(w=Largo16, h=Alto11, txt="COLOR", border=1, align='C', fill=1)
            pdf.cell(w=Largo17, h=Alto11, txt="UNIDAD", border=1, align='C', fill=1)
            pdf.cell(w=Largo18, h=Alto11, txt="CANTIDAD", border=1, align='C', fill=1)
            pdf.cell(w=Largo19, h=Alto11, txt="PROVEEDOR", border=1, align='C', fill=1)
            pdf.cell(w=Largo20, h=Alto11, txt="LUGAR", border=1, align='C', fill=1)
            pdf.multi_cell(w=Largo, h=Alto11, txt="FECHA", border=1, align='C', fill=1)
            
            e = "si"
            pdf.set_text_color(r=0,g=0,b=0)
            #print(Datos)
            for i in Datos:
                #print(i)
                if e == "no":
                    #print(e)
                    pdf.set_font('Arial', '', 8)
                    pdf.set_text_color(r=0,g=0,b=0)
                    pdf.cell(w=Largo11, h=Alto11, txt=str(i[0]), border=1, align='C', fill=0)
                    pdf.cell(w=Largo12, h=Alto11, txt=str(i[1]), border=1, align='C', fill=0)
                    pdf.cell(w=Largo13, h=Alto11, txt=str(i[2]), border=1, align='C', fill=0)
                    pdf.cell(w=Largo14, h=Alto11, txt=str(i[3]), border=1, align='C', fill=0)
                    pdf.cell(w=Largo15, h=Alto11, txt=str(i[4]), border=1, align='C', fill=0)
                    pdf.cell(w=Largo16, h=Alto11, txt=str(i[5]), border=1, align='C', fill=0)
                    pdf.cell(w=Largo17, h=Alto11, txt=str(i[6]), border=1, align='C', fill=0)
                    pdf.cell(w=Largo18, h=Alto11, txt=str(i[7]), border=1, align='C', fill=0)
                    pdf.cell(w=Largo19, h=Alto11, txt=str(i[8]), border=1, align='C', fill=0)
                    pdf.cell(w=Largo20, h=Alto11, txt=str(i[9]), border=1, align='C', fill=0)
                    pdf.multi_cell(w=Largo, h=Alto11, txt=str(i[10]), border=1, align='C', fill=0)
                    e = "si"
                else:
                    #print(e)
                    pdf.set_fill_color(r=221,g=235,b=247)
                    pdf.set_font('Arial', '', 8)
                    pdf.cell(w=Largo11, h=Alto11, txt=str(i[0]), border=1, align='C', fill=1)
                    pdf.cell(w=Largo12, h=Alto11, txt=str(i[1]), border=1, align='C', fill=1)
                    pdf.cell(w=Largo13, h=Alto11, txt=str(i[2]), border=1, align='C', fill=1)
                    pdf.cell(w=Largo14, h=Alto11, txt=str(i[3]), border=1, align='C', fill=1)
                    pdf.cell(w=Largo15, h=Alto11, txt=str(i[4]), border=1, align='C', fill=1)
                    pdf.cell(w=Largo16, h=Alto11, txt=str(i[5]), border=1, align='C', fill=1)
                    pdf.cell(w=Largo17, h=Alto11, txt=str(i[6]), border=1, align='C', fill=1)
                    pdf.cell(w=Largo18, h=Alto11, txt=str(i[7]), border=1, align='C', fill=1)
                    pdf.cell(w=Largo19, h=Alto11, txt=str(i[8]), border=1, align='C', fill=1)
                    pdf.cell(w=Largo20, h=Alto11, txt=str(i[9]), border=1, align='C', fill=1)
                    pdf.multi_cell(w=Largo, h=Alto11, txt=str(i[10]), border=1, align='C', fill=1)
                    e = "no" 
            #contenido#

            #Metadatos#
            pdf.set_title(title=nombre)
            pdf.set_author(author="DesinGlass Company")
            pdf.set_creator(creator="DesinGlass Smart Windows")
            pdf.set_keywords(keywords=f"Hoja, {nombre}, DesinGlass")
            pdf.set_subject(subject="Reporte DesinGlass")
            #Metadatos

            pdf.output(str(fileName))
            print('listo')
            #========== CREACION DEL PDF ==========#
        else:
            dialogo = QMessageBox()
            dialogo.setText("Operacion Cancelada")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Critical)
            dialogo.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = CrearPDF()
    #myApp = arranque()
    myApp.show()
    #myApp.PDFListas('Folio') #SE BORRAN
    myapp = HojaInventario()
    #myapp.PDFInventario('Folio') #SE BORRAN
    myyApp = HojaReporte()
    #myyApp.PDFReporte("2022/12/07", "2022/12/07", 'Lista') #SE BORRAN
    sys.exit(app.exec_())