from abc import ABC, abstractmethod

class Fracao(ABC):

    def __init__(self, num, den):
        self.__num = num
        self.__den = den
    
    @abstractmethod
    def __str__(self):
        pass

    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den

    def simplifica(self):
        divComum = a.mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum