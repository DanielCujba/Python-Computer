from Source.Logic_Gates.Mux16 import Mux16
from Source.Pre_Built_Gates.Power import Power

class Mux8Way16:
    def __init__(self,a,b,c,d,e,f,g,h,sel) -> None:
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        self.g=g
        self.h=h
        self.sel=sel
        self.out=[Power(False) for _ in range(16)]
        self()
    def __call__(self):
        mux1=Mux16(self.a,self.b,self.sel.out[2])
        mux2=Mux16(self.c,self.d,self.sel.out[2])
        mux3=Mux16(self.e,self.f,self.sel.out[2])
        mux4=Mux16(self.g,self.h,self.sel.out[2])
        mux5=Mux16(mux1,mux2,self.sel.out[1])
        mux6=Mux16(mux3,mux4,self.sel.out[1])
        mux7=Mux16(mux5,mux6,self.sel.out[0])
        for i in range(16):
            self.out[i].out=mux7.out[i].out