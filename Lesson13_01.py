class Student:

    def __init__(self,name):
        self.name = name

    def avg(self,math,english):
        print((math + english)/2)

a001 = Student("sato")
#a001.name = "sato"
print(a001.name)

a002 = Student("tanaka")
#a002.name  = "tanaka"
print(a002.name)