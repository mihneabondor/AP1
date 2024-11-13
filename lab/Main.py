import os
from UI.CerinteCommon import CerinteCommon

def main():
    students = []
    problems = []
    cerinteGeneral = CerinteCommon()
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