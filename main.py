import os

def sortareNoteAlfabetic(allStudents):
    return sorted(allStudents, key= lambda x: (x["nota"], x["nume"]))

def printStudentiNoteAlfabetic(allStudents):
    printStudents(sortareNoteAlfabetic(allStudents))

def medieStud(allStudents):
    sum = 0
    cont = 0
    for stud in allStudents:
        if stud["nota"] >= 5:
            sum += stud["nota"]
            cont += 1
    
    return sum / cont if cont else 0

def printMedieStud(allStudents):
    print("Media studentilor cu note peste 5 este " + str(medieStud(allStudents)))

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
    for stud in allStudents:
        if stud["nota"] < 5:
            allStudents.remove(stud)
    printStudents(allStudents)

def printStudentCuNumeInString(allStudents):
    string = input("string: ")
    for stud in allStudents:
        if string in stud["nume"]:
            printStudent(stud)

def printStudentNotaMaiMare(allStudents):
    try:
        nota = int(input("Nota: "))
        for student in allStudents:
            if student["nota"] >= nota:
                printStudent(student)
    except:
        print("Datele introduse nu sunt valide.")

def printStudentNotaMax(allStudents):
    nota = 0
    for stud in allStudents:
        nota = max(nota, stud["nota"])
    for stud in allStudents:
        if stud["nota"] == nota:
            printStudent(stud)

def deleteStudent(allStudents):
    printStudents(allStudents)
    try:
        id = int(input("\nid: "))
        student = next((stud for stud in allStudents if stud["id"] == id), None)
    
        if student is not None:
            allStudents.remove(student)
            print("A fost sters studentul " + student["nume"])
        else:
            print("Nu exista niciun student cu id-ul " + str(id))
    except:
        print("Datele introduse nu sunt valide")

def printOptions(options):
    os.system('clear')
    for i in range(len(options)):
        print(str(i + 1) + ". " + options[i]["nume"])
    print("x. Iesire\n")

def printStudent(student):
    print('\n')
    print("id: " + str(student["id"]))
    print("nume: " + student["nume"])
    print("nota: " + str(student["nota"]))

def printStudents(allStudents):
    for student in allStudents:
        printStudent(student)
    
def waitForX():
    print('\n')
    while True:
        print("x. Iesire")
        option = input()
        if option == "x" or option == "X":
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
        if stud["id"] == student["id"]:
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
            "func": deleteStudent
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
            "func": deleteStudentNotaMaiMica5
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

        if option == "x" or option == 'X':
            break
        
        option = int(option) - 1
        options[option]["func"](allStudents)
        
        waitForX()

main()