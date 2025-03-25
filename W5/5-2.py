class Student:
    def __init__(self,id,name,major):
        self.id=id
        self.name=name
        self.major=major
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name=new_name
        return self.name
    def set_major(self,new_major):
        self.major=new_major
        return self.major
    def print_info(self):
        print(f"ID:<{self.id}>,Name:<{self.name}>,Major:<{self.major}>")

student_id, name, major = input().split()
student=Student(student_id,name,major)
new_name=input()
new_major=input()
student.print_info()
student.set_name(new_name)
student.print_info()
student.set_major(new_major)
student.print_info()