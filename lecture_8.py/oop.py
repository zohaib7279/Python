# class Student:
#     name = "Zohaib"
#     def __init__(self , name , marks):
#         self.name = name
#         self.marks = marks
#         print("adding name in my data base")
# s1 = Student("karan",97)
# print(s1.name,s1.marks)
# s2 = Student("arjun",88)
# print(s2.name,s2.marks)
class Student:
    @staticmethod    
    def hello():
        print("hello")

    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
       
    def welcome(self):
        print("Welcome Student",self.name)
        
    def get_marks(self):
        return self.marks

s1 = Student("karan",97)
s1.welcome()
print(s1.get_marks())
s1.hello()

