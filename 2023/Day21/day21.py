import time 

class day21():
    def startloop(self,arr):
        for line in range(1,len(arr)-1):
            for col in range(1,len(arr[line])-1):
                if(arr[line][col]=='S'):
                    arr[line][col]='.'
                    if(arr[line-1][col]=='.'):
                        arr[line-1][col]='O'
                    if(arr[line+1][col]=='.'):
                        arr[line+1][col]='O'
                    if(arr[line][col-1]=='.'):
                        arr[line][col-1]='O'
                    if(arr[line][col+1]=='.'):
                        arr[line][col+1]='O'
        for col in range(1,len(arr[-1])-1):
            if(arr[-1][col]=='S'):
                arr[-1][col]='.'
                if(arr[-2][col]=='.'):
                    arr[-2][col]='O'
                if(arr[-1][col-1]=='.'):
                    arr[-1][col-1]='O'
                if(arr[-1][col+1]=='.'):
                    arr[-1][col+1]='O'
        for col in range(1,len(arr[0])-1):
            if(arr[0][col]=='S'):
                arr[0][col]='.'
                if(arr[1][col]=='.'):
                    arr[1][col]='O'
                if(arr[0][col-1]=='.'):
                    arr[0][col-1]='O'
                if(arr[0][col+1]=='.'):
                    arr[0][col+1]='O'
        for line in range(1,len(arr)-1):
            if(arr[line][0]=='S'):
                arr[line][0]='.'
                if(arr[line-1][0]=='.'):
                    arr[line-1][0]='O'
                if(arr[line+1][0]=='.'):
                    arr[line+1][0]='O'
                if(arr[line][1]=='.'):
                    arr[line][1]='O'
        for line in range(1,len(arr)-1):
            if(arr[line][-1]=='S'):
                arr[line][-1]='.'
                if(arr[line-1][-1]=='.'):
                    arr[line-1][-1]='O'
                if(arr[line+1][-1]=='.'):
                    arr[line+1][-1]='O'
                if(arr[line][-2]=='.'):
                    arr[line][-2]='O'
        if(arr[0][0]=='S'):
            arr[0][0]='.'
            if(arr[1][0]=='.'):
                arr[1][0]='O'
            if(arr[0][1]=='.'):
                arr[0][1]='O'
        if(arr[0][-1]=='S'):
            arr[0][-1]='.'
            if(arr[1][-1]=='.'):
                arr[1][-1]='O'
            if(arr[0][-2]=='.'):
                arr[0][-2]='O'
        if(arr[-1][0]=='S'):
            arr[-1][0]='.'
            if(arr[-2][0]=='.'):
                arr[-2][0]='O'
            if(arr[-1][1]=='.'):
                arr[-1][1]='O'
        if(arr[-1][-1]=='S'):
            arr[-1][-1]='.'
            if(arr[-2][-1]=='.'):
                arr[-2][-1]='O'
            if(arr[-1][-2]=='.'):
                arr[-1][-2]='O'
        return arr
    
    def loop(self,arr):
        temp=[]
        for lin in arr:
            temp.append(lin)
        for line in range(1,len(arr)-1):
            for col in range(1,len(arr[line])-1):
                if(arr[line][col]=='O'):
                    temp[line][col]='.'
                    if(arr[line-1][col]=='.'):
                        temp[line-1][col]='O'
                    if(arr[line+1][col]=='.'):
                        temp[line+1][col]='O'
                    if(arr[line][col-1]=='.'):
                        temp[line][col-1]='O'
                    if(arr[line][col+1]=='.'):
                        temp[line][col+1]='O'
        for col in range(1,len(arr[-1])-1):
            if(arr[-1][col]=='O'):
                temp[-1][col]='.'
                if(arr[-2][col]=='.'):
                    temp[-2][col]='O'
                if(arr[-1][col-1]=='.'):
                    temp[-1][col-1]='O'
                if(arr[-1][col+1]=='.'):
                    temp[-1][col+1]='O'
        for col in range(1,len(arr[0])-1):
            if(arr[0][col]=='O'):
                temp[0][col]='.'
                if(arr[1][col]=='.'):
                    temp[1][col]='O'
                if(arr[0][col-1]=='.'):
                    temp[0][col-1]='O'
                if(arr[0][col+1]=='.'):
                    temp[0][col+1]='O'
        for line in range(1,len(arr)-1):
            if(arr[line][0]=='O'):
                temp[line][0]='.'
                if(arr[line-1][0]=='.'):
                    temp[line-1][0]='O'
                if(arr[line+1][0]=='.'):
                    temp[line+1][0]='O'
                if(arr[line][1]=='.'):
                    temp[line][1]='O'
        for line in range(1,len(arr)-1):
            if(arr[line][-1]=='O'):
                temp[line][-1]='.'
                if(arr[line-1][-1]=='.'):
                    temp[line-1][-1]='O'
                if(arr[line+1][-1]=='.'):
                    temp[line+1][-1]='O'
                if(arr[line][-2]=='.'):
                    temp[line][-2]='O'
        if(arr[0][0]=='O'):
            temp[0][0]='.'
            if(arr[1][0]=='.'):
                temp[1][0]='O'
            if(arr[0][1]=='.'):
                temp[0][1]='O'
        if(arr[0][-1]=='O'):
            temp[0][-1]='.'
            if(arr[1][-1]=='.'):
                temp[1][-1]='O'
            if(arr[0][-2]=='.'):
                temp[0][-2]='O'
        if(arr[-1][0]=='O'):
            temp[-1][0]='.'
            if(arr[-2][0]=='.'):
                temp[-2][0]='O'
            if(arr[-1][1]=='.'):
                temp[-1][1]='O'
        if(arr[-1][-1]=='O'):
            temp[-1][-1]='.'
            if(arr[-2][-1]=='.'):
                temp[-2][-1]='O'
            if(arr[-1][-2]=='.'):
                temp[-1][-2]='O'
        return temp

    def preproc(self,line):
        temp=[]
        for elm in line:
            if(elm!='\n'):
                temp.append(elm)
        return temp
    def find(self,arr):
        count=0
        for line in arr:
            for col in line:
                if(col=='O'):
                    count+=1
        return count
    def main(self,filename):
        steps=1
        f=open(filename,"r")
        arr=[]
        for line in f:
            arr.append(self.preproc(line))
        #print(arr)
        #arr=self.startloop(arr)
        for i in range(0, steps):
            arr=self.loop(arr)
        for line in arr:
            print(line)
        return self.find(arr)
        


start=time.time_ns()
start1=time.time()
obj=day21()
total=obj.main("Day21test.txt")
end=time.time_ns()
end1=time.time()
print((end-start)/1000," microseconds to execute")
print(end1-start1," seconds to execute")
print(total)