from Source.Logic_Gates.DMux import DMux
from Source.Pre_Built_Gates.Power import Power

class DMux8Way:
    def __init__(self,a,sel) -> None:
        self.a=a
        self.sel=sel
        self.out=[Power(False) for _ in range(8)]
        self()
    def __call__(self):
        dmux1=DMux(self.a,self.sel.out[0])
        dmux2=DMux(dmux1.out[0],self.sel.out[1])
        dmux3=DMux(dmux1.out[1],self.sel.out[1])
        dmux4=DMux(dmux2.out[0],self.sel.out[2])
        dmux5=DMux(dmux2.out[1],self.sel.out[2])
        dmux6=DMux(dmux3.out[0],self.sel.out[2])
        dmux7=DMux(dmux3.out[1],self.sel.out[2])
        self.out[0].out=dmux4.out[0].out
        self.out[1].out=dmux4.out[1].out
        self.out[2].out=dmux5.out[0].out
        self.out[3].out=dmux5.out[1].out
        self.out[4].out=dmux6.out[0].out
        self.out[5].out=dmux6.out[1].out
        self.out[6].out=dmux7.out[0].out
        self.out[7].out=dmux7.out[1].out