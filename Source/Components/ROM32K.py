from Source.Pre_Built_Gates.Power import Power

class ROM32K:
    def __init__(self,a,file_path) -> None:
        self.a=a
        self.file_path=file_path
        self.out=[Power(False) for _ in range(16)]
        self.memory=[]
        self.loadROM(self.file_path)
        self()
    def __call__(self) -> None:
        instuction=self.memory[self.bool_to_int(self.a)]
        for i in range(16):
            self.out[i].out=instuction[i]
    def loadROM(self,file_path):
        self.memory.clear()
        f=open(file_path,"r")
        for _ in range(32768):
            line=f.readline()
            self.memory.append([line[j]=="1" for j in range(16)])
        f.close()
    def bool_to_int(self,a):
        x=0
        for i in range(14,-1,-1):
            x+=a.out[i].out*(2**(14-i))
        return x