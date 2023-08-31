import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5 import QtCore, QtWidgets, uic 
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator
import sqlite3

class Pagina8():
    def __init__(self):
        #Conectar a la base de datos#
        self.conn = sqlite3.connect("PrgogramaInventarios.db")

    def __str__(self):
        Datos = self.ConsultarEncabezado()
        Aux = ""

        for row in Datos:
            Aux = Aux + str(row) + "\n"
        return Aux

    def ConsultarEncabezado(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM Encabezado")

        Dato = c.fetchall()
        #c.close()
        return Dato

    def BuscarEncabezado(self, Folio):
        c = self.conn.cursor()
        buscar = "SELECT * FROM Encabezado WHERE Folio= '{}'".format(Folio)
        c.execute(buscar)

        Dato = c.fetchall()
        c.close()
        return Dato

    def BuscarEncabezadoN(self, Folio):
        c = self.conn.cursor()
        buscar = "SELECT * FROM Encabezado WHERE Obra= '{}'".format(Folio)
        c.execute(buscar)

        Dato = c.fetchall()
        c.close()
        return Dato

    def AgregarEncabezado(self, Folio, Obra, Solicita, Autoriza, Almacen, OrdenCompra, FolioFactura, Observaciones, Type):
        c = self.conn.cursor()
        Agregar = "INSERT INTO Encabezado (Folio, Obra, Solicita, Autoriza, Almacen, OrdenCompra, FolioFactura, Observaciones, Type) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(Folio, Obra, Solicita, Autoriza, Almacen, OrdenCompra, FolioFactura, Observaciones, Type)
        c.execute(Agregar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def EliminarEncabezado(self, Folio):
        c = self.conn.cursor()
        Elimiar = "DELETE FROM Encabezado WHERE Folio='{}'".format(Folio)
        c.execute(Elimiar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def ActualizarEncabezado(self, ID, Folio, Obra, Solicita, Autoriza, Almacen, OrdenCompra, FolioFactura, Observaciones, Type):
        c = self.conn.cursor()
        Actualizar = "UPDATE Encabezado SET Folio='{}', Obra='{}', Solicita='{}', Autoriza='{}', Almacen='{}', OrdenCompra='{}', FolioFactura='{}', Observaciones='{}', Type='{}' WHERE Folio='{}'".format(Folio, Obra, Solicita, Autoriza, Almacen, OrdenCompra, FolioFactura, Observaciones, Type, ID)
        c.execute(Actualizar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n