import time
class day9():
    def preproc(self,line):
        temp=[]
        temp=line.split(' ')
        count=0
        for val in temp:
            if(val!='\n'):
                temp[count]=int(temp[count])
            else:
                print("HI?",temp[-1])
                temp=temp[:-1]
            count+=1
        return temp
    def show(self,arr):
        for lin in arr:
            print(lin)
    def recur(self,list,lasts,flag2):
        temp=[]
        z=0
        val=0
        flag=False
        for i in range(1,len(list)):
            temp.append(abs(list[i-1]-list[i]))
            if(list[i-1]>list[i]):
                temp[-1]=temp[-1]*-1
            if(temp[-1]==0):
                z+=1
        if(z==(len(temp))):
            #print(temp,"\nFOUND!")
            val=lasts
        else:
            if(flag2):
                lasts-=temp[0]
                flag2=False
            else:
                lasts+=temp[0]
                flag2=True
            val=self.recur(temp,lasts,flag2)
        return val
    
    def main(self,filename):
        f=open(filename,"r")
        total=0
        arr=[]
        for line in f:
            arr.append(self.preproc(line))
        #self.show(arr)
        for i in range(0,len(arr)):
            temp=arr[i][0]
            #print("\n")
            #print(arr[i])
            value=self.recur(arr[i],temp,True)
            total+=value
            print(arr[i],value)
        return total

start=time.time_ns()
start1=time.time()
obj=day9()
total=obj.main("Day9.txt")
end=time.time_ns()
end1=time.time()
print((end-start)/1000," microseconds to execute")
print(end1-start1," seconds to execute")
print(total)
