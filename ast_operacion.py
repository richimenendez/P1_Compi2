from ast import *
from values import * 

class Expresion(Nodo):
    def __init__(self,val1,val2):
        self.val1 = val1 
        self.val2 = val2


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''                CASTEOS
def calcularEntero(v1):
        if(v1.tipo==TIPO.ERROR):
            return v1
        elif(v1.tipo==TIPO.ENTERO):
            return v1
        elif(v1.tipo==TIPO.DOBLE):
            return Valor(int(v1.value),TIPO.ENTERO)
        elif(v1.tipo==TIPO.STRING):
            return Valor(ord(v1.value[0]),TIPO.ENTERO)        
        elif(v1.tipo==TIPO.ARRAY):
            for x,y in v1.value.items():
                if(y.tipo==TIPO.ERROR):
                    return y
                elif(y.tipo==TIPO.ENTERO):
                    return y
                elif(y.tipo==TIPO.DOBLE):
                    return Valor(int(y.value),TIPO.ENTERO)
                elif(y.tipo==TIPO.STRING):
                    return Valor(ord(y.value[0]),TIPO.ENTERO)
                elif(y.tipo==TIPO.ARRAY):
                    return calcularEntero(y)

class Cast2Int():
    def __init__(self,val1):
        self.val1 = val1
    
    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v = calcularEntero(v1)
        return v
        

def calcularDouble(v1):
        if(v1.tipo==TIPO.ERROR):
            return v1
        elif(v1.tipo==TIPO.ENTERO):
            return Valor((v1.value)/1.0,TIPO.DOBLE)
        elif(v1.tipo==TIPO.DOBLE):
            return v1
        elif(v1.tipo==TIPO.STRING):
            return Valor(ord(v1.value[0])/1.0,TIPO.DOBLE)        
        elif(v1.tipo==TIPO.ARRAY):
            for x,y in v1.value.items():
                if(y.tipo==TIPO.ERROR):
                    return y
                elif(y.tipo==TIPO.ENTERO):
                    return Valor((y.value)/1.0,TIPO.DOBLE)
                elif(y.tipo==TIPO.DOBLE):
                    return y
                elif(y.tipo==TIPO.STRING):
                    return Valor(ord(y.value[0])/1.0,TIPO.DOBLE)
                elif(y.tipo==TIPO.ARRAY):
                    return calcularEntero(y)

class Cast2Double():
    def __init__(self,val1):
        self.val1 = val1
    
    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v = calcularDouble(v1)
        return v
        


def calcularString(v1):
        if(v1.tipo==TIPO.ERROR):
            return v1
        elif(v1.tipo==TIPO.ENTERO):
            return Valor(chr(v1.value%255),TIPO.STRING)
        elif(v1.tipo==TIPO.DOBLE):
            return Valor(chr(int(v1.value)%255),TIPO.STRING)
        elif(v1.tipo==TIPO.STRING):
            return Valor((v1.value[0]),TIPO.STRING)        
        elif(v1.tipo==TIPO.ARRAY):
            for x,y in v1.value.items():
                if(y.tipo==TIPO.ERROR):
                    return y
                elif(y.tipo==TIPO.ENTERO):
                    return Valor(chr((y.value)%255),TIPO.STRING)
                elif(y.tipo==TIPO.DOBLE):
                    return Valor(chr(int(y.value)%255),TIPO.STRING)
                elif(y.tipo==TIPO.STRING):
                    return Valor((y.value[0]),TIPO.STRING)
                elif(y.tipo==TIPO.ARRAY):
                    return calcularEntero(y)

class Cast2Char():
    def __init__(self,val1):
        self.val1 = val1
    
    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v = calcularString(v1)
        return v
        



# ??????????????????????????????????????????????????????                OPERACIONES ARITMETICAS

