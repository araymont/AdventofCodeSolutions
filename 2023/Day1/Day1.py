import time
class Day1():
    def main(self):
        numDict={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        f=open("Day1.txt","r")
        first=-1
        last=-1
        total=0
        count=0
        #print(f.readline())
        for x in f:
            #print(x)
            for c in x:
                if(c in numDict):
                    if(first==-1):
                        first=numDict[c]
                    last=numDict[c]
            total+=(first*10) + last
            print(count,": ",total,(first*10)+last,first,last)
            count+=1
            first=-1
            last=-1
        f.close()
print("Begin")
obj=Day1()
obj.main()
print("END")
#time.sleep(5)
