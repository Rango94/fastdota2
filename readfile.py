
class readfile():
    f=0
    path=""
    def __init__(self,path):
        self.f=open(path)
        self.path=path

    def readl(self):
        line=self.f.readline().replace("\n","")
        if line!="":
            return line.split(" ")
        else:
            self.f.close()
            self.f=open(self.path)
            return self.f.readline().split(" ")
    

