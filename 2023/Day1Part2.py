import time
class Day1():
    def preproc(self,string):
        tstring=string
        if("zero" in tstring):
            tstring=tstring.replace('zero','0')
        if("one" in tstring):
            tstring=tstring.replace('one','1')
        if("two" in tstring):
            tstring=tstring.replace('two','2')
        if("three" in tstring):
            tstring=tstring.replace('three','3')
        if("four" in tstring):
            tstring=tstring.replace('four','4')
        if("five" in tstring):
            tstring=tstring.replace('five','5')
        if("six" in tstring):
            tstring=tstring.replace('six','6')
        if("seven" in tstring):
            tstring=tstring.replace('seven','7')
        if("eight" in tstring):
            tstring=tstring.replace('eight','8')
        if("nine" in tstring):
            tstring=tstring.replace('nine','9')
        return tstring

    def main(self):
        numDict={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

        f=open("Day1part2Test.txt","r")
        first=-1
        last=-1
        total=0
        count=0
        ind=0
        #print(f.readline())
        
        for x in f:
            print(x)
            x=self.preproc(x)
            #print(x)
            for c in x:
                if(c in numDict):
                    if(first==-1):
                        first=numDict[c]
                    last=numDict[c]
            total+=(first*10) + last
            print(count,": ",total,(first*10)+last,first,last, x)
            count+=1
            first=-1
            last=-1
        f.close()
print("Begin")
obj=Day1()
obj.main()
print("END")
#time.sleep(5)

