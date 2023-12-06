from math import sqrt


class day6():
    def findRange(self,time,distance):
        a=-1
        b=int(time)
        c=int(distance) * -1
        val1=((-b + (sqrt((b*b)-(4*a*c))))/(2*a))
        val2=((-b - (sqrt((b*b)-(4*a*c))))/(2*a))
        #print(val1,val2)
        
        val1=int(val1)+1
        if(val2!=int(val2)):
            val2=int(val2)
        else:
            val2=int(val2)-1
        #print(val1,val2)
        return (max(1+val2-val1,0))
    def ltoarr(self,line):
        temp=[]
        line=line.split(':')
        line=line[1]
        if(line[-1]=='\n'):
            line=line[:-1]
        line=line.split(' ')
        #print(line)
        for i in range(0,len(line)):
            if(line[i]!=''):
                temp.append(line[i])
        #print(temp)
        return temp

    def main(self,filename):
        f=open(filename,'r')
        time=[]
        distance=[]
        flag=False
        for line in f:
            if(flag==False):
                time=self.ltoarr(line)
                flag=True
            else:
                distance=self.ltoarr(line)
        #print(time)
        #print(distance)
        ranges=[]
        total=1
        for i in range(0,len(distance)):
            ranges.append(self.findRange(time[i],distance[i]))
            total=total*(ranges[i])
        print(ranges)
        print(total)


obj=day6()
obj.main("Day6.txt")