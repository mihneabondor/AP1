from Domain.Problema import Problema
from Operations.StudentOperations import StudentOperations

class ProblemeOperations:
    def notareProblema(self, problems):
        tuples, id = self.getStudenti(problems)
        print()
        self.__afisareStudentiNota(tuples)
        print()
        idStudent = int(input("id student: "))
        nota = int(input("nota: "))

        problems[self.findById(id, problems)].setStudents(self.modificareNota(tuples, idStudent, nota))

    def modificareNota(self, students, idStudent, nota):
        for stud in students:
            if stud["student"].getId() == idStudent:
                stud["nota"] = nota
        return students

    def afisareStudenti(self, problems):
        tuples, id = self.getStudenti(problems)
        self.__afisareStudentiNota(self.__sortareStudentiNota(tuples))

    def __sorting_keys(self, entry):
        nume = entry["student"].getNume()
        nota = entry["nota"] if entry["nota"] is not None else float('-inf')
        return (-nota, nume) 

    def __sortareStudentiNota(self, studenti):
        return sorted(studenti, key = self.__sorting_keys)

    def getStudenti(self, problems):
        self.afisareProbleme(problems)
        id = int(input("id: "))
        return problems[self.findById(id, problems)].getStudents(), id

    
    def __afisareStudentiNota(self, students):
        for stud in students:
            print(stud["student"])
            if stud["nota"] is not None:
                print(f'Nota: {stud["nota"]}')
            else:
                print("Nota: nedefinit")
            print()

    def modificareProblema(self, problems):
        self.afisareProbleme(problems)
        problema = self.__read()
        problems[self.findById(problema.getId(), problems)] = problema

    def cautare(self, problems):
        id = int(input("id: "))
        print()
        print(problems[self.findById(id, problems)])
        
    def findById(self, id, problems):
        for i in range(len(problems)):
            if problems[i].getId() == id:
                return i
        raise LookupError

    def adaugareProblema(self, problems):
        problema = self.__read()
        self.__idUnic(problema, problems)
        problems.append(problema)

    def afisareProbleme(self, problems):
        for prob in problems:
            print(prob)
            print()

    def __read(self):
        id = int(input("id: "))
        lab = int(input("lab: "))
        desc = input("descriere: ")
        deadline = input("deadline: ")
        return Problema(lab, id, desc, deadline)
    
    def __idUnic(self, problema, problems):
        for prob in problems:
            if prob.getId == problema.getId:
                raise ArithmeticError