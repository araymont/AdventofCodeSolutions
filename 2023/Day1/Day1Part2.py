import time
class Day1():
    def isZero(self,string,index):
        return False,string
        if(index+3>=len(string)):
            return string
        elif(string[index+1]=='e'and string[index+2]=='r'and string[index+3]=='o'):
            string=string.replace('zero','0',1)
        return string
    def isOne(self,string,index):
        if(index+2>=len(string)):
            return False,string
        elif(string[index+1]=='n'and string[index+2]=='e'):
            string=string.replace('one','1ne',1)
            return True,string
        return False,string
    def isTwo(self,string,index):
        if(index+2>=len(string)):
            return False,string
        elif(string[index+1]=='w'and string[index+2]=='o'):
            string=string.replace('two','2wo',1)
            return True,string
        return False,string
    def isThree(self,string,index):
        if(index+4>=len(string)):
            return False,string
        elif(string[index+1]=='h'and string[index+2]=='r' and string[index+3]=='e' and string[index+4]=='e'):
            string=string.replace('three','3hree',1)
            return True,string
        return False,string
    def isFour(self,string,index):
        if(index+3>=len(string)):
            return False,string
        elif(string[index+1]=='o'and string[index+2]=='u' and string[index+3]=='r'):
            string=string.replace('four','4our',1)
            return True,string
        return False,string
    def isFive(self,string,index):
        if(index+3>=len(string)):
            return False,string
        elif(string[index+1]=='i'and string[index+2]=='v' and string[index+3]=='e'):
            string=string.replace('five','5ive',1)
            return True,string
        return False,string
    def isSix(self,string,index):
        if(index+2>=len(string)):
            return False,string
        elif(string[index+1]=='i'and string[index+2]=='x'):
            string=string.replace('six','6ix',1)
            return True,string
        return False,string
    def isSeven(self,string,index):
        if(index+4>=len(string)):
            return False,string
        elif(string[index+1]=='e'and string[index+2]=='v' and string[index+3]=='e' and string[index+4]=='n'):
            string=string.replace('seven','7even',1)
            return True,string
        return False,string
    def isEight(self,string,index):
        if(index+4>=len(string)):
            return False,string
        elif(string[index+1]=='i'and string[index+2]=='g' and string[index+3]=='h' and string[index+4]=='t'):
            string=string.replace('eight','8ight',1)
            return True,string
        return False,string
    def isNine(self,string,index):
        if(index+3>=len(string)):
            return False,string
        elif(string[index+1]=='i'and string[index+2]=='n' and string[index+3]=='e'):
            string=string.replace('nine','9ine',1)
            return True,string
        return False,string
    def preproc(self,string):
        numDict={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        tstring=string
        i=0
        found=False
        while(i<len(tstring)):
            if(tstring[i]in numDict):
                found=True
            elif(tstring[i]=='z'):
                found,tstring=self.isZero(tstring,i)
            elif(tstring[i]=='o'):
                found,tstring=self.isOne(tstring,i)
            elif(tstring[i]=='t'):
                found,tstring=self.isTwo(tstring,i)
                found,tstring=self.isThree(tstring,i)
            elif(tstring[i]=='f'):
                found,tstring=self.isFour(tstring,i)
                found,tstring=self.isFive(tstring,i)
            elif(tstring[i]=='s'):
                found,tstring=self.isSix(tstring,i)
                found,tstring=self.isSeven(tstring,i)
            elif(tstring[i]=='e'):
                found,tstring=self.isEight(tstring,i)
            elif(tstring[i]=='n'):
                found,tstring=self.isNine(tstring,i)
            i+=1
        
        # i=len(tstring)-1
        # found=False
        # while(i>=0 and found==False):
        #     if(tstring[i]in numDict):
        #         found=True
        #     elif(tstring[i]=='z'):
        #         found,tstring=self.isZero(tstring,i)
        #     elif(tstring[i]=='o'):
        #         found,tstring=self.isOne(tstring,i)
        #     elif(tstring[i]=='t'):
        #         found,tstring=self.isTwo(tstring,i)
        #         found,tstring=self.isThree(tstring,i)
        #     elif(tstring[i]=='f'):
        #         found,tstring=self.isFour(tstring,i)
        #         found,tstring=self.isFive(tstring,i)
        #     elif(tstring[i]=='s'):
        #         found,tstring=self.isSix(tstring,i)
        #         found,tstring=self.isSeven(tstring,i)
        #     elif(tstring[i]=='e'):
        #         found,tstring=self.isEight(tstring,i)
        #     elif(tstring[i]=='n'):
        #         found,tstring=self.isNine(tstring,i)
        #     i-=1
        return tstring

    def main(self):
        numDict={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

        f=open("Day1.txt","r")
        first=-1
        last=-1
        total=0
        count=0
        ind=0
        #print(f.readline())
        
        for x in f:
            #print(x)
            x=self.preproc(x)
            #print(x)
            for c in x:
                if(c in numDict):
                    if(first==-1):
                        first=numDict[c]
                    last=numDict[c]
            total+=(first*10) + last
            #print(count,": ",total,(first*10)+last,first,last, x)
            print(total,count,first,last)
            count+=1
            first=-1
            last=-1
        f.close()
        print(total)
print("Begin")
obj=Day1()
obj.main()
print("END")
print("53885 is too high")
#time.sleep(5)

