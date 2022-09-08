from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Enum.typeExpression import typeExpression
from math import log, log10
from Environment.Contexto import listaErrores


class Logaritmo(Expression):

#Type boolean 0 = log10  and 1 = log
    def __init__(self, expr: Expression, expr1:Expression=None , type=None, column=None, line=None ) -> None:
        if type: 
            self.expr = expr
            self.expr1 = expr1
            self.column = column
            self.type = type
            self.line = line 
        else: 
            self.expr = expr
            self.column = column
            self.type = type
            self.line = line            


    def execute(self, environment: Environment) -> Symbol:
        if self.type == False:
            exp = self.expr.execute(environment)
            if exp.getType() == typeExpression.INT or exp.getType() == typeExpression.FLOAT:
                return Symbol("", log10(exp.getValue()), typeExpression.FLOAT)
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "Tipo  de dato no es numerico", "fila":  self.line , "columna": self.column })                                                
                return Symbol("",+"Es un tipo incompatible para el log10 ", typeExpression.ERROR)
        else:
            exp = self.expr.execute(environment)
            exp2 = self.expr1.execute(environment)
            if exp.getType() == typeExpression.FLOAT or exp.getType() == typeExpression.INT:
                if exp2.getType() == typeExpression.INT or exp2.getType() == typeExpression.FLOAT:
                    return Symbol("", log(exp.getValue(),exp2.getValue()), typeExpression.FLOAT)
                else:
                    listaErrores.append({"tipo":"Error Semantico", "descripcion" : "Error no se puede operar por este tipo de dato"+str(exp2.getType()), "fila":  self.line , "columna": self.column })                                                
                    return Symbol("","Error no se puede operar por este tipo de dato"+str(exp2.getType()), typeExpression.ERROR )        
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "Error no se puede operar por este tipo de dato"+str(exp.getType()), "fila":  self.line , "columna": self.column })                                                
                return  Symbol("","Error no se puede operar por este tipo de dato"+str(exp.getType()), typeExpression.ERROR ) 
