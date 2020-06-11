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

        try:
            if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value + v2.value 
                return Valor(val3, TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value + v2.value 
                return Valor(val3, TIPO.DOBLE)
            elif((v1.tipo==TIPO.STRING)&(v2.tipo==TIPO.STRING)):
                val3 = v1.value + v2.value 
                return Valor(val3, TIPO.STRING)
            else:
                print("Error")
        except:
            print("Error")

class Resta(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value - v2.value 
                return Valor(val3, TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value - v2.value 
                return Valor(val3, TIPO.DOBLE)
            else:
                print("Error")
        except:
            print("Error Critico")

class Multi(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value * v2.value 
                return Valor(val3, TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value * v2.value 
                return Valor(val3, TIPO.DOBLE)
            else:
                print("Error")
        except:
            print("Error Critico")


class Divi(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value / v2.value 
                return Valor(val3, TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value / v2.value 
                return Valor(val3, TIPO.DOBLE)
            else:
                print("Error")
        except:
            print("Error Critico")


class Rest(Expresion):
    def __init__(self,val1):
        super().__init__(val1,val1)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)):
                val3 = -v1.value 
                return Valor(val3, TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)):
                val3 = -v1.value 
                return Valor(val3, TIPO.DOBLE)
            else:
                print("Error")
        except:
            print("Error Critico")



#                   OPERACIONES RELACIONALES

class Igual(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value == v2.value
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value == v2.value 
                return Valor(val3, TIPO.ENTERO)
            else:
                print("Error")
        except:
            print("Error fatal")


class DesIgual(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value != v2.value
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value != v2.value 
                return Valor(int(val3), TIPO.DOBLE)
            else:
                print("Error")
        except:
            print("Error Critico")


class Mayor(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value > v2.value
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value > v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            else:
                print("Error")
        except:
            print("Error Critico")


class Menor(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value < v2.value
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value < v2.value 
                return Valor(int(val3), TIPO.DOBLE)
            else:
                print("Error")
        except:
            print("Error Critico")


class MayorI(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value >= v2.value
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value >= v2.value 
                return Valor(int(val3), TIPO.DOBLE)
            else:
                print("Error")
        except:
            print("Error Critico")


class MenorI(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value <= v2.value
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)&(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value <= v2.value 
                return Valor(int(val3), TIPO.DOBLE)
            else:
                print("Error")
        except:
            print("Error Critico")

#                   OPERACIONES LOGICAS


class Not(Expresion):
    def __init__(self,val1):
        super().__init__(val1)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)):
                if(v1.value==1):
                    return Valor(1,TIPO.ENTERO)
                elif(v1.value==0):
                    return Valor(1,TIPO.ENTERO)
                print("Error,no se puede negar")
            else:
                print("Error")
        except:
            print("Error Critico")

class And(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)&(v2.tipo==TIPO.ENTERO)):
                print(v1.value,v2.value)
                if((v1.value==1 or v1.value==0) and (v2.value==1 or v2.value ==0) ):
                    if(v1.value==1 and v2.value==1):
                        return Valor(1,TIPO.ENTERO)
                    else:
                        return Valor(0,TIPO.ENTERO)
                else:
                    print("Error, no es booleano2222")
            else:
                print("Error")
        except:
            print("Error Critico")

class Or(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        try:
            if((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.ENTERO)):
                if((v1.value==1 or v1.value==0) and (v2.value==1 or v2.value ==0) ):
                    if(v1.value==1 or v2.value==1):
                        return Valor(1,TIPO.ENTERO)
                    else:
                        return Valor(0,TIPO.ENTERO)
                else:
                    print("Error, no es booleano")
            else:
                print("Error")
        except:
            print("Error Critico")


class Xor(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        print(v1.value," -- ",v2.value)
        try:
            if((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.ENTERO)):
                if((v1.value==1 or v1.value==0) and (v2.value==1 or v2.value ==0) ):
                    if(v1.value== v2.value):
                        return Valor(0,TIPO.ENTERO)
                    else:
                        return Valor(1,TIPO.ENTERO)
                else:
                    print("Error, no es booleano")
            else:
                print("Error")
        except:
            print("Error Critico")


