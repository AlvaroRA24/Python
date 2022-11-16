caracter = input("Introduce un único caracter: ")
cont = 0

def check(a):
    if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
        return True
    else:
        return False

print(check(caracter))