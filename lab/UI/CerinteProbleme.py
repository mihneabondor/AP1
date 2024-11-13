from Operations.ProblemeOperations import ProblemeOperations
from Domain.Problema import Problema

class CerinteProbleme:
    def __init__(self):
        problemOps = ProblemeOperations()
        self.__cerinte = [{
            "nume" : "Afisare",
            "func" : self.afisareProbleme
        }, {
            "nume" : "Adaugare",
            "func" : self.adaugareProblema
        }, {
            "nume" : "Modificare",
            "func" : self.modificareProblema
        }, {
            "nume" : "Cautare",
            "func" : self.cautare
        }, {
            "nume" : "Afisare studenti atribuiti la o problema",
            "func" : self.afisareStudentiProblema
        }, {
            "nume" : "Notare problema",
            "func" : self.notareProblema
        }]

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
    
    def runOption(self, option, problems):
        if int(option) > len(self.__cerinte):
            raise ValueError
        try:
            option = int(option) - 1
            self.__cerinte[option]["func"](problems)
        except ValueError:
            print("Datele introduse nu sunt valide!")
        except ArithmeticError:
            print("ID-ul ales exista deja in lista de studenti!")
        except LookupError:
            print("Nu exista nicio problema cu acest id!")
    
    def __read(self):
        id = int(input("id: "))
        lab = int(input("lab: "))
        desc = input("descriere: ")
        deadline = input("deadline: ")
        return Problema(lab, id, desc, deadline)
    
    def adaugareProblema(self, problems):
        problemOps = ProblemeOperations()
        problema = self.__read()
        problemOps.adaugareProblema(problema, problems)
    
    def afisareProbleme(self, problems):
        for prob in problems:
            print(prob)
            print()

    def modificareProblema(self, problems):
        self.afisareProbleme(problems)
        problema = self.__read()
        problemOps = ProblemeOperations()
        problemOps.modificareProblema(problema, problems)

    def cautare(self, problems):
        id = int(input("id: "))
        print()
        problemOps = ProblemeOperations()
        problema = problemOps.cautare(id, problems)
        print(problema)
    
    def afisareStudentiNota(self, students):
        for stud in students:
            print(stud["student"])
            if stud["nota"] is not None:
                print(f'Nota: {stud["nota"]}')
            else:
                print("Nota: nedefinit")
            print()

    def getStudent(self, problems):
        self.afisareProbleme(problems)
        id = int(input("id: "))
        return id
    
    def afisareStudentiProblema(self, problems):
        problemOps = ProblemeOperations()
        tuples, id = problemOps.getStudent(self.getStudent(problems), problems)
        studenti = problemOps.sortareStudentiNota(tuples)
        self.afisareStudentiNota(studenti)

    def notareProblema(self, problems):
        problemOps = ProblemeOperations()
        tuples, id = problemOps.getStudent(self.getStudent(problems), problems)
        print()
        self.afisareStudentiNota(tuples)
        print()
        idStudent = int(input("id student: "))
        nota = int(input("nota: "))
        problemOps.notareProblema(id, idStudent, tuples, nota, problems)
    