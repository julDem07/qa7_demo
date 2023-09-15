# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получения
#     значений этого атрибута  нужно использовать методы get и set
# 5.2. Создайте репозиторий на Github и отправьте файл с домашним заданием в этот удаленный репозиторий

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def hello(self):
        return f'Hello, mi name is {self.name} {self.surname}'

person_1 = Person('Alex', 'Parker')
person_2 = Person('Albus', 'Damboldor')
print(person_1.hello())
print(person_2.hello())

class Teacher(Person):
    def __init__(self, name, surname, fild):
        super().__init__(name, surname)
        self.fild = fild

    def greet(self):
        return f'{self.hello()} I work in {self.fild}'

teacher_1 = Teacher('Severus', 'Sneg', 'poushen')
teacher_2 = Teacher('Meggi', 'Smith', 'transformation')
print(teacher_1.greet())
print(teacher_2.greet())



class Student(Person):
    def __init__(self, name, surname, grade, age):
        super().__init__(name, surname)
        self.__grade = grade
        self.__age = age

    def answer(self):
        return f'{self.hello()} I have {self.get_grade()} grade, Im {self.get_age()}'

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def get_age(self):
        return self.__age

    def set_age(self, a):
        self.__age = a



student_1 = Student('Harry', 'Potter', 1, 11)
print(student_1._Student__grade)
# print(student_1.get_atter())
print(student_1.get_grade())
student_1.set_grade(3)
print(student_1.get_grade())
print(student_1.get_age())
student_1.set_age(13)
print(student_1.get_age())
print(student_1.__dict__)
print(student_1.answer())
