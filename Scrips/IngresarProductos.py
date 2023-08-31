import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5 import QtCore, QtWidgets, uic 
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator
import sqlite3
import datetime

class Pagina1():
    def __init__(self):
        #Conectar a la base de datos#
        self.conn = sqlite3.connect("PrgogramaInventarios.db")

    def __str__(self):
        Datos = self.ConsultarProductos()
        Aux = ""

        for row in Datos:
            Aux = Aux + str(row) + "\n"
        return Aux

    def ConsultarProductos(self):
        c = self.conn.cursor()
        consulta = "SELECT * FROM Inventario ORDER BY {} ".format("Producto")
        c.execute(consulta)

        Dato = c.fetchall()
        #c.close()
        return Dato

    def BuscarProducto(self, Clave):
        c = self.conn.cursor()
        buscar = "SELECT * FROM Inventario WHERE Clave= '{}'".format(Clave)
        c.execute(buscar)

        Dato = c.fetchall()
        c.close()
        return Dato

    def BuscarProductoN(self, Clave):
        c = self.conn.cursor()
        buscar = "SELECT * FROM Inventario WHERE Producto= '{}'".format(Clave)
        c.execute(buscar)

        Dato = c.fetchall()
        c.close()
        return Dato

    def AgregarProducto(self, Producto, Clave, Numero, Marca, Color, Unidad, Stock, Proveedor, Lugar, PCompra, PVenta, Imagen):
        c = self.conn.cursor()
        '''Agregar = "INSERT INTO Inventario (Producto, Clave, Numero, Marca, Color, Unidad, Stock, Proveedor, Lugar, PCompra, PVenta, Imagen) VALUES('{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}')".format(Producto, Clave, Numero, Marca, Color, Unidad, Stock, Proveedor, Lugar, PCompra, PVenta, Imagen)
        c.execute(Agregar)'''
        
        c.execute("INSERT INTO Inventario VALUES(NULL, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Producto, Clave, Numero, Marca, Color, Unidad, Stock, Proveedor, Lugar, PCompra, PVenta, Imagen))
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def EliminarProducto(self, Clave):
        c = self.conn.cursor()
        Elimiar = "DELETE FROM Inventario WHERE Clave='{}'".format(Clave)
        c.execute(Elimiar)
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n
    
    def ActualizarProducto(self, ID, Producto, Clave, Numero, Marca, Color, Unidad, Stock, Proveedor, Lugar, PCompra, PVenta, Imagen):
        c = self.conn.cursor()
        '''Actualizar = "UPDATE Inventario SET Producto='{}', Clave='{}', Numero='{}', Marca='{}', Color='{}', Unidad='{}', Stock={}, Proveedor='{}', Lugar='{}', PCompra='{}', PVenta='{}', Imagen='{}' WHERE ID={}".format(Producto, Clave, Numero, Marca, Color, Unidad, Stock, Proveedor, Lugar, PCompra, PVenta, Imagen, ID)
        c.execute(Actualizar)'''

        c.execute("UPDATE Inventario SET Producto=?, Clave=?, Numero=?, Marca=?, Color=?, Unidad=?, Stock=?, Proveedor=?, Lugar=?, PCompra=?, PVenta=?, Imagen=? WHERE ID=?", (Producto, Clave, Numero, Marca, Color, Unidad, Stock, Proveedor, Lugar, PCompra, PVenta, Imagen, ID))
        n = c.rowcount
        self.conn.commit()
        c.close()
        return n

    def NomColumMov(self):
        NombreColumnas = (
            'Tipo de Mov.', #1
            'Producto', #2
            'Clave', #3
            'Numero', #4
            'Marca', #5
            'Color', #6
            'Unidad', #7
            'Cantidad', #8
            'Proveedor', #9
            'Lugar', #10
            'Fecha', #11
        )
        return NombreColumnas

    def NomColum(self):
        NombreColumnas = (
            'Folio', #1
            'Obra', #2
            'Fecha', #3
            'Solicita', #4
            'Autoriza', #5
            'Almacen', #6
            'Referencia', #7
            'Descripcion', #8
            'Unidad', #9
            'Cantidad', #10
            'Ancho', #11
            'Largo', #12
            'Lugar', #13
            'Folio REQ', #14
            'Referencia 2', #15
            'Descripcion 2', #16
            'Unidad 2', #17
            'Cantidad 2', #18
            'Ancho 2', #19
            'Largo 2', #20
            'Lugar 2', #21
            'Folio REQ 2', #22
            'Referencia 3', #23
            'Descripcion 3', #24
            'Unidad 3', #25
            'Cantidad 3', #26
            'Ancho 3', #27
            'Largo 3', #28
            'Lugar 3', #29
            'Folio REQ 3', #30
            'Referencia 4', #31
            'Descripcion 4', #32
            'Unidad 4', #33
            'Cantidad 4', #34
            'Ancho 4', #35
            'Largo 4', #36
            'Lugar 4', #37
            'Folio REQ 4', #38
            'Referencia 5', #39
            'Descripcion 5', #40
            'Unidad 5', #41
            'Cantidad 5', #42
            'Ancho 5', #43
            'Largo 5', #44
            'Lugar 5', #45
            'Folio REQ 5', #46
            'Referencia 6', #47
            'Descripcion 6', #48
            'Unidad 6', #49
            'Cantidad 6', #50
            'Ancho 6', #51
            'Largo 6', #52
            'Lugar 6', #53
            'Folio REQ 6', #54
            'Referencia 7', #55
            'Descripcion 7', #56
            'Unidad 7', #57
            'Cantidad 7', #58
            'Ancho 7', #59
            'Largo 7', #60
            'Lugar 7', #61
            'Folio REQ 7', #62
            'Referencia 8', #63
            'Descripcion 8', #64
            'Unidad 8', #65
            'Cantidad 8', #66
            'Ancho 8', #67
            'Largo 8', #68
            'Lugar 8', #69
            'Folio REQ 8', #70
            'Referencia 9', #71
            'Descripcion 9', #72
            'Unidad 9', #73
            'Cantidad 9', #74
            'Ancho 9', #75
            'Largo 9', #76
            'Lugar 9', #77
            'Folio REQ 9', #78
            'Referencia 10', #79
            'Descripcion 10', #80
            'Unidad 10', #81
            'Cantidad 10', #82
            'Ancho 10', #83
            'Largo 10', #84
            'Lugar 10', #85
            'Folio REQ 10', #86
            'Referencia 11', #87
            'Descripcion 11', #88
            'Unidad 11', #89
            'Cantidad 11', #90
            'Ancho 11', #91
            'Largo 11', #92
            'Lugar 11', #93
            'Folio REQ 11', #94
            'Referencia 12', #95
            'Descripcion 12', #96
            'Unidad 12', #97
            'Cantidad 12', #98
            'Ancho 12', #99
            'Largo 12', #100
            'Lugar 12', #101
            'Folio REQ 12', #102
            'Referencia 13', #103
            'Descripcion 13', #104
            'Unidad 13', #105
            'Cantidad 13', #106
            'Ancho 13', #107
            'Largo 13', #108
            'Lugar 13', #109
            'Folio REQ 13', #110
            'Referencia 14', #111
            'Descripcion14', #112
            'Unidad 14', #113
            'Cantidad 14', #114
            'Ancho 14', #115
            'Largo 14', #116
            'Lugar 14', #117
            'Folio REQ 14', #118
            'Referencia 15', #119
            'Descripcion 15', #120
            'Unidad 15', #121
            'Cantidad 15', #122
            'Ancho 15', #123
            'Largo 15', #124
            'Lugar 15', #125
            'Folio REQ 15', #126
            'Referencia 16', #127
            'Descripcion 16', #128
            'Unidad 16', #129
            'Cantidad 16', #130
            'Ancho 16', #131
            'Largo 16', #132
            'Lugar 16', #133
            'Folio REQ 16', #134
            'Referencia 17', #135
            'Descripcion 17', #136
            'Unidad 17', #137
            'Cantidad 17', #138
            'Ancho 17', #139
            'Largo 17', #140
            'Lugar 17', #141
            'Folio REQ 17', #142
            'Referencia 18', #143
            'Descripcion 18', #144
            'Unidad 18', #145
            'Cantidad 18', #146
            'Ancho 18', #147
            'Largo 18', #148
            'Lugar 18', #149
            'Folio REQ 18', #150
            'Referencia 19', #151
            'Descripcion 19', #152
            'Unidad 19', #153
            'Cantidad 19', #154
            'Ancho 19', #155
            'Largo 19', #156
            'Lugar 19', #157
            'Folio REQ 19', #158
            'Referencia 20', #159
            'Descripcion 20', #160
            'Unidad 20', #161
            'Cantidad 20', #162
            'Ancho 20', #163
            'Largo 20', #164
            'Lugar 20', #165
            'Folio REQ 20' #166
        )
        return NombreColumnas
    
    def FechaLetra(self):
        Valor = datetime.datetime.now()
        Fecha = datetime.datetime.strftime(Valor, '%Y/%m/%d %H:%M:%S')
        #Fecha = str(Fecha)[0: 19].replace("-", "/")
        #print(Fecha)

        nombre = datetime.datetime.strftime(Valor, '%A')
        nombre = str(nombre)
        if nombre == "Monday":
            nombre = "Lunes"
        elif nombre == "Tuesday":
            nombre = "Martes"
        elif nombre == "Wednesday":
            nombre = "Miercoles"
        elif nombre == "Thursday":
            nombre = "Jueves"
        elif nombre == "Friday":
            nombre = "Viernes"
        elif nombre == "Saturday":
            nombre = "Sabado"
        elif nombre == "Sunday":
            nombre = "Domingo"
        else:
            print("Error Dia")
        #print(nombre)

        Dia = datetime.datetime.strftime(Valor, '%d')
        Dia = str(Dia)
        #print(Dia)

        Mes = datetime.datetime.strftime(Valor, '%m')
        Mes = int(Mes)
        if Mes == 1:
            Mes = "Enero"
        elif Mes == 2:
            Mes = "Febrero"
        elif Mes == 3:
            Mes = "Marzo"
        elif Mes == 4:
            Mes = "Abril"
        elif Mes == 5:
            Mes = "Mayo"
        elif Mes == 6:
            Mes = "Junio"
        elif Mes == 7:
            Mes = "Julio"
        elif Mes == 8:
            Mes = "Agosto"
        elif Mes == 9:
            Mes = "Septiembre"
        elif Mes == 10:
            Mes = "Octubre"
        elif Mes == 11:
            Mes = "Noviembre"
        elif Mes == 12:
            Mes = "Diciembre"
        else:
            print('Error Mes')
        #print(Mes)

        Allo = datetime.datetime.strftime(Valor, '%Y')
        Allo = str(Allo)
        #print(Allo)

        Hora = datetime.datetime.strftime(Valor, '%H:%M:%S')
        Hora = str(Hora)
        #print(Hora)

        formato = "{}, {} de {} de {}".format(nombre, Dia, Mes, Allo)
        #print(formato)

        Lista = [
            Fecha,
            nombre,
            Dia,
            Mes,
            Allo,
            Hora,
            formato
        ]
        #print(Lista)
        return Lista
    
'''cosa = Pagina1()
fecha = cosa.FechaLetra()

print(fecha[0])'''