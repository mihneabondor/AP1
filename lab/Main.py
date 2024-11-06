import os
from UI.CerinteGeneral import CerinteGeneral

def main():
    students = []
    problems = []
    cerinteGeneral = CerinteGeneral()
    os.system("clear")
    while True:
        try:
            print(cerinteGeneral)
            option = input("Optiune: ")
            if option.lower() == "x":
                break
            cerinteGeneral.runOption(option, students, problems)
            if int(option) == 4:
                cerinteGeneral.waitForX()
            os.system("clear")
        except ValueError:
            print("Optiunea aleasa nu exista")
main()