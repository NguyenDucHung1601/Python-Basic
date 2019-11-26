class Student:
    name = ""
    age = 0

    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def __str__(self):
        return ("--------------------")

    def __del__(self):  # Disstructor
        print("Obj destroyed")

    def info(self):
        print("Name: ", self.name, " Age: ", self.age)

    def sayHello(self):
        print(self.name, "hello everyone!")


obj = Student("Hung", 21)
# print(obj) # tac dung cua __str__
obj.info()
obj.sayHello()
del obj
