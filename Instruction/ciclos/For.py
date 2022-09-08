from Abstract.Expression import Expression
from Instruction.transferencia.Break import Break
from Instruction.bloque import Bloque
from Enum.typeExpression import typeExpression
from Environment.Rango import Rango
from Environment.Environment import Environment
from Abstract.Instruction import Instrucction
from  Environment.Contexto import executeContext , listaErrores
from  Enum.typeInstruction import typeInstruc

'''
 type = 1 ->  RANGO
 type = 2 ->  CADENA
 type = 3 ->  ARREGLO
'''

class IFor(Instrucction):

    def __init__(self, iterador, rango , bloque: Bloque, column, row) -> None:
        self.iterador = iterador
        self.rango = rango
        self.bloque = bloque
        self.column = column
        self.row = row


    def execute(self, environment: Environment):
        
        #For con rango de numeros  ej: 1:5
        encabezado = Environment(environment)
        if  isinstance(self.rango, Rango):  
            executeContext.append(typeInstruc.CICLO)
            #De menor a mayor
            if self.rango.isLowHight():
                 print("Guardar la variable con el inicio")   
                 encabezado.saveVarible(self.iterador , self.rango.getInicio(), typeExpression.INT) #Se guarda la varibl en el encabezado 
                 #Inicia el ciclo con un true 
                 resultado = True
                 while resultado:
                     # 
                     temp = self.bloque.execute(Environment(encabezado, encabezado.mainScope))
                     simbol = encabezado.getVariable(self.iterador)
                     if simbol != None:
                        encabezado.saveVarible(self.iterador, simbol.getValue()+1 ,typeExpression.INT) 
                        resultado = self.rango.stillLow(simbol.getValue()+1)
                        if temp != None:
                            if isinstance(temp, Break):
                                print("Se encontro un break")
                                executeContext.pop()
                                return None
                    #Aqui va el del continue     
                     else :
                        listaErrores.append({"tipo":"Error Semantico", "descripcion" : "la variable no existe en el entorno" , "fila":  self.row , "columna": self.column })                                                
                        print("la variable no existe")
                 #Al terminar el ciclo se debe sacar del contexto que esta dentor de un ciclo        
                 executeContext.pop()            
            else:
                executeContext.pop()         
        elif isinstance(self.rango , Expression):
            expTemp = self.rango.execute(encabezado)
            #Se espera que el typo de la expresion que sera el rango sea una cadena
            if expTemp.getType() == typeExpression.STRING:
                executeContext.append(typeInstruc.CICLO)   
                print("Se va iterar sobre una cadena ")
                valorInicio = 0;
                valorFinal = len(expTemp.getValue()) - 1
                
                looping = True
                while looping: 
                    #Se guarda la varibale iterable en el scope del encabezado del for con su valor  0 
                    encabezado.saveVarible(self.iterador , expTemp.getValue()[valorInicio], typeExpression.CHAR)
                    #Se ejecuta el bloque de codigo dentro del For
                    temp = self.bloque.execute(Environment(encabezado, encabezado.mainScope))
                    valorInicio += 1
                    looping = valorFinal >= valorInicio
                    if temp != None:
                        if isinstance(temp, Break):
                            print("Se encontro un break as")
                            executeContext.pop()
                            return None
                #Al terminar el ciclo se debe sacar del contexto que esta dentor de un ciclo        
                executeContext.pop()  
            else:
                listaErrores.append({"tipo":"Error Semantico", "descripcion" : "El tipo de expresion es invalido para iterar" , "fila":  self.row , "columna": self.column })                                                
                print("Error tipo de expresion invalidad para iterar")    
        return