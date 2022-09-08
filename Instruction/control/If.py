from Environment.Environment import Environment
from Abstract.Instruction import Instrucction



__author__  = "$Widjos"


class If(Instrucction):
    def __init__(self, condicionIf , bloque , colum , row ) -> None:
       self.cond = condicionIf
       self.actual= bloque
       self.column = colum
       self.row = row


    def execute(self, environment: Environment):
        self.cumplido = False
        for condicion in self.cond:
            result = condicion.execute(environment)
            if condicion.ejecutado : 
                self.cumplido = True
                if result != None :
                    print("Se  cumplio y encontro un break")
                    return result
                else:
                    return None