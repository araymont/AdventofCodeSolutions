sum=0
max1=0
max2=0
max3=0
f = open("day1Input.txt", 'r')

with open('day1Input.txt') as f:
    for line in f:
        lines=line.rstrip()
        if lines == '':
            if sum>=max1:
                max3=max2
                max2=max1
                max1=sum
            elif sum>=max2:
                max3=max2
                max2=sum
            elif sum>=max3:
                max3=sum
            sum=0
        else:
            sum=sum+int(lines)

temp=max1+max2+max3
print(temp)
print(max1+max2+max3)
print(max1,max2,max3)

f.close()

