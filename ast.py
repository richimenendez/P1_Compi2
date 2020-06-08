from values import *
from simbolos import * 

errorSemantico = []

class Nodo:
    def ejecutar(self,metodos,ts):
        pass
    def graficar(self, metodos, ts):
        pass

class Tag(Nodo):
    # Esta clase permite guardar las instrucciones de las clases
    def __init__(self, nombre, instrucciones):
        self.instrucciones = instrucciones
        self.nombre = nombre

    def ejecutar(self, metodos, ts):
        print(self.nombre," :")
        for inst in self.instrucciones:
            inst.ejecutar(metodos,ts)
            if(isinstance(inst,Salto)):
                return 1
        return 0
    
    
class Print(Nodo):
    #Esta clase permite imprimir un valor.
    def __init__(self, valor):
        self.valor = valor

class Asignacion(Nodo):
    #Esta clase representa una asignación
    def __init__(self,variable, expresion):
        self.variable = variable
        self.expresion = expresion
    
    def ejecutar(self, metodos, ts):
        v1 = self.expresion.ejecutar(metodos,ts)
        if self.variable in metodos.variables:
            metodos.añadirVariable(self.variable,self.expresion.ejecutar(metodos,ts),"1,1")
            print("Nueva variable")
        else:
            metodos.añadirVariable(self.variable,self.expresion.ejecutar(metodos,ts),"1,1")
            print("Sobre escribiendo variable")
        print("La variable ",self.variable," = ",v1.value)

class Si(Nodo):
    #Esta clase representa un salto condicional
    def __init__(self, condicion, etiqueta):
        self.condicion = condicion
        self.etiqueta = etiqueta 

    def ejecutar(self, metodos, ts):
        cond = condicion.ejecutar(metodos,ts)
        if(cond.value == 1):
            pass
        else:
            pass

class Salto(Nodo):
    #Esta clase representa un salto normal
    def __init__(self,etiqueta):
        self.etiqueta = etiqueta

    def ejecutar(self, metodos, ts):
        flag = 0
        v = 1
        for x,y in metodos.metodos.items(): 
            if(x==self.etiqueta):
                flag =1
            if(flag==1):
                v = y.ejecutar(metodos,ts)
                if(v==1):
                    return 1

class NodoEntero(Nodo):
    #Esta clase representa cuando viene un valor entero
    def __init__(self, valor):
        self.valor = valor
    
    def ejecutar(self, metodos, ts):
        return Valor(self.valor, TIPO.ENTERO)
    

class NodoDouble(Nodo):
    #Esta clase representa cuando viene un valor entero
    def __init__(self, valor):
        self.valor = valor
    
    def ejecutar(self, metodos, ts):
        return Valor(self.valor, TIPO.DOBLE)
    

class NodoCadena(Nodo):
    #Esta clase representa cuando viene un valor entero
    def __init__(self, valor):
        self.valor = valor
    

class NodoArreglo(Nodo):
    #Esta clase representa cuando viene un valor entero
    def __init__(self, valor):
        pass

    
