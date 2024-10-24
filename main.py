import os

def sortareNoteAlfabetic(allStudents):
    return sorted(allStudents, key= lambda x: (-x["nota"], x["nume"]))

def printStudentiNoteAlfabetic(allStudents):
    printStudents(sortareNoteAlfabetic(allStudents))

def medieStud(allStudents):
    sum = 0
    cont = 0
    for stud in allStudents:
        if getNota(stud) >= 5:
            sum += getNota(stud)
            cont += 1
    
    return sum / cont if cont else 0

def printMedieStud(allStudents):
    print("Media studentilor cu note peste 5 este ", medieStud(allStudents))

def printTopNStudenti(allStudents):
    try:
        n = int(input("Primii n: "))
        sortedStudents = sortareNoteDesc(allStudents)
        for i in range(n):
            printStudent(sortedStudents[i])
    except:
        print("Datele introduse nu sunt valide.")

def printStudentiNoteDesc(allStudents):
    printStudents(sortareNoteDesc(allStudents))

def sortareNoteDesc(allStudents):
    return sorted(allStudents, key= lambda x: x["nota"], reverse=True)

def deleteStudentNotaMaiMica5(allStudents):
    studsToBeDeleted = []
    for stud in allStudents:
        if getNota(stud) < 5:
            studsToBeDeleted.append(stud)
    for stud in studsToBeDeleted:
        allStudents.remove(stud)
    return allStudents

def printDeleteStudentNotaMaiMica5(allStudents):
    allStudents = deleteStudentNotaMaiMica5(allStudents)
    printStudents(allStudents)

def printStudentCuNumeInString(allStudents):
    string = input("string: ")
    for stud in allStudents:
        if string in getNume(stud):
            printStudent(stud)

def printStudentNotaMaiMare(allStudents):
    try:
        nota = int(input("Nota: "))
        for student in allStudents:
            if getNota(student) >= nota:
                printStudent(student)
    except:
        print("Datele introduse nu sunt valide.")

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

def printStudentNotaMax(allStudents):
    printStudents(getStudNotaMax(allStudents))

def deleteStudent(allStudents, id):
    student = next((stud for stud in allStudents if getId(stud) == id), None)
    if student is not None:
        allStudents.remove(student)
    return allStudents, student

def printDeleteStudent(allStudents):
    printStudents(allStudents)
    try:
        id = int(input("\nid: "))
        allStudents, student = deleteStudent(allStudents, id)

        if student is not None:
            print("A fost sters studentul " + getNume(student))
        else:
            print("Nu exista niciun student cu id-ul ", id)
    except:
        print("Datele introduse nu sunt valide")

def printOptions(options):
    os.system('clear')
    for i in range(len(options)):
        print(str(i + 1) + ". " + options[i]["nume"])
    print("x. Iesire\n")

def printStudent(student):
    print('\n')
    print("id: ", getId(student))
    print("nume: " + getNume(student))
    print("nota: " + getNota(student))

def printStudents(allStudents):
    for student in allStudents:
        printStudent(student)
    
def waitForX():
    print('\n')
    while True:
        print("x. Iesire")
        option = input()
        if option.lower() == 'x':
            break

def createStudent(id, nota, nume):
    return {"id": id, "nume": nume, "nota": nota}

def readStudent():
    try:
        id = int(input("id: "))
        nume = input("nume: ")
        nota = int(input("nota: "))
        return createStudent(id, nota, nume)
    except:
        print("Datele introduse nu sunt valide.")
        return

def idUnic(student, allStudents):
    for stud in allStudents:
        if getId(stud) == getId(student):
            return False
    return True

def addStudent(allStudents):
    student = readStudent()
    if student is not None and idUnic(student, allStudents):
        allStudents.append(student)

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

def main():
    allStudents = []
    options = [
        {
            "nume": "Afisare studenti",
            "func": printStudents
        },
        {
            "nume": "Adaugare student",
            "func": addStudent
        },
        {
            "nume": "Stergere student",
            "func": printDeleteStudent
        
        },
        {
            "nume": "Afisare student cu nota mai mare sau egala decat",
            "func": printStudentNotaMaiMare
        },
        {
            "nume": "Afisare student cu nota maxima",
            "func": printStudentNotaMax
        },
        {
            "nume": "Afisare student cu numele continut de un alt string",
            "func": printStudentCuNumeInString
        },
        {
            "nume": "Stergere student cu nota mai mica decat 5",
            "func": printDeleteStudentNotaMaiMica5
        },
        {
            "nume": "Sortare dupa note descrescator",
            "func": printStudentiNoteDesc
        },
        {
            "nume": "Primii n studenti dupa note",
            "func": printTopNStudenti
        },
        {
            "nume": "Media studentilor cu note peste 5",
            "func": printMedieStud
        },
        {
            "nume": "Sortare dupa nota si alfabetic",
            "func": printStudentiNoteAlfabetic
        }
    ]

    while True:
        printOptions(options)

        option = input("Optiune: ")

        if option.lower() == "x":
            break
        
        option = int(option) - 1
        options[option]["func"](allStudents)
        
        waitForX()

main()