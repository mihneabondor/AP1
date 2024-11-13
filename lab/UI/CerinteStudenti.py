from Operations.StudentOperations import StudentOperations
from Domain.Student import Student

class CerinteStudenti:
    def __init__(self):
        studentOps = StudentOperations()
        self.__cerinte = [{
            "nume": "Afisare studenti",
            "func": self.printStudents
        }, {
            "nume": "Adaugare student",
            "func": self.addStudent
        }, {
            "nume": "Modificare student",
            "func": self.modificareStudent
        }, {
            "nume": "Cautare student",
            "func": self.cautare
        },]

    def __str__(self):
        txt = ''
        for i in range(len(self.__cerinte)):
            txt += f'{i + 1}. {self.__cerinte[i]["nume"]}\n'
        txt += '\nx. Iesire\n'
        return txt
    
    def waitForX(self):
        print()
        while True:
            x = input("x. Iesire\n")
            if x.lower() == "x":
                break

    def getCerinteLength(self):
        return len(self.__cerinte)
    
    def runOption(self, option, students):
        if int(option) > len(self.__cerinte):
            raise ValueError
        try:
            option = int(option) - 1
            self.__cerinte[option]["func"](students)
        except ValueError:
            print("Datele introduse nu sunt valide!")
        except ArithmeticError:
            print("ID-ul ales exista deja in lista de studenti!")
        except LookupError:
            print("Nu exista niciun student cu acest id!")

    def __read(self):
        id = int(input("id: "))
        nume = input("nume: ")   
        grupa = int(input("grupa: "))
        return self.__getStudent(id, nume, grupa)
    
    def __getStudent(self, id, nume, grupa):
        return Student(nume, id, grupa)
    
    def printStudents(self, students):
        for stud in students:
            print(stud)

    def addStudent(self, students):
        student = self.__read()
        studOps = StudentOperations()
        studOps.addStudent(student, students)

    def cautare(self, students):
        id = int(input("id: "))
        print()
        studOps = StudentOperations()
        student = studOps.cautare(id, students)
        print(student)

    def modificareStudent(self, students):
        self.printStudents(students)
        student = self.__read()
        studOps = StudentOperations()
        studOps.modifyStudent(student, students)