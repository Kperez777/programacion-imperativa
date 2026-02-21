#saldo inicial 
saldo=1000
opcion = 0
while opcion != 4:
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción: "))

    if opcion ==1:
        print("su saldo actual es ",saldo)

    elif opcion ==2:
        deposito=float(input("ingrese la cantidad que va a depositar: "))
        if deposito>0:
            saldo=deposito+saldo
            print("deposito exitoso")
        else:
            print("cantidad invalida")
            
    elif opcion ==3:
        retiro=float(input("ingrese la cantidad que va a retirar: "))
        if retiro>0 and retiro<=saldo:
            saldo=retiro-saldo
            print("su retiro ha sido exitoso")
        else:
            print("cantidad insuficientes")

    elif opcion ==4:
        print("gracias por usar el cajero. ")


    else:
        print("opcion no valida")
        



    