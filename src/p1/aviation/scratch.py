from dataclasses import dataclass


@dataclass
class A:
    x: int
    s: str = 'NA'
    health: bool = True

    def __repr__(self):
        return f'Klasa A, x={self.x}, s={self.s}, zrowie:{self.health}'


a = A(x=4, health=True)
print(a)
print(str(a))
