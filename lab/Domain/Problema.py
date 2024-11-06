class Problema:
    def __init__(self, lab, id, desc, deadline):
        self.__lab = lab
        self.__id = id
        self.__desc = desc
        self.__deadline = deadline
        self.__studenti = []

    def getLab(self):
        return self.__lab
    def setLab(self, lab):
        self.__lab = lab

    def getId(self):
        return self.__id
    def getLab(self, lab):
        self.__lab = lab

    def getDesc(self):
        return self.__desc
    def setDesc(self, desc):
        self.__desc = desc
    
    def getDeadline(self):
        return self.__deadline
    def setDeadline(self, deadline):
        self.__deadline = deadline

    def __str__(self):
        return f'id: {self.__id}\nlab: {self.__lab}\ndesc: {self.__desc}\ndeadline: {self.__deadline}'