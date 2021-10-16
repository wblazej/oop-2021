class Component:
    __in_use: bool = False

    @property
    def avaliable(self):
        return not self.__in_use

    def connect(self):
        if not self.avaliable:
            raise RuntimeError("This component is already in use")
        self.__in_use = True
        return self

    def disconnect(self):
        if self.avaliable:
            raise RuntimeError("This component is not in usage")
        self.__in_use = False
