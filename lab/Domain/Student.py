class Student:
    def __init__(self, nume, id, grupa):
        self.__nume = nume
        self.__id = id
        self.__grupa = grupa

    def getNume(self):
        return self.__nume
    def setNume(self, nume):
        self.__nume = nume

    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id
    
    def getGrupa(self):
        return self.__grupa
    def setGrupa(self, grupa):
        self.__grupa = grupa

    def __str__(self):
        return f'id: {self.__id}\nnume: {self.__nume}\ngrupa: {self.__grupa}\n'
        
