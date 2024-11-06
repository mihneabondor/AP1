import os
from UI.CerinteGeneral import CerinteGeneral

def main():
    students = []
    cerinteGeneral = CerinteGeneral()
    while True:
        try:
            os.system("clear")
            print(cerinteGeneral)
            option = input("Optiune: ")
            if option.lower() == "x":
                break
            cerinteGeneral.runOption(option, students)
        except ValueError:
            print("Optiunea aleasa nu exista")
main()