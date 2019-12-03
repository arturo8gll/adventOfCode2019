f = open("input.txt","r")
input = f.readlines()[0].strip().split(",")
input=[int(x) for x in input]
comp = input.copy()
input[1]=12
input[2]=2

for i in range(4,len(input)+1,4):
    intcode=input[i-4:i]
    if intcode[0]==1:
        input[intcode[3]]=input[intcode[1]]+input[intcode[2]]
    elif intcode[0]==2:
        input[intcode[3]]=input[intcode[1]]*input[intcode[2]]


for i in range(4,len(input),4):
    print(i,input[i-4:i])
print(len(input))
