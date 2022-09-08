from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Environment.Contexto import listaErrores

class String(Expression):
    
    def __init__(self, expr : Expression , column , line) -> None:
        self.expr = expr
        self.column = column
        self.line = line

    def execute(self, environment: Environment) -> Symbol:
        expr = self.expr.execute(environment)

        if expr.getType() != typeExpression.ERROR :
            return Symbol("", str(expr.getValue()), typeExpression.STRING)
        else:
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : "Error la expresion no se puede convetir a string ", "fila":  self.line , "columna": self.column })                                               
            return Symbol("", "La expresion no se puede convertir en string", typeExpression.ERROR)    

