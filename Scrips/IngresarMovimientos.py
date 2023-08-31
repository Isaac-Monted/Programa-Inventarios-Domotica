import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5 import QtCore, QtWidgets, uic 
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator
import sqlite3

class Pagina2():
    def __init__(self):
        #Conectar a la base de datos#
        self.conn = sqlite3.connect("PrgogramaInventarios.db")

    def __str__(self):
        Datos = self.ConsultarMovimientos()
        Aux = ""

        for row in Datos:
            Aux = Aux + str(row) + "\n"
        return Aux

    def ConsultarMovimientos(self, Filtro):
        c = self.conn.cursor()
        consulta = f"SELECT * FROM Movimientos ORDER BY {Filtro} DESC"
        c.execute(consulta)

        Dato = c.fetchall()
        #c.close()
        return Dato

    def ConsultarMovimientosR(self, Filtro):
        c = self.conn.cursor()
        consulta = f"SELECT * FROM Movimientos ORDER BY {Filtro}"
        c.execute(consulta)

        Dato = c.fetchall()
        #c.close()
        return Dato

    def BuscarMovimientos(self, Clave):
        c = self.conn.cursor()
        buscar = "SELECT * FROM Movimientos WHERE Clave= '{}'".format(Clave)
        c.execute(buscar)

        Dato = c.fetchall()
        c.close()
        return Dato

    def BuscarMovimientosN(self, Clave):
        c = self.conn.cursor()
        buscar = "SELECT * FROM Movimientos WHERE Producto= '{}'".format(Clave)
        c.execute(buscar)

        Dato = c.fetchall()
        c.close()
        return Dato

    def AgregarMovimientos(self, TipMov, Producto, Clave, Numero, Marca, Color, Unidad, Cantidad, Proveedor, Lugar, Fecha):
        c = self.conn.cursor()
        Agregar = "INSERT INTO Movimientos (TipMov, Producto, Clave, Nuemro, Marca, Color, Unidad, Cantidad, Proveedor, Lugar, Fecha) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}')".format(TipMov, Producto, Clave, Numero, Marca, Color, Unidad, Cantidad, Proveedor, Lugar, Fecha)
        c.execute(Agregar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def EliminarMovimientos(self, Clave):
        c = self.conn.cursor()
        Elimiar = "DELETE FROM Movimientos WHERE Clave='{}'".format(Clave)
        c.execute(Elimiar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def ActualizarMovimientos(self, ID, TipMov, Producto, Clave, Numero, Marca, Color, Unidad, Cantidad, Proveedor, Lugar, Fecha):
        c = self.conn.cursor()
        Actualizar = "UPDATE Movimientos SET TipMov='{}' Producto='{}', Clave='{}', Numero='{}', Marca='{}', Color='{}', Unidad='{}', Cantidad={}, Proveedor='{}', Lugar='{}', Fecha='{}' WHERE ID={}".format(TipMov, Producto, Clave, Numero, Marca, Color, Unidad, Cantidad, Proveedor, Lugar, Fecha, ID)
        c.execute(Actualizar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
