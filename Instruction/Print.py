from math import acosh, asin
from Enum.typeExpression import typeExpression
from Abstract.Instruction import Instrucction
from Abstract.Expression import Expression
from Environment.Environment import  Environment
from Environment.Contexto import listaErrores , resultJolc



class Print(Instrucction):
    
    # true = salto , false = misma linea
    def __init__(self, exp, jump: bool, column, row) -> None:
        self.expr = exp
        self.jump = jump
        self.column = column
        self.row = row


    def execute(self, environment: Environment):        
        
        for expr in self.expr:
            exp = expr.execute(environment)
            if exp.getType() != typeExpression.ERROR:
                if self.jump :
                    resultJolc.append(str('\n'+str(exp.getValue())))
                    #print('\n'+str(exp.getValue()), end="")
                else:
                    resultJolc.append( str(exp.getValue())) 
                    #print(exp.getValue(), end="")    
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "Tipo de expresion no manejable" , "fila":  self.row , "columna": self.column })                                                
                print("Error tipo de expresion no manejable")

               
