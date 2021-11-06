class A:
    pole: int = 12  # publiczne pole klasy...
    __field: int = 10  # prywatne pole klasy...

    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, new_field_value):
        print('ustawiamy pole field')
        self.__field = new_field_value


a = A()
print(a.pole)
print(a.field)  # wygląda jak publiczne pole.. ale jest tak naprawdę metodą (getterem)

a.field = 19
print(a.field)  # wygląda jak publiczne pole.. ale jest tak naprawdę metodą (getterem)
