from Source.Components.ROM32K import ROM32K
from Source.Components.Memory import Memory
from Source.Components.CPU import CPU
from Source.Pre_Built_Gates.Power import Power

class Computer:
    def __init__(self,reset,file_path) -> None:
        self.reset=reset
        self.address=Power([Power(False) for _ in range(15)])
        self.inM=Power([Power(False) for _ in range(16)])
        self.ROM=ROM32K(self.address,file_path)
        self.CPU=CPU(self.inM,self.ROM,self.reset)
        self.Memory=Memory(self.CPU.out[0],self.CPU.out[1],self.CPU.out[2])
        self()
    def __call__(self) -> None:
        self.ROM()
        self.CPU()
        self.Memory()
        for i in range(15):
            self.address.out[i].out=self.CPU.out[3].out[i].out
        for i in range(16):
            self.inM.out[i].out=self.Memory.out[i].out