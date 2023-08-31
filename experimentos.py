import datetime
from IngresarMovimientos import *
import os
import subprocess

from datetime import datetime

fecha = datetime.now()
fecha = str(fecha)
fecha = fecha[0: 19]
fecha = fecha.replace("-", "/")
print(fecha)

TipMov = "Ingeso"
Producto = "Producto"
Clave = "xxxxx"
Numero = "Ninguno"
Marca = "Desinglass"
Color = "Ninguno"
Unidad = "Pieza"
Cantidad = "0"
Proveedor = "Interno"
Lugar = "Interno"
Fecha = str(fecha)

agregar = Pagina2
#agregar.AgregarMovimientos(TipMov, Producto, Clave, Numero, Marca, Color, Unidad, Cantidad, Proveedor, Lugar, Fecha, Fecha)

'''TipMov
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
TP.Mov VARCHAR(20) NOT NULL )

Folio TEXT NOT NULL UNIQUE,
Obra TEXT NOT NULL,
Solicita VARCHAR(20) NOT NULL,
Autoriza VARCHAR(20) NOT NULL,
Almacen VARCHAR(20) NOT NULL,
OrdenCompra VARCHAR(20) NOT NULL,
FolioFactura VARCHAR(20) NOT NULL,
Observaciones TEXT,
Type TEXT NOT NULL )'''

#Acompletador

'''lista = [
    (1,2),
    (2,3),
    (3,4),
    (4,5),
    (5,6),
    (6,7),
    (7,8),
    (8,9),
    (9,10),
    (10,11),
    (11,12),
    (12,13),
    (13,14),
    (14,15),
    (15,16),
    (16,17),
    (17,18),
    (18,19),
    (19,20),
    (20,21)
]

num = len(lista)
listaR = []
for i in lista:
    
    listaR.append(i[0])

num2 = len(listaR)

for i2 in range (0, 20-num2):
    listaR.append("")

print(listaR, " Total: " ,len(listaR))'''

#Cilclo for con dos iteradores 

'''z = iter(range(11))
for i,e in enumerate(z, start=0):
    e += 1
    print(i,e)'''

#siclo for cambiante uno si uno no 
'''z = iter(range(11))
e = "no"
for i in z:
    if e == "no":
        print(e)
        e = "si"
    else:
        print(e)
        e = "no"'''

#rutas
'''ruta = "C:" + chr(92)+ "Users"+ chr(92) 
carpetas = os.listdir(ruta)
#print(carpetas)
usuario = ""
conta = 0
for i in carpetas:
    conta += 1
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
                    else:
                        usuario = str(i)
                        #print(i,conta)

print(usuario)
#usuario = subprocess.call('query user')'''

#c = os.path.exists("C:\Users\OFICINA\Desktop\CarpetaCompartir")
#print(c)

'''pregunta = QMessageBox.question(self,"DesinGlass Smart Windows", "¿Esta Seguro de Realizar la Operacion?", QMessageBox.Yes | QMessageBox.No)
if pregunta == QMessageBox.Yes:
    pass
else:
    dialogo2 = QMessageBox()
    dialogo2.setText("Operacion Cancelada")
    dialogo2.setWindowTitle("DesinGlass Smart Windows")
    dialogo2.setIcon(QMessageBox.Warning)
    dialogo2.exec_()'''


Fecha1 = "2022-12-12"
Fecha2 = "2022-12-12"

FCH11 = str(Fecha1)
FCH21 = str(Fecha2)
print(FCH11)
print(FCH21)

Valor1 = str(Fecha1.replace("-","/"))
Valor2 = str(Fecha2.replace("-","/"))

FCH1 = datetime.strptime(Valor1, '%Y/%m/%d')
FCH2 = datetime.strptime(Valor2, '%Y/%m/%d')
print(type(FCH2))
print(FCH2)


