# Person sınıfı tanımlanıyor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Ad: {self.name}, Yaş: {self.age}"

# Student sınıfı tanımlanıyor (Person'dan miras alıyor)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        return f"{super().display_info()}, Öğrenci Numarası: {self.student_id}"

# Teacher sınıfı tanımlanıyor (Person'dan miras alıyor)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        return f"{super().display_info()}, Öğretmenlik Yapılan Ders: {self.subject}"

# Öğrenci ve öğretmen nesneleri oluşturuluyor
student = Student("Ali", 20, "S12345")
teacher = Teacher("Ayşe", 35, "Matematik")

# Bilgiler ekrana yazdırılıyor
print(student.display_info())
print(teacher.display_info())
