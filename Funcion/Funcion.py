from Enum.typeInstruction import typeInstruc
from Enum.typeExpression import typeExpression
from Abstract.Instruction import Instrucction
from Environment.Environment import Environment



class Funcion(Instrucction):
    def __init__(self, idFuncion , parametros , code, column, row) -> None:
       self.idFuncion = idFuncion
       self.parametros = parametros
       self.bloque = code
       self.column = column
       self.row = row


    def execute(self, environment: Environment):
        tempParam = self.parametros    
        if tempParam != None:
            for varid in  tempParam:
                self.idFuncion += "_" + str(varid.getType().value)
                
            environment.saveVarible(self.idFuncion, self.bloque, typeInstruc.FUNCION, tempParam)
            print("Se guardo una funcion con parametros nombre :" + str(self.idFuncion))
            return None

        else:    
            environment.saveVarible(self.idFuncion, self.bloque, typeInstruc.FUNCION)
            print("Se guardo una funcion en el entorno actual")
            return None
