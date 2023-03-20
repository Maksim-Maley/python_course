class One:
    a=0
    b=0
    def multiplication(self):
       print(self.a * self.b)
    def addition(self):
        print(self.a + self.b)
    def division(self):
        print(self.a / self.b)
    def subtraction(self):
        print(self.a - self.b)


One1 = One()
One1.a = 13
One1.b = 6
One1.multiplication()
One1.addition()
One1.division()
One1.subtraction()

class Student:
    name = " "
    nomber = 0
    age = 0
    def name_student(self):
        print(self.name)
    def nomber_student(self):
        print(self.nomber)
    def age_student(self):
        print(self.age)
    def age_(self):
        self.age = int(input("Измените ваш возраст: "))
    def nomber_(self):
        self.nomber = int(input("Измените ваш номер: "))



Student1 = Student()
Student1.name = "Максим"
Student1.age = 18
Student1.nomber = 13
Student1.name_student()
Student1.nomber_student()
Student1.age_student()      
Student1.age_() 
Student1.age_student()   
Student1.nomber_()
Student1.nomber_student()