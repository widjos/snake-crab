from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Enum.typeExpression import typeExpression
from Enum.typeOperation import typeOperation
from math import sin , cos ,tan , sqrt
from Environment.Contexto import listaErrores


class Trignometry(Expression):
    def __init__(self, exp: Expression , operation , column , line) -> None:
        self.exp = exp
        self.operation = operation
        self.column = column
        self.line = line

    def execute(self, environment: Environment) -> Symbol:
        
        exp = self.exp.execute(environment)

        if exp.getType() == typeExpression.INT or exp.getType() == typeExpression.FLOAT:
            if self.operation == typeOperation.SIN:
               return Symbol("", sin(exp.getValue()), typeExpression.FLOAT)
            elif self.operation == typeOperation.COS :
                return Symbol("", cos(exp.getValue()), typeExpression.FLOAT)
            elif self.operation == typeOperation.TAN: 
                return Symbol("", tan(exp.getValue()), typeExpression.FLOAT)
            elif self.operation == typeOperation.SQR:
                return Symbol("", sqrt(exp.getValue()), typeExpression.FLOAT)
        else:
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : "Error el tipo de la expresion es invalido"+str(exp.getType()), "fila":  self.line , "columna": self.column })                                   
            return Symbol("", "Error el tipo de la expresion es invalido"+str(exp.getType()), typeExpression.ERROR)                