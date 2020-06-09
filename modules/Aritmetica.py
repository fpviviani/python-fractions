from modules import FracaoMista as fm
from modules import FracaoInteira as fi

def mdc(m, n):
    while m%n != 0:
        oldM = m
        oldN = n
        m = oldN
        n = oldM%oldN
    return n

def mmc(m, n):
    if (m > n):
        maior = m
    else:
        maior = n

    for i in range(maior+1):
        if(i == 0):
            pass
        else:
            aux = m * i
            if ((aux % n) == 0):
                return aux

def mesmaFracao(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())

def __add__(frac, outraFrac):
    if(type(frac) is fm.FracaoMista):
        mmcNumber = mmc(frac.getDen(), outraFrac.getDen())
        novoInt = frac.getInt() + outraFrac.getInt()
        novoNum = (outraFrac.getNum() * frac.getDen()) + (frac.getNum() * outraFrac.getDen())

        if (novoNum > mmcNumber):
            intAux = novoNum // mmcNumber
            resto = novoNum % mmcNumber
            return fm.FracaoMista((novoInt+intAux), resto, mmcNumber)
        else:
            return fm.FracaoMista(novoInt, novoNum, mmcNumber)

    else:
        novoNum = frac.getNum() * outraFrac.getDen() + frac.getDen() * outraFrac.getNum()
        novoDen = frac.getDen() * outraFrac.getDen()
        divComum = mdc(novoNum, novoDen)
        if (((novoNum//divComum) / (novoDen//divComum)) < 1):
            return fi.FracaoInteira(novoNum//divComum, novoDen//divComum)
        else:
            resto = (novoNum//divComum) % (novoDen//divComum)
            if (resto == 0):
                return fi.FracaoInteira(novoNum//divComum, novoDen//divComum)
            else:
                inteiro = (novoNum//divComum) // (novoDen//divComum)
                return fm.FracaoMista(inteiro, resto, novoDen//divComum)