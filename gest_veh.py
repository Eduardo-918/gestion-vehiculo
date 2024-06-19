from fun_gest import seleccionTipo,seleccionMarca,limpiar,Agregar,EliminarVehiculo,Listar,ModificarVehiculo,generarReporte,menu,filtrar,generarReporte,printR,printA,printV
while True:
    limpiar()
    menu()
    op=input("Seleccione: ")
    if op=="0":
        break
    elif op=="1":
     printA("═════════════════════════════")
     printA("     Agregar vehiculo")
     printA("═════════════════════════════")
     patente=input("Ingrese patente: ").upper()
     marca=seleccionMarca()
     tipo=seleccionTipo()
     precio=int(input("Ingrese precio: "))
     stock=int(input("Ingrese stock: "))
     Agregar(patente,marca,tipo,precio,stock)
    elif op=="2":
     printA("═════════════════════════════")
     printA("     Listar vehiculo")
     printA("═════════════════════════════")
     Listar()
    elif op=="3":
     printA("═════════════════════════════")
     printA("     Eliminar vehiculo")
     printA("═════════════════════════════")
     patente=input("Ingrese patente: ").upper()
     EliminarVehiculo(patente)
    elif op=="4":
     printA("═════════════════════════════")
     printA("  Modificar vehiculo")
     printA("═════════════════════════════")
     patente=input("Ingrese patente: ").upper()
     marca=seleccionMarca()
     tipo=seleccionTipo()
     precio=int(input("Ingrese precio: "))
     stock=int(input("Ingrese stock: "))
     Agregar(patente,marca,tipo,precio,stock)
    elif op=="5":
     printA("═════════════════════════════")
     printA(" Filtrar vehiculo")
     printA("═════════════════════════════")
     marca=seleccionMarca()
     filtrar(marca)
    elif op=="6":
     printA("═════════════════════════════")
     printA(" Generar reporte")
     printA("═════════════════════════════")
     generarReporte()
    else:
      printR("Opcion no valida")