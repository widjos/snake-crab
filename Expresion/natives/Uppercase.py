from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Environment.Contexto import listaErrores


class Uppercase(Expression):

    def __init__(self, exp , column , row) -> None:
        self.exp = exp
        self.column = column
        self.row = row 

    def execute(self, environment: Environment) -> Symbol:
        expr = self.exp.execute(environment)
        if expr.getType() == typeExpression.STRING :
            return Symbol("", str(expr.getValue()).upper(), typeExpression.STRING)
        else:
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : " La expresion no se puede convertir en mayusculas", "fila":  self.row , "columna": self.column })
            return Symbol("", "La expresion no se puede convertir en mayusculas", typeExpression.ERROR)    