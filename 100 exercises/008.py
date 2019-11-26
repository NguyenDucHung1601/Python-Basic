'''
Bai 8: Dinh nghia 1 class gom co tham so lop va co cung tham so instance
'''


class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = Person("Hung", 21)
print("Name: ", obj.name)
print("Age : ", obj.age)
