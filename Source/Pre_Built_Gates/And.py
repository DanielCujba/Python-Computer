class And:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
        self.out=None
        self()
    def __call__(self) -> None:
        self.out = self.a.out and self.b.out