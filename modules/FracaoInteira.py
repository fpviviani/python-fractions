from modules import Fracao as f

class FracaoInteira(f.Fracao):

    def __init__(self, num, den):
        super().__init__(num, den)

    def __str__(self):
        if (self.getNum() == self.getDen()):
            return str(1)
        return str(self.getNum()) + "/" + str(self.getDen())
