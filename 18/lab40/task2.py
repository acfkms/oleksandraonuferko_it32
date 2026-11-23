class Student:
    college = "FKTBP VNU"
    count = 0
    def __init__(self, name, surname, group, birth_year):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year
        Student.count += 1
    def full_name(self):
        return f"{self.name} {self.surname}"
student1 = Student("Oleksandra", "Onuferko", "IT-32", 2009)
student2 = Student("Ivan", "Petrenko", "IT-32", 2007)
print("College through class:", Student.college)
print("College through object:", student1.college)
student1.college = "My New College"
print("Student 1 college:", student1.college)
print("Student 2 college:", student2.college)
print("Number of students:", Student.count)
print("\nStudent 1 dictionary:")
print(student1.__dict__)
print("\nStudent class dictionary:")
print(Student.__dict__)