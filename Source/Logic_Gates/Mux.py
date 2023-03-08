from Source.Pre_Built_Gates.And import And
from Source.Pre_Built_Gates.Not import Not
from Source.Pre_Built_Gates.Or import Or

class Mux:
    def __init__(self,a,b,sel) -> None:
        self.a=a
        self.b=b
        self.sel=sel
        self.out=None
        self()
    def __call__(self) -> None:
        negSel=Not(self.sel)
        out1=And(self.a,negSel)
        out2=And(self.b,self.sel)
        out3=Or(out1,out2)
        self.out=out3.out