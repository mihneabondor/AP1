from Operations.StudentOperations import StudentOperations

class CerinteStudenti:
    def __init__(self):
        studentOps = StudentOperations()
        self.__cerinte = [{
            "nume": "Afisare studenti",
            "func": studentOps.printStudents
        }, {
            "nume": "Adaugare student",
            "func": studentOps.addStudent
        }, {
            "nume": "Modificare student",
            "func": studentOps.modifyStudent
        }, {
            "nume": "Cautare student",
            "func": studentOps.cautare
        },]

    def __str__(self):
        txt = ''
        for i in range(len(self.__cerinte)):
            txt += f'{i + 1}. {self.__cerinte[i]["nume"]}\n'
        txt += '\nx. Iesire\n'
        return txt
    
    def waitForX(self):
        print()
        while True:
            x = input("x. Iesire\n")
            if x.lower() == "x":
                break

    def getCerinteLength(self):
        return len(self.__cerinte)
    
    def runOption(self, option, students):
        if int(option) > len(self.__cerinte):
            raise ValueError
        try:
            option = int(option) - 1
            self.__cerinte[option]["func"](students)
        except ValueError:
            print("Datele introduse nu sunt valide!")
        except ArithmeticError:
            print("ID-ul ales exista deja in lista de studenti!")
        except LookupError:
            print("Nu exista niciun student cu acest id!")
