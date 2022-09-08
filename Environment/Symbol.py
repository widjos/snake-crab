class Symbol:
    
    def __init__(self, id:str , value, type, parametros = None):
        self.id = id
        self.type = type
        self.value = value
        self.param = parametros

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def getParams(self):
        return self.param    