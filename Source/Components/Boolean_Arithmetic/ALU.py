from Source.Pre_Built_Gates.Power import Power
from Source.Logic_Gates.Mux16 import Mux16
from Source.Logic_Gates.Not16 import Not16
from Source.Logic_Gates.And16 import And16
from Source.Components.Boolean_Arithmetic.Add16 import Add16
from Source.Logic_Gates.Or8Way import Or8Way
from Source.Pre_Built_Gates.Or import Or
from Source.Pre_Built_Gates.And import And
from Source.Pre_Built_Gates.Not import Not

class ALU:
    def __init__(self,x,y,zx,nx,zy,ny,f,no) -> None:
        self.x=x
        self.y=y
        self.zx=zx
        self.nx=nx
        self.zy=zy
        self.ny=ny
        self.f=f
        self.no=no
        self.out=[Power([Power(False) for _ in range(16)]),Power(False),Power(False)]
        self()
    def __call__(self) -> None:
        x1=Mux16(self.x,Power([Power(False) for _ in range(16)]),self.zx)
        y1=Mux16(self.y,Power([Power(False) for _ in range(16)]),self.zy)
        notx1=Not16(x1)
        noty1=Not16(y1)
        x2=Mux16(x1,notx1,self.nx)
        y2=Mux16(y1,noty1,self.ny)
        addout=Add16(x2,y2)
        andout=And16(x2,y2)
        fout=Mux16(andout,addout,self.f)
        notfout=Not16(fout)
        out1=Mux16(fout,notfout,self.no)
        zr1=Or8Way(Power(out1.out[0:8]))
        zr2=Or8Way(Power(out1.out[8:16]))
        zr3=Or(zr1,zr2)
        zr=Not(zr3)
        for i in range(16):
            self.out[0].out[i].out=out1.out[i].out
        self.out[1].out=zr.out
        self.out[2].out=out1.out[0].out