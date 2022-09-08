from Abstract.Expression import Expression
from Environment.Environment import Environment
from Abstract.Instruction import Instrucction



class CondicionIf(Instrucction):
    def __init__(self, exp: Expression , temp , ejecutado:bool , column , row) -> None:
        self.expr = exp
        self.temp = temp
        self.ejecutado = ejecutado
        self.column = column
        self.row = row;


    def execute(self, environment: Environment):
        result = self.expr.execute(environment)
        if result.getValue() :
           self.ejecutado = True
           return self.temp.execute(Environment(environment));          
        return None