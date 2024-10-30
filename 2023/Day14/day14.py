import time
class day14():
    def remNL(self,arr):
        for i in range(0,len(arr)-1):
            arr[i]=arr[i][:-1]
        arr[-1]=arr[-1]
        return arr
    def allnorth(self,arr):
        for i in range(1,len(arr)):
            for j in range(0,len(arr[i])):
                if(arr[i][j]=='O'):
                    arr[i][j]='.'
                    count=i-1
                    while(count>=1 and arr[count][j]=='.'):
                        count-=1
                    if(arr[count][j]!='.'):
                        arr[count+1][j]='O'
                    else:
                        arr[count][j]='O'
        return arr
    def findWeights(self,arr,flag):
        length=len(arr)
        sum=0
        print(length)
        for l in arr:
            total=0
            for elm in l:
                if(elm=='O'):
                    total+=length
            sum+=total
            length-=1
        if(flag):
            print(sum)
            return sum
        return 0

    def main(self,filename):
        f=open(filename,'r')
        total=0
        arr=[]
        tarr=[]
        for l in f:
            temp=[]
            for i in range(0,len(l)):
                temp.append(l[i])
            arr.append(temp)
        #tarr=arr
        arr=self.allnorth(arr)
        arr=self.remNL(arr)
        total+=self.findWeights(arr)
        return total


start=time.time_ns()
start1=time.time()
obj=day14()
total=obj.main("Day14test2.txt")
end=time.time_ns()
end1=time.time()
print((end-start)/1000," microseconds to execute")
print(end1-start1," seconds to execute")
print(total)