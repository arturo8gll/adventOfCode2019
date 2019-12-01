from math import floor
import numpy as np
def fuel(x):
	return floor(x/3)-2

f= open("input.txt","r")
input = f.readlines()
arr=[]
for i in input:
    cont=0
    aux=int(i)
    while True:
        aux=fuel(aux)
        if aux<=0:
            break
        cont=cont+aux
    arr.append(cont)
print(np.sum(arr))


