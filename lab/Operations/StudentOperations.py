from Domain.Student import Student

class StudentOperations:
    def modifyStudent(self, student, students):
        students[self.findById(students, student.getId())] = student
    
    def cautare(self, id, students):
        return students[self.findById(students, id)]

    def findById(self, students, id):
        for i in range(len(students)):
            if students[i].getId() == id:
                return i
        raise LookupError

    def addStudent(self, student, students):
        self.__idUnic(student, students)
        students.append(student)

    def __idUnic(self, student, students):
        for stud in students:
            if stud.getId() == student.getId():
                raise ArithmeticError