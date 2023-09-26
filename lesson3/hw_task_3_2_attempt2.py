class Subjects:
   # def __new__(cls, *args, **kwargs):
   #     print("Subjects list init")
   #     return super().__new__(cls)

    def __init__(self, my_list):
        self.my_list = list(my_list)

    def __getitem__(self, item):
        return self.my_list[item]

class Students:

    def __init__(self):
        self.knowledge = [] #list(knowledge)
        print(f'Базовые знания:  {self.knowledge}')

    def take(self, my_list):
        self.knowledge.append(my_list)
        #print(f'Знания ученика после обучения: {res}')

class Teachers:
    def __init__(self):
        self.number_of_teached_students = 0


    def teach(self, list_materials, number_of_students):
        for student in number_of_students:
            student.take(list_materials)
            self.number_of_teached_students +=1
        print(f'Количество обученных учеников: {self.number_of_teached_students}')


sub_1 = Subjects(["Python",\
"Version Control Systems",\
"Relational Databases",\
"NoSQL databases",\
"Message Brokers"])

sub_2 = Subjects(['english'])

teacher_1 = Teachers()
student_1 = Students()
teacher_1.teach(sub_2[0],[student_1])
print(student_1.knowledge)
#student_1.take(sub_1)
#student_1.take(sub_1)
#teacher_1.teach(sub_1, student_1)
