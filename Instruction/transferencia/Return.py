from Abstract.Expression import Expression
from Environment.Environment import Environment
from Enum.typeInstruction import typeInstruc
from Abstract.Instruction import Instrucction
from Environment.Contexto import executeContext , listaErrores



class Return(Instrucction):
    def __init__(self, expresion:Expression , column, row) -> None:
        self.exp = expresion
        self.colum = column
        self.row = row

    def execute(self, environment: Environment):

        #Return con una expresion 
        if  len(executeContext) != 0 :
            if executeContext[-1] == typeInstruc.FUNCION :
                if self.exp != None:
                    print("-------> Retornara un exp")
                    return self.exp.execute(environment)
                else: 
                    return self
        else:
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : "El RETURN no se encuentra en una funcion" , "fila":  self.row , "columna": self.column })                                                
            print("El return no se encuentra en una funcion")

                                     