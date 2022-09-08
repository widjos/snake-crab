from Abstract.Expression import Expression


class Rango:

    def __init__(self, inicio , fin) -> None:
        self.inicio = inicio
        self.fin = fin 

    def getInicio(self):
        return self.inicio

    def getFin(self):
        return self.fin 

    def isLowHight(self ) -> bool:
        return   self.inicio < self.fin  

    def stillLow(self, inicio):
        return inicio <= self.fin          