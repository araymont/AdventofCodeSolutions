class day3():
    def final(self,array):
        total=0
        for i in range(0,len(array)):
            for j in range(0,len(array[i])):
                if(array[i][j]!='.'):
                    total+=array[i][j]
        return total
    def calc(self,aline,line,bline):
        no=['.','#']
        count=0
        tot=1
        if(line[0]=='#'):
            if(aline[0]not in no):
                count+=1
                tot=tot*aline[0]
            aline[0]='.'
            if(aline[1]not in no):
                count+=1
                tot=tot*aline[1]
            aline[1]='.'
            if(line[1]not in no):
                count+=1
                tot=tot*line[1]
            line[1]='.'
            if(bline[0]not in no):
                count+=1
                tot=tot*bline[0]
            bline[0]='.'
            if(bline[1]not in no):
                count+=1
                tot=tot*bline[1]
            bline[1]='.'
            if(count==2):
                line[0]=tot
            else:
                line[0]='.'
            
        for i in range(1,len(line)-1):
            tot=1
            count=0
            if(line[i]=='#'):
                print(line[i-1])
                if(aline[i-1]not in no):
                    count+=1
                    tot=tot*int(aline[i-1])
                aline[i-1]='.'
                if(aline[i]not in no):
                    count+=1
                    tot=tot*aline[i]
                aline[i]='.'
                if(aline[i+1]not in no):
                    count+=1
                    tot=tot*aline[i+1]
                aline[i+1]='.'
                if(line[i-1]not in no):
                    count+=1
                    tot=tot*line[i-1]
                    print("hi",line[i-1])
                line[i-1]='.'
                if(line[i+1]not in no):
                    count+=1
                    tot=tot*line[i+1]
                line[i+1]='.'
                if(bline[i-1]not in no):
                    count+=1
                    tot=tot*bline[i-1]
                bline[i-1]='.'
                if(bline[i]not in no):
                    count+=1
                    tot=tot*bline[i]
                bline[i]='.'
                if(bline[i+1]not in no):
                    count+=1
                    tot=tot*bline[i+1]
                bline[i+1]='.'
                if(count==2):
                    line[i]=tot
                else:
                    line[i]='.'
        count=0
        tot=1
        if(line[-1]=='#'):
            if(bline[-2]not in no):
                count+=1
                tot=tot*bline[-2]
            bline[-2]='.'
            if(bline[-1]not in no):
                count+=1
                tot=tot*bline[1]
            bline[1]='.'
            if(line[-2]not in no):
                count+=1
                tot=tot*line[-2]
            line[-2]='.'
            if(aline[-2]not in no):
                count+=1
                tot=tot*aline[-2]
            aline[-2]='.'
            if(aline[-1]not in no):
                count+=1
                tot=tot*aline[1]
            aline[-1]='.'
            if(count==2):
                line[-1]=tot
            else:
                line[-1]='.'
        return aline,line,bline
            
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
            for i in range(index-val,min(index+(len(value)-val),len(line)-1)):
                line[i]='.'
            line[index]=[int(value),15]
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
        t=['.' for elm in arr[0]]
        empt=[]
        empt,arr[0],arr[1] = self.extract(t,arr[0],arr[1])
        for i in range(1,len(arr)-1):
            empt=[]
            arr[i-1],arr[i],arr[i+1]=self.extract(arr[i-1],arr[i],arr[i+1])
        empt=[]
        arr[-2],arr[-1],empt = self.extract(arr[-2],arr[-1],t)

        

        for line in arr:
            ttotal=0
            line,ttotal=self.removeUnconnected(line)
            total+=ttotal

        empt,arr[0],arr[1] = self.calc(t,arr[0],arr[1])
        for i in range(1,len(arr)-1):
            arr[i-1],arr[i],arr[i+1]=self.calc(arr[i-1],arr[i],arr[i+1])
        arr[-2],arr[-1],empt = self.calc(arr[-2],arr[-1],t)
        #total=0
        print(" \n")
        
        for line in arr:
            print(line)
        print(self.final(arr))
        #print(total)

        

obj=day3()
obj.main("Day3.txt")
