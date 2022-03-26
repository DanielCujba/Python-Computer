from Source.Pre_Built_Gates.FlipFlop import FlipFlop
from Source.Logic_Gates.Mux import Mux

class Bit:
    def __init__(self,a,load) -> None:
        self.a=a
        self.load=load
        self.out=None
        self.mux=Mux(self,self.a,self.load)
        self.flipflop=FlipFlop(self.mux)
        self()
    def __call__(self) -> None:
        self.mux()
        self.flipflop()
        self.out=self.mux.out

