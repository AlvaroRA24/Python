def ES_BISIESTO(ano):
    if ano%4 == 0:
        if ano%100 != 0:
            print("ES BISIESTO")
        else:
            print("NO ES BISIESTO")

ano = int(input("ESCRIBE UN AÑO PARA SABER SI ES BISIESTO: "))
ES_BISIESTO(ano)