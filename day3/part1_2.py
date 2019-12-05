def parserRuta(ruta):
    newRuta=[]
    for i in ruta:
        for j in range(int(i[1:])):
            newRuta.append(i[0])
    return newRuta


def move(dir,actual,toString=False):
    if dir == "R":
        #  print("RIGHT")
        actual[0]=actual[0]+1
    elif dir == "L":
        #  print("LEFT")
        actual[0]=actual[0]-1
    elif dir == "U":
        #  print("UP")
        actual[1]=actual[1]+1
    elif dir == "D":
        #  print("DOWN")
        actual[1]=actual[1]-1
    if toString==True:
        return f":{actual[0]},{actual[1]}:"
    else:
        return actual
def manhatan(point):
    return abs(point[0])+abs(point[1])
from time import process_time 
import re
t1_start = process_time()  

f = open("input.txt", "r")

x,y=[i.strip().split(",") for i in f.readlines()]
#  print(parserRuta(x))
#  print(parserRuta(y))

r1=parserRuta(x)
r2=parserRuta(y)

r1_actual=[0,0]
r2_actual=[0,0]

r1_ruta=[]
r2_ruta=[]
#  print(move(r1[0],r1_actual))
#  print(move(r1[1],r1_actual))
#  print(move(r1[2],r1_actual))

for i in r1:
    r1_ruta.append(move(i,r1_actual).copy())
    #  print(move(i,r1_actual))
    #  print(r1_ruta)

for i in r2:
    r2_ruta.append(move(i,r2_actual).copy())

#  print(len(r1_ruta))
#  print(len(r2_ruta))

#  print(r1_ruta)
#  print(r2_ruta)

res=[]
j=0
k=0
for i in r1_ruta:
    print(j)
    j=j+1
    #  print(f"{i[0]},{i[1]}")    
    if i in r2_ruta:
        res=i
        break
for i in r2_ruta:
    k=k+1
    if res==i:
        break
print(j+k)
#147050
#  print(len(r2_ruta))
#  print(sorted(res))


t1_stop = process_time() 
print("Elapsed time:", t1_stop-t1_start)
