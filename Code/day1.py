sum=0
max1=0
f = open("day1Input.txt", 'r')

with open('day1Input.txt') as f:
    for line in f:
        lines=line.rstrip()
        if lines == '':
            if sum>=max1:
                max1=sum
            sum=0
        else:
            sum=sum+int(lines)


print(max1)

f.close()

