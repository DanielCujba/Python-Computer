from Source.Pre_Built_Gates.Power import Power
from Source.Components.Boolean_Arithmetic.HalfAdder import HalfAdder

class Inc16:
    def __init__(self,a) -> None:
        self.a=a
        self.out=[Power(False) for _ in range(16)]
        self()
    def __call__(self) -> None:
        add1=HalfAdder(self.a.out[15],Power(True))
        add2=HalfAdder(self.a.out[14],add1.out[1])
        add3=HalfAdder(self.a.out[13],add2.out[1])
        add4=HalfAdder(self.a.out[12],add3.out[1])
        add5=HalfAdder(self.a.out[11],add4.out[1])
        add6=HalfAdder(self.a.out[10],add5.out[1])
        add7=HalfAdder(self.a.out[9],add6.out[1])
        add8=HalfAdder(self.a.out[8],add7.out[1])
        add9=HalfAdder(self.a.out[7],add8.out[1])
        add10=HalfAdder(self.a.out[6],add9.out[1])
        add11=HalfAdder(self.a.out[5],add10.out[1])
        add12=HalfAdder(self.a.out[4],add11.out[1])
        add13=HalfAdder(self.a.out[3],add12.out[1])
        add14=HalfAdder(self.a.out[2],add13.out[1])
        add15=HalfAdder(self.a.out[1],add14.out[1])
        add16=HalfAdder(self.a.out[0],add15.out[1])

        self.out[0].out=add16.out[0].out
        self.out[1].out=add15.out[0].out
        self.out[2].out=add14.out[0].out
        self.out[3].out=add13.out[0].out
        self.out[4].out=add12.out[0].out
        self.out[5].out=add11.out[0].out
        self.out[6].out=add10.out[0].out
        self.out[7].out=add9.out[0].out
        self.out[8].out=add8.out[0].out
        self.out[9].out=add7.out[0].out
        self.out[10].out=add6.out[0].out
        self.out[11].out=add5.out[0].out
        self.out[12].out=add4.out[0].out
        self.out[13].out=add3.out[0].out
        self.out[14].out=add2.out[0].out
        self.out[15].out=add1.out[0].out