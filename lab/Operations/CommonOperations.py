from Operations.ProblemeOperations import ProblemeOperations
from Operations.StudentOperations import StudentOperations

class CommonOperations:
    def adaugareStudent(self, students, problems):
        problemOps = ProblemeOperations()
        problemOps.afisareProbleme(problems)
        idProblema = int(input("id problema: "))
        problema = problems[problemOps.findById(idProblema, problems)]

        studentOps = StudentOperations()
        studentOps.printStudents(students)
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