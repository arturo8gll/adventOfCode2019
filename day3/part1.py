def med(x):
    l,r,d,u=0,0,0,0

    for i in x:
        dir= i[0]
        val=int(i[1:])
        if dir == "R":
            #  print("RIGHT",val)
            r=r+val
        elif dir == "L":
            #  print("LEFT",val)
            l=l+val
        elif dir == "U":
            #  print("UP",val)
            u=u+val
        elif dir == "D":
            #  print("DOWN",val)
            d=d+val
    return l if l>r else r,d if d>u else u
def sum_ruta(x):
    l,r,d,u=0,0,0,0

    for i in x:
        dir= i[0]
        val=int(i[1:])
        if dir == "R":
            #  print("RIGHT",val)
            r=r+val
        elif dir == "L":
            #  print("LEFT",val)
            l=l+val
        elif dir == "U":
            #  print("UP",val)
            u=u+val
        elif dir == "D":
            #  print("DOWN",val)
            d=d+val
    return l+r+u+d
def sum_arr(x):
    cont=0
    for i in x:
        cont=cont+sum(i)
    return cont
def llenarRuta(ruta,arr,x,y):
    actual=[y,x].copy()
    for i in ruta:
        dir= i[0]
        val=int(i[1:])
        if dir == "R":
            #  print("RIGHT")
            for i in range(val):
                arr[actual[0]][actual[1]]=arr[actual[0]][actual[1]]+1
                actual[1]=actual[1]+1
                #  print(actual)
        elif dir == "L":
            #  print("LEFT")
            for i in range(val):
                arr[actual[0]][actual[1]]=arr[actual[0]][actual[1]]+1
                actual[1]=actual[1]-1
                #  print(actual)
        elif dir == "U":
            #  print("UP")
            for i in range(val):
                arr[actual[0]][actual[1]]=arr[actual[0]][actual[1]]+1
                actual[0]=actual[0]-1
                #  print(actual)
        elif dir == "D":
            #  print("DOWN")
            for i in range(val):
                arr[actual[0]][actual[1]]=arr[actual[0]][actual[1]]+1
                actual[0]=actual[0]+1
                #  print(actual)

    return actual

def print_mat(mat):
    for i in mat:
        print(i)
def manhatan(origen,final):
    return abs(origen[0]-final[0])+abs(origen[1]-final[1])

f = open("input.txt", "r")

x,y=[i.strip().split(",") for i in f.readlines()]


x1,x2=med(x),med(y)

#  print(x1,x2)
x0=x1[0] if x1[0]>x2[0] else x2[0]
y0=x1[1] if x1[1]>x2[1] else x2[1]

print(y0,x0)
#  arr = [[0 for i in range((x0*2)+2)] for j in range((y0*2)+2)]
#  print(len(arr),len(arr[0]))
#  print("ruta 1",x0,y0)
#  llenarRuta(x,arr,x0,y0)
#  print("ruta 2",x0,y0)
#  llenarRuta(y,arr,x0,y0)

#  print(sum_ruta(x),sum_ruta(y))

#print(sum_arr(arr))

#  cont=[]
#  for i in range(len(arr)):
    #  for j in range(len(arr[i])):
        #  if arr[i][j]>1:
            #  cont.append(i)
            #  break
#  print("cruces",cont)
#  print_mat(arr)
#  man_res=[]
#  for i in cont:
    #  for j in range(len(arr[i])):
        #  if arr[i][j]==2:
            #  man_res.append(manhatan([x0,y0],[j,i]))

#  print(sorted(man_res))
