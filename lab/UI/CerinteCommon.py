from UI.CerinteStudenti import CerinteStudenti
from UI.CerinteProbleme import CerinteProbleme

from Operations.CommonOperations import CommonOperations
from Operations.ProblemeOperations import ProblemeOperations
from Operations.StudentOperations import StudentOperations

import os

class CerinteCommon:
    def __init__(self):
        self.__cerinte = [{
            "nume": "Studenti",
            "func": self.handleStudents
        }, {
            "nume": "Probleme",
            "func": self.handleProbleme
        }, {
            "nume": "Asignare problema",
            "func": self.handleAsignareProblema
        }, {
            "nume": "Studentii cu media sub 5",
            "func": self.afisareStudentiNoteSub5
        }]

    def afisareStudentiNoteSub5(self, students, problems):
        commonOps = CommonOperations()
        stud = commonOps.getStudentiNoteSub5(students, problems)
        for st in stud:
            print(st[0])
            print(f'Medie: {st[1]}')
    
    def __str__(self):
        txt = ''
        for i in range(len(self.__cerinte)):
            txt += f'{i + 1}. {self.__cerinte[i]["nume"]}\n'
        txt += '\nx. Iesire\n'
        return txt
    
    def runOption(self, option, students, problems):
        if int(option) > len(self.__cerinte):
            raise ValueError
        try:
            option = int(option) - 1
            if option == 0:
                self.__cerinte[option]["func"](students)
            elif option == 1:
                self.__cerinte[option]["func"](problems)
            else:
                self.__cerinte[option]["func"](problems, students)    
        except ValueError:
            print("Datele introduse nu sunt valide!")
        except ArithmeticError:
            print("ID-ul ales exista deja in lista de studenti!")
        except LookupError:
            print("Nu exista niciun student cu acest id!")

    def waitForX(self):
        print()
        while True:
            x = input("x. Iesire\n")
            if x.lower() == "x":
                break
        
    
    def handleAsignareProblema(self, problems, students):
        problemUI = CerinteProbleme()
        problemUI.afisareProbleme(problems)
        print()
        idProblema = int(input("id problema: "))

        problemeOps = ProblemeOperations()
        problema = problems[problemeOps.findById(idProblema, problems)]

        studentUI = CerinteStudenti()
        studentUI.printStudents(students)
        print()
        idStudent = int(input("id student: "))

        studOps = StudentOperations()
        student = students[studOps.findById(students, idStudent)]

        commonOps = CommonOperations()
        commonOps.adaugareStudent(student, problema)


    def handleStudents(self, students):
        cerinte = CerinteStudenti()
        while True:
            try:
                os.system("clear")
                print(cerinte)
                option = input("Optiune: ")
                if option.lower() == "x":
                    break

                print()
                cerinte.runOption(option, students)
                cerinte.waitForX()
            except ValueError:
                print("Optiunea aleasa nu exista")

    def handleProbleme(self, problems):
        cerinte = CerinteProbleme()
        while True:
            try:
                os.system("clear")
                print(cerinte)
                option = input("Optiune: ")
                if option.lower() == "x":
                    break

                print()
                cerinte.runOption(option, problems)
                cerinte.waitForX()
            except ValueError:
                print("Optiunea aleasa nu exista")
