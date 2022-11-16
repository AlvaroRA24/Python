def max ():
    a = int(input("Proporciona el primer numero : "))
    b = int(input("Proporciona el segundo numero : "))
    if a > b:
        print("El numero mayor es:",a)
    elif a < b:
        print("El numero mayor es:",b)
    else:
        print ("Son iguales")
max()