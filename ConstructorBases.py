import sqlite3
from sqlite3 import *


class inevntario:
    def __init__(self):
        pass
    def Inventario(self):
        conn = sqlite3.connect('PrgogramaInventarios.db')
        c = conn.cursor()
        try:
            c.execute('''
                CREATE TABLE IF NOT EXISTS Inventario (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Producto TEXT NOT NULL,
                Clave TEXT NOT NULL UNIQUE,
                Numero VARCHAR(20),
                Marca VARCHAR(20),
                Color VARCHAR(20),
                Unidad VARCHAR(20) NOT NULL,
                Stock INTEGER NOT NULL,
                Proveedor VARCHAR(20),
                Lugar VARCHAR(50),
                PCompra VARCHAR(20),
                PVenta  VARCHAR(20),
                Imagen BLOB )
            ''')
        except:
            print('Error Base Inventario')
    
    def Movimientos(self):
        conn = sqlite3.connect('PrgogramaInventarios.db')
        c = conn.cursor()
        try:
            c.execute('''
                CREATE TABLE IF NOT EXISTS Movimientos (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                TipMov VARCHAR(20) NOT NULL,
                Producto TEXT NOT NULL,
                Clave TEXT NOT NULL,
                Nuemro VARCHAR(20),
                Marca VARCHAR(20),
                Color VARCHAR(20),
                Unidad VARCHAR(20) NOT NULL,
                Cantidad INTEGER NOT NULL,
                Proveedor VARCHAR(20),
                Lugar VARCHAR(50) NOT NULL,
                Fecha TEXT NOT NULL )
            ''')
        except:
            print('Error Base Movimientos')

    def Proveedores(self):
        conn = sqlite3.connect('PrgogramaInventarios.db')
        c = conn.cursor()
        try:
            c.execute('''
                CREATE TABLE IF NOT EXISTS Proveedores (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Proveedor	TEXT NOT NULL,
	            Numero	VARCHAR(20) NOT NULL UNIQUE,
                Correo VARCHAR(50),
                Telefono VARCHAR(20) )
            ''')
        except:
            print('Error Base Proveedores')

    def Encabezado(self):
        conn = sqlite3.connect('PrgogramaInventarios.db')
        c = conn.cursor()
        try:
            c.execute('''
                CREATE TABLE IF NOT EXISTS Encabezado (
                Folio TEXT NOT NULL UNIQUE,
                Obra TEXT NOT NULL,
                Solicita VARCHAR(20) NOT NULL,
                Autoriza VARCHAR(20) NOT NULL,
                Almacen VARCHAR(20) NOT NULL,
                OrdenCompra VARCHAR(20) NOT NULL,
                FolioFactura VARCHAR(20) NOT NULL,
                Observaciones TEXT,
                Type TEXT NOT NULL )
            ''')
        except:
            print('Error Base Encabezado')

    def Lista(self):
        conn = sqlite3.connect('PrgogramaInventarios.db')
        c = conn.cursor()
        try:
            c.execute('''
                CREATE TABLE IF NOT EXISTS Lista (
                ID INTEGER NOT NULL UNIQUE,
                Referencia TEXT NOT NULL,
                Descripcion TEXT NOT NULL,
                Unidad TEXT NOT NULL,
                Cantidad INTEGER NOT NULL,
                Ancho VARCHAR(20),
                Largo VARCHAR(20),
                Lugar VARCHAR(50) NOT NULL,
                FolioREQ VARCHAR(50),
                Numero VARCHAR(20),
                Marca VARCHAR(20),
                Color VARCHAR(20),
                Proveedor VARCHAR(20),
                Stock INTEGER NOT NULL,
                TPMov VARCHAR(20) NOT NULL )
            ''')
        except:
            print('Error Base Lista')

    def RegistroSalidas(self):
        conn = sqlite3.connect('PrgogramaInventarios.db')
        c = conn.cursor()
        try:
            c.execute('''
                CREATE TABLE IF NOT EXISTS RegistroSalidas (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Folio TEXT NOT NULL UNIQUE,
                Obra TEXT NOT NULL,
                Fecha TEXT NOT NULL,
                Solicita VARCHAR(20) NOT NULL,
                Autoriza VARCHAR(20) NOT NULL,
                Almacen VARCHAR(20) NOT NULL,

                Referencia TEXT NOT NULL,
                Descripcion TEXT NOT NULL,
                Unidad TEXT NOT NULL,
                Cantidad INTEGER NOT NULL,
                Ancho VARCHAR(20),
                Largo VARCHAR(20),
                Lugar VARCHAR(50) NOT NULL,
                FolioReq VARCHAR(50),

                Referencia2 TEXT NOT NULL,
                Descripcion2 TEXT NOT NULL,
                Unidad2 TEXT NOT NULL,
                Cantidad2 INTEGER NOT NULL,
                Ancho2 VARCHAR(20),
                Largo2 VARCHAR(20),
                Lugar2 VARCHAR(50) NOT NULL,
                FolioReq2 VARCHAR(50),

                Referencia3 TEXT NOT NULL,
                Descripcion3 TEXT NOT NULL,
                Unidad3 TEXT NOT NULL,
                Cantidad3 INTEGER NOT NULL,
                Ancho3 VARCHAR(20),
                Largo3 VARCHAR(20),
                Lugar3 VARCHAR(50) NOT NULL,
                FolioReq3 VARCHAR(50),

                Referencia4 TEXT NOT NULL,
                Descripcion4 TEXT NOT NULL,
                Unidad4 TEXT NOT NULL,
                Cantidad4 INTEGER NOT NULL,
                Ancho4 VARCHAR(20),
                Largo4 VARCHAR(20),
                Lugar4 VARCHAR(50) NOT NULL,
                FolioReq4 VARCHAR(50),

                Referencia5 TEXT NOT NULL,
                Descripcion5 TEXT NOT NULL,
                Unidad5 TEXT NOT NULL,
                Cantidad5 INTEGER NOT NULL,
                Ancho5 VARCHAR(20),
                Largo5 VARCHAR(20),
                Lugar5 VARCHAR(50) NOT NULL,
                FolioReq5 VARCHAR(50),

                Referencia6 TEXT NOT NULL,
                Descripcion6 TEXT NOT NULL,
                Unidad6 TEXT NOT NULL,
                Cantidad6 INTEGER NOT NULL,
                Ancho6 VARCHAR(20),
                Largo6 VARCHAR(20),
                Lugar6 VARCHAR(50) NOT NULL,
                FolioReq6 VARCHAR(50),

                Referencia7 TEXT NOT NULL,
                Descripcion7 TEXT NOT NULL,
                Unidad7 TEXT NOT NULL,
                Cantidad7 INTEGER NOT NULL,
                Ancho7 VARCHAR(20),
                Largo7 VARCHAR(20),
                Lugar7 VARCHAR(50) NOT NULL,
                FolioReq7 VARCHAR(50),

                Referencia8 TEXT NOT NULL,
                Descripcion8 TEXT NOT NULL,
                Unidad8 TEXT NOT NULL,
                Cantidad8 INTEGER NOT NULL,
                Ancho8 VARCHAR(20),
                Largo8 VARCHAR(20),
                Lugar8 VARCHAR(50) NOT NULL,
                FolioReq8 VARCHAR(50),

                Referencia9 TEXT NOT NULL,
                Descripcion9 TEXT NOT NULL,
                Unidad9 TEXT NOT NULL,
                Cantidad9 INTEGER NOT NULL,
                Ancho9 VARCHAR(20),
                Largo9 VARCHAR(20),
                Lugar9 VARCHAR(50) NOT NULL,
                FolioReq9 VARCHAR(50),

                Referencia10 TEXT NOT NULL,
                Descripcion10 TEXT NOT NULL,
                Unidad10 TEXT NOT NULL,
                Cantidad10 INTEGER NOT NULL,
                Ancho10 VARCHAR(20),
                Largo10 VARCHAR(20),
                Lugar10 VARCHAR(50) NOT NULL,
                FolioReq10 VARCHAR(50),

                Referencia11 TEXT NOT NULL,
                Descripcion11 TEXT NOT NULL,
                Unidad11 TEXT NOT NULL,
                Cantidad11 INTEGER NOT NULL,
                Ancho11 VARCHAR(20),
                Largo11 VARCHAR(20),
                Lugar11 VARCHAR(50) NOT NULL,
                FolioReq11 VARCHAR(50),

                Referencia12 TEXT NOT NULL,
                Descripcion12 TEXT NOT NULL,
                Unidad12 TEXT NOT NULL,
                Cantidad12 INTEGER NOT NULL,
                Ancho12 VARCHAR(20),
                Largo12 VARCHAR(20),
                Lugar12 VARCHAR(50) NOT NULL,
                FolioReq12 VARCHAR(50),

                Referencia13 TEXT NOT NULL,
                Descripcion13 TEXT NOT NULL,
                Unidad13 TEXT NOT NULL,
                Cantidad13 INTEGER NOT NULL,
                Ancho13 VARCHAR(20),
                Largo13 VARCHAR(20),
                Lugar13 VARCHAR(50) NOT NULL,
                FolioReq13 VARCHAR(50),

                Referencia14 TEXT NOT NULL,
                Descripcion14 TEXT NOT NULL,
                Unidad14 TEXT NOT NULL,
                Cantidad14 INTEGER NOT NULL,
                Ancho14 VARCHAR(20),
                Largo14 VARCHAR(20),
                Lugar14 VARCHAR(50) NOT NULL,
                FolioReq14 VARCHAR(50),

                Referencia15 TEXT NOT NULL,
                Descripcion15 TEXT NOT NULL,
                Unidad15 TEXT NOT NULL,
                Cantidad15 INTEGER NOT NULL,
                Ancho15 VARCHAR(20),
                Largo15 VARCHAR(20),
                Lugar15 VARCHAR(50) NOT NULL,
                FolioReq15 VARCHAR(50),

                Referencia16 TEXT NOT NULL,
                Descripcion16 TEXT NOT NULL,
                Unidad16 TEXT NOT NULL,
                Cantidad16 INTEGER NOT NULL,
                Ancho16 VARCHAR(20),
                Largo16 VARCHAR(20),
                Lugar16 VARCHAR(50) NOT NULL,
                FolioReq16 VARCHAR(50),

                Referencia17 TEXT NOT NULL,
                Descripcion17 TEXT NOT NULL,
                Unidad17 TEXT NOT NULL,
                Cantidad17 INTEGER NOT NULL,
                Ancho17 VARCHAR(20),
                Largo17 VARCHAR(20),
                Lugar17 VARCHAR(50) NOT NULL,
                FolioReq17 VARCHAR(50),

                Referencia18 TEXT NOT NULL,
                Descripcion18 TEXT NOT NULL,
                Unidad18 TEXT NOT NULL,
                Cantidad18 INTEGER NOT NULL,
                Ancho18 VARCHAR(20),
                Largo18 VARCHAR(20),
                Lugar18 VARCHAR(50) NOT NULL,
                FolioReq18 VARCHAR(50),

                Referencia19 TEXT NOT NULL,
                Descripcion19 TEXT NOT NULL,
                Unidad19 TEXT NOT NULL,
                Cantidad19 INTEGER NOT NULL,
                Ancho19 VARCHAR(20),
                Largo19 VARCHAR(20),
                Lugar19 VARCHAR(50) NOT NULL,
                FolioReq19 VARCHAR(50),

                Referencia20 TEXT NOT NULL,
                Descripcion20 TEXT NOT NULL,
                Unidad20 TEXT NOT NULL,
                Cantidad20 INTEGER NOT NULL,
                Ancho20 VARCHAR(20),
                Largo20 VARCHAR(20),
                Lugar20 VARCHAR(50) NOT NULL,
                FolioReq20 VARCHAR(50),

                OrdenComp VARCHAR(20),
                FolFactura VARCHAR(20),
                Comentario TEXT )
            ''')
        except:
            print('Error Base RegistroSalidas')

    def RegistroEntradas(self):
        conn = sqlite3.connect('PrgogramaInventarios.db')
        c = conn.cursor()
        try:
            c.execute('''
                CREATE TABLE IF NOT EXISTS RegistroEntradas (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Folio TEXT NOT NULL UNIQUE,
                Obra TEXT NOT NULL,
                Fecha TEXT NOT NULL,
                Solicita VARCHAR(20) NOT NULL,
                Autoriza VARCHAR(20) NOT NULL,
                Almacen VARCHAR(20) NOT NULL,

                Referencia TEXT NOT NULL,
                Descripcion TEXT NOT NULL,
                Unidad TEXT NOT NULL,
                Cantidad INTEGER NOT NULL,
                Ancho VARCHAR(20),
                Largo VARCHAR(20),
                Lugar VARCHAR(50) NOT NULL,
                FolioReq VARCHAR(50),

                Referencia2 TEXT NOT NULL,
                Descripcion2 TEXT NOT NULL,
                Unidad2 TEXT NOT NULL,
                Cantidad2 INTEGER NOT NULL,
                Ancho2 VARCHAR(20),
                Largo2 VARCHAR(20),
                Lugar2 VARCHAR(50) NOT NULL,
                FolioReq2 VARCHAR(50),

                Referencia3 TEXT NOT NULL,
                Descripcion3 TEXT NOT NULL,
                Unidad3 TEXT NOT NULL,
                Cantidad3 INTEGER NOT NULL,
                Ancho3 VARCHAR(20),
                Largo3 VARCHAR(20),
                Lugar3 VARCHAR(50) NOT NULL,
                FolioReq3 VARCHAR(50),

                Referencia4 TEXT NOT NULL,
                Descripcion4 TEXT NOT NULL,
                Unidad4 TEXT NOT NULL,
                Cantidad4 INTEGER NOT NULL,
                Ancho4 VARCHAR(20),
                Largo4 VARCHAR(20),
                Lugar4 VARCHAR(50) NOT NULL,
                FolioReq4 VARCHAR(50),

                Referencia5 TEXT NOT NULL,
                Descripcion5 TEXT NOT NULL,
                Unidad5 TEXT NOT NULL,
                Cantidad5 INTEGER NOT NULL,
                Ancho5 VARCHAR(20),
                Largo5 VARCHAR(20),
                Lugar5 VARCHAR(50) NOT NULL,
                FolioReq5 VARCHAR(50),

                Referencia6 TEXT NOT NULL,
                Descripcion6 TEXT NOT NULL,
                Unidad6 TEXT NOT NULL,
                Cantidad6 INTEGER NOT NULL,
                Ancho6 VARCHAR(20),
                Largo6 VARCHAR(20),
                Lugar6 VARCHAR(50) NOT NULL,
                FolioReq6 VARCHAR(50),

                Referencia7 TEXT NOT NULL,
                Descripcion7 TEXT NOT NULL,
                Unidad7 TEXT NOT NULL,
                Cantidad7 INTEGER NOT NULL,
                Ancho7 VARCHAR(20),
                Largo7 VARCHAR(20),
                Lugar7 VARCHAR(50) NOT NULL,
                FolioReq7 VARCHAR(50),

                Referencia8 TEXT NOT NULL,
                Descripcion8 TEXT NOT NULL,
                Unidad8 TEXT NOT NULL,
                Cantidad8 INTEGER NOT NULL,
                Ancho8 VARCHAR(20),
                Largo8 VARCHAR(20),
                Lugar8 VARCHAR(50) NOT NULL,
                FolioReq8 VARCHAR(50),

                Referencia9 TEXT NOT NULL,
                Descripcion9 TEXT NOT NULL,
                Unidad9 TEXT NOT NULL,
                Cantidad9 INTEGER NOT NULL,
                Ancho9 VARCHAR(20),
                Largo9 VARCHAR(20),
                Lugar9 VARCHAR(50) NOT NULL,
                FolioReq9 VARCHAR(50),

                Referencia10 TEXT NOT NULL,
                Descripcion10 TEXT NOT NULL,
                Unidad10 TEXT NOT NULL,
                Cantidad10 INTEGER NOT NULL,
                Ancho10 VARCHAR(20),
                Largo10 VARCHAR(20),
                Lugar10 VARCHAR(50) NOT NULL,
                FolioReq10 VARCHAR(50),

                Referencia11 TEXT NOT NULL,
                Descripcion11 TEXT NOT NULL,
                Unidad11 TEXT NOT NULL,
                Cantidad11 INTEGER NOT NULL,
                Ancho11 VARCHAR(20),
                Largo11 VARCHAR(20),
                Lugar11 VARCHAR(50) NOT NULL,
                FolioReq11 VARCHAR(50),

                Referencia12 TEXT NOT NULL,
                Descripcion12 TEXT NOT NULL,
                Unidad12 TEXT NOT NULL,
                Cantidad12 INTEGER NOT NULL,
                Ancho12 VARCHAR(20),
                Largo12 VARCHAR(20),
                Lugar12 VARCHAR(50) NOT NULL,
                FolioReq12 VARCHAR(50),

                Referencia13 TEXT NOT NULL,
                Descripcion13 TEXT NOT NULL,
                Unidad13 TEXT NOT NULL,
                Cantidad13 INTEGER NOT NULL,
                Ancho13 VARCHAR(20),
                Largo13 VARCHAR(20),
                Lugar13 VARCHAR(50) NOT NULL,
                FolioReq13 VARCHAR(50),

                Referencia14 TEXT NOT NULL,
                Descripcion14 TEXT NOT NULL,
                Unidad14 TEXT NOT NULL,
                Cantidad14 INTEGER NOT NULL,
                Ancho14 VARCHAR(20),
                Largo14 VARCHAR(20),
                Lugar14 VARCHAR(50) NOT NULL,
                FolioReq14 VARCHAR(50),

                Referencia15 TEXT NOT NULL,
                Descripcion15 TEXT NOT NULL,
                Unidad15 TEXT NOT NULL,
                Cantidad15 INTEGER NOT NULL,
                Ancho15 VARCHAR(20),
                Largo15 VARCHAR(20),
                Lugar15 VARCHAR(50) NOT NULL,
                FolioReq15 VARCHAR(50),

                Referencia16 TEXT NOT NULL,
                Descripcion16 TEXT NOT NULL,
                Unidad16 TEXT NOT NULL,
                Cantidad16 INTEGER NOT NULL,
                Ancho16 VARCHAR(20),
                Largo16 VARCHAR(20),
                Lugar16 VARCHAR(50) NOT NULL,
                FolioReq16 VARCHAR(50),

                Referencia17 TEXT NOT NULL,
                Descripcion17 TEXT NOT NULL,
                Unidad17 TEXT NOT NULL,
                Cantidad17 INTEGER NOT NULL,
                Ancho17 VARCHAR(20),
                Largo17 VARCHAR(20),
                Lugar17 VARCHAR(50) NOT NULL,
                FolioReq17 VARCHAR(50),

                Referencia18 TEXT NOT NULL,
                Descripcion18 TEXT NOT NULL,
                Unidad18 TEXT NOT NULL,
                Cantidad18 INTEGER NOT NULL,
                Ancho18 VARCHAR(20),
                Largo18 VARCHAR(20),
                Lugar18 VARCHAR(50) NOT NULL,
                FolioReq18 VARCHAR(50),

                Referencia19 TEXT NOT NULL,
                Descripcion19 TEXT NOT NULL,
                Unidad19 TEXT NOT NULL,
                Cantidad19 INTEGER NOT NULL,
                Ancho19 VARCHAR(20),
                Largo19 VARCHAR(20),
                Lugar19 VARCHAR(50) NOT NULL,
                FolioReq19 VARCHAR(50),

                Referencia20 TEXT NOT NULL,
                Descripcion20 TEXT NOT NULL,
                Unidad20 TEXT NOT NULL,
                Cantidad20 INTEGER NOT NULL,
                Ancho20 VARCHAR(20),
                Largo20 VARCHAR(20),
                Lugar20 VARCHAR(50) NOT NULL,
                FolioReq20 VARCHAR(50),

                OrdenComp VARCHAR(20),
                FolFactura VARCHAR(20),
                Comentario TEXT)
            ''')
        except:
            print('Error Base RegistroEntradas')

    def ListasDeSalidas(self):
        conn = sqlite3.connect('PrgogramaInventarios.db')
        c = conn.cursor()
        try:
            c.execute('''
                CREATE TABLE IF NOT EXISTS ListasDeSalidas (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Folio TEXT NOT NULL UNIQUE,
                Obra TEXT NOT NULL,
                Fecha TEXT NOT NULL,
                Solicita VARCHAR(20) NOT NULL,
                Autoriza VARCHAR(20) NOT NULL,
                Almacen VARCHAR(20) NOT NULL,

                Referencia TEXT NOT NULL,
                Descripcion TEXT NOT NULL,
                Unidad TEXT NOT NULL,
                Cantidad INTEGER NOT NULL,
                Ancho VARCHAR(20),
                Largo VARCHAR(20),
                Lugar VARCHAR(50) NOT NULL,
                FolioReq VARCHAR(50),

                Referencia2 TEXT NOT NULL,
                Descripcion2 TEXT NOT NULL,
                Unidad2 TEXT NOT NULL,
                Cantidad2 INTEGER NOT NULL,
                Ancho2 VARCHAR(20),
                Largo2 VARCHAR(20),
                Lugar2 VARCHAR(50) NOT NULL,
                FolioReq2 VARCHAR(50),

                Referencia3 TEXT NOT NULL,
                Descripcion3 TEXT NOT NULL,
                Unidad3 TEXT NOT NULL,
                Cantidad3 INTEGER NOT NULL,
                Ancho3 VARCHAR(20),
                Largo3 VARCHAR(20),
                Lugar3 VARCHAR(50) NOT NULL,
                FolioReq3 VARCHAR(50),

                Referencia4 TEXT NOT NULL,
                Descripcion4 TEXT NOT NULL,
                Unidad4 TEXT NOT NULL,
                Cantidad4 INTEGER NOT NULL,
                Ancho4 VARCHAR(20),
                Largo4 VARCHAR(20),
                Lugar4 VARCHAR(50) NOT NULL,
                FolioReq4 VARCHAR(50),

                Referencia5 TEXT NOT NULL,
                Descripcion5 TEXT NOT NULL,
                Unidad5 TEXT NOT NULL,
                Cantidad5 INTEGER NOT NULL,
                Ancho5 VARCHAR(20),
                Largo5 VARCHAR(20),
                Lugar5 VARCHAR(50) NOT NULL,
                FolioReq5 VARCHAR(50),

                Referencia6 TEXT NOT NULL,
                Descripcion6 TEXT NOT NULL,
                Unidad6 TEXT NOT NULL,
                Cantidad6 INTEGER NOT NULL,
                Ancho6 VARCHAR(20),
                Largo6 VARCHAR(20),
                Lugar6 VARCHAR(50) NOT NULL,
                FolioReq6 VARCHAR(50),

                Referencia7 TEXT NOT NULL,
                Descripcion7 TEXT NOT NULL,
                Unidad7 TEXT NOT NULL,
                Cantidad7 INTEGER NOT NULL,
                Ancho7 VARCHAR(20),
                Largo7 VARCHAR(20),
                Lugar7 VARCHAR(50) NOT NULL,
                FolioReq7 VARCHAR(50),

                Referencia8 TEXT NOT NULL,
                Descripcion8 TEXT NOT NULL,
                Unidad8 TEXT NOT NULL,
                Cantidad8 INTEGER NOT NULL,
                Ancho8 VARCHAR(20),
                Largo8 VARCHAR(20),
                Lugar8 VARCHAR(50) NOT NULL,
                FolioReq8 VARCHAR(50),

                Referencia9 TEXT NOT NULL,
                Descripcion9 TEXT NOT NULL,
                Unidad9 TEXT NOT NULL,
                Cantidad9 INTEGER NOT NULL,
                Ancho9 VARCHAR(20),
                Largo9 VARCHAR(20),
                Lugar9 VARCHAR(50) NOT NULL,
                FolioReq9 VARCHAR(50),

                Referencia10 TEXT NOT NULL,
                Descripcion10 TEXT NOT NULL,
                Unidad10 TEXT NOT NULL,
                Cantidad10 INTEGER NOT NULL,
                Ancho10 VARCHAR(20),
                Largo10 VARCHAR(20),
                Lugar10 VARCHAR(50) NOT NULL,
                FolioReq10 VARCHAR(50),

                Referencia11 TEXT NOT NULL,
                Descripcion11 TEXT NOT NULL,
                Unidad11 TEXT NOT NULL,
                Cantidad11 INTEGER NOT NULL,
                Ancho11 VARCHAR(20),
                Largo11 VARCHAR(20),
                Lugar11 VARCHAR(50) NOT NULL,
                FolioReq11 VARCHAR(50),

                Referencia12 TEXT NOT NULL,
                Descripcion12 TEXT NOT NULL,
                Unidad12 TEXT NOT NULL,
                Cantidad12 INTEGER NOT NULL,
                Ancho12 VARCHAR(20),
                Largo12 VARCHAR(20),
                Lugar12 VARCHAR(50) NOT NULL,
                FolioReq12 VARCHAR(50),

                Referencia13 TEXT NOT NULL,
                Descripcion13 TEXT NOT NULL,
                Unidad13 TEXT NOT NULL,
                Cantidad13 INTEGER NOT NULL,
                Ancho13 VARCHAR(20),
                Largo13 VARCHAR(20),
                Lugar13 VARCHAR(50) NOT NULL,
                FolioReq13 VARCHAR(50),

                Referencia14 TEXT NOT NULL,
                Descripcion14 TEXT NOT NULL,
                Unidad14 TEXT NOT NULL,
                Cantidad14 INTEGER NOT NULL,
                Ancho14 VARCHAR(20),
                Largo14 VARCHAR(20),
                Lugar14 VARCHAR(50) NOT NULL,
                FolioReq14 VARCHAR(50),

                Referencia15 TEXT NOT NULL,
                Descripcion15 TEXT NOT NULL,
                Unidad15 TEXT NOT NULL,
                Cantidad15 INTEGER NOT NULL,
                Ancho15 VARCHAR(20),
                Largo15 VARCHAR(20),
                Lugar15 VARCHAR(50) NOT NULL,
                FolioReq15 VARCHAR(50),

                Referencia16 TEXT NOT NULL,
                Descripcion16 TEXT NOT NULL,
                Unidad16 TEXT NOT NULL,
                Cantidad16 INTEGER NOT NULL,
                Ancho16 VARCHAR(20),
                Largo16 VARCHAR(20),
                Lugar16 VARCHAR(50) NOT NULL,
                FolioReq16 VARCHAR(50),

                Referencia17 TEXT NOT NULL,
                Descripcion17 TEXT NOT NULL,
                Unidad17 TEXT NOT NULL,
                Cantidad17 INTEGER NOT NULL,
                Ancho17 VARCHAR(20),
                Largo17 VARCHAR(20),
                Lugar17 VARCHAR(50) NOT NULL,
                FolioReq17 VARCHAR(50),

                Referencia18 TEXT NOT NULL,
                Descripcion18 TEXT NOT NULL,
                Unidad18 TEXT NOT NULL,
                Cantidad18 INTEGER NOT NULL,
                Ancho18 VARCHAR(20),
                Largo18 VARCHAR(20),
                Lugar18 VARCHAR(50) NOT NULL,
                FolioReq18 VARCHAR(50),

                Referencia19 TEXT NOT NULL,
                Descripcion19 TEXT NOT NULL,
                Unidad19 TEXT NOT NULL,
                Cantidad19 INTEGER NOT NULL,
                Ancho19 VARCHAR(20),
                Largo19 VARCHAR(20),
                Lugar19 VARCHAR(50) NOT NULL,
                FolioReq19 VARCHAR(50),

                Referencia20 TEXT NOT NULL,
                Descripcion20 TEXT NOT NULL,
                Unidad20 TEXT NOT NULL,
                Cantidad20 INTEGER NOT NULL,
                Ancho20 VARCHAR(20),
                Largo20 VARCHAR(20),
                Lugar20 VARCHAR(50) NOT NULL,
                FolioReq20 VARCHAR(50),

                OrdenComp VARCHAR(20),
                FolFactura VARCHAR(20),
                Comentario TEXT )
            ''')
        except:
            print('Error Base ListasDeSalidas')


'''cosa = inevntario()
cosa.Encabezado()'''