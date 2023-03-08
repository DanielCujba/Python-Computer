class FlipFlop:
    def __init__(self,a) -> None:
        self.a=a
        self.prev_a=None
        self.out=None
        self()
    def __call__(self) -> None:
        self.out=self.prev_a
        self.prev_a=self.a.out
