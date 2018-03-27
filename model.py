import numpy as np
import random
class model():
    dic={}
    size=0
    def __init__(self,size):
        self.size=size
        for i in range(114):
            self.dic[str(i+1)]=self.vector(size)
            
    def vector(self,size):
        arr_tmp=[]
        for i in range(size):
            arr_tmp.append((0.5-random.random())/self.size)
        return np.array(arr_tmp)

    def getvector(self,name):
        return self.dic[name]

    def save(self,path,outlayer):
        f=open(path,"w")
        for i in outlayer:
            f.write("outlayer"+":")
            for j in i:
                f.write(str(j)+"\t")
            f.write("\n")

        for e in self.dic.keys():
            f.write(e+":")
            for item in self.dic[e]:
                f.write(str(item)+"\t")
            f.write("\n")

