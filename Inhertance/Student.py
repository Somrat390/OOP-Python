from User import User
class Student(User):
    def enroll(self):
        print("enroll into the course")

u = User()
s = Student()
print(s.name)