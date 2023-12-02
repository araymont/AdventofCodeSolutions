import time
#12r,13g,14b
class day2():
    def findmax(self,inLine,rMax,gMax,bMax):
        r=0
        g=0
        b=0
        for shown in inLine:
            if(shown[-1]=='b'):
                b=max(int(shown[:-2]),b)
            elif(shown[-1]=='r'):
                r=max(int(shown[:-2]),r)
            elif(shown[-1]=='g'):
                g=max(int(shown[:-2]),g)
            else:
                raise Exception("UHH Shouldnt be here")
        print(r,g,b)
        if(b>bMax or r>rMax or g>gMax):
            return False
        return True
        
    def preprocess(self,line):
        line=line.split(':')
        line=line[1:]
        line=line[0]
        line=line.replace('\n','')
        line=line.replace(' ','')
        line=line.replace('blue',' b')
        line=line.replace('red',' r')
        line=line.replace('green',' g')
        line=line.replace(';',',')
        line=line.split(',')
        return line
    def main(self,input):
        rm=12
        gm=13
        bm=14
        f=open("Day2.txt","r")
        count=1
        total=0
        for line in f:
            line=self.preprocess(line)
            if(self.findmax(line,rm,gm,bm)):
                total+=count
                print(line,count)
            count+=1
        return total
                

obj=day2()
total=obj.main("hi")
print(total)