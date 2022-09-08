from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Environment.Contexto import listaErrores


class Trunc(Expression):
    def __init__(self , expr: Expression , column , row) -> Symbol:
        self.expr = expr
        self.column = column
        self.row = row 

    def execute(self, environment: Environment) -> Symbol:
        exp = self.expr.execute(environment)

        if exp.getType() == typeExpression.FLOAT:
            temp = str(exp.getValue())
            return Symbol("", int(temp.split(".",1)[0]), typeExpression.INT)
        else:
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : " La expresion no se puede truncar porque no es de tipo NUMERICO", "fila":  self.row , "columna": self.column })                       
            return Symbol("", "Error seemantico , no se puede truncar este tipo de dato", typeExpression.ERROR)
                   

