from Domain.Student import Student

class StudentOperations:
    def modifyStudent(self, students):
        self.printStudents(students)
        student = self.__read()
        students[self.findById(students, student.getId())] = student
    
    def cautare(self, students):
        id = int(input("id: "))
        print()
        print(students[self.findById(students, id)])

    def findById(self, students, id):
        for i in range(len(students)):
            if students[i].getId() == id:
                return i
        raise LookupError

    def addStudent(self, students):
        student = self.__read()
        self.__idUnic(student, students)
        students.append(student)
    
    def printStudents(self, students):
        for stud in students:
            print(stud)

    def __idUnic(self, student, students):
        for stud in students:
            if stud.getId() == student.getId():
                raise ArithmeticError

    def __getStudent(self, id, nume, grupa):
        return Student(nume, id, grupa)
    
    def __read(self):
        id = int(input("id: "))
        nume = input("nume: ")   
        grupa = int(input("grupa: "))
        return self.__getStudent(id, nume, grupa)