class Suma(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)

        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
            if((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value + v2.value 
                return Valor(val3, TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value + v2.value 
                return Valor(val3, TIPO.DOBLE)
            elif((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value + v2.value 
                return Valor(val3, TIPO.DOBLE)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value + v2.value 
                return Valor(val3, TIPO.DOBLE)
            elif((v1.tipo==TIPO.STRING)and(v2.tipo==TIPO.STRING)):
                val3 = v1.value + v2.value 
                return Valor(val3, TIPO.STRING)
            else:
                return Valor("Imposible realizar Suma!",TIPO.ERROR)
        except:
            return Valor("Imposible realizar Suma!",TIPO.ERROR)

class Resta(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
            if((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value - v2.value 
                return Valor(val3, TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value - v2.value 
                return Valor(val3, TIPO.DOBLE)
            elif((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value - v2.value 
                return Valor(val3, TIPO.DOBLE)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value - v2.value 
                return Valor(val3, TIPO.DOBLE)
            else:
                return Valor("Imposible realizar Resta!",TIPO.ERROR)
        except:
            return Valor("Imposible realizar Resta!",TIPO.ERROR)

class Multi(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
            if((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value * v2.value 
                return Valor(val3, TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value * v2.value 
                return Valor(val3, TIPO.DOBLE)
            elif((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value * v2.value 
                return Valor(val3, TIPO.DOBLE)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value * v2.value 
                return Valor(val3, TIPO.DOBLE)
            else:
                return Valor("Imposible realizar MULTIPLICACION!",TIPO.ERROR)
        except:
            return Valor("Imposible realizar MULTIPLICACION!",TIPO.ERROR)


class Divi(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
            if((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value / v2.value 
                return Valor(val3, TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value / v2.value 
                return Valor(val3, TIPO.DOBLE)
            elif((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value / v2.value 
                return Valor(val3, TIPO.DOBLE)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value / v2.value 
                return Valor(val3, TIPO.DOBLE)
            else:
                return Valor("Imposible realizar División!",TIPO.ERROR)
        except:
            return Valor("Imposible realizar División!",TIPO.ERROR)


class Rest(Expresion):
    def __init__(self,val1):
        super().__init__(val1,val1)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        
        try:
            if((v1.tipo==TIPO.ENTERO)):
                val3 = -v1.value 
                return Valor(val3, TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)):
                val3 = -v1.value 
                return Valor(val3, TIPO.DOBLE)
            else:
                return Valor("Imposible realizar Negacion!",TIPO.ERROR)
        except:
            return Valor("Imposible realizar Negacion!",TIPO.ERROR)

class Absoluto(Expresion):
    def __init__(self,val1):
        super().__init__(val1,val1)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        
        try:
            if((v1.tipo==TIPO.ENTERO)):
                val3 = abs(v1.value) 
                return Valor(val3, TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)):
                val3 = abs(v1.value) 
                return Valor(val3, TIPO.DOBLE)
            else:
                return Valor("Imposible realizar Valor Absoluto!",TIPO.ERROR)
        except:
            return Valor("Imposible realizar Valor Absoluto!",TIPO.ERROR)



#                   OPERACIONES RELACIONALES

class Igual(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
            if((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value == v2.value
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value == v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value == v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value == v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.STRING)and(v2.tipo==TIPO.STRING)):
                val3 = v1.value == v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            else:
                return Valor("Imposible realizar comparación Igual!",TIPO.ERROR)
        except:
            return Valor("Imposible realizar comparación Igual!",TIPO.ERROR)


class DesIgual(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
            if((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value != v2.value
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value != v2.value 
                return Valor(int(val3), TIPO.DOBLE)
            elif((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value != v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value != v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.STRING)and(v2.tipo==TIPO.STRING)):
                val3 = v1.value != v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            else:
                return Valor("Imposible realizar comparación Desigual!",TIPO.ERROR)
        except:
            return Valor("Imposible realizar comparación Desigual!",TIPO.ERROR)


class Mayor(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
            if((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value > v2.value
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value > v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value > v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value > v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.STRING)and(v2.tipo==TIPO.STRING)):
                val3 = v1.value > v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            else:
                return Valor("Imposible realizar comparación Mayor!",TIPO.ERROR)
        except:
            return Valor("Imposible realizar comparación Mayor!",TIPO.ERROR)


class Menor(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
            if((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value < v2.value
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value < v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value < v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value < v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.STRING)and(v2.tipo==TIPO.STRING)):
                val3 = v1.value < v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            else:
                return Valor("Imposible realizar comparación Menor!",TIPO.ERROR)
        except:
            return Valor("Imposible realizar comparación Menor!",TIPO.ERROR)


class MayorI(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
            if((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value >= v2.value
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value >= v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value >= v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value >= v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.STRING)and(v2.tipo==TIPO.STRING)):
                val3 = v1.value >= v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            else:
                return Valor("Imposible realizar comparación Mayor!",TIPO.ERROR)
        except:
            return Valor("Imposible realizar comparación Mayor!",TIPO.ERROR)
         


class MenorI(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
            if((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value <= v2.value
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value <= v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.ENTERO)and(v2.tipo==TIPO.DOBLE)):
                val3 = v1.value <= v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.DOBLE)and(v2.tipo==TIPO.ENTERO)):
                val3 = v1.value <= v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            elif((v1.tipo==TIPO.STRING)and(v2.tipo==TIPO.STRING)):
                val3 = v1.value <= v2.value 
                return Valor(int(val3), TIPO.ENTERO)
            else:
                return Valor("Imposible realizar comparación MenorIGUAL!",TIPO.ERROR)
        except:
            return Valor("Imposible realizar comparación MenorIGUAL!",TIPO.ERROR)



# =====================================================================================================================      OPERACIONES LOGICAS


class Not(Expresion):
    def __init__(self,val1):
        super().__init__(val1)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        try:
            return Valor(not(v1.value), TIPO.ERROR)
        except:
            return Valor("Error, No se puede negar el numero!", TIPO.ERROR)

class And(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
                vr = v1.value and v2.value
                return Valor(vr,TIPO.ENTERO)    
        except:
                return Valor("Error, No se puede realizar el AND!", TIPO.ERROR)

class Or(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
                vr = v1.value or v2.value
                return Valor(vr,TIPO.ENTERO)    
        except:
                return Valor("Error, No se puede realizar el OR!", TIPO.ERROR)


class Xor(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
                vr = v1.value ^ v2.value
                return Valor(vr,TIPO.ENTERO)    
        except:
                return Valor("Error, No se puede realizar el XOR!", TIPO.ERROR)




# =====================================================================================================================      OPERACIONES BIT LOGICAS


class BNot(Expresion):
    def __init__(self,val1):
        super().__init__(val1)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        try:
            v = ~v1.value
            return Valor(v,TIPO.ENTERO)
        except:
            return Valor("Error, No se puede negar el numero!", TIPO.ERROR)


class BOr(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
                vr = v1.value | v2.value
                return Valor(vr,TIPO.ENTERO)    
        except:
                return Valor("Error, No se puede realizar el BitwiseOR!", TIPO.ERROR)

class BAnd(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
                vr = v1.value & v2.value
                return Valor(vr,TIPO.ENTERO)    
        except:
                return Valor("Error, No se puede realizar el BitwiseAnd!", TIPO.ERROR)

class BXor(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
                vr = v1.value ^ v2.value
                return Valor(vr,TIPO.ENTERO)    
        except:
                return Valor("Error, No se puede realizar el BitwiseOR!", TIPO.ERROR)

class BLeft(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
                vr = v1.value << v2.value
                return Valor(vr,TIPO.ENTERO)    
        except:
                return Valor("Error, No se puede realizar el BitwiseLeft!", TIPO.ERROR)

class BRight(Expresion):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)

    def ejecutar(self, metodos, ts):
        v1 = self.val1.ejecutar(metodos,ts)
        v2 = self.val2.ejecutar(metodos,ts)
        
        if(v1.tipo==TIPO.ERROR):
            return v1
        if(v2.tipo==TIPO.ERROR):
            return v2

        try:
                vr = v1.value >> v2.value
                return Valor(vr,TIPO.ENTERO)    
        except:
                return Valor("Error, No se puede realizar el BitwiseRight!", TIPO.ERROR)