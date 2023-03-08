from Source.Pre_Built_Gates.Or import Or

class Or8Way:
    def __init__(self,a) -> None:
        self.a=a
        self.out=None
        self()
    def __call__(self) -> None:
        or1=Or(self.a.out[0],self.a.out[1])
        or2=Or(self.a.out[2],self.a.out[3])
        or3=Or(self.a.out[4],self.a.out[5])
        or4=Or(self.a.out[6],self.a.out[7])
        or5=Or(or1,or2)
        or6=Or(or3,or4)
        or7=Or(or5,or6)
        self.out=or7.out
