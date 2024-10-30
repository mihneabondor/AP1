import domain

def medieStud(allStudents):
    sum = 0
    cont = 0
    for stud in allStudents:
        if domain.getNota(stud) >= 5:
            sum += domain.getNota(stud)
            cont += 1
    
    return sum / cont if cont else 0

def sortareNoteDesc(allStudents):
    return sorted(allStudents, key= lambda x: x["nota"], reverse=True)

def sortareNoteAlfabetic(allStudents):
    return sorted(allStudents, key= lambda x: (-x["nota"], x["nume"]))

def deleteStudentNotaMaiMica5(allStudents):
    studsToBeDeleted = []
    for stud in allStudents:
        if domain.getNota(stud) < 5:
            studsToBeDeleted.append(stud)
    for stud in studsToBeDeleted:
        allStudents.remove(stud)
    return allStudents