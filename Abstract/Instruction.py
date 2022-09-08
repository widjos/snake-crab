from abc import ABC , abstractmethod
from Environment.Environment import Environment 

class Instrucction(ABC):
    @abstractmethod
    def  execute(self, environment: Environment):
        pass