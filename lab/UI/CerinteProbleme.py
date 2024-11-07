from Operations.ProblemeOperations import ProblemeOperations

class CerinteProbleme:
    def __init__(self):
        problemOps = ProblemeOperations()
        self.__cerinte = [{
            "nume" : "Afisare",
            "func" : problemOps.afisareProbleme
        }, {
            "nume" : "Adaugare",
            "func" : problemOps.adaugareProblema
        }, {
            "nume" : "Modificare",
            "func" : problemOps.modificareProblema
        }, {
            "nume" : "Cautare",
            "func" : problemOps.cautare
        }, {
            "nume" : "Afisare studenti atribuiti la o problema",
            "func" : problemOps.afisareStudenti
        }, {
            "nume" : "Notare problema",
            "func" : problemOps.notareProblema
        }]

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
    
    def runOption(self, option, problems):
        if int(option) > len(self.__cerinte):
            raise ValueError
        try:
            option = int(option) - 1
            self.__cerinte[option]["func"](problems)
        except ValueError:
            print("Datele introduse nu sunt valide!")
        except ArithmeticError:
            print("ID-ul ales exista deja in lista de studenti!")
        except LookupError:
            print("Nu exista nicio problema cu acest id!")
    