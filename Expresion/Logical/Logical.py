from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Enum.Dominant import LogicDominant
from Enum.typeExpression import typeExpression
from Enum.typeOperation import typeOperation
from Environment.Contexto import listaErrores


class Logical(Expression):
    
    def __init__(self, leftExpr: Expression , rightExpr: Expression , operation: typeOperation, column, line):
        self.leftExpr = leftExpr
        self.rightExpr = rightExpr
        self.operation  =  operation
        self.column = column
        self.line = line


    def execute(self, environment: Environment) -> Symbol:
        leftExpr = self.leftExpr.execute(environment)
        rightExpr = self.rightExpr.execute(environment)
        
        dominant = LogicDominant[leftExpr.getType().value][rightExpr.getType().value] 

        if self.operation == typeOperation.AND:
            if dominant == typeExpression.BOOL:
                return Symbol("", leftExpr.getValue() and rightExpr.getValue(), typeExpression.BOOL)
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "No se puede realizar la operacion AND "+ str(dominant) , "fila":  self.line , "columna": self.column })                                                
                return Symbol("","Error no se puede realizar la operacion AND ", typeExpression.ERROR)
        elif self.operation == typeOperation.OR:
            if dominant == typeExpression.BOOL:
                return Symbol("", leftExpr.getValue() or rightExpr.getValue(), typeExpression.BOOL)
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : " No se puede realizar la operacion OR" + str(dominant) , "fila":  self.line , "columna": self.column })                                                
                return Symbol("", "Error no se puede realizar la operacion OR", typeExpression.ERROR)
