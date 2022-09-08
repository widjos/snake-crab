from Environment.Primitive import Primitive
from Instruction.transferencia.Return import Return
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Contexto import  executeContext , listaErrores
from Enum.typeInstruction import typeInstruc
from Funcion.Funcion import Funcion
from Instruction.Asignacion import Asignacion
from Enum.typeExpression import typeExpression

class CallFunction(Expression):

    def __init__(self, idFunction , parameter , column , row  ) -> None:
        self.id = idFunction
        self.param = parameter
        self.column = column
        self.row = row


    def execute(self, environment: Environment) -> Symbol:

        idTemp = ""
        params = self.param
        if  params != None:
            idTemp = self.id

            for exp in params:
                tempType = exp.execute(environment)    
                idTemp += "_" + str(tempType.getType())
            print("El id de la funcion es " + str(idTemp))
            actualFunct = environment.getVariable(idTemp)
            if actualFunct != None:
                executeContext.append(typeInstruc.FUNCION)
                if actualFunct.getType() == typeInstruc.FUNCION:
                    #Entonrno de la funcion
                    funcHead = Environment(environment, environment.mainScope)
                    if len(self.param) == len(actualFunct.getParams()):
                        contador = 0
                        for paramTemp in  actualFunct.getParams():
                            #Se crea un objeto asignacion para declarar todas las variables dentro del entorno de la funcion 
                            declarationTemp = Asignacion(paramTemp.getId() , self.param[contador], paramTemp.getType(), self.column ,self.rowpip  )
                            declarationTemp.execute(funcHead)
                            contador += 1

                        #Se ejecuta todo el codigo del bloque de instrucciones de la funcion 
                        resultadoTemp = actualFunct.getValue().execute(funcHead)
                        if resultadoTemp != None:
                        
                            if isinstance(resultadoTemp , Return):
                                executeContext.pop();
                                return Primitive("nothing", typeExpression.NOTHING) 
                            elif isinstance(resultadoTemp, Symbol):
                                executeContext.pop();
                                return resultadoTemp    
                        executeContext.pop();

                    else:
                        listaErrores.append({"tipo":"Error Semantico", "descripcion" : "El numero de parametros no coincide", "fila":  self.row , "columna": self.column })                                                
                
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "La funcion "+ idTemp + " no existe en este en el entorno" , "fila":  self.row , "columna": self.column })                                                
                                    
        else:
            funcTemp = environment.getVariable(self.id)
            if funcTemp != None:
                executeContext.append(typeInstruc.FUNCION)
                funcHead = Environment(environment, environment.mainScope)
                resultadoTemp = funcTemp.getValue().execute(funcHead)
                if resultadoTemp != None:
                    if isinstance(resultadoTemp , Return):
                        print("Return vacio entonces regresa un primitivo nothing")
                        executeContext.pop();
                        return Primitive("nothing", typeExpression.NOTHING) 
                    elif isinstance(resultadoTemp, Symbol):
                        executeContext.pop();
                        return resultadoTemp
                executeContext.pop();                            
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "La funcion "+ str(self.id) + " no existe en este en el entorno" , "fila":  self.row , "columna": self.column })                                                
                  

        return None            