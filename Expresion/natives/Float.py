from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Environment.Contexto import listaErrores

class Float(Expression):
    def __init__(self, expr: Expression , column, line) -> None:
       self.expr = expr
       self.column = column
       self.line = line


    def execute(self, environment: Environment) -> Symbol:

        exp = self.expr.execute(environment)

        if(exp.getType() == typeExpression.INT):
           return Symbol("", float(exp.getValue()), typeExpression.FLOAT)
        else:
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : "Error no se puede convertir a float por este tipo de dato"+str(exp.getType()), "fila":  self.line , "columna": self.column })                                                
            return Symbol("", "Error el tipo de dato " + str(exp.getType())+ "es incorrecto", typeExpression.ERROR)    
