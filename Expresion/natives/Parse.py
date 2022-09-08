from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Environment.Contexto import listaErrores


class Parse(Expression):
    
    def __init__(self, type: Expression , exp : Expression , column , line) -> None:
        self.type = type
        self.exp = exp
        self.column = column
        self.line = line

    def execute(self, environment: Environment) -> Symbol:
        type = self.type.execute(environment)
        exp = self.exp.execute(environment)

        if exp.getType() == typeExpression.STRING:
            if str(exp.getValue()).isnumeric():
                if type.getValue() == typeExpression.INT:    
                    return Symbol("", int(exp.getValue()), typeExpression.INT )
            elif '.' in exp.getValue():
                if exp.getValue().replace('.','',1).isdigit() :        
                    if type.getValue() == typeExpression.FLOAT:
                        return Symbol("", float(exp.getValue()), typeExpression.INT )
                else:
                    return    
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "No se puede parsear el tipo de expresion", "fila":  self.line , "columna": self.column })                                                
                return Symbol("", "Error semantico no se puede convertir la cadena", typeExpression.ERROR)    
        else:
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : "No se puede parsear el tipo de expresion", "fila":  self.line , "columna": self.column })                                                
            return Symbol("","Error semantico la cadena no se puede convertir a entero", typeExpression.ERROR ) 