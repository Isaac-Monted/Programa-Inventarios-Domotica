import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5 import QtCore, QtWidgets, uic 
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator
import sqlite3

class Pagina4():
    def __init__(self):
        #Conectar a la base de datos#
        self.conn = sqlite3.connect("PrgogramaInventarios.db")

    def __str__(self):
        Datos = self.ConsultarEntradas()
        Aux = ""

        for row in Datos:
            Aux = Aux + str(row) + "\n"
        return Aux

    def ConsultarEntradas(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM RegistroEntradas")

        Dato = c.fetchall()
        #c.close()
        return Dato
    
    def ConsultarEntradasR(self, filtro):
        c = self.conn.cursor()
        consulta = f"SELECT * FROM RegistroEntradas ORDER BY {filtro} DESC"
        c.execute(consulta)

        Dato = c.fetchall()
        #c.close()
        return Dato

    def BuscarEntradas(self, Clave):
        c = self.conn.cursor()
        buscar = "SELECT * FROM RegistroEntradas WHERE Folio= '{}'".format(Clave)
        c.execute(buscar)

        Dato = c.fetchall()
        c.close()
        return Dato

    def BuscarEntradasN(self, Clave):
        c = self.conn.cursor()
        buscar = "SELECT * FROM RegistroEntradas WHERE Obra= '{}'".format(Clave)
        c.execute(buscar)

        Dato = c.fetchall()
        c.close()
        return Dato

    def AgregarEntradas(self,Folio , Obra, Fecha, Solicita, Autoriza, Almacen, Referencia, Descripcion, Unidad, Cantidad, Ancho, Largo, Lugar, FolioReq, Referencia2, Descripcion2, Unidad2, Cantidad2, Ancho2, Largo2, Lugar2, FolioReq2, Referencia3, Descripcion3, Unidad3, Cantidad3, Ancho3, Largo3, Lugar3, FolioReq3, Referencia4, Descripcion4, Unidad4, Cantidad4, Ancho4, Largo4, Lugar4, FolioReq4, Referencia5, Descripcion5, Unidad5, Cantidad5, Ancho5, Largo5, Lugar5, FolioReq5, Referencia6, Descripcion6, Unidad6, Cantidad6, Ancho6, Largo6, Lugar6, FolioReq6, Referencia7, Descripcion7, Unidad7, Cantidad7, Ancho7, Largo7, Lugar7, FolioReq7, Referencia8, Descripcion8, Unidad8, Cantidad8, Ancho8, Largo8, Lugar8, FolioReq8, Referencia9, Descripcion9, Unidad9, Cantidad9, Ancho9, Largo9, Lugar9, FolioReq9, Referencia10, Descripcion10, Unidad10, Cantidad10, Ancho10, Largo10, Lugar10, FolioReq10, Referencia11, Descripcion11, Unidad11, Cantidad11, Ancho11, Largo11, Lugar11, FolioReq11, Referencia12, Descripcion12, Unidad12, Cantidad12, Ancho12, Largo12, Lugar12, FolioReq12, Referencia13, Descripcion13, Unidad13, Cantidad13, Ancho13, Largo13, Lugar13, FolioReq13, Referencia14, Descripcion14, Unidad14, Cantidad14, Ancho14, Largo14, Lugar14, FolioReq14, Referencia15, Descripcion15, Unidad15, Cantidad15, Ancho15, Largo15, Lugar15, FolioReq15, Referencia16, Descripcion16, Unidad16, Cantidad16, Ancho16, Largo16, Lugar16, FolioReq16, Referencia17, Descripcion17, Unidad17, Cantidad17, Ancho17, Largo17, Lugar17, FolioReq17, Referencia18, Descripcion18, Unidad18, Cantidad18, Ancho18, Largo18, Lugar18, FolioReq18, Referencia19, Descripcion19, Unidad19, Cantidad19, Ancho19, Largo19, Lugar19, FolioReq19, Referencia20, Descripcion20, Unidad20, Cantidad20, Ancho20, Largo20, Lugar20, FolioReq20, OrdenComp, FolFactura, Comentario):
        c = self.conn.cursor()
        Agregar = "INSERT INTO RegistroEntradas (ID, Folio , Obra, Fecha, Solicita, Autoriza, Almacen, Referencia, Descripcion, Unidad, Cantidad, Ancho, Largo, Lugar, FolioReq, Referencia2, Descripcion2, Unidad2, Cantidad2, Ancho2, Largo2, Lugar2, FolioReq2, Referencia3, Descripcion3, Unidad3, Cantidad3, Ancho3, Largo3, Lugar3, FolioReq3, Referencia4, Descripcion4, Unidad4, Cantidad4, Ancho4, Largo4, Lugar4, FolioReq4, Referencia5, Descripcion5, Unidad5, Cantidad5, Ancho5, Largo5, Lugar5, FolioReq5, Referencia6, Descripcion6, Unidad6, Cantidad6, Ancho6, Largo6, Lugar6, FolioReq6, Referencia7, Descripcion7, Unidad7, Cantidad7, Ancho7, Largo7, Lugar7, FolioReq7, Referencia8, Descripcion8, Unidad8, Cantidad8, Ancho8, Largo8, Lugar8, FolioReq8, Referencia9, Descripcion9, Unidad9, Cantidad9, Ancho9, Largo9, Lugar9, FolioReq9, Referencia10, Descripcion10, Unidad10, Cantidad10, Ancho10, Largo10, Lugar10, FolioReq10, Referencia11, Descripcion11, Unidad11, Cantidad11, Ancho11, Largo11, Lugar11, FolioReq11, Referencia12, Descripcion12, Unidad12, Cantidad12, Ancho12, Largo12, Lugar12, FolioReq12, Referencia13, Descripcion13, Unidad13, Cantidad13, Ancho13, Largo13, Lugar13, FolioReq13, Referencia14, Descripcion14, Unidad14, Cantidad14, Ancho14, Largo14, Lugar14, FolioReq14, Referencia15, Descripcion15, Unidad15, Cantidad15, Ancho15, Largo15, Lugar15, FolioReq15, Referencia16, Descripcion16, Unidad16, Cantidad16, Ancho16, Largo16, Lugar16, FolioReq16, Referencia17, Descripcion17, Unidad17, Cantidad17, Ancho17, Largo17, Lugar17, FolioReq17, Referencia18, Descripcion18, Unidad18, Cantidad18, Ancho18, Largo18, Lugar18, FolioReq18, Referencia19, Descripcion19, Unidad19, Cantidad19, Ancho19, Largo19, Lugar19, FolioReq19, Referencia20, Descripcion20, Unidad20, Cantidad20, Ancho20, Largo20, Lugar20, FolioReq20, OrdenComp, FolFactura, Comentario) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(Folio , Obra, Fecha, Solicita, Autoriza, Almacen, Referencia, Descripcion, Unidad, Cantidad, Ancho, Largo, Lugar, FolioReq, Referencia2, Descripcion2, Unidad2, Cantidad2, Ancho2, Largo2, Lugar2, FolioReq2, Referencia3, Descripcion3, Unidad3, Cantidad3, Ancho3, Largo3, Lugar3, FolioReq3, Referencia4, Descripcion4, Unidad4, Cantidad4, Ancho4, Largo4, Lugar4, FolioReq4, Referencia5, Descripcion5, Unidad5, Cantidad5, Ancho5, Largo5, Lugar5, FolioReq5, Referencia6, Descripcion6, Unidad6, Cantidad6, Ancho6, Largo6, Lugar6, FolioReq6, Referencia7, Descripcion7, Unidad7, Cantidad7, Ancho7, Largo7, Lugar7, FolioReq7, Referencia8, Descripcion8, Unidad8, Cantidad8, Ancho8, Largo8, Lugar8, FolioReq8, Referencia9, Descripcion9, Unidad9, Cantidad9, Ancho9, Largo9, Lugar9, FolioReq9, Referencia10, Descripcion10, Unidad10, Cantidad10, Ancho10, Largo10, Lugar10, FolioReq10, Referencia11, Descripcion11, Unidad11, Cantidad11, Ancho11, Largo11, Lugar11, FolioReq11, Referencia12, Descripcion12, Unidad12, Cantidad12, Ancho12, Largo12, Lugar12, FolioReq12, Referencia13, Descripcion13, Unidad13, Cantidad13, Ancho13, Largo13, Lugar13, FolioReq13, Referencia14, Descripcion14, Unidad14, Cantidad14, Ancho14, Largo14, Lugar14, FolioReq14, Referencia15, Descripcion15, Unidad15, Cantidad15, Ancho15, Largo15, Lugar15, FolioReq15, Referencia16, Descripcion16, Unidad16, Cantidad16, Ancho16, Largo16, Lugar16, FolioReq16, Referencia17, Descripcion17, Unidad17, Cantidad17, Ancho17, Largo17, Lugar17, FolioReq17, Referencia18, Descripcion18, Unidad18, Cantidad18, Ancho18, Largo18, Lugar18, FolioReq18, Referencia19, Descripcion19, Unidad19, Cantidad19, Ancho19, Largo19, Lugar19, FolioReq19, Referencia20, Descripcion20, Unidad20, Cantidad20, Ancho20, Largo20, Lugar20, FolioReq20, OrdenComp, FolFactura, Comentario)
        c.execute(Agregar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def AgregarEntradasL(self,Lista):
        c = self.conn.cursor()
        Agregar = "INSERT INTO RegistroEntradas VALUES(NULL,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        c.execute(Agregar, Lista)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def EliminarEntradas(self, Clave):
        c = self.conn.cursor()
        Elimiar = "DELETE FROM RegistroEntradas WHERE Folio='{}'".format(Clave)
        c.execute(Elimiar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def ActualizarEntradas(self, ID, Folio , Obra, Fecha, Solicita, Autoriza, Almacen, Referencia, Descripcion, Unidad, Cantidad, Ancho, Largo, Lugar, FolioReq, Referencia2, Descripcion2, Unidad2, Cantidad2, Ancho2, Largo2, Lugar2, FolioReq2, Referencia3, Descripcion3, Unidad3, Cantidad3, Ancho3, Largo3, Lugar3, FolioReq3, Referencia4, Descripcion4, Unidad4, Cantidad4, Ancho4, Largo4, Lugar4, FolioReq4, Referencia5, Descripcion5, Unidad5, Cantidad5, Ancho5, Largo5, Lugar5, FolioReq5, Referencia6, Descripcion6, Unidad6, Cantidad6, Ancho6, Largo6, Lugar6, FolioReq6, Referencia7, Descripcion7, Unidad7, Cantidad7, Ancho7, Largo7, Lugar7, FolioReq7, Referencia8, Descripcion8, Unidad8, Cantidad8, Ancho8, Largo8, Lugar8, FolioReq8, Referencia9, Descripcion9, Unidad9, Cantidad9, Ancho9, Largo9, Lugar9, FolioReq9, Referencia10, Descripcion10, Unidad10, Cantidad10, Ancho10, Largo10, Lugar10, FolioReq10, Referencia11, Descripcion11, Unidad11, Cantidad11, Ancho11, Largo11, Lugar11, FolioReq11, Referencia12, Descripcion12, Unidad12, Cantidad12, Ancho12, Largo12, Lugar12, FolioReq12, Referencia13, Descripcion13, Unidad13, Cantidad13, Ancho13, Largo13, Lugar13, FolioReq13, Referencia14, Descripcion14, Unidad14, Cantidad14, Ancho14, Largo14, Lugar14, FolioReq14, Referencia15, Descripcion15, Unidad15, Cantidad15, Ancho15, Largo15, Lugar15, FolioReq15, Referencia16, Descripcion16, Unidad16, Cantidad16, Ancho16, Largo16, Lugar16, FolioReq16, Referencia17, Descripcion17, Unidad17, Cantidad17, Ancho17, Largo17, Lugar17, FolioReq17, Referencia18, Descripcion18, Unidad18, Cantidad18, Ancho18, Largo18, Lugar18, FolioReq18, Referencia19, Descripcion19, Unidad19, Cantidad19, Ancho19, Largo19, Lugar19, FolioReq19, Referencia20, Descripcion20, Unidad20, Cantidad20, Ancho20, Largo20, Lugar20, FolioReq20, OrdenComp, FolFactura, Comentario):
        c = self.conn.cursor()
        Actualizar = "UPDATE RegistroEntradas SET Folio='{}', Obra='{}', Fecha='{}', Solicita='{}', Autoriza='{}', Almacen='{}', Referencia='{}', Descripcion='{}', Unidad='{}', Cantidad={}, Ancho='{}', Largo='{}', Lugar='{}', FolioReq='{}', Referencia2='{}', Descripcion2='{}', Unidad2='{}', Cantidad2={}, Ancho2='{}', Largo2='{}', Lugar2='{}', FolioReq2='{}', Referencia3='{}', Descripcion3='{}', Unidad3='{}', Cantidad3={}, Ancho3='{}', Largo3='{}', Lugar3='{}', FolioReq3='{}', Referencia4='{}', Descripcion4='{}', Unidad4='{}', Cantidad4={}, Ancho4='{}', Largo4='{}', Lugar4='{}', FolioReq4='{}', Referencia5='{}', Descripcion5='{}', Unidad5='{}', Cantidad5={}, Ancho5='{}', Largo5='{}', Lugar5='{}', FolioReq5='{}', Referencia6='{}', Descripcion6='{}', Unidad6='{}', Cantidad6={}, Ancho6='{}', Largo6='{}', Lugar6='{}', FolioReq6='{}', Referencia7='{}', Descripcion7='{}', Unidad7='{}', Cantidad7={}, Ancho7='{}', Largo7='{}', Lugar7='{}', FolioReq7='{}', Referencia8='{}', Descripcion8='{}', Unidad8='{}', Cantidad8={}, Ancho8='{}', Largo8='{}', Lugar8='{}', FolioReq8='{}', Referencia9='{}', Descripcion9='{}', Unidad9='{}', Cantidad9={}, Ancho9='{}', Largo9='{}', Lugar9='{}', FolioReq9='{}', Referencia10='{}', Descripcion10='{}', Unidad10='{}', Cantidad10={}, Ancho10='{}', Largo10='{}', Lugar10='{}', FolioReq10='{}', Referencia11='{}', Descripcion11='{}', Unidad11='{}', Cantidad11={}, Ancho11='{}', Largo11='{}', Lugar11='{}', FolioReq11='{}', Referencia12='{}', Descripcion12='{}', Unidad12='{}', Cantidad12={}, Ancho12='{}', Largo12='{}', Lugar12='{}', FolioReq12='{}', Referencia13='{}', Descripcion13='{}', Unidad13='{}', Cantidad13={}, Ancho13='{}', Largo13='{}', Lugar13='{}', FolioReq13='{}', Referencia14='{}', Descripcion14='{}', Unidad14='{}', Cantidad14={}, Ancho14='{}', Largo14='{}', Lugar14='{}', FolioReq14='{}', Referencia15='{}', Descripcion15='{}', Unidad15='{}', Cantidad15={}, Ancho15='{}', Largo15='{}', Lugar15='{}', FolioReq15='{}', Referencia16='{}', Descripcion16='{}', Unidad16='{}', Cantidad16={}, Ancho16='{}', Largo16='{}', Lugar16='{}', FolioReq16='{}', Referencia17='{}', Descripcion17='{}', Unidad17='{}', Cantidad17={}, Ancho17='{}', Largo17='{}', Lugar17='{}', FolioReq17='{}', Referencia18='{}', Descripcion18='{}', Unidad18='{}', Cantidad18={}, Ancho18='{}', Largo18='{}', Lugar18='{}', FolioReq18='{}', Referencia19='{}', Descripcion19='{}', Unidad19='{}', Cantidad19={}, Ancho19='{}', Largo19='{}', Lugar19='{}', FolioReq19='{}', Referencia20='{}', Descripcion20='{}', Unidad20='{}', Cantidad20={}, Ancho20='{}', Largo20='{}', Lugar20='{}', FolioReq20='{}', OrdenComp='{}', FolFactura='{}', Comentario='{}' WHERE ID={}".format(Folio , Obra, Fecha, Solicita, Autoriza, Almacen, Referencia, Descripcion, Unidad, Cantidad, Ancho, Largo, Lugar, FolioReq, Referencia2, Descripcion2, Unidad2, Cantidad2, Ancho2, Largo2, Lugar2, FolioReq2, Referencia3, Descripcion3, Unidad3, Cantidad3, Ancho3, Largo3, Lugar3, FolioReq3, Referencia4, Descripcion4, Unidad4, Cantidad4, Ancho4, Largo4, Lugar4, FolioReq4, Referencia5, Descripcion5, Unidad5, Cantidad5, Ancho5, Largo5, Lugar5, FolioReq5, Referencia6, Descripcion6, Unidad6, Cantidad6, Ancho6, Largo6, Lugar6, FolioReq6, Referencia7, Descripcion7, Unidad7, Cantidad7, Ancho7, Largo7, Lugar7, FolioReq7, Referencia8, Descripcion8, Unidad8, Cantidad8, Ancho8, Largo8, Lugar8, FolioReq8, Referencia9, Descripcion9, Unidad9, Cantidad9, Ancho9, Largo9, Lugar9, FolioReq9, Referencia10, Descripcion10, Unidad10, Cantidad10, Ancho10, Largo10, Lugar10, FolioReq10, Referencia11, Descripcion11, Unidad11, Cantidad11, Ancho11, Largo11, Lugar11, FolioReq11, Referencia12, Descripcion12, Unidad12, Cantidad12, Ancho12, Largo12, Lugar12, FolioReq12, Referencia13, Descripcion13, Unidad13, Cantidad13, Ancho13, Largo13, Lugar13, FolioReq13, Referencia14, Descripcion14, Unidad14, Cantidad14, Ancho14, Largo14, Lugar14, FolioReq14, Referencia15, Descripcion15, Unidad15, Cantidad15, Ancho15, Largo15, Lugar15, FolioReq15, Referencia16, Descripcion16, Unidad16, Cantidad16, Ancho16, Largo16, Lugar16, FolioReq16, Referencia17, Descripcion17, Unidad17, Cantidad17, Ancho17, Largo17, Lugar17, FolioReq17, Referencia18, Descripcion18, Unidad18, Cantidad18, Ancho18, Largo18, Lugar18, FolioReq18, Referencia19, Descripcion19, Unidad19, Cantidad19, Ancho19, Largo19, Lugar19, FolioReq19, Referencia20, Descripcion20, Unidad20, Cantidad20, Ancho20, Largo20, Lugar20, FolioReq20, OrdenComp, FolFactura, Comentario, ID)
        c.execute(Actualizar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def ActualizarEntradasL(self, ID, Lista):
        c = self.conn.cursor()
        Actualizar = "UPDATE RegistroEntradas SET Folio=?, Obra=?, Fecha=?, Solicita=?, Autoriza=?, Almacen=?, Referencia=?, Descripcion=?, Unidad=?, Cantidad=?, Ancho=?, Largo=?, Lugar=?, FolioReq=?, Referencia2=?, Descripcion2=?, Unidad2=?, Cantidad2=?, Ancho2=?, Largo2=?, Lugar2=?, FolioReq2=?, Referencia3=?, Descripcion3=?, Unidad3=?, Cantidad3=?, Ancho3=?, Largo3=?, Lugar3=?, FolioReq3=?, Referencia4=?, Descripcion4=?, Unidad4=?, Cantidad4=?, Ancho4=?, Largo4=?, Lugar4=?, FolioReq4=?, Referencia5=?, Descripcion5=?, Unidad5=?, Cantidad5=?, Ancho5=?, Largo5=?, Lugar5=?, FolioReq5=?, Referencia6=?, Descripcion6=?, Unidad6=?, Cantidad6=?, Ancho6=?, Largo6=?, Lugar6=?, FolioReq6=?, Referencia7=?, Descripcion7=?, Unidad7=?, Cantidad7=?, Ancho7=?, Largo7=?, Lugar7=?, FolioReq7=?, Referencia8=?, Descripcion8=?, Unidad8=?, Cantidad8=?, Ancho8=?, Largo8=?, Lugar8=?, FolioReq8=?, Referencia9=?, Descripcion9=?, Unidad9=?, Cantidad9=?, Ancho9=?, Largo9=?, Lugar9=?, FolioReq9=?, Referencia10=?, Descripcion10=?, Unidad10=?, Cantidad10=?, Ancho10=?, Largo10=?, Lugar10=?, FolioReq10=?, Referencia11=?, Descripcion11=?, Unidad11=?, Cantidad11=?, Ancho11=?, Largo11=?, Lugar11=?, FolioReq11=?, Referencia12=?, Descripcion12=?, Unidad12=?, Cantidad12=?, Ancho12=?, Largo12=?, Lugar12=?, FolioReq12=?, Referencia13=?, Descripcion13=?, Unidad13=?, Cantidad13=?, Ancho13=?, Largo13=?, Lugar13=?, FolioReq13=?, Referencia14=?, Descripcion14=?, Unidad14=?, Cantidad14=?, Ancho14=?, Largo14=?, Lugar14=?, FolioReq14=?, Referencia15=?, Descripcion15=?, Unidad15=?, Cantidad15=?, Ancho15=?, Largo15=?, Lugar15=?, FolioReq15=?, Referencia16=?, Descripcion16=?, Unidad16=?, Cantidad16=?, Ancho16=?, Largo16=?, Lugar16=?, FolioReq16=?, Referencia17=?, Descripcion17=?, Unidad17=?, Cantidad17=?, Ancho17=?, Largo17=?, Lugar17=?, FolioReq17=?, Referencia18=?, Descripcion18=?, Unidad18=?, Cantidad18=?, Ancho18=?, Largo18=?, Lugar18=?, FolioReq18=?, Referencia19=?, Descripcion19=?, Unidad19=?, Cantidad19=?, Ancho19=?, Largo19=?, Lugar19=?, FolioReq19=?, Referencia20=?, Descripcion20=?, Unidad20=?, Cantidad20=?, Ancho20=?, Largo20=?, Lugar20=?, FolioReq20=?, OrdenComp=?, FolFactura=?, Comentario=? WHERE ID={}".format(ID)
        c.execute(Actualizar, Lista)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n


