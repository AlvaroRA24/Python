def sum(a):
    cont=0
    for i in a:
        cont+=i
    return cont

print(sum([1,2,3,4]))

def mult(a):
    cont=1
    for i in a:
        cont=cont*i
    return cont

print(mult([1,2,3,4]))