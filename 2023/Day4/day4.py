class Day4():
    def scorecard(self,line):
        count=-1
        res=line[1]
        for elm in line[0]:
            if(elm in res):
                count+=1
        return count
    def preproc(self,line):
        line=line.split(':')
        line=line[1][1:]
        #print(line)
        line=line.split('|')
        line[0]=line[0].split(' ')
        line[1]=line[1].split(' ')
        for i in range(0,len(line)):
            length=len(line[i])
            for j in range(0,length):
                if(j>=length):
                    continue
                else:
                    #print(j)
                    if(line[i][j]==''):
                        line[i].pop(j)
                        j-=1
                        #print("HERE")
                    if('\n' in line[i][j]):
                        line[i][j]=line[i][j].split('\n')
                        line[i][j]=line[i][j][0]
                length=len(line[i])
        return line
    def main(self,filename):
        f=open(filename,"r")
        total=0
        counts=[]
        init=False
        multi=[]
        count=0
        for line in f:
            line=self.preproc(line)
            lval=self.scorecard(line)
            if(not init):
                init=True
                multi=[1 for val in range(1,199)]
            for i in range(count+1,count+lval+2):
                multi[i]+=(multi[count])
            print(line," ",lval," ",int(2**lval)," ",count+lval+1," ",count)
            total+=(int(2**lval))*multi[count]
            counts.append(lval)
            count+=1
        print(total)
        print(multi)
        print(counts)
        total=0
        for num in multi:
            total+=num
        print(total)



obj=Day4()
obj.main("Day4.txt")