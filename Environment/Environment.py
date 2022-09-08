#Describe el entorno de ejecucion 
from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
import enum



class Environment: 

    def __init__(self,father,mainScope = None ):
        #the dictionary stand for  symbol table 
        self.table = {}
        self.father = father
        if mainScope == None:
            self.mainScope = self
        else:
            self.mainScope = mainScope    

    def saveVarible(self, id:str , value, type: enum.Enum, param = None):        
        #if(self.table.get(id) != None):
        #    print("La variable "+ id + "ya existe")
        #    return
        tempVar = Symbol(id,value,type,param)
        self.table[id] = tempVar

    def getVariable(self, id:str ):
        tempEnv = self 
        while(tempEnv != None):
            if(tempEnv.table.get(id) != None):
                return tempEnv.table.get(id)
            tempEnv = tempEnv.father

        print("Error : la variable " + id + " no existe")
              
    def getScope(self):
        return self.mainScope