from Domain.Problema import Problema

class ProblemeOperations:
    def modificareProblema(self, problems):
        self.afisareProbleme(problems)
        problema = self.__read()
        problems[self.findById(problema.getId(), problems)] = problema

    def cautare(self, problems):
        id = int(input("id: "))
        print()
        print(problems[self.findById(id, problems)])
        
    def findById(self, id, problems):
        for i in range(len(problems)):
            if problems[i].getId() == id:
                return i
        raise LookupError

    def adaugareProblema(self, problems):
        problema = self.__read()
        self.__idUnic(problema, problems)
        problems.append(problema)

    def afisareProbleme(self, problems):
        for prob in problems:
            print(prob)
            print()

    def __read(self):
        id = int(input("id: "))
        lab = int(input("lab: "))
        desc = input("descriere: ")
        deadline = input("deadline (dd/mm/yyyy): ")
        return Problema(lab, id, desc, deadline)
    
    def __idUnic(self, problema, problems):
        for prob in problems:
            if prob.getId == problema.getId:
                raise ArithmeticError