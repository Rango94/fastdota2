import model
import readfile
import numpy as np
import math
import random

class trainer():
    model=0
    n=0
    file=0
    weghtlayer=0
    N=0
    def __init__(self,md,n,f):
        self.n=n
        self.N=n
        self.model=md
        self.file=f
        self.weghtlayer=np.zeros((2,md.size))

    def train(self,time):
        for i in range(time):
            self.n=(1-i/time)*self.N
            self.trainline()

    def trainline(self):
        if(random.random()>0.99):
            print(self.model.getvector("10"))
        line=self.file.readl()
        radiant=line[0:5]
        dire=line[5:10]
        label=line[10]
        radiant_vector=0
        dire_vector=0
        for e in radiant:
            radiant_vector+=self.model.getvector(e)
        for e in dire:
            dire_vector+=self.model.getvector(e)
        train_vector=radiant_vector-dire_vector
        outlayer_value=[np.dot(train_vector,self.weghtlayer[0]),np.dot(train_vector,self.weghtlayer[1])]
        # print(outlayer_value)
        softmax_out=self.softdown(outlayer_value)
        # print(softmax_out)
        flag=[0,0]
        if label=="1":
            flag[1]=1
        else:
            flag[0]=1
        # print(flag,label)
        if random.random()>0.9:
            if (outlayer_value[0]>outlayer_value[1] and flag[0]>flag[1]) or (outlayer_value[0]<outlayer_value[1] and flag[0]<flag[1]):
                print("right")
            else:
                print("wrong")

        for i in range(len(softmax_out)):
            if flag[i]==1:
                self.weghtlayer[i]+=self.n*(1-softmax_out[i])*train_vector
                for hero in radiant:
                    hero_tmp=self.model.getvector(hero)
                    hero_tmp+=self.n*0.5*(1-softmax_out[i])*self.weghtlayer[i]
                for hero in dire:
                    hero_tmp=self.model.getvector(hero)
                    hero_tmp-=self.n*0.5*(1-softmax_out[i])*self.weghtlayer[i]
            else:
                self.weghtlayer[i]-=self.n*softmax_out[i]*train_vector
                for hero in radiant:
                    hero_tmp=self.model.getvector(hero)
                    hero_tmp-=self.n*0.5*softmax_out[i]*self.weghtlayer[i]
                for hero in dire:
                    hero_tmp=self.model.getvector(hero)
                    hero_tmp+=self.n*0.5*softmax_out[i]*self.weghtlayer[i]


    def softdown(self,values):
        sum=0
        out=[]
        for e in values:
            sum+=math.pow(math.e,e)
        for e in values:
            out.append(math.pow(math.e,e)/sum)
        return out


    def prediction(self,path):
        f=open(path)
        total=0
        right=0
        line=f.readline()
        while(line!=""):
            total+=1
            line=line.split(" ")
            radiant = line[0:5]
            dire = line[5:10]
            label = line[10]
            radiant_vector = 0
            dire_vector = 0
            for e in radiant:
                radiant_vector += self.model.getvector(e)
            for e in dire:
                dire_vector += self.model.getvector(e)
            train_vector = radiant_vector - dire_vector
            outlayer_value = [np.dot(train_vector, self.weghtlayer[0]), np.dot(train_vector, self.weghtlayer[1])]
            flag = [0, 0]
            if label == "-1":
                flag[0] = 1
            else:
                flag[1] = 1
            if (outlayer_value[0] > outlayer_value[1] and flag[0] > flag[1]) or (
                    outlayer_value[0] < outlayer_value[1] and flag[0] < flag[1]):
                right+=1
            line = f.readline()
        print(right/total)
