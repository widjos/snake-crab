from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Enum.typeExpression import typeExpression
from Enum.typeOperation import typeOperation
from Environment.Contexto import listaErrores




class Not(Expression):
           
    def __init__(self, leftExpr: Expression  , operation: typeOperation, column, line):
        self.leftExpr = leftExpr
        self.operation  =  operation
        self.column = column
        self.line = line 


    def execute(self, environment: Environment) -> Symbol:
        
        leftExpr = self.leftExpr.execute(environment)

        if self.operation == typeOperation.NOT:
            if leftExpr.getType().value == 2:
                return Symbol("", not leftExpr.getValue(), typeExpression.BOOL)
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "la expresion no es de tipo BOOL" , "fila":  self.line , "columna": self.column })                                                
                return Symbol("", "Error en no se puede relizar la negacion NOT", typeExpression.ERROR)

