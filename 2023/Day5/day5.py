class day5():
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
        ttb=False
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
        res=[]
        res=self.mapto(seedlist,seedsoil)
        #print(res)
        res=self.mapto(res,soilfertilizer)
        #print(res)
        res=self.mapto(res,fertilizerwater)
        #print(res)
        res=self.mapto(res,waterlight)
        #print(res)
        res=self.mapto(res,lighttemperature)
        #print(res)
        res=self.mapto(res,temperaturehumidity)
        #print(res)
        res=self.mapto(res,humiditylocation)
        #print(res)
        print(min(res))
obj=day5()
obj.main("Day5.txt")
