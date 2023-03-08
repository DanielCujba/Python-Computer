from Source.Pre_Built_Gates.And import And
from Source.Pre_Built_Gates.Not import Not
from Source.Pre_Built_Gates.Power import Power

class DMux:
    def __init__(self,a,sel) -> None:
        self.a=a
        self.sel=sel
        self.out=[Power(False),Power(False)]
        self()
    def __call__(self) -> None:
        negSel=Not(self.sel)
        out1=And(self.a,negSel)
        out2=And(self.a,self.sel)
        self.out[0].out=out1.out
        self.out[1].out=out2.out