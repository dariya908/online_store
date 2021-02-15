class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"{self.name} {self.age}")


class Male(Human):
    def __init__(self,name, age):
        super().__init__(name, age)
        self.education = True


def description(self):
    print(f"{self.name} {self.age}")


class Female(Human):
    def __init__(self,name, age):
        super().__init__(name, age)
        self.education = True

    def description(self):
        print(f"{self.name} {self.age}")

    male1=Male(name='dari',age=20)
    male1=description()
