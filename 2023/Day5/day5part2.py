class day5():
    def turn2D(self,list):
        temp=[]
        ttemp=[]
        for i in range(0,int(len(list)),2):
            ttemp=[]
            ttemp.append(int(list[i]))
            ttemp.append(int(list[i+1])+int(list[i])-1)
            temp.append(ttemp)
        #print("turn2d :",temp)
        return temp
    def findRanges(self,list):
        #print(list,int(len(list)/2))
        temp=[]
        for i in range(0,int(len(list)/2)):
            #print(i)
            for j in range(int(list[2*i]),int(list[2*i])+int(list[(2*i)+1])):
                temp.append(j)
        return temp
    def mapto2(self,source,res):
        results=[]
        #print(res)
        for val in source:
            found=False
            count=0
            while(count<len(res) and val[0]<=val[1] and found==False):
                if(int(res[count][1])<=val[0] and (int(res[count][2]) + int(res[count][1])>val[1])):
                    results.append([(val[0]-int(res[count][1]))+int(res[count][0]),(min(int(res[count][2])-1,val[1]-val[0])+(val[0]-int(res[count][1]))+int(res[count][0]))])
                    found=True
                elif(int(res[count][1])<=val[0] and (int(res[count][2]) + int(res[count][1])>val[0])):
                    #print("hi3",val,res[count][2],res[count][1])
                    results.append([(val[0]-int(res[count][1]))+int(res[count][0]),(int(res[count][2])+int(res[count][0])-1)])
                    val[0]=(int(res[count][1]) + int(res[count][2]))
                elif(int(res[count][1])<=val[1] and (int(res[count][2]) + int(res[count][1])>val[1])):
                    #print("hi2")
                    results.append([(int(res[count][0])),(val[1]-int(res[count][1]))+int(res[count][0])])
                    val[1]=(int(res[count][1])-1)
                elif(int(res[count][1])>val[0] and (int(res[count][2]) + int(res[count][1])<val[1])):
                    #print("hi ",val)
                    results.append([int(res[count][0]),int(res[count][0])+int(res[count][2])-1])
                    source.append([int(res[count][1])+int(res[count][2]),val[1]])
                    val[1]=int(res[count][1]) -1
                    #print(source[-1],val)
                count+=1
            if(not found):
                results.append(val)
        #print(results)
        return results
    def mapto(self,source,res):
        results=[]
        for val in source:
            found=False
            count=0
            while(count<len(res) and found==False):
                if(int(res[count][1]) <= int(val) and (int(res[count][2]) + int(res[count][1])>int(val))):
                    found=True
                    results.append((int(val)-int(res[count][1]))+int(res[count][0]))
                count+=1
            if(found==False):
                results.append(val)
        return results
    def preproc(self,f):
        init=True
        sl=[]
        sts=[]
        stsb=False
        stf=[]
        stfb=False
        ftw=[]
        ftwb=False
        wtl=[]
        wtlb=False
        ltt=[]
        lttb=False
        tth=[]
        tthb=False
        htl=[]
        htlb=False
        for line in f:
            if(init):
                temp=line.split(':')
                temp=temp[1:]
                temp=temp[0][1:-1]
                sl=temp.split(' ')
                init=False
            elif(line=='\n'):
                stsb=False
                stfb=False
                ftwb=False
                wtlb=False
                lttb=False
                tthb=False
                htlb=False
            elif(line=='seed-to-soil map:\n'):
                stsb=True
            elif(line=='soil-to-fertilizer map:\n'):
                stfb=True
            elif(line=='fertilizer-to-water map:\n'):
                ftwb=True
            elif(line=='water-to-light map:\n'):
                wtlb=True
            elif(line=='light-to-temperature map:\n'):
                lttb=True
            elif(line=='temperature-to-humidity map:\n'):
                tthb=True
            elif(line=='humidity-to-location map:\n'):
                htlb=True
            elif(stsb==True):
                temp=line[0:-1]
                temp=temp.split(' ')
                sts.append(temp)
            elif(stfb==True):
                temp=line[0:-1]
                temp=temp.split(' ')
                stf.append(temp)
            elif(ftwb==True):
                temp=line[0:-1]
                temp=temp.split(' ')
                ftw.append(temp)
            elif(wtlb==True):
                temp=line[0:-1]
                temp=temp.split(' ')
                wtl.append(temp)
            elif(lttb==True):
                temp=line[0:-1]
                temp=temp.split(' ')
                ltt.append(temp)
            elif(tthb==True):
                temp=line[0:-1]
                temp=temp.split(' ')
                tth.append(temp)
            elif(htlb==True):
                if(line[-1]=='\n'):
                    temp=line[0:-1]
                else:
                    temp=line
                temp=temp.split(' ')
                htl.append(temp)
        return sl,sts,stf,ftw,wtl,ltt,tth,htl
    def main(self,filename):
        f=open(filename,"r")
        seedlist=[]
        seedsoil=[]
        soilfertilizer=[]
        fertilizerwater=[]
        waterlight=[]
        lighttemperature=[]
        temperaturehumidity=[]
        humiditylocation=[]
        seedlist,seedsoil,soilfertilizer,fertilizerwater,waterlight,lighttemperature,temperaturehumidity,humiditylocation=self.preproc(f)
        #print(seedlist)
        #print(seedsoil)
        #print(soilfertilizer)
        #print(fertilizerwater)
        #print(waterlight)
        #print(lighttemperature)
        #print(temperaturehumidity)
        #print(humiditylocation)
        #print("\n")
        test=self.turn2D(seedlist)
        #self.mapto2(test,seedsoil)
        seedlist=self.turn2D(seedlist)

        #print(seedlist)
        #return 0
        res=[]
        res=self.mapto2(seedlist,seedsoil)
        #print(res)
        #return 0
        res=self.mapto2(res,soilfertilizer)
        #print(res)
        res=self.mapto2(res,fertilizerwater)
        #print(res)
        res=self.mapto2(res,waterlight)
        #print(res)
        res=self.mapto2(res,lighttemperature)
        #print(res)
        res=self.mapto2(res,temperaturehumidity)
        #print(res)
        res=self.mapto2(res,humiditylocation)
        #print(res)
        print(min(res))
        print(min(res)[0])
obj=day5()
obj.main("Day5.txt")
