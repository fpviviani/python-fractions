from modules import Fracao as f

class FracaoMista(f.Fracao):

    def __init__(self, inteiro, num, den):
        super().__init__(num, den)
        self.__int = inteiro

    def getInt(self):
        return self.__int

    def __str__(self):
        return str(self.__int) + " " + str(self.getNum()) + "/" + str(self.getDen())