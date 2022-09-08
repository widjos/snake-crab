from Enum.typeExpression import typeExpression
from Environment.Environment import Environment 
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Environment.Contexto import listaErrores


class Typeof(Expression):

    def __init__(self, exp , column , row) -> None:
        self.exp = exp
        self.column = column
        self.row = row 

    def execute(self, environment: Environment) -> Symbol:
        expr = self.exp.execute(environment)
        if expr != None:
            return Symbol("", str(expr.getType()), typeExpression.STRING)
        else:
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : " La expresion no tiene un tipo de dato  definido", "fila":  self.row , "columna": self.column })           
            return Symbol("", "La expresion no tiene un tipo definido", typeExpression.ERROR)   