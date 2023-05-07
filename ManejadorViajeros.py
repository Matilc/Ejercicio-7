from ViajeroFrecuente import ViajeroF
import csv
class ManejadorViajero:
    __listaviajero=[]

    def __init__(self):
        self.__listaviajero=[]

    def get_viajero (self, i):
        return self.__listaviajero[i]

    def cargarviajeros (self):
        archivo=open("Viajeros.csv")
        reader= csv.reader(archivo,delimiter=';')
        for fila in reader:
            viajero= ViajeroF(int(fila[0]), fila[1].strip(),fila[2].strip(),fila[3].strip(),int(fila[4]))
            self.__listaviajero.append(viajero)
    
    def obtener_viajero(self,numaux):
        i=0
        while self.__listaviajero[i].compararnumviajero(numaux) and i<len(self.__listaviajero):
            i+=1
        return i-1