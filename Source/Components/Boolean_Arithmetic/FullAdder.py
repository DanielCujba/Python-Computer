from Source.Components.Boolean_Arithmetic.HalfAdder import HalfAdder
from Source.Logic_Gates.Xor import Xor
from Source.Pre_Built_Gates.Power import Power

class FullAdder:
    def __init__(self,a,b,c) -> None:
        self.a=a
        self.b=b
        self.c=c
        self.out=[Power(False),Power(False)]
        self()
    def __call__(self) -> None:
        ha1=HalfAdder(self.a,self.b)
        ha2=HalfAdder(ha1.out[0],self.c)
        xor=Xor(ha1.out[1],ha2.out[1])
        self.out[0].out=ha2.out[0].out
        self.out[1].out=xor.out