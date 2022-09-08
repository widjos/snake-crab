from Enum.typeOperation import typeOperation
from Enum.typeExpression import typeExpression
from Enum.Dominant import Dominant
from  Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Environment.Contexto import listaErrores


class Add(Expression):

    def __init__(self , leftExpr: Expression, rightExpr: Expression, operation: typeOperation, column, line): 
       self.leftExpr = leftExpr
       self.rightExpr = rightExpr
       self.operation  =  operation
       self.column = column
       self.row = line  

    def execute(self, environment: Environment) -> Symbol:
        leftValue = self.leftExpr.execute(environment)
        rightValue = self.rightExpr.execute(environment)

        dominant = Dominant[leftValue.getType().value][rightValue.getType().value]
        
        if(self.operation == typeOperation.SUMA):
            if(dominant == typeExpression.INT):
                return Symbol("", int(leftValue.getValue())+ int(rightValue.getValue()), typeExpression.INT)

            elif(dominant == typeExpression.FLOAT):
                return Symbol("" , float(leftValue.getValue()) + float(rightValue.getValue()), typeExpression.FLOAT)

            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "El tipo de dato no se puede sumar" , "fila":  self.row , "columna": self.column })                                                
                return Symbol("", "Error semantico no se puede sumar, en columna =" + str(self.column) +" , y fila = "+ str(self.row), typeExpression.ERROR )              
        
        elif(self.operation == typeOperation.RESTA):
            if(dominant == typeExpression.INT):
                return Symbol("", int(leftValue.getValue()) - int(rightValue.getValue()), typeExpression.INT)

            elif(dominant == typeExpression.FLOAT):
                return Symbol("" , float(leftValue.getValue()) - float(rightValue.getValue()), typeExpression.FLOAT)

            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "El tipo de dato no se puede restar" , "fila":  self.row , "columna": self.column })                                                
                return Symbol("", "Error semantico no se puede resta, en columna =" + str(self.column) +" , y fila = "+ str(self.row), typeExpression.ERROR )              
        
        elif(self.operation == typeOperation.DIVISION):
            if(dominant == typeExpression.INT):
                return Symbol("", int(leftValue.getValue()) / int(rightValue.getValue()), typeExpression.INT)

            elif(dominant == typeExpression.FLOAT):
                return Symbol("" , float(leftValue.getValue()) / float(rightValue.getValue()), typeExpression.FLOAT)

            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "El tipo de dato no se puede dividir" , "fila":  self.row , "columna": self.column })                                                
                return Symbol("", "Error semantico no se puede resta, en columna =" + str(self.column) +" , y fila = "+ str(self.row), typeExpression.ERROR )              
        
        elif(self.operation == typeOperation.MODULO):
            if(dominant == typeExpression.INT):
                return Symbol("", int(leftValue.getValue()) % int(rightValue.getValue()), typeExpression.INT)

            elif(dominant == typeExpression.FLOAT):
                return Symbol("" , float(leftValue.getValue()) % float(rightValue.getValue()), typeExpression.FLOAT)

            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "El tipo de dato no se puede realizar el modulo" , "fila":  self.row , "columna": self.column })                                                
                return Symbol("", "Error semantico no se puede resta, en columna =" + str(self.column) +" , y fila = "+ str(self.row), typeExpression.ERROR )              
                

        else:
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : "El tipo de dato no se puede realizar la operacion" , "fila":  self.row , "columna": self.column })                                                
            return Symbol("", "Error semantico no se pude operar", typeExpression.ERROR )

            
