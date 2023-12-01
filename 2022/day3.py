count=0
arrtemp=[]
arrtemp2=[]
sum=0
print(";;;")
dict={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"A":27,"B":28,"C":29,"D":30,"E":31,"F":32,"G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,"O":41,"P":42,"Q":43,"R":44,"S":45,"T":46,"U":47,"V":48,"W":49,"X":50,"Y":51,"Z":52}
f = open("temp.txt", 'r')

print("lll")
with open('temp.txt') as f:
    for line in f:
        arrtemp.append(line[:(line.index("\n"))])
for i in range(0,len(arrtemp)):
    tempstr=arrtemp[i]
    print(tempstr[:len(tempstr)//2])
    print(tempstr[len(tempstr)//2:])
    for j in range(0,len(tempstr)//2):
        for k in range(len(tempstr)//2,len(tempstr)):
            if tempstr[j]==tempstr[k]:
                print(tempstr[j]," ",tempstr[k])
                sum+=dict[tempstr[j]]
    
print("l")
print(arrtemp)
print(arrtemp2)
print(sum)








f.close()