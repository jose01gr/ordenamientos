from random import randint
import pandas as pd
print "messi is gay"
#Abrimos el archivo csv y le asignamos los valores a reservaciones y clientes
reservaciones = pd.read_csv('reservas.csv', sep=',')
clientes = pd.read_csv('clientes.csv', sep = ',')
    
#Introduccion de datos en la base de datos
def nuevosDatos(clientes, reservaciones):
    print()
    print('-------Nuevo cliente-------')
    nombre = input('Ingrese Nombre y apellido: ')
    preferencias = input('Ingrese sus Preferencias Alimentarias: ')
    telefono = int(input('Ingrese Telefono de contacto: '))
    correo = input('Ingrese Correo Electronico: ')
    iden = randint(0,100)
    v1 =[nombre, preferencias, telefono, correo, iden]
    clientes.loc[len(clientes)] = v1
    print()
    
    print('-------Datos de Reservacion-------')
    fechaR = input('Ingrese la Fecha de la reserva (en formato yy-mm-dd): ')
    fechaE = input('Ingrese la Fecha de la entrada (en formato yy-mm-dd): ')
    fechaS = input('Ingrese la Fecha de la salida (en formato yy-mm-dd): ')
    duracion = input("ingrese duracion de la estadia: ")
    tipoH = input('Ingrese el tipo de habitacion (doble, sencilla, suite, presidencial): ')
    habitacion = input('Ingrese la habitacion a elegir (ej: I54): ')
    personas = int(input('Ingrese la cantidad de personas: '))
    precio = input('Ingrese El precio ($): ') + "$"
    pago = input('Ingrese el tipo de pago (debito, credito, efectivo): ')
    notas = input('Ingrese Notas adicionales: ')
    estado = input('Ingrese Estado de la reserva(Reservado o No Reservado): ')
    checkin = input('Ingrese la Fecha y hora del check in (en formato dd-mm-yy hh:mm): ')
    checkout = input('Ingrese la Fecha y hora del check out (en formato dd-mm-yy hh:mm):')
    v2 = [fechaR, fechaE, fechaS, duracion, tipoH, habitacion, personas, precio, pago, notas, estado, checkin, checkout, iden]
    reservaciones.loc[len(reservaciones)]  = v2
    
    clientes.to_csv('clientes.csv', index=False ) #guardamos los datos en un archivo csv 
    reservaciones.to_csv('reservas.csv', index=False ) #guardamos los datos en un archivo csv 
    
def validarInput(mensaje, op):
    print()
    x = int(input(mensaje))
    if x not in op:
        print('\n\tOpción no válida.\n')
        menu(clientes, reservaciones)
    return x
def ordenarCriterio(reservaciones=reservaciones):
        z = validarInput('Orden por fecha de reservacion: 1.   Orden por Fecha de entrada: 2\nOrden por Fecha de salida: 3.  Orden por Habitacion: 4', [1,2,3,4])
        if z == 1:
            result = reservaciones.sort_values(by="Fecha Reserva", ascending=False)
            print(result)
            w = validarInput('desea agregar un criterio mas?.   si: 1.   no: 2', [1,2])
            if w == 1:
              ordenarCriterio()
            if w == 2 :
                menu(clientes, reservaciones)
        if z == 2:
            result = reservaciones.sort_values(by="Fecha Entrada", ascending=False)
            print(result)
            w = validarInput('desea agregar un criterio mas?.   si: 1.   no: 2', [1,2])
            if w == 1:
              ordenarCriterio()
            if w == 2 :
                menu(clientes, reservaciones)
        if z == 3:
            result = reservaciones.sort_values(by="Fecha Salida", ascending=False)
            print(result)
            w = validarInput('desea agregar un criterio mas?.   si: 1.   no: 2', [1,2])
            if w == 1:
              ordenarCriterio()
            if w == 2 :
                menu(clientes, reservaciones)
        if z == 4:
            result = reservaciones.sort_values(by="Habitacion", ascending=False)
            w = validarInput('desea agregar un criterio mas?.   si: 1.   no: 2', [1,2])
            if w == 1:
              ordenarCriterio()
            if w == 2 :
                menu(clientes, reservaciones)
                
def ordenarRe(reservaciones=reservaciones):
        z = validarInput('rango por fecha de reservacion(ascendente): 1.   rango por Fecha de reservacion(descendente): 2\nrango por duracion de estadia(ascendente) 3.  rango duracion de estadia(descendente): 4', [1,2,3,4])
        if z == 1:
            fechaI = input("ingrese una fecha inferior (formato yy-mm-dd): ")
            fechaS = input("ingrese una superior inferior (formato yy-mm-dd): ")
            filtracion = reservaciones[reservaciones["Fecha Reserva"].between(fechaI, fechaS)]
            result = filtracion.sort_values(by="Precio", ascending=True, kind='mergesort')
            print(result)
            
        if z == 2:
            fechaI = input("ingrese una fecha inferior (formato yy-mm-dd): ")
            fechaS = input("ingrese una superior inferior (formato yy-mm-dd): ")
            filtracion = reservaciones[reservaciones["Fecha Reserva"].between(fechaI, fechaS)]
            result = filtracion.sort_values(by="Precio", ascending=False, kind='mergesort')
            print(result)
            
        if z == 3:
            result = reservaciones.sort_values(by="Duracion Estadia", ascending=True, kind='heapsort')
            print(result)
            
        if z == 4:
            result = reservaciones.sort_values(by="Duracion Estadia", ascending=True, kind='heapsort')
            print(result)

        menu(clientes, reservaciones)
        
        
def menu(clientes=clientes, reservaciones=reservaciones):
    print()
    print("Seleccione una opcion: ")
    print()
    x = validarInput("Para ver las reservaciones ingrese 1.    para ingresar un nuevo registro ingrese 2. para elegir ordenar por algun criterio 3: ", [1,2,3])
    if x == 1:
        print(clientes.head())
        print()
        print(reservaciones.head())
        print()
        print(reservaciones.iloc[7:13])
        
        y = validarInput("Si desea volver al menu ingrese 1.   Si desea cerrar el programa presione 2: ", [1,2])
        if y == 1:
            menu(clientes, reservaciones)
        if y == 2:
            print('FIN')
        
    if x == 2:
        nuevosDatos(clientes, reservaciones)
        y = validarInput("Si desea volver al menu ingrese 1.   Si desea cerrar el programa presione 2: ", [1,2])
        if y == 1:
            menu(clientes, reservaciones)
        if y == 2:
            print('FIN')
    if x == 3:
        print()
        y = validarInput('Si desea ordenar multiples criterios ingrese 1.   Si desea ordenar por ascendencia o descendenia ingrese 2:', [1,2])
        if y == 1:
            ordenarCriterio()          
        if y == 2:
            ordenarRe()
            
menu(clientes, reservaciones)
