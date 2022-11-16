curso_ano = int(input("ESCRIBE EL AÑO DEL CURSO: "))
nom_uno =input("PRIMER NOMBRE: ")
ano_uno = int(input("PRIMER AÑO: "))

nom_dos =input("SEGUNDO NOMBRE: ")
ano_dos = int(input("SEGUNDO AÑO: "))

nom_tres =input("TERCER NOMBRE: ")
ano_tres = int(input("TERCER AÑO: "))

cumple_uno = curso_ano - ano_uno
cumple_dos = curso_ano - ano_dos
cumple_tres = curso_ano - ano_tres

print(nom_uno + " CUMPLIRA " + str(cumple_uno))
print(nom_dos + " CUMPLIRA " + str(cumple_dos))
print(nom_tres + " CUMPLIRA " + str(cumple_tres))