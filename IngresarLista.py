import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5 import QtCore, QtWidgets, uic 
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator
import sqlite3

class Pagina7():
    def __init__(self):
        #Conectar a la base de datos#
        self.conn = sqlite3.connect("PrgogramaInventarios.db")

    def __str__(self):
        Datos = self.ConsultarLista()
        Aux = ""

        for row in Datos:
            Aux = Aux + str(row) + "\n"
        return Aux

    def ConsultarLista(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM Lista")

        Dato = c.fetchall()
        #c.close()
        return Dato

    def BuscarLista(self, Referencia):
        c = self.conn.cursor()
        buscar = "SELECT * FROM Lista WHERE Referencia= '{}'".format(Referencia)
        c.execute(buscar)

        Dato = c.fetchall()
        c.close()
        return Dato

    def BuscarListaN(self, Clave):
        c = self.conn.cursor()
        buscar = "SELECT * FROM Lista WHERE Descripcion= '{}'".format(Clave)
        c.execute(buscar)

        Dato = c.fetchall()
        c.close()
        return Dato

    def AgregarLista(self, ID, Referencia, Descripcion, Unidad, Cantidad, Ancho, Largo, Lugar, FolioREQ, Numero, Marca, Color, Proveedor, Stock, TPMov):
        c = self.conn.cursor()
        Agregar = "INSERT INTO Lista (ID, Referencia, Descripcion, Unidad, Cantidad, Ancho, Largo, Lugar, FolioREQ, Numero, Marca, Color, Proveedor, Stock, TPMov ) VALUES('{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}')".format(ID, Referencia, Descripcion, Unidad, Cantidad, Ancho, Largo, Lugar, FolioREQ, Numero, Marca, Color, Proveedor, Stock, TPMov)
        c.execute(Agregar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def EliminarLista(self, ID):
        c = self.conn.cursor()
        Elimiar = "DELETE FROM Lista WHERE ID='{}'".format(ID)
        c.execute(Elimiar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def ActualizarLista(self, ID, Referencia, Descripcion, Unidad, Cantidad, Ancho, Largo, Lugar, FolioREQ, Numero, Marca, Color, Proveedor, Stock, TPMov):
        c = self.conn.cursor()
        Actualizar = "UPDATE Lista SET Referencia='{}', Descripcion='{}', Unidad='{}', Cantidad={}, Ancho='{}', Largo='{}', Lugar='{}', FolioREQ='{}', Numero='{}', Marca='{}', Color='{}', Proveedor='{}', Stock={}, TPMov='{}' WHERE ID={}".format(Referencia, Descripcion, Unidad, Cantidad, Ancho, Largo, Lugar, FolioREQ, Numero, Marca, Color, Proveedor, Stock, TPMov, ID)
        c.execute(Actualizar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n