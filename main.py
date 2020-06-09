from modules import FracaoMista as fm
from modules import FracaoInteira as fi
from modules import Aritmetica as a

fracao1 = fi.FracaoInteira(7, 6)
fracao2 = fi.FracaoInteira(13, 7)
fracao3 = fi.FracaoInteira(1, 3)
fracao4 = fi.FracaoInteira(2, 3)
fracaoMista1 = fm.FracaoMista(3, 1, 2)
fracaoMista2 = fm.FracaoMista(4, 2, 3)

novaFracao1 = a.__add__(fracao1, fracao2)
print("7/6 + 13/7 = {}".format(novaFracao1.__str__()))
novaFracao2 = a.__add__(fracao3, fracao4)
print("1/3 + 2/3 = {}".format(novaFracao2.__str__()))
novaFracao3 = a.__add__(fracaoMista1, fracaoMista2)
print("3 1/2 + 4 2/3 = {}".format(novaFracao3.__str__()))

