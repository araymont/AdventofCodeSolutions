arr=[]
dict={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0,}
locDict={}
hY=0
hX=0

def moveUp():
    return 1
def moveRight():
    return 1
def moveDown():
    return -1
def moveLeft():
    return -1


def move(array,hy,hx):
    y=0
    x=0
    for j in range(0,array[1]):
        if array[0]=="U":
            y+=moveUp()
        elif array[0]=="R":
            x+=moveRight()
        elif array[0]=="D":
            y+=moveDown()
        elif array[0]=="L":
            x+=moveLeft()
        else:
            print("aaaaaaaaaaaaaa")
    if x!=hx:
        return x
    else:
        return y
    

with open('day9Input.txt') as f:
    for line in f:
        arrtemp=[]
        arrtemptemp=[]
        for letter in line:
            arrtemp=line.split()
            count=0
            for j in range(0,len(arrtemp[1])):
                count+=dict[arrtemp[1][j]]*(10**(len(arrtemp[1])-j-1))
            arrtemp[1]=count
        arr.append(arrtemp)

for i in range(0,len(arr)):
    if arr[i][0]=="U" or arr[i][0]=="D":
        hY+=move(arr[i],hY,hX)
    else:
        hX+=move(arr[i],hY,hX)

f.close()