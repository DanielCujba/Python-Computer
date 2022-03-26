from Source.Pre_Built_Gates.Not import Not
from Source.Pre_Built_Gates.And import And

class Nand:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
        self.out=None
        self()
    def __call__(self) -> None:
        out1=And(self.a,self.b)
        out2=Not(out1)
        self.out=out2.out
