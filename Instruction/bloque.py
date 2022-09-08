from Environment.Environment import Environment
from Abstract.Instruction import Instrucction



class Bloque(Instrucction):
    def __init__(self,  lista , column , row) -> None:
        if lista != None:
            self.lista = lista
            self.column = column
            self.line = row
        else: 
            self.lista = []
            self.column = column
            self.line = row    


    def execute(self, environment: Environment):

        for instruction in self.lista:
            temp = instruction.execute(environment)

            if temp != None:
                return temp

        return None           