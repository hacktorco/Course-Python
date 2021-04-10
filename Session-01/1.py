
inta = 16516516516516515615665465165161651616516165161
stringa = "hello this is python programming language"

chara = 'asd'

floata = 123123123.123124124131231241234124138712538712538715387152331

"""
    how to implement  function in python

    def <name> (args, ...):
        state code ...
"""

def sum1(a, b):
    c = a + b
    print(c)

print(sum1(1, 2))

class Student:

    def __init__(self, age=0):
        self.name: str = str("")
        self.age = age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    @staticmethod
    def get_nothing():
        return "Nothing"



stu = Student(age=1)

stu.set_name("reza") # set reza as name
print(stu.get_name()) # reza
print(stu.get_age()) # 1 
print(stu.get_nothing()) # nothing
