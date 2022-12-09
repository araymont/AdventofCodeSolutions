arr=[]
countl=0
f = open("day8Input.txt", 'r')
maxi=0

def above(array, x, y, ymax):
    count1=0
    for k in range(y+1,ymax):
        if array[x][k] >= array[x][y]:
            return (count1+1)
        else:
            count1+=1
    return count1

def below(array, x, y):
    count2=0
    for k in range(1,y+1):
        if array[x][y-k] >= array[x][y]:
            return (count2+1)
        else:
            count2+=1
    return count2

def right(array,x,y,xmax):
    count3=0
    for k in range(x+1,xmax):
        if array[k][y] >= array[x][y]:
            return (count3+1)
        else:
            count3+=1
    return count3

def left(array,x,y):
    count4=0
    for k in range(1,x+1):
        if array[x-k][y] >= array[x][y]:
            return (count4+1)
        else:
            count4+=1
    return count4


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
        temp= (above(arr,j,i,len(arr[i]))*(below(arr,j,i))*(right(arr,j,i,len(arr)))*(left(arr,j,i)))
        if (temp>maxi):
            maxi=temp
            print("MAX    ",maxi,j,i,arr[j][i])

print(maxi)
# 30373
# 255,1,2
# 6,53,32
# 3,3,549
# 35390


f.close()