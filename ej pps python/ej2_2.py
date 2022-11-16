def max_de_tres():
    a = int(input("Proporciona el primer numero : "))
    b = int(input("Proporciona el segundo numero : "))
    c = int(input("Proporciona el tercer numero : "))

    if a != b and a != c and b != c:
        if a > b:
            if a > c:
                print("El numero mayor es:",a)
        if b > a:
            if b > c:
                print("El numero mayor es:",b)
        if c > a:
            if c > b:
                print("El numero mayor es:",c)
    else:
        print ("Son iguales")
max_de_tres()