import msvcrt
import csv
import os

# coleccion para almacenar vehiculos
coche=[]
#tupla
marca=("KIA", "CHEVROLET", "AUDI","NISSAN", "OTRO")
tipo=( "Automóvil", "Camión", "Autobús","motocicleta")
#funciones de diseño
def limpiar():
    print("<<<< Press any key >>>>")
    os.system("cls")
    msvcrt.getch()

def printR(texto):
    print(f"\033[31m{texto}\033[0m")

def printV(texto):
    print(f"\033[32m{texto}\033[0m")

def printA(texto):
    print(f"\033[34m{texto}\033[0m")

def menu():
    printA("═════════════════════════════")
    printA("  Sistema gestion vehiculo")
    printA("═════════════════════════════")
    print(" 1) Agregar vehiculo")
    print(" 2) Listar vehiculo")
    print(" 3) Eliminar vehiculo")
    print(" 4) Modificar vehiculo")
    print(" 5) Filtrar vehiculo")
    print(" 6) generar reporte")
    print(" 0) Salir")

def seleccionMarca():
    print("Marcas disponibles")
    for i in range(len(marca)):
        printA(f"{i+1} .- {marca[i]}")
    seleccion=int(input("Seleccione: "))-1
    if seleccion>=0 and seleccion< len(marca):
        return marca[seleccion]
    else: 
        return None
def seleccionTipo():
    print("Marcas disponibles")
    for i in range(len(tipo)):
        printA(f"{i+1} .- {tipo[i]}")
    seleccion=int(input("Seleccione: "))-1
    if seleccion>=0 and seleccion< len(tipo):
        return tipo[seleccion]
    else: 
        return None

##########Funciones CRUD

#guardar
def validarPatente(patente):
    for i in range(len(coche)):
        if coche[i][0]==patente:
            return i #retorna si encontro la patente
        
    return -1   
def Agregar(patente,marca,tipo,precio,stock):
   if validarPatente(patente)==-1:
     if marca!=None:
       if tipo != None:
           if precio>0:
             if stock>=0:
                    coche.append([patente,marca,tipo,precio,stock])
                    printV("Vehiculo registrado")
             else:
                   printR("Stock no valido")
           else:
               printR("Precio debe ser mayor a 0")
       else:
           printR("Tipo no valido")
     else:
         printR("Marca no valida")
   else:
       printR("Patente repetida")
    
def Listar():
    if len(coche)>0:
     for i in range(len(coche)):
         print(f"{i+1} .- Patente: {coche[i][0]}.- Marca: {coche[i][1]}.- Tipo: {coche[i][2]}.- Precio: {coche[i][3]}.- Stock: {coche[i][4]} " )
    else:
     printR("No hay vehiculos registrados")

def EliminarVehiculo(patente):
    pos=validarPatente(patente)
    if pos>=0:
        coche.pop(pos)
        printV("Vehiculo eliminado")
    else:
        printR("Patente no existe")

def ModificarVehiculo(patente,marca,tipo,precio,stock):
    pos=validarPatente(patente)
    if pos>=0:
        if marca!=None:
         if tipo != None:
           if precio>0:
               if stock>=0:
                    coche.pop(pos)
                    coche.append([patente,marca,tipo,precio,stock])
                    printV("Vehiculo registrado")
               else:
                   printR("Stock no valido")
           else:
               printR("Precio debe ser mayor a 0")
         else:
           printR("Tipo no valido")
        else:
          printR("Marca no valida")
    else:
        print("Patente repetida")    

def filtrar(marca):
    if len(coche)>0:
        for i in range(len(coche)):
            if coche[i][1]== marca:
                print(f"{i+1} .- Patente: {coche[i][0]}.- Marca: {coche[i][1]}.- Tipo: {coche[i][2]}.- Precio: {coche[i][3]}.- Stock: {coche[i][4]} " )
    else:
        printR("No hay vehiculos")   


def generarReporte():
    if len(coche)>0:
        with open('registro_vehiculo.csv','w',newline='',encoding='utf-8') as a:
            escribir=csv.writer(a,delimiter=",")
            coche.insert(0,["PATENTE","MARCA","TIPO","PRECIO","STOCK"])
            escribir.writerows(coche)
            coche.pop(0)
            printV("Reporte generado")
    else:
        printR("No hay coches")

#Listar()
#Agregar("LLDD","KIA","AUTOMOVIL",5000,1)

#filtrar("KIA")