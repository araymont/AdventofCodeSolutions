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
            return (chosen("Z")+0)
        elif you=="Y":
            return (chosen("X")+3)
        elif you=="Z":
            return (chosen("Y")+6)
    elif opp == "B":
        if you=="X":
            return (chosen("X")+0)
        elif you=="Y":
            return (chosen("Y")+3)
        elif you=="Z":
            return (chosen("Z")+6)
    elif opp == "C":
        if you=="X":
            return (chosen("Y")+0)
        elif you=="Y":
            return (chosen("Z")+3)
        elif you=="Z":
            return (chosen("X")+6)
    print("Shouldn't be here")
    return 0;

arrtemp=[[],[]]
chosenpoints=0
outcomepoints=0
f = open("day2Input.txt", 'r')

with open('day2Input.txt') as f:
    for line in f:
        arrtemp=line.split()
        outcomepoints+=out(arrtemp[0],arrtemp[1])

print(chosenpoints,outcomepoints,chosenpoints+outcomepoints)
f.close()

