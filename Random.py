import random
n=[1,2,3,4,5,6]
l=['A','B','C','D','E','F']
fin=False
while fin==False:
    if len(l)!=0 or len(n)!=0:
        resultn=random.choice(n)
        resultl=random.choice(l)
        n.remove(resultn)
        l.remove(resultl)
        print("["+str(resultl)+","+str(resultn)+"]")
    else:
        fin=True

#esto es para probar la re subida de este codigo

