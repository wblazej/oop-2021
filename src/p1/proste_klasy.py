class A:
    x = 4
    y = 'kadabra'

    def __init__(self, a: int, b: int):
        print('konstruktor uruchomiony')
        self.x = a + b

    def square_x(self):
        print('podnoszę x do potęgi 2')
        self.x **= 2


def gg(n):
    g = [i * i for i in range(n)]
    return g


w = [1, 2, 3]
x = 12

w.append(x)
w.extend(gg(15))

instance1 = A(2, 5)
instance2 = A(2, 3)

print(instance1)
print(instance2)
print(instance1.x)
print(instance2.x)
print('---------')
instance1.square_x()
print(instance1.x)
print(instance2.x)
