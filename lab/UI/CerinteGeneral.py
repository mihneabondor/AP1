from UI.CerinteStudenti import CerinteStudenti
from UI.CerinteProbleme import CerinteProbleme
import os

class CerinteGeneral:
    def __init__(self):
        self.__cerinte = [{
            "nume": "Studenti",
            "func": self.handleStudents
        }, {
            "nume": "Probleme",
            "func": self.handleProbleme
        }, {
            "nume": "Statistici",
            "func": self.handleStudents
        }]
    
    def __str__(self):
        txt = ''
        for i in range(len(self.__cerinte)):
            txt += f'{i + 1}. {self.__cerinte[i]["nume"]}\n'
        txt += '\nx. Iesire\n'
        return txt
    
    def runOption(self, option, students):
        if int(option) > len(self.__cerinte):
            raise ValueError
        try:
            option = int(option) - 1
            self.__cerinte[option]["func"](students)
                
        except ValueError:
            print("Datele introduse nu sunt valide!")

    def handleStudents(self, students):
        cerinte = CerinteStudenti()
        while True:
            try:
                os.system("clear")
                print(cerinte)
                option = input("Optiune: ")
                if option.lower() == "x":
                    break

                print()
                cerinte.runOption(option, students)
                cerinte.waitForX()
            except ValueError:
                print("Optiunea aleasa nu exista")

    def handleProbleme(self, problems):
        cerinte = CerinteProbleme()
        while True:
            try:
                os.system("clear")
                print(cerinte)
                option = input("Optiune: ")
                if option.lower() == "x":
                    break

                print()
                cerinte.runOption(option, problems)
                cerinte.waitForX()
            except ValueError:
                print("Optiunea aleasa nu exista")
