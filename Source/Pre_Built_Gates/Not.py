class Not:
    def __init__(self,a) -> None:
        self.a = a
        self.out=None
        self()
    def __call__(self) -> None:
        self.out = not self.a.out