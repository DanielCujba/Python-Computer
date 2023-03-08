from Source.Components.Sequential_Logic.Bit import Bit
from Source.Pre_Built_Gates.Power import Power

class Register:
    def __init__(self,a,load) -> None:
        self.a=a
        self.load=load
        self.bits=[Bit(self.a.out[i],self.load) for i in range(16)]
        self.out=[Power(False) for _ in range(16)]
        self()
    def __call__(self) -> None:
        for i in range(16):
            self.bits[i]()
            self.out[i].out=self.bits[i].out