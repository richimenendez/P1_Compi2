from ast import *
from values import * 

class Expresion(Nodo):
    def __init__(self,val1,val2):
        self.val1 = val1 
        self.val2 = val2


class Suma(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
            val3 = v1.value + v2.value 
            return Valor(val3, TIPO.ENTERO)
        elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
            val3 = v1.value + v2.value 
            return Valor(val3, TIPO.DOBLE)
        else:
            print("Error")

class Resta(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
            val3 = v1.value - v2.value 
            return Valor(val3, TIPO.ENTERO)
        elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
            val3 = v1.value - v2.value 
            return Valor(val3, TIPO.DOBLE)
        else:
            print("Error")

class Multi(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
            val3 = v1.value * v2.value 
            return Valor(val3, TIPO.ENTERO)
        elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
            val3 = v1.value * v2.value 
            return Valor(val3, TIPO.DOBLE)
        else:
            print("Error")

class Divi(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
            val3 = v1.value / v2.value 
            return Valor(val3, TIPO.ENTERO)
        elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
            val3 = v1.value / v2.value 
            return Valor(val3, TIPO.DOBLE)
        else:
            print("Error")



#                   OPERACIONES RELACIONALES

class Igual(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
            val3 = v1.value == v2.value
            print(int(1)) 
            return Valor(val3*1, TIPO.ENTERO)
        elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
            val3 = v1.value / v2.value 
            return Valor(val3, TIPO.DOBLE)
        else:
            print("Error")