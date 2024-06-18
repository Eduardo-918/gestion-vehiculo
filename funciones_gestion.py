import msvcrt
import os
import csv
coche=[]
def limpiar():
   print("<<<< Press any key >>>>")
   msvcrt.getch()
   os.system("cls")

def printR(texto):
   print(f"\033[31m{texto}\033[0m")
def printV(texto):
   print(f"\033[32m{texto}\033[0m")
def printA(texto):
   print(f"\033[34m{texto}\033[0m")

def menu():
   printA("╔═══════════════════════════════ ")
   printV("║    Sistema gestion vehiculo   ║")
   printA("╚═══════════════════════════════  ")
   print("1) Agregar vehiculo")
   print("2) Listar vehiculo")
   print("3) Eliminar vehiculo")
   print("4) Modificar vehiculo")
   print("5) Filtrar vehiculo")
   print("6) Generar reporte")
   print("0) Salir")

marca=("Kia","Chevrolet","Audi","Nissan","Otro")
def seleccionMarca():
   for i in range(len(marca)):
      print(f"{i+1}.- {marca[i]} ")
   seleccion=int(input("Seleccione: "))-1
   if seleccion>=0 and seleccion<(len(marca)):
      return marca[seleccion]
   else:
      return None
tipo=("Automovil","Camion","Motocicleta","Autobus")
def seleccionTipo():
   for v in range(len(tipo)):
      print(f"{v+1}.- {tipo[v]} ")
   sel=int(input("Seleccione: "))-1
   if sel>=0 and sel<(len(tipo)):
      return tipo[sel]
   else:
      return None
   
def validarpatente(patente):
    for i in range(len(coche)):
        if coche[i][0]== patente:
            return i #retornando posicion del producto
    return -1 #retornando valor 

def guardar(patente,marca,tipo,precio,stock):
   if validarpatente(patente)==-1:
      if marca!= None:
         if tipo !=None:
            if precio>0:
               if stock>0:
                  coche.append([patente,marca,tipo, precio,stock])
                  printV("Automovil registrado")
               else:
                  printR("No hay stock")   
            else:
               printR("Precio invalido")    
         else:
            printR("Tipo no valido")
      else:
         printR("Marca no valida")
   else:
      printR("Automovil ya registrado")

def listarproductos():
   if len(coche)>0:
     for i in range(len(coche)):
        printA(f"""{i+1}.- Patente: {coche[i][0]}.- Marca: {coche[i][1]}.- Tipo: {coche[i][2]}.-Precio: ${coche[i][3]}.- Stock: {coche[i][3]} """)
   else: 
      printR("No hay vehiculos registrados")

def eliminarVehiculo(patente):
   delco=validarpatente(patente)
   if delco>=0:
     coche.remove(coche[delco])
     printV("Vehiculo eliminado")
     
   else:
      printR("No hay vehiculos registrados")

def modificarVehiculo(patente,marca,tipo,precio,stock):    
     if validarpatente(patente)==-1:
      if marca!= None:
         if tipo !=None:
            if precio>0:
               if stock>0:
                  coche.append([patente,marca,tipo, precio,stock])
                  printV("Automovil modificado")
               else:
                  printR("No hay stock")   
            else:
               printR("Precio invalido")    
         else:
            printR("Tipo no valido")
      else:
         printR("Marca no valida")
     else:
      printR("Automovil ya registrado")

def imprimirReporteCSV(nombreReporte):
   if len(coche)>0:
      with open(f'{nombreReporte}.csv','w',newline='',encoding='utf-8') as a:
         escribir=csv.writer(a,delimiter=",")
         escribir.writerows(coche)
         printV(f"Reporte {nombreReporte}.csv Generado")
   else:
      printR("No hay productos registrados")

def filtrarVehiculo(marca):
   
   if len(coche)>0:
     for i in range(len(coche)):
        if coche[i][1]==marca:
          printA(f"""{i+1}.- Patente: {coche[i][0]}.- Marca: {coche[i][1]}.- Tipo: {coche[i][2]}.-Precio: ${coche[i][3]}.- Stock: {coche[i][3]} """)
   else:
         
    printR("No hay coches registrados")
def eliminar(patente):
   delco=validarpatente(patente)
   if delco>=0:
     coche.remove(coche[delco])
     
   else:
      printR("No hay vehiculos registrados")