from Domain.Problema import Problema
from Operations.StudentOperations import StudentOperations

class ProblemeOperations:
    def notareProblema(self, id, idStudent, tuples, nota, problems):
        index = self.findById(id, problems)
        problems[index].setStudents(self.modificareNota(tuples, idStudent, nota))

    def modificareNota(self, students, idStudent, nota):
        for stud in students:
            if stud["student"].getId() == idStudent:
                stud["nota"] = nota
        return students

    def __sorting_keys(self, entry):
        nume = entry["student"].getNume()
        nota = entry["nota"] if entry["nota"] is not None else float('-inf')
        return (-nota, nume) 

    def sortareStudentiNota(self, studenti):
        return sorted(studenti, key = self.__sorting_keys)

    def getStudent(self, id, problems):
        return problems[self.findById(id, problems)].getStudents(), id

    def modificareProblema(self, problema, problems):
        id = self.findById(problema.getId(), problems)
        problems[id] = problema

    def cautare(self, id, problems):
        return problems[self.findById(id, problems)]
        
    def findById(self, id, problems):
        for i in range(len(problems)):
            if problems[i].getId() == id:
                return i
        raise LookupError

    def adaugareProblema(self, problema, problems):
        self.__idUnic(problema, problems)
        problems.append(problema)
    
    def __idUnic(self, problema, problems):
        for prob in problems:
            if prob.getId == problema.getId:
                raise ArithmeticError