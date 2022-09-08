from Instruction.transferencia.Break import Break
from Enum.typeInstruction import typeInstruc
from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Abstract.Instruction import Instrucction
from Abstract.Expression import Expression
from Environment.Contexto import listaErrores, executeContext

class While(Instrucction):

    def __init__(self, condicion:Expression, bloque:Instrucction, column, row) -> None:
        self.condicion = condicion
        self.block = bloque      
        self.column = column
        self.row = row

    
    def execute(self, environment: Environment):
        result = self.condicion.execute(environment)

        #Posterior validar el error si no retornar directamente 
        if result.getType() == typeExpression.BOOL: 
            isExecute = result.getValue()
            executeContext.append(typeInstruc.CICLO)
            while isExecute :
                temp = self.block.execute(Environment(environment, environment.mainScope))
                if temp != None:
                    if isinstance(temp, Break):
                        print("Se encontro un break")
                        executeContext.pop()
                        return None
                    #Aqui va el continue

                result = self.condicion.execute(environment)
                isExecute = result.getValue()
            #Al terminar el ciclo se debe sacar del contexto que esta dentor de un ciclo        
            executeContext.pop()      
        else:
            #El error en es que la condicion del while no es un booleando 
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : "La expresion del la coindicion no es de tipo BOOL" , "fila":  self.row , "columna": self.column })                                                                    
            print("Error no booleano")

        return None          
                    
