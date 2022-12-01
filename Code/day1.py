
f = open("day1Input.txt", 'r')

with open('day1Input.txt') as f:
    lines = [line.rstrip() for line in f]
print(lines)

f.close()

