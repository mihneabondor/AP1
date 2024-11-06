from domain import getId
from prints import printStudents, printOptions, printDeleteStudentNotaMaiMica5, printMedieStud, printStudentCuNumeInString, printStudentiNoteAlfabetic, printStudentiNoteDesc, printStudentNotaMaiMare, printStudentNotaMax, printTopNStudenti, printDeleteStudent
    
def waitForX():
    print('\n')
    while True:
        print("x. Iesire")
        option = input()
        if option.lower() == 'x':
            break

def createStudent(id, nota, nume):
    if not str(id).isnumeric() or not str(nota).isnumeric():
        raise(ValueError)
    return {"id": int(id), "nume": nume, "nota": int(nota)}

def readStudent():
    id = input("id: ")
    nume = input("nume: ")
    nota = input("nota: ")
    return createStudent(id, nota, nume)

def idUnic(student, allStudents):
    for stud in allStudents:
        if getId(stud) == getId(student):
            return False
    return True

def addStudent(allStudents):
    try:
        student = readStudent()
        if not idUnic(student, allStudents):
            raise(ValueError)
        allStudents.append(student)
    except ValueError:
        print("Datele introduse nu sunt valide")

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