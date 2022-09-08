from Enum.typeInstruction import typeInstruc
from Enum.typeExpression import typeExpression
from Abstract.Instruction import Instrucction
from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Contexto import executeContext, listaErrores



class Asignacion(Instrucction):
    
    # expression is  None there is no validation of type
    def __init__(self, name, value: Expression , typExp: Expression, column ,row  ) -> None:
        self.name = name
        self.value = value
        self.typExp = typExp
        self.column = column
        self.row = row


    def execute(self, environment: Environment):
        exp = self.value.execute(environment) #Hay que validar si es un id 
        if exp.getType() != typeExpression.ERROR:
            if self.typExp != None:
                tempType = self.typExp.execute(environment)    
                if exp.getType() == tempType.getValue():
                    if len(executeContext) != 0 and executeContext[-1] == typeInstruc.CICLO:  #Verifica si el acceso al id es desde un ciclo
                        environment.mainScope.saveVarible(self.name, exp.getValue(), exp.getType())
                        return
                    environment.saveVarible(self.name, exp.getValue(), exp.getType())
                else:
                    #Aqui se guarda el error porque no se puede realizar la asignacion ni guardado
                    listaErrores.append({"tipo":"Error Semantico", "descripcion" : "No se puede relizar la asignacion de variable , los tipos no coinciden" , "fila":  self.row , "columna": self.column })                                                
                    print("No se puede relizar la asignacion de variable , los tipos no coinciden")
            else:
                if len(executeContext) != 0 and executeContext[-1] == typeInstruc.CICLO:  #Verifica si el acceso al id es desde un ciclo
                    environment.mainScope.saveVarible(self.name, exp.getValue(), exp.getType())
                    return
                environment.saveVarible(self.name, exp.getValue(), exp.getType())
                print("Varibale guardada en el entorno actual ")
        else:
            #Guardar el error 
            listaErrores.append({"tipo":"Error Semantico", "descripcion" : "No se puede almacenar la variable" + str(self.name) , "fila":  self.row , "columna": self.column })                                                
            print("Existe un error en la expresion que quiere almacenar en la variable " + str(self.name) )        
            





