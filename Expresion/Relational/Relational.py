from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Enum.Dominant import RelationalDominant
from Enum.typeExpression import typeExpression
from Enum.typeOperation import typeOperation
from Environment.Contexto import listaErrores



class Relational(Expression):

     def __init__(self , leftExpr: Expression, rightExpr: Expression, operation: typeOperation, column, line): 
       self.leftExpr = leftExpr
       self.rightExpr = rightExpr
       self.operation  =  operation
       self.column = column
       self.row = line

     def execute(self, environment: Environment) -> Symbol:
        leftExpr = self.leftExpr.execute(environment)
        rightExpr = self.rightExpr.execute(environment)

        dominant = RelationalDominant[leftExpr.getType().value][rightExpr.getType().value]

        if self.operation == typeOperation.MAYOR:
            if dominant == typeExpression.BOOL:
               return Symbol("", leftExpr.getValue() > rightExpr.getValue(), typeExpression.BOOL)
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "No se puede realizar la operacion >" , "fila":  self.row , "columna": self.column })                                                
                return Symbol("", "Error no se puede realizar la operacion >", typeExpression.ERROR)
        elif self.operation == typeOperation.MENOR:
            if dominant == typeExpression.BOOL:
               return Symbol("", leftExpr.getValue() < rightExpr.getValue(), typeExpression.BOOL)
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "No se puede realizar la operacion MENORQUE" , "fila":  self.row , "columna": self.column })                                                
                return Symbol("", "Error no se puede realizar la operacion <" + str(self.column), typeExpression.ERROR)
        elif self.operation == typeOperation.GMAYOR:
            if dominant == typeExpression.BOOL:    
                return Symbol("", leftExpr.getValue() >= rightExpr.getValue(), typeExpression.BOOL)
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "No se puede realizar la operacion MAYORIGUAL" , "fila":  self.row , "columna": self.column })                                                
                return Symbol("", "Error no se puede la operacion >=", typeExpression.ERROR)
        elif self.operation == typeOperation.GMENOR:
            if dominant == typeExpression.BOOL:
                return Symbol("", leftExpr.getValue() <= rightExpr.getValue(), typeExpression.BOOL )
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "No se puede realizar la operacion MENORIGUAL" , "fila":  self.row , "columna": self.column })                                                
                return Symbol("", "Error no se puede relizar la operacion <= ", typeExpression.ERROR)
        elif self.operation == typeOperation.NIGUAL:
            if dominant == typeExpression.BOOL:
                return Symbol("", leftExpr.getValue() != rightExpr.getValue() , typeExpression.BOOL)
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "No se puede realizar la operacion NOIGUAL" , "fila":  self.row , "columna": self.column })                                                
                return Symbol("","Existe un error no se puede realizar la operacion != ", typeExpression.ERROR)
        elif self.operation == typeOperation.IGUAL:
            if dominant == typeExpression.BOOL:
                return Symbol("", leftExpr.getValue() == rightExpr.getValue() , typeExpression.BOOL)
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "No se puede realizar la operacion IGUAL" , "fila":  self.row , "columna": self.column })                                                
                return Symbol("","Existe un error no se puede realizar la operacion == ", typeExpression.ERROR)                          





