from Source.Logic_Gates.DMux8Way import DMux8Way
from Source.Logic_Gates.Mux8Way16 import Mux8Way16
from Source.Components.Sequential_Logic.Register import Register
from Source.Pre_Built_Gates.Power import Power

class RAM8:
    def __init__(self,a,load,address) -> None:
        self.a=a
        self.load=load
        self.address=address
        self.dmux=Power([Power(False) for _ in range(16)])
        self.registers=Power([Register(self.a,self.dmux.out[i]) for i in range(8)])
        self.out=[Power(False) for _ in range(16)]
        self()
    def __call__(self) -> None:
        dmux=DMux8Way(self.load,self.address)
        for i in range(8):
            self.dmux.out[i].out=dmux.out[i].out
        for i in range(8):
            self.registers.out[i]()
        mux=Mux8Way16(self.registers.out[0],self.registers.out[1],self.registers.out[2],self.registers.out[3],self.registers.out[4],self.registers.out[5],self.registers.out[6],self.registers.out[7],self.address)
        for i in range(16):
            self.out[i].out=mux.out[i].out