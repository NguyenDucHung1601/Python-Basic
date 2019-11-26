class Person:
    # name = ""
    # age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def Name(self):
        print("Name: ",self.name)
    def Age(self):
        print("Age : ",self.age)

class Student(Person):
    # mark = 0
    def __init__(self,name,age,mark):
        Person.__init__(self,name,age)
        self.mark = mark
    def Mark(self):
        print("Mark: ",self.mark)

obj = Student("Nguyen Duc Hung",21,10)
obj.Name()
obj.Age()
obj.Mark()

