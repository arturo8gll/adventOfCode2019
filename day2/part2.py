def gas(x1,x2,input):
    input=[int(x) for x in input]
    input[1]=x1
    input[2]=x2

    for i in range(4,len(input)+1,4):
        intcode=input[i-4:i]
        if intcode[0]==1:
            input[intcode[3]]=input[intcode[1]]+input[intcode[2]]
        elif intcode[0]==2:
            input[intcode[3]]=input[intcode[1]]*input[intcode[2]]

    return input[0]


def part2(num):
    f = open("input.txt","r")
    input = f.readlines()[0].strip().split(",")
    cont=0
    valores=[[x,y] for x in range(100) for y in range(100)]
    while len(valores)!=0:
        mitad=int(len(valores)/2)
        y=gas(valores[mitad][0],valores[mitad][1],input.copy())
        if y == num:
            return valores[mitad]
            break
        elif y > num:
            valores=valores[0:mitad]
        elif y < num:
            valores=valores[mitad:len(valores)]
    return false

print(part2(19690720))
