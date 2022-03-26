from Source.Pre_Built_Gates.Or import Or
from Source.Pre_Built_Gates.And import And
from Source.Logic_Gates.Nand import Nand

class Xor:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
        self.out=None
        self()
    def __call__(self) -> None:
        out1=Or(self.a,self.b)
        out2=Nand(self.a,self.b)
        out3=And(out1,out2)
        self.out=out3.out