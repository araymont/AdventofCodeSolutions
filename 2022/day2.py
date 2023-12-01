# X = A = Rock
# Y = B = Paper
# Z = C = Scissors

def chosen(c):
    if c =="X":
        return 1
    elif c=="Y":
        return 2
    else:
        return 3

def out(opp,you):
    if opp == "A":
        if you=="X":
            return 3
        elif you=="Y":
            return 6
        elif you=="Z":
            return 0
    elif opp == "B":
        if you=="X":
            return 0
        elif you=="Y":
            return 3
        elif you=="Z":
            return 6
    elif opp == "C":
        if you=="X":
            return 6
        elif you=="Y":
            return 0
        elif you=="Z":
            return 3
    print("Shouldn't be here")
    return 0;

arrtemp=[[],[]]
chosenpoints=0
outcomepoints=0
f = open("day2Input.txt", 'r')

with open('day2Input.txt') as f:
    for line in f:
        arrtemp=line.split()
        chosenpoints+=chosen(arrtemp[1])
        outcomepoints+=out(arrtemp[0],arrtemp[1])

print(chosenpoints,outcomepoints,chosenpoints+outcomepoints)
f.close()

