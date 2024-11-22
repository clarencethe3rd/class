self.x = 0
class Student():
    def __init__(self):
        self.age = 12
        self.name = ""
        self.school = "xyz"
        self.student_id = ""
    def show_details(self):
        print(" name:",self.name,"\n","age:",self.age,"\n","school:",self.school,"\n","student ID:",self.student_id,"\n",)
    def change_details(self):
        self.x = self.x + 1
        
        print("student",self.x,"enter your name: ")
        self.name = input()
        self.student_id = input("enter your student ID: ")
student1 = Student()
student1.change_details()
student1.show_details()
student2 = Student()
student2.change_details()
student2.show_details()