from main import createStudent, getStudNotaMax

def adaugareTest(allStudents):
    student = createStudent(1, 1, "mihnea")
    allStudents.append(student)
    assert(allStudents[0] == student)

def adaugareErrTest():
    try:
        student = createStudent("as", 1, "mihnea")
        assert(False)
    except ValueError:
        assert(True)

def studentNotaMaximaTest():
    studs = [createStudent(1, 1, "mihnea"), createStudent(2, 10, "alex"), createStudent(3, 8, "ana"), createStudent(4, 10, "alo")]
    students = getStudNotaMax(studs)
    assert(students == [createStudent(2, 10, "alex"), createStudent(4, 10, "alo")])

def stergereTest(allStudents):
    student = allStudents[0]
    allStudents.remove(student)
    assert(not student in allStudents)

def allTests(allStudents):
    adaugareTest(allStudents)
    adaugareErrTest()
    stergereTest(allStudents)
    studentNotaMaximaTest()