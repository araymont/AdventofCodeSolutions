class day3():
    def removeUnconnected(self,line):
        count=0
        total=0
        for elm in line:
            if(elm!='.' and elm!='#'):
                if(elm[1]!=15):
                    line[count]='.'
                else:
                    line[count]=elm[0]
                    total+=int(line[count])
            count+=1
        return line,total
    def removeall(self,line,index):
        if(line[index]!='.' and line[index]!='#'):
            print(line[index])
            val=line[index][1]
            if(val==15):
                return line
            value=line[index][0]
            for i in range(index-val,min(index+(len(value)-1),len(line)-1)):
                line[i]='.'
            line[index]=[value,15]
        return line
    def extract(self,aline,line,bline):
        if(line[0]=='#'):
            aline=self.removeall(aline,0)
            aline=self.removeall(aline,1)
            line=self.removeall(line,1)
            bline=self.removeall(bline,0)
            bline=self.removeall(bline,1)
        for i in range(1,len(line)-1):
            if(line[i]=='#'):
                aline=self.removeall(aline,i-1)
                aline=self.removeall(aline,i)
                aline=self.removeall(aline,i+1)
                line=self.removeall(line,i-1)
                line=self.removeall(line,i+1)
                bline=self.removeall(bline,i-1)
                bline=self.removeall(bline,i)
                bline=self.removeall(bline,i+1)
        if(line[-1]=='#'):
            aline=self.removeall(aline,len(line)-1)
            aline=self.removeall(aline,len(line)-2)
            line=self.removeall(line,len(line)-2)
            bline=self.removeall(bline,len(line)-1)
            bline=self.removeall(bline,len(line)-2)
        return aline,line,bline
    def preproc(self,line):
        numlist=['0','1','2','3','4','5','6','7','8','9']
        temp=[]
        count=0
        run=0
        for sec in line:
            if(sec in numlist):
                temp.append([0,run])
                temp[count-run][0]=str((int(temp[count-run][0])*10)+int(sec))
                for j in range(count-(run),count+1):
                    temp[j][0]=temp[count-run][0]
                run+=1
                #temp.append(sec)
            elif(sec=='*'):
                run=0
                temp.append('#')
            elif(sec!='\n'):
                run=0
                temp.append('.')
            count+=1
        return temp

    def main(self,filename):
        arr=[]
        total=0
        f=open(filename,"r")
        for line in f:
            line=self.preproc(line)
            arr.append(line)
            print(line)
        print(" \n\n\n")
        t=['.' for elm in arr[0]]
        empt=[]
        empt,arr[0],arr[1] = self.extract(t,arr[0],arr[1])
        for i in range(1,len(arr)-1):
            arr[i-1],arr[i],arr[i+1]=self.extract(arr[i-1],arr[i],arr[i+1])
        arr[-2],arr[-1],empt = self.extract(arr[-2],arr[-1],t)
        for line in arr:
            ttotal=0
            line,ttotal=self.removeUnconnected(line)
            total+=ttotal
            print(line)
        print(total)

        

obj=day3()
obj.main("Day3test.txt")
