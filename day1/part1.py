from math import floor
def fuel(x):
	return floor(x/3)-2

f= open("input.txt","r")
input = f.readlines()
cont=0
for i in input:
    cont=cont+fuel(int(i))
print(cont)
