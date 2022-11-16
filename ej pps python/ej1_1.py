nota = int(input("Introduce la nota: "))

if nota <= 10 and nota >= 0:
    if nota >= 9:
        letra = "A"
    else:
        if nota >= 8:
            letra = "B"
        else:
            if nota >= 7:
                letra = "C"
            else:
                if nota >= 6:
                    letra = "D"
                else:
                    if nota >= 0:
                        letra = "F"
    print("Nota:",letra)

else:
    print("Valor desconocido")