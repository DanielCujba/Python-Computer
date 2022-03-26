from Source.Pre_Built_Gates.And import And
from Source.Pre_Built_Gates.Power import Power

class And16:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
        self.out=[Power(False) for _ in range(16)]
        self()
    def __call__(self) -> None:
        for i in range(16):
            self.out[i].out=And(self.a.out[i],self.b.out[i]).out 