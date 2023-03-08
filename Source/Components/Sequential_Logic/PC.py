from Source.Logic_Gates.Mux16 import Mux16
from Source.Components.Boolean_Arithmetic.Inc16 import Inc16
from Source.Components.Sequential_Logic.Register import Register
from Source.Pre_Built_Gates.Power import Power

class PC:
    def __init__(self,a,load,inc,reset) -> None:
        self.a=a
        self.load=load
        self.inc=inc
        self.reset=reset
        self.out=[Power(False) for _ in range(16)]
        self.mux3=Power([Power(False) for _ in range(16)])
        self.register=Register(self.mux3,Power(True))
        self()
    def __call__(self) -> None:
        inc1=Inc16(self)
        mux1=Mux16(self,inc1,self.inc)
        mux2=Mux16(mux1,self.a,self.load)
        mux3=Mux16(mux2,Power([Power(False) for _ in range(16)]),self.reset)
        for i in range(16):
            self.mux3.out[i].out=mux3.out[i].out
        self.register()
        for i in range(16):
            self.out[i].out=self.register.out[i].out