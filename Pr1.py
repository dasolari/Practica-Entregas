print("Elige un número")
p=int(input())
print("Si el numero fue par, imprimire todos los numeros desde el 1 al que elegiste. Si fue impar, lo multiplicare por 2")
if p%2==1:
    z=p*2
    print(int(z))
elif p%2==0:
    i=1
    while i<=p:
        print(int(i))
        i+=1
else:
    print("No se que paso")
