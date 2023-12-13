class Day13():
    def transpose(self,arr):
        temp=[]
        for i in range(0,len(arr[0])):
            temp.append([])
            for j in range(0,len(arr)):
                temp[i].append(arr[j][i])
        #print(arr)
        #print(temp)
        return temp[:-1]
    def checkvert(self,arr):
        vals=[]
        for i in range(1,len(arr)):
            if(arr[i]==arr[i-1]):
                count=i
                count2=i-1
                done=False
                doned=False
                donea=False
                while(done==False and arr[count]==arr[count2]):
                    count-=1
                    count2+=1
                    if(count<0 or count2 >= len(arr)):
                        done=True
                        if(count<0):
                            doned=True
                        if(count2>=len(arr)):
                            donea=True

                if(done==True):
                    if(donea and doned):
                        vals.append([count+1,count2-1])
                    elif(donea):
                        vals.append([count+1,count2-1])
                    elif(doned):
                        vals.append([count+1,count2-1])
                    else:
                        vals.append([count,count2])
                #print(done,donea,count2,doned,count)
        return vals
    def preproct(self,arr):
        tarr=[]
        for p in arr:
            tarr.append(self.transpose(p))
        return tarr
    def preproc(self,f):
        arr=[]
        temp=[]
        for line in f:
            if(line=='\n' or line==""):
                #print("EMPTY")
                arr.append(temp)
                temp=[]
            else:
                temp.append(line)
        arr.append(temp)
        return arr
    def show(self,arr):
        for p in arr:
            print(" ")
            for l in p:
                print(l)
    def findrefLines(self,arr,tarr):
        vals=[]
        lines=[]
        for i in range(0,len(arr)):
            vals=[]
            lines.append([])
            vals.append(self.checkvert(arr[i]))
            if(len(vals[-1])>=1):
                lines[-1].append(int((vals[-1][-1][0]+vals[-1][-1][1])/2)+1)
            else:
                lines[-1].append(0)
            vals.append(self.checkvert(tarr[i]))
            if(len(vals[-1])>=1):
                lines[-1].append(int((vals[-1][-1][0]+vals[-1][-1][1])/2)+1)
            else:
                lines[-1].append(0)
            #print(vals)
        return lines
    def calc(self,l):
        return ((l[0]*100)+l[1])
    def main(self,filename):
        ver=[]
        horz=[]
        f=open(filename,'r')
        arr=self.preproc(f)
        tarr=self.preproct(arr)
        #self.show(arr)
        #self.show(tarr)
        lines=self.findrefLines(arr,tarr)
        total=0
        for l in lines:
            total+=self.calc(l)
        return total

obj=Day13()
total=obj.main("Day13.txt")
print(total)