from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Contexto import listaErrores

class Negativo(Expression):

    def __init__(self, expr:Expression, column , row) -> None:
        self.exp = expr
        self.column = column
        self.row = row

    def execute(self, environment: Environment) -> Symbol:
        temp = self.exp.execute(environment)
        if temp != None:
            if temp.getType() == typeExpression.FLOAT or temp.getType() == typeExpression.INT:
                return Symbol("" , - temp.getValue(),temp.getType())
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "Tipo de dato incorrecto para convertir a negativo", "fila":  self.row , "columna": self.column })                                                
                return Symbol("", "La expresion no tiene un tipo definido", typeExpression.ERROR)    
