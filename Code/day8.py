arr=[]
countl=0
f = open("day8Input.txt", 'r')

def above(array, x, y, ymax):
    for k in range(y+1,ymax):
        if array[x][k] >= array[x][y]:
            return False
    return True

def below(array, x, y):
    for k in range(0,y):
        if array[x][k] >= array[x][y]:
            return False
    return True

def right(array,x,y,xmax):
    for k in range(x+1,xmax):
        if array[k][y] >= array[x][y]:
            return False
    return True

def left(array,x,y):
    for k in range(0,x):
        if array[k][y] >= array[x][y]:
            return False
    return True


with open('day8Input.txt') as f:
    for line in f:
        arrtemp=[]
        for letter in line:
            if letter == "\n":
                continue
            else:
                arrtemp.append(letter)
        arr.append(arrtemp)


for i in range(0,len(arr)):
    for j in range(0,len(arr[i])):
        if ((above(arr,j,i,len(arr[i])))or(below(arr,j,i))or(right(arr,j,i,len(arr)))or(left(arr,j,i))):
            countl+=1

# 30373
# 255,1,2
# 6,53,32
# 3,3,549
# 35390
print(countl)


f.close()