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

