from Environment.Environment import Environment


from Abstract.Instruction import Instrucction
from Environment.Contexto import executeContext , listaErrores
from Enum.typeInstruction import typeInstruc


class Continue(Instrucction):
    def __init__(self, column , row) -> None:
        self.column = column
        self.row = row


    def execute(self, environment: Environment):
        if  len(executeContext) != 0 :
            if executeContext[-1] == typeInstruc.CICLO :
                return self  
        else:
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : "El CONTINUE no se encuentra en un ciclo" , "fila":  self.row , "columna": self.column })                                                
            print("El continue no se encuentra en un ciclo")
            return None     