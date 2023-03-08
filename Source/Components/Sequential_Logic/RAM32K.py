from Source.Logic_Gates.DMux8Way import DMux8Way
from Source.Logic_Gates.Mux8Way16 import Mux8Way16
from Source.Components.Sequential_Logic.RAM4K import RAM4K
from Source.Pre_Built_Gates.Power import Power

class RAM32K:
    def __init__(self,a,load,address) -> None:
        self.a=a
        self.load=load
        self.address=address
        self.dmux=Power([Power(False) for _ in range(16)])
        self.ram=Power([RAM4K(self.a,self.dmux.out[i],Power(self.address.out[3:15])) for i in range(8)])
        self.out=[Power(False) for _ in range(16)]
        self()
    def __call__(self) -> None:
        dmux=DMux8Way(self.load,Power(self.address.out[0:3]))
        for i in range(8):
            self.dmux.out[i].out=dmux.out[i].out
        for i in range(8):
            self.ram.out[i]()
        mux=Mux8Way16(self.ram.out[0],self.ram.out[1],self.ram.out[2],self.ram.out[3],self.ram.out[4],self.ram.out[5],self.ram.out[6],self.ram.out[7],Power(self.address.out[0:3]))
        for i in range(16):
            self.out[i].out=mux.out[i].out