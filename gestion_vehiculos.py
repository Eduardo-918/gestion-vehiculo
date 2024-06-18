
from funciones_gestion import   eliminar,filtrarVehiculo,imprimirReporteCSV,modificarVehiculo,eliminarVehiculo,limpiar,printR,printA,seleccionMarca,seleccionTipo,guardar,menu,listarproductos
while True:
    limpiar()
    menu()
    op=input("Ingrese una opcion: ")
    if op=="0":
        printA("Adios")
        break
    elif op=="1":
        printA("═════════════════════")
        printA("  Agregar vehiculo")
        printA("═════════════════════")
        patente=input("Ingrese patente: ").title()
        
        marca=seleccionMarca()
    
        tipo=seleccionTipo()
        precio=int(input("Ingrese precio: "))
        stock=int(input("Ingrese cantidad de stock: "))
        guardar(patente,marca,tipo,precio,stock)

    elif op=="2":
        printA("═════════════════════")
        printA("  Listar vehiculo")
        printA("═════════════════════")
        listarproductos()
    elif op=="3":
        printA("═════════════════════")
        printA("  Eliminar vehiculo")
        printA("═════════════════════")
        patente=input("Ingrese patente de auto: ").title()
        eliminarVehiculo(patente)
    elif op=="4":
        printA("═════════════════════")
        printA("  Modificar producto")
        printA("═════════════════════")
        patente=input("Ingrese patente de vehiculo: ").title()
        eliminar(patente)
        newpatente=input("Ingrese patente: ").title()
        newmarca=seleccionMarca()
        newtipo=seleccionTipo()
        newprecio=int(input("Ingrese precio: "))
        newstock=int(input("Ingrese cantidad de stock: "))
        modificarVehiculo(newmarca,newpatente,newprecio,newstock,newtipo)
    elif op=="5":
        printA("═════════════════════")
        printA("  Filtrar vehiculo")
        printA("═════════════════════")
        marca=input("Ingrese la marca del auto que desea buscar: ").title()
        filtrarVehiculo(marca)
    elif op=="6":
        printA("═════════════════════")
        printA("  Generar reporte")
        printA("═════════════════════")
        nombre=input("Ingrese nombre de reporte: ").title()
        imprimirReporteCSV(nombre)
    else:
        printR("Opcion no valida")