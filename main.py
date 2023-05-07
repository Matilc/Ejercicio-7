import os
from ManejadorViajeros import ManejadorViajero
def menu_opciones():
    print("Menú de opciones:")
    print("1. Comparar cantidad de millas totales")
    print("2. Acumular millas")
    print("3. Canjear millas")
    print("4. Salir")

if __name__=='__main__':
    mv=ManejadorViajero()
    mv.cargarviajeros()
    numaux= int(input('Ingrese número de viajero '))
    i=mv.obtener_viajero(numaux)
    print (i)
    viajeroaux=mv.get_viajero(i)
    opc=None
    while opc!='4':
        os.system('cls')
        menu_opciones()
        opc=input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc=='1':
            millasaux=int(input("Ingrese las millas a comparar:\n"))
            print ('La comparación resultó: ',end="")
            if viajeroaux==millasaux:
                print ("Verdadera")
            else:
                print ("Falsa")
            aux=input("\nIngrese cualquier tecla para continuar\n")
        if opc=='2':
            millasaux=int(input("Ingrese las millas a sumar:\n"))
            print ('Sus millas totales son '+str(millasaux+viajeroaux))
            aux=input("\nIngrese cualquier tecla para continuar\n")
        if opc=='3':
            millasaux=int(input("Ingrese las millas a canjear:\n"))
            print ('Sus millas totales son '+str(millasaux-viajeroaux))
            aux=input("\nIngrese cualquier tecla para continuar\n")
        
    print("Gracias por usar el sistema")