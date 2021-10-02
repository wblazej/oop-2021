class Z:
    __g: int
    g: int

    def __init__(self, g):
        self.__g = g // 10
        self.g = g


z = Z(12)
print(z.g)

