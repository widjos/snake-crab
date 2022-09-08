from Enum.typeOperation import typeOperation
from Enum.typeExpression import typeExpression
from Enum.Dominant import Dominant2
from  Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Environment.Contexto import listaErrores


class Mult(Expression):

     def __init__(self , leftExpr: Expression, rightExpr: Expression, operation: typeOperation, column, line): 
       self.leftExpr = leftExpr
       self.rightExpr = rightExpr
       self.operation  =  operation
       self.column = column
       self.row = line

     def execute(self, environment: Environment) -> Symbol:
        leftValue = self.leftExpr.execute(environment)
        rightValue = self.rightExpr.execute(environment)

        dominant = Dominant2[leftValue.getType().value][rightValue.getType().value]

        if(self.operation == typeOperation.MULT):
            if(dominant == typeExpression.INT):
                return Symbol("", int(leftValue.getValue()) * int(rightValue.getValue()), typeExpression.INT)
            elif(dominant == typeExpression.FLOAT):
                return Symbol("" , float(leftValue.getValue()) * float(rightValue.getValue()), typeExpression.FLOAT)
            elif(dominant == typeExpression.STRING and rightValue.getType() == typeExpression.STRING):
                return  Symbol("" , leftValue.getValue() + rightValue.getValue(), typeExpression.STRING)
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "El tipo de dato no se puede multiplicar" , "fila":  self.row , "columna": self.column })                                                
                return Symbol("", "Error semantico no se puede puede multiplicar, en columna =" + str(self.column) +" , y fila = "+ str(self.row), typeExpression.ERROR )              
  
        elif(self.operation == typeOperation.POTENCIA):
            if(dominant == typeExpression.INT):
                return Symbol("", int(leftValue.getValue()) ^ int(rightValue.getValue()), typeExpression.INT)
            elif(dominant == typeExpression.FLOAT):
                return Symbol("" , float(leftValue.getValue()) ^ float(rightValue.getValue()), typeExpression.FLOAT)
            elif(dominant == typeExpression.STRING and rightValue.getType() == typeExpression.INT):
                return  Symbol("" , leftValue.getValue() * rightValue.getValue(), typeExpression.STRING) #Multiplicacion normal de Python                     
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "El tipo de dato no se puede realizar la potencia" , "fila":  self.row , "columna": self.column })                                                
                return Symbol("", "Error semantico no se puede puede realizar la potencia, en columna =" + str(self.column) +" , y fila = "+ str(self.row), typeExpression.ERROR )              
                        