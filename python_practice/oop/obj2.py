# obj2.py
class Student:

	def __init__(self,name,age,grade):
		self.name = name
		self.age = age
		self.grade = grade

	def get_grade(self):
		return self.grade


class Cource:
	def __init__(self,name,max_students):
		self.name = name
		self.max_students = max_students
		self.students = []

	def add_student(self,student):
		self.students.append(student)
		return True

	def get_avg_grade(self):
		value = 0
		for student in self.students:
			value = value + student.grade

		return (value / len(self.students) )
#created students
s1 = Student("samaran",19,8)
s2 = Student("harani",19,9)

#adding students to cource

phy = Cource("physics",10)
phy.add_student(s1)
phy.add_student(s2)


print(phy.students[0].name)
print(phy.get_avg_grade())

