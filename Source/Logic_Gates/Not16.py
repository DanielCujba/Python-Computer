from Source.Pre_Built_Gates.Not import Not
from Source.Pre_Built_Gates.Power import Power

class Not16:
    def __init__(self,a) -> None:
        self.a=a
        self.out=[Power(False) for _ in range(16)]
        self()
    def __call__(self) -> None:
        for i in range(16):
            self.out[i].out=Not(self.a.out[i]).out