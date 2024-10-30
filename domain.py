def getId(student):
    return student["id"]

def getNota(student):
    return student["nota"]

def getNume(student):
    return student["nume"]

def setId(student, id):
    student["id"] = id

def setNota(student, nota):
    student["nota"] = nota

def setNume(student, nume):
    student["nume"] = nume

def getStudNotaMax(allStudents):
    students = []
    nota = 0
    for stud in allStudents:
        if nota < getNota(stud):
            nota = getNota(stud)
            students = [stud]
        elif nota == getNota(stud):
            students.append(stud)
    return students