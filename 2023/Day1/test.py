def proparpart2(filename):
    conv={
        "1":"1",
        "2":"2",
        "3":"3",
        "4":"4",
        "5":"5",
        "6":"6",
        "7":"7",
        "8":"8",
        "9":"9",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    with open(filename) as f:
        dataset=f.readlines()
    
    output=0
    sumofparts=0
    count=0
    for line in dataset:
        inputrange=range(0,len(line))
        leftpart=processPart2(line,inputrange,conv)
        inputrange=reversed(inputrange)
        rightpart=processPart2(line,inputrange,conv)
        sumofparts+=int(leftpart+rightpart)
        count+=1
        print(count,sumofparts)
    print("Part 2?", sumofparts)

def processPart2(line,inputrange,conv):
    for x in inputrange:
        for c in conv.keys():
            if(line[x:x+len(c)]==c):
                return conv[c]
            
proparpart2("Day1.txt")