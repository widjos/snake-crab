from Enum.typeInstruction import typeInstruc
from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Environment.Contexto import executeContext , listaErrores

class Id(Expression):
    def __init__(self, id, column, line) -> None:
        self.id = id
        self.column = column
        self.row = line 

    def execute(self, environment: Environment) -> Symbol:
        if len(executeContext) != 0 and executeContext[-1] == typeInstruc.CICLO:  #Verifica si el acceso al id es desde un ciclo
            tempG = environment.mainScope.getVariable(self.id)
            if  tempG != None:
                return tempG

        tempSymbol = environment.getVariable(self.id)
        if tempSymbol != None:
            return tempSymbol
        else:
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : "No existe la variable "+ str(id), "fila":  self.row , "columna": self.column })                                                
            return Symbol("", "No existe la variable "+ str(id), typeExpression.ERROR )      