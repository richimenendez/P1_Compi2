from enum import Enum 

class TIPO(Enum):
    ENTERO = 1
    DOBLE = 2
    STRING = 3
    ARRAY = 4
    ERROR = 5
    PUNTERO = 6

class OPERACION_RELACIONAL(Enum):
    IGUAL = 1

class OPERACION(Enum):
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    MODULO = 5
    ABS = 6
    BNOT = 7
    BAND = 8
    BOR = 9
    BXOR = 10
    BL = 11
    BR = 12

class Valor():
    def __init__(self, value, tipo):
        self.tipo = tipo
        self.value = value

    def ejecutar(self, metodos, ts):
        if(self.tipo == TIPO.ENTERO):
            try:
                self.value = int(self.value)
            except:
                 errorSemantico.add("ErrorSemantico: No se puede convertir a Entero")
                 print("Error 1")
        elif(self.tipo == TIPO.DOBLE):
            try:
                self.value = float(self.value)
            except:
                errorSemantico.add("ErrorSemantico: No se puede convertir a Double")
                print("Error 2")
        elif(self.tipo == TIPO.STRING):
            try:
                self.value = self.value
            except:
                errorSemantico.add("ErrorSemantico: No se puede convertir a String")
        elif(self.tipo == TIPO.ERROR):
            try:
                self.value = self.value
            except:
                errorSemantico.add("ErrorSemantico: Se dio un error semantico!")
        return Valor(self.value, self.tipo)

