class A:
    w = [i for i in range(100)]

    def __getitem__(self, key: int) -> int:
        return self.w[key]

    def __setitem__(self, key, value):
        self.w[key] = value


a = A()
a[5] = 12
print(a[5])
