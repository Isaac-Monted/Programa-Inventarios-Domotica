import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5 import QtCore, QtWidgets, uic 
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator
import sqlite3

class Pagina3():
    def __init__(self):
        #Conectar a la base de datos#
        self.conn = sqlite3.connect("PrgogramaInventarios.db")

    def __str__(self):
        Datos = self.ConsultarProveedores()
        Aux = ""

        for row in Datos:
            Aux = Aux + str(row) + "\n"
        return Aux

    def ConsultarProveedores(self):
        c = self.conn.cursor()
        consulta = "SELECT * FROM Proveedores ORDER BY {}".format("Proveedor")
        c.execute(consulta)

        Dato = c.fetchall()
        #c.close()
        return Dato

    def BuscarProveedores(self, Clave):
        c = self.conn.cursor()
        buscar = "SELECT * FROM Proveedores WHERE Numero= '{}'".format(Clave)
        c.execute(buscar)

        Dato = c.fetchall()
        c.close()
        return Dato

    def BuscarProveedoresN(self, Clave):
        c = self.conn.cursor()
        buscar = "SELECT * FROM Proveedores WHERE Proveedor= '{}'".format(Clave)
        c.execute(buscar)

        Dato = c.fetchall()
        c.close()
        return Dato

    def AgregarProveedores(self, Proveedor, Numero, Correo, Telefono):
        c = self.conn.cursor()
        Agregar = "INSERT INTO Proveedores (Proveedor, Numero, Correo, Telefono) VALUES('{}', '{}', '{}', '{}')".format(Proveedor, Numero, Correo, Telefono)
        c.execute(Agregar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def EliminarProveedores(self, Numero):
        c = self.conn.cursor()
        Elimiar = "DELETE FROM Proveedores WHERE Numero='{}'".format(Numero)
        c.execute(Elimiar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def ActualizarProveedores(self, ID, Proveedor, Numero, Correo, Telefono):
        c = self.conn.cursor()
        Actualizar = "UPDATE Proveedores SET Proveedor='{}', Numero='{}', Correo='{}', Telefono='{}' WHERE ID={}".format(Proveedor, Numero, Correo, Telefono, ID)
        c.execute(Actualizar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n