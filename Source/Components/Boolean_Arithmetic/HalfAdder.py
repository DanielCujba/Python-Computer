from Source.Pre_Built_Gates.And import And
from Source.Logic_Gates.Xor import Xor
from Source.Pre_Built_Gates.Power import Power

class HalfAdder:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
        self.out=[Power(False),Power(False)]
        self()
    def __call__(self) -> None:
        bit_sum=Xor(self.a,self.b)
        carry=And(self.a,self.b)
        self.out[0].out=bit_sum.out
        self.out[1].out=carry.out