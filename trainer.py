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
    tmpdic={}
    weghtlayer_tmp=0
    def __init__(self,md,n,f):
        self.n=n
        self.N=n
        self.model=md
        self.file=f
        self.weghtlayer=np.zeros((2,md.size))
        self.weghtlayer_tmp=np.zeros((2,md.size))

    def train(self,time):
        for i in range(time):
            if i%10000==0:
                print(self.weghtlayer)
                print("-----------------------------")
                r=0
                for e in self.tmpdic.keys():
                   if self.tmpdic[e]=="right":
                       r+=1
                print(r/100)
            tmp_n=(1-i/time)*self.N
            if tmp_n<0.001:
                tmp_n=0.001
            self.n=random.random()*tmp_n
            if i%100==0:
                self.tmpdic[i%100]=self.trainline(True)
            else:
                self.tmpdic[i % 100] = self.trainline(False)


    def trainline(self,renew):
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
        softmax_out=self.softdown(outlayer_value)
        if softmax_out==-1:
            print("超出范围")
            self.normalize()
            return 0
        flag=[0,0]
        if label=="1":
            flag[1]=1
        else:
            flag[0]=1
        if renew:
            self.weghtlayer+=self.weghtlayer_tmp/100
            self.weghtlayer_tmp=np.zeros((2,self.model.size))
        for i in range(len(softmax_out)):
            if flag[i]==1:
                self.weghtlayer_tmp[i]+=self.n*(1-softmax_out[i])*train_vector
                for hero in radiant:
                    hero_tmp=self.model.getvector(hero)
                    hero_tmp+=self.n*0.5*(1-softmax_out[i])*self.weghtlayer[i]
                for hero in dire:
                    hero_tmp=self.model.getvector(hero)
                    hero_tmp-=self.n*0.5*(1-softmax_out[i])*self.weghtlayer[i]
            else:
                self.weghtlayer_tmp[i]-=self.n*softmax_out[i]*train_vector
                for hero in radiant:
                    hero_tmp=self.model.getvector(hero)
                    hero_tmp-=self.n*0.5*softmax_out[i]*self.weghtlayer[i]
                for hero in dire:
                    hero_tmp=self.model.getvector(hero)
                    hero_tmp+=self.n*0.5*softmax_out[i]*self.weghtlayer[i]
        if (outlayer_value[0] > outlayer_value[1] and flag[0] > flag[1]) or (
                outlayer_value[0] < outlayer_value[1] and flag[0] < flag[1]):
            return "right"
        else:
            return "wrong"

    def softdown(self,values):
        sum=0
        out=[]
        try:
            for e in values:
                sum+=math.pow(math.e,e)
            for e in values:
                out.append(math.pow(math.e,e)/sum)
        except:
            print(values)
            return -1
        return out


    def prediction(self,path):
        f=open(path)
        total=0
        right=0
        line=f.readline()
        while(line!=""):
            total+=1
            line=line.replace("\n","").split(" ")
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


    def normalize(self):
        tmp_sum=0
        for e in self.weghtlayer[0]:
            tmp_sum+=math.pow(e,2)
        tmp_sum=math.pow(tmp_sum,0.5)
        self.weghtlayer[0] /= tmp_sum
        tmp_sum = 0
        for e in self.weghtlayer[1]:
            tmp_sum += math.pow(e, 2)
        tmp_sum = math.pow(tmp_sum, 0.5)
        self.weghtlayer[1] /= tmp_sum
        for i in range(114):
            tmp_sum = 0
            for e in self.model.dic[str(i+1)]:
                tmp_sum+=math.pow(e,2)
            tmp_sum=math.pow(tmp_sum,0.5)
            self.model.dic[str(i+1)]/=tmp_sum