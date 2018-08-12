lista=[1,2,3,4,5,6,7,8,9]
lista.append(10)
lista.insert(7,"hola")
print(lista)
a=lista.pop(7)
print(lista)
print(a)

lista2=['a','b','c','d','e','f']
for p in lista2:
    if p == 'f':
        lista2.pop(len(lista2)-1)
    else:
        print(p)
print(lista2)
lista2.append('fffff')
print(lista2)
