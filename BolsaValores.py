import pandas as pd 
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox, QSystemTrayIcon
from PyQt5.QtGui import QIcon
from requests import get
from bs4 import BeautifulSoup
import re 
from datetime import datetime

class CalcularDiv:

    def Dolar(self):
        try:
            website = "https://www.x-rates.com/table/?from=USD&amount=1"


            llamar = get(website)
            extraer = BeautifulSoup(llamar.text, 'html.parser')

            extraer.find('p')
            extraer.find('div')
            extraer.find(id ='p')

            filtro = extraer.find_all("table", class_="tablesorter ratesTable")

            filtro = str(filtro)

            #print(filtro)
            #print('Final')

            filtro = re.sub(r'<.*?>', lambda g: g.group(0).upper(), filtro)

            filtro = filtro.splitlines()

            #print(filtro)
            #print(type(filtro))

            #print(len(filtro))
            #print(filtro[155] + filtro[156])

            NoDiv = filtro[155]
            NoDiv = NoDiv[-17:-5]

            self.Valor = filtro[156]
            self.Val = [float(self.Val) for self.Val in re.findall(r'-?\d+\.?\d*', self.Valor)]
            #Valor = Valor[ -18:-9] 

            #print(NoDiv + ': ' + Valor)
            return float(self.Val[0])
        except:
            dialogo = QMessageBox()
            dialogo.setText("Se Ha Perdido la Conexion a Internet, Por Favor Intentelo Mas Tarde")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Information)
            dialogo.exec_()
    
    def Euro(self):
        try:
            website = "https://www.x-rates.com/table/?from=EUR&amount=1"


            llamar = get(website)
            extraer = BeautifulSoup(llamar.text, 'html.parser')

            extraer.find('p')
            extraer.find('div')
            extraer.find(id ='p')

            filtro = extraer.find_all("table", class_="tablesorter ratesTable")

            filtro = str(filtro)

            #print(filtro)
            #print('Final')

            filtro = re.sub(r'<.*?>', lambda g: g.group(0).upper(), filtro)

            filtro = filtro.splitlines()

            #print(filtro)
            #print(type(filtro))

            #print(len(filtro))
            #print(filtro[150] + filtro[151])

            NoDiv = filtro[150]
            NoDiv = NoDiv[-17:-5]

            self.Valor = filtro[151]
            self.Val = [float(self.Val) for self.Val in re.findall(r'-?\d+\.?\d*', self.Valor)] 

            #print(NoDiv + ': ' + Valor)
            return float(self.Val[0])
        except:
            dialogo = QMessageBox()
            dialogo.setText("Se Ha Perdido la Conexion a Internet, Por Favor Intentelo Mas Tarde")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Information)
            dialogo.exec_()

    
    def Yuan(self):
        try:
            website = "https://www.x-rates.com/table/?from=CNY&amount=1"


            llamar = get(website)
            extraer = BeautifulSoup(llamar.text, 'html.parser')

            extraer.find('p')
            extraer.find('div')
            extraer.find(id ='p')

            filtro = extraer.find_all("table", class_="tablesorter ratesTable")

            filtro = str(filtro)

            #print(filtro)
            #print('Final')

            filtro = re.sub(r'<.*?>', lambda g: g.group(0).upper(), filtro)

            filtro = filtro.splitlines()

            #print(filtro)
            #print(type(filtro))

            #print(len(filtro))
            #print(filtro[150] + filtro[151])

            NoDiv = filtro[150]
            NoDiv = NoDiv[-17:-5]

            self.Valor = filtro[151]
            self.Val = [float(self.Val) for self.Val in re.findall(r'-?\d+\.?\d*', self.Valor)] 

            #print(NoDiv + ': ' + Valor)
            return float(self.Val[0])
        except:
            dialogo = QMessageBox()
            dialogo.setText("Se Ha Perdido la Conexion a Internet, Por Favor Intentelo Mas Tarde")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Information)
            dialogo.exec_()
    
    def Libra(self):
        try:
            website = "https://www.x-rates.com/table/?from=GBP&amount=1"


            llamar = get(website)
            extraer = BeautifulSoup(llamar.text, 'html.parser')

            extraer.find('p')
            extraer.find('div')
            extraer.find(id ='p')

            filtro = extraer.find_all("table", class_="tablesorter ratesTable")

            filtro = str(filtro)

            #print(filtro)
            #print('Final')

            filtro = re.sub(r'<.*?>', lambda g: g.group(0).upper(), filtro)

            filtro = filtro.splitlines()

            #print(filtro)
            #print(type(filtro))

            #print(len(filtro))
            #print(filtro[155] + filtro[156])

            NoDiv = filtro[150]
            NoDiv = NoDiv[-17:-5]

            self.Valor = filtro[156]
            self.Val = [float(self.Val) for self.Val in re.findall(r'-?\d+\.?\d*', self.Valor)] 

            #print(NoDiv + ': ' + self.Valor)
            return float(self.Val[0])
        except:
            dialogo = QMessageBox()
            dialogo.setText("Se Ha Perdido la Conexion a Internet, Por Favor Intentelo Mas Tarde")
            dialogo.setWindowTitle("DesinGlass Smart Windows")
            dialogo.setWindowIcon(QIcon('DG.png'))
            dialogo.setIcon(QMessageBox.Information)
            dialogo.exec_()
    
'''cosa = CalcularDiv()
print(cosa.Dolar())'''
