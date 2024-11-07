from Operations.ProblemeOperations import ProblemeOperations
from Operations.StudentOperations import StudentOperations

class CommonOperations:
    def getStudentiNoteSub5(self, problems, students):
        studenti = []
        for stud in students:
            medie = self.__medieStudent(stud, problems)
            if medie > 0 and medie < 5:
                studenti.append((stud, medie))
        return studenti    

    def __medieStudent(self, student, problems):
        note = self.__getNoteStudent(student, problems)
        return sum(note)/len(note) if len(note) > 0 else 0
    
    def __getNoteStudent(self, student, problems):
        note = []
        for prob in problems:
            studenti = prob.getStudents()
            for stud in studenti:
                if stud["student"].getId == student.getId and stud["nota"] is not None:
                    note.append(int(stud["nota"]))
        return note

    def adaugareStudent(self, students, problems):
        problemOps = ProblemeOperations()
        problemOps.afisareProbleme(problems)
        print()
        idProblema = int(input("id problema: "))
        problema = problems[problemOps.findById(idProblema, problems)]

        studentOps = StudentOperations()
        studentOps.printStudents(students)
        print()
        idStudent = int(input("id student: "))
        student = students[studentOps.findById(students, idStudent)]

        assignedStudents = problema.getStudents()
        self.__idUnic(student, assignedStudents)
        assignedStudents.append({
            "student": student,
            "nota": None
        })
        problema.setStudents(assignedStudents)

    def __idUnic(self, student, students):
        for stud in students:
            if stud["student"].getId() == student.getId():
                raise ArithmeticError