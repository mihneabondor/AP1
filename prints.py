import main
import os
import domain
import calcule

def printStudentiNoteAlfabetic(allStudents):
    printStudents(calcule.sortareNoteAlfabetic(allStudents))

def printMedieStud(allStudents):
    print("Media studentilor cu note peste 5 este ", calcule.medieStud(allStudents))

def printTopNStudenti(allStudents):
    try:
        n = int(input("Primii n: "))
        sortedStudents = calcule.sortareNoteDesc(allStudents)
        for i in range(n):
            printStudent(sortedStudents[i])
    except ValueError:
        print("Datele introduse nu sunt valide.")

def printStudentiNoteDesc(allStudents):
    printStudents(calcule.sortareNoteDesc(allStudents))

def printDeleteStudentNotaMaiMica5(allStudents):
    allStudents = calcule.deleteStudentNotaMaiMica5(allStudents)
    printStudents(allStudents)

def printStudentCuNumeInString(allStudents):
    string = input("string: ")
    for stud in allStudents:
        if string in domain.getNume(stud):
            printStudent(stud)

def printStudentNotaMaiMare(allStudents):
    try:
        nota = int(input("Nota: "))
        for student in allStudents:
            if main.getNota(student) >= nota:
                printStudent(student)
    except ValueError:
        print("Datele introduse nu sunt valide.")

def printStudentNotaMax(allStudents):
    printStudents(domain.getStudNotaMax(allStudents))

def printOptions(options):
    os.system('clear')
    for i in range(len(options)):
        print(str(i + 1) + ". " + options[i]["nume"])
    print("x. Iesire\n")

def printStudent(student):
    print('\n')
    print("id: ", domain.getId(student))
    print("nume: ", domain.getNume(student))
    print("nota: ", domain.getNota(student))

def printStudents(allStudents):
    for student in allStudents:
        printStudent(student)

def deleteStudent(allStudents, id):
    student = next((stud for stud in allStudents if domain.getId(stud) == id), None)
    if student is None:
        raise(ValueError)
    allStudents.remove(student)
    return allStudents, student

def printDeleteStudent(allStudents):
    printStudents(allStudents)
    try:
        id = int(input("\nid: "))
        allStudents, student = deleteStudent(allStudents, id)
        print("A fost sters studentul " + domain.getNume(student))
    except ValueError:
        print("Datele introduse nu sunt valide")