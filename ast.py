from values import *
from simbolos import * 
import tkinter
from tkinter import simpledialog
from tkinter.messagebox import showinfo
import re

errorSemantico = []

class Nodo:
    def ejecutar(self,metodos,ts):
        pass
    def graficar(self, metodos, ts):
        pass

class Root(Nodo):
    def __init__(self,inst):
        self.inst = inst 

    def ejecutar(self,metodos, ts):
        for x,y in self.inst.items():
            metodos.metodos[x] = y 
        nodo = self.inst.get("main")
        if(nodo!=None):
            v = 0
            for x,y in self.inst.items(): 
                if(x=="main"):
                    flag =1
                if(flag==1):
                    v = y.ejecutar(ts,ts)
                    if(v==1):
                        break

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="ROOT "] \n '
        for x,y in self.inst.items():
            v+="n"+str(node)+"->"+y.ast()
        return v

def getHash(obj):
    return hash(obj)

def calcularArreglo(var,indx,args,metodos,ts,val):
    v = var.ejecutar(metodos,ts)
    i = args[indx].ejecutar(metodos,ts)
    if(i.tipo==TIPO.ENTERO or i.tipo == TIPO.STRING):            
        if(indx==len(args)-1):
            if(v.tipo==TIPO.STRING):
                v.value = v.value[:i.value]+val.value+v.value[i.value+1:]
            elif(v.tipo==TIPO.ARRAY):
                v.value[i.value] = val
        else:
            if(v.tipo==TIPO.ARRAY):
                if(i.value) in v.value:
                    v.value[i.value] = calcularArreglo(v.value[i.value],indx+1,args,metodos,ts,val)
                else:
                    v.value[i.value] = Valor({},TIPO.ARRAY)
                    v.value[i.value] = calcularArreglo(v.value[i.value],indx+1,args,metodos,ts,val)      
    else:
        return Valor("Indice no es numero ni String.",TIPO.ERROR) 
    return v

class Tag(Nodo):
    # Esta clase permite guardar las instrucciones de las clases
    def __init__(self, nombre, instrucciones, linea):
        self.instrucciones = instrucciones
        self.nombre = nombre
        self.linea = linea

    def ejecutar(self, metodos, ts):
        print(self.nombre," :")
        for inst in self.instrucciones:
            print(inst)
            a = inst.ejecutar(metodos,ts)
            if(isinstance(inst,Salto)):
                return 1
            if(isinstance(inst,Exit)):
                return 1
            if(isinstance(inst,Si)and(a==1)):
                return 1
        return 0
    
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="ETIQUETA: '+ self.nombre+'"] \n '
        for x in self.instrucciones:
            v+="n"+str(node)+"->"+x.ast()
        return v
    
    def grammarASC(self):
        v =('''<tr> <td colspan=2  class="et" > Contenido Etiqueta  '''+ self.nombre +''' </td> </tr>
        <tr> 
        <td> <p>ListaInstrucciones => ListaInstrucciones  PC ";"<br/> |  Instrucciones PC ";"<br/> </p></td> 
        <td><p> 
    if(len(t)==3):<br/>
        t[0] = []<br/>
        t[0].append(t[1])<br/><br/>
    if(len(t)==4):<br/>
        t[0] = t[1]<br/>
        t[0].append(t[2]) </p></td> 
        </tr>
        <tr>
            <td> Intrucciones =>    asignacion<br/>
                    |   iff<br/>
                    |   jump<br/>
                    |   printt<br/>
                    |   ext<br/>
                    |   uns<br/> </td> <td> <p> t[0] = t[1] </p> </td>
        </tr>\n''')
        
        for x in (self.instrucciones):
            try:
                v+=x.grammarASC()
            except Exception as ex:
                print("ERrrrrrroooooooorrrrrrrrrrrrrr:    "+ str(ex))
        return v

    
class Print(Nodo):
    #Esta clase permite imprimir un valor.
    def __init__(self, valor, linea):
        self.valor = valor
        self.linea = linea
    
    def ejecutar(self,metodos,ts):
        
        if(self.valor==None):
            metodos.errores.append(Simbolo("Error Semantico: No existe un valor para el Print, viene un valor Nulo!",self.linea))
            return
        v = self.valor.ejecutar(metodos,ts)
        if(v.tipo==TIPO.ERROR):
            metodos.errores.append(Simbolo("Error Semantico: No existe un valor para Imprimir!\n"+v.value,self.linea))
            return

        metodos.mensajes.append(v.value)
    
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="PRINT()"] \n '
        v+="n"+str(node)+"->"+self.valor.ast()
        return v

    def grammarASC(self):
        v =('''<tr> <td colspan=2  class="et" > Contenido PRINT  '''+ " " +''' </td> </tr>
        <tr> 
        <td> <p>Print => PRINT LEFTPAR "("  ID2    ")" <br/> ID2 => ID LArray <br/> | ID <br/> LArray => IZQLLAVE"[" Expresion DERLLAVE"]" </p></td> 
        <td><p> t[0] = Print()</p></td> 
        </tr>\n'''+self.valor.grammarASC())
        return v
 
    
class Unset(Nodo):
    #Esta clase permite imprimir un valor.
    def __init__(self, valor, linea):
        self.valor = valor
        self.linea = linea
    
    def ejecutar(self,metodos,ts):
        if self.valor.valor in metodos.variables:
            del metodos.variables[self.valor.valor]
        else:
            metodos.errores.append(Simbolo("Error Semantico:  No existe la variable en la tabla de simbolos! No se puede hacer Pop",self.linea))
        return 0
    
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="Unset()"] \n '
        v+="n"+str(node)+"->"+self.valor.ast()
        return v

    def grammarASC(self):
        v =('''<tr> <td colspan=2  class="et" > Contenido Unset  '''+ " " +''' </td> </tr>
        <tr> 
        <td> <p>Unset => Unset LEFTPAR "("  ID2    ")" <br/> ID2 => ID LArray <br/> | ID <br/> LArray => IZQLLAVE"[" Expresion DERLLAVE"]" </p></td> 
        <td><p> t[0] = Unset(t[3]</p></td> 
        </tr>\n''')
        return v


class Array(Nodo):
    #Esta clase permite imprimir un valor.
    def __init__(self):
        pass
    
    def ejecutar(self,metodos,ts):
        return Valor({},TIPO.ARRAY)

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="Array()"] \n '
        return v

    def grammarASC(self):
        v =('''<tr> <td colspan=2  class="et" > Contenido ARRAY  '''+ " " +''' </td> </tr>
        <tr> 
        <td> <p>arry => ARRAY LEFTPAR "("     DERPAR ")" <br/> </td> 
        <td><p> Se crea un objeto de tipo Array. </p></td> 
        </tr>\n''')
        return v
        
    
class Leer(Nodo):
    #Esta clase permite imprimir un valor.
    def __init__(self):
        pass

    def ejecutar(self,metodos,ts):

        tk = tkinter.Tk() # Create the object
        tk.withdraw()
        name = simpledialog.askstring("Information","Mensaje")
        tk.destroy()
        print("Read >>>  ",name)
        metodos.mensajes.append("Read>>>  "+str(name))
        if(re.match(r'-?\d+\.\d+',name)!=None):
            print("----------- VALOR DOBLE------------")
            return Valor(float(name),TIPO.DOBLE)
        if(re.match(r'-?\d+',name)!=None):
            print(".---------- VALOR ENTERO ---------------")
            return Valor(int(name),TIPO.ENTERO)
        return Valor(name,TIPO.STRING)


    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="Read()"] \n '
        return v
        v

    def grammarASC(self):
        v =('''<tr> <td colspan=2  class="et" > Contenido READ  '''+ " " +''' </td> </tr>
        <tr> 
        <td> <p>arry => Read LEFTPAR "("     DERPAR ")" <br/> </td> 
        <td><p> t[0] = Leer(). </p></td> 
        </tr>\n''')
        return v


class Exit(Nodo):
    #Esta clase permite imprimir un valor.
    def __init__(self):
        pass
    
    def ejecutar(self,metodos,ts):
        return 1
    
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="Exit"] \n '
        return v
    
    def grammarASC(self):
        v =('''<tr> <td colspan=2  class="et" > Contenido EXIT  '''+ " " +''' </td> </tr>
        <tr> 
        <td> <p>ext => exit  </p></td> 
        <td><p> t[0] = Exit() </p></td> 
        </tr>\n''')
        return v

class Asignacion(Nodo):
    #Esta clase representa una asignación
    def __init__(self,variable, expresion, linea):
        self.variable = variable
        self.expresion = expresion
        self.linea = linea
    
    def ejecutar(self, metodos, ts):
        if(self.expresion==None):
            metodos.errores.append(Simbolo("Error Semantico: No existe un valor, viene un valor Nulo!",self.linea))
            return
        v1 = self.expresion.ejecutar(metodos,ts)
        if(v1.tipo==TIPO.ERROR):
            metodos.errores.append(Simbolo("Error Semantico: No se puede asignar, hay un error\n"+v1.value,self.linea))
            return
        if self.variable.args == None:
            if self.variable.valor in metodos.variables:
                metodos.añadirVariable(self.variable.valor,v1,"1,1")
            else:
                metodos.añadirVariable(self.variable.valor,v1,"1,1")
        else:
            for x in self.variable.args:
                print(x.ejecutar(metodos,ts).value)     
            if self.variable.valor in metodos.variables:#HAY UNA VARIABLE
                v = metodos.variables.get(self.variable.valor).valor
                v = calcularArreglo(v,0,self.variable.args,metodos,ts,v1)
                metodos.añadirVariable(self.variable.valor,v,"1,1")
            else:                                       #CREAR ARREGLO
                v = Valor({},TIPO.ARRAY)
                v = calcularArreglo(v,0,self.variable.args,metodos,ts,v1)
                metodos.añadirVariable(self.variable.valor,v,"1,1")
        if(v1!=None):
            print("La variable ",self.variable.valor," = ",v1.value)
        
    def grammarASC(self):
        v =('''<tr> <td colspan=2  class="et" > Contenido ASIGNACION  '''+ " " +''' </td> </tr>
        <tr> 
        <td> <p>asignacion => var2 IGUAL exp  </p></td> 
        <td><p> t[0] = Asignacion(t[1],t[3]) </p></td> 
        </tr>
        <tr>
            <td> var2 => VAR arr <br/> arr </td> <td> 
    if(len(t)==3): <br/>
        t[0] = NodoVariable(t[1],t[2]) <br/>
    else: <br/>
        t[0] = NodoVariable(t[1],None) </td> 
        </tr>
        <tr>
        <td> arr => arr IZQLLAVE E DERLLAVE <br/> | IZQLLAVE E DERLLAVE</td> <td>  if(len(t)==5):<br/> 
        lar = t[1]<br/> 
        lar.append(t[3])<br/> 
        t[0] = lar <br/> 
    else:<br/> 
        lar = []<br/> 
        lar.append(t[2])<br/> 
        t[0] = lar </td><br/> 
        </tr>\n'''+self.expresion.grammarASC())
        return v

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="Asignacion: '+ self.variable.valor+'"] \n n'+str(node)+" ->"+self.expresion.ast()
        return v

class Si(Nodo):
    #Esta clase representa un salto condicional
    def __init__(self, condicion, etiqueta, linea):
        self.condicion = condicion
        self.etiqueta = etiqueta 
        self.linea = linea

    def ejecutar(self, metodos, ts):
        if(self.condicion==None):
            metodos.errores.append(Simbolo("Error Semantico: No existe un valor, viene un valor Nulo!",self.linea))
            return
        cond = self.condicion.ejecutar(metodos,ts)
        if(cond.tipo==TIPO.ERROR):
            metodos.errores.append(Simbolo("Error Semantico: No se puede asignar, hay un error\n"+cond.value,self.linea))
            return
        if(cond.value == 1):
            flag = 0
            v = 1
            for x,y in metodos.metodos.items(): 
                if(x==self.etiqueta):
                    flag =1
                if(flag==1):
                    v = y.ejecutar(metodos,ts)
                    if(v==1):
                        break
            if(flag==1):
                return 1
            else:
                print("Error Semantico: No existe la etiqueta!")
                return 1
        else:
            print("No se cumplio la condición")
            return 0

        
    def grammarASC(self):
        v =('''<tr> <td colspan=2  class="et" > Contenido SALTO CONDICIONAL  '''+ " " +''' </td> </tr>
        <tr> 
        <td> <p>iff =>   if IZQPAR "(" exp DERPAR ")" goto ID</p></td> 
        <td><p> t[0] = Si(t[3],t[6]) </p></td> 
        </tr>\n'''+self.condicion.grammarASC())
        return v

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="Salto Condicional A: '+ self.etiqueta+'"] \n n'+str(node)+" ->"+self.condicion.ast()
        return v

class Salto(Nodo):
    #Esta clase representa un salto normal
    def __init__(self,etiqueta, linea):
        self.etiqueta = etiqueta
        self.linea = linea

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
                    
    def grammarASC(self):
        v =('''<tr> <td colspan=2  class="et" > Contenido SALTO  '''+ " " +''' </td> </tr>
        <tr> 
        <td> <p>jump  => goto ID";" </p></td> 
        <td><p> t[0] = Salto(t[2]) </p></td> 
        </tr>\n''')
        return v

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="Goto:  '+ self.etiqueta+'"] \n '
        return v

class NodoEntero(Nodo):
    #Esta clase representa cuando viene un valor entero
    def __init__(self, valor):
        self.valor = valor
    
    def ejecutar(self, metodos, ts):
        return Valor(self.valor, TIPO.ENTERO)
    
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="Entero: '+ str(self.valor)+'"] \n '
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>E  =>  ENTERO   <br/> </p></td> 
        <td><p>t[0] = NodoEntero(t[1]) </p></td> 
        </tr>''')
        return v

class NodoDouble(Nodo):
    #Esta clase representa cuando viene un valor entero
    def __init__(self, valor):
        self.valor = valor
    
    def ejecutar(self, metodos, ts):
        return Valor(self.valor, TIPO.DOBLE)

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="Doble: '+ str(self.valor)+'"] \n '
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>E  =>  DOBLE   <br/> </p></td> 
        <td><p>t[0] = NodoDouble(t[1]) </p></td> 
        </tr>''')
        return v
    

class NodoCadena(Nodo):
    #Esta clase representa cuando viene un valor entero
    def __init__(self, valor):
        self.valor = valor
    
    def ejecutar(self, metodos, ts):
        return Valor(self.valor, TIPO.STRING)
    
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="Cadena: '+ self.valor+'"] \n '
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>E  =>  CADENA   <br/> </p></td> 
        <td><p>t[0] = NodoCadena(t[1]) </p></td> 
        </tr>''')
        return v

class NodoArreglo(Nodo):
    #Esta clase representa cuando viene un valor entero
    def __init__(self, valor):
        pass

    
class NodoVariable(Nodo):
    #Esta clase representa cuando viene un valor entero
    def __init__(self, valor, args):
        self.valor = valor
        self.args = args 
    
    def ejecutar(self, metodos, ts):
        try:
            v = metodos.variables.get(self.valor).valor
            val = v
                
            if(self.args!=None):
                for x in self.args:
                    if(v.tipo == TIPO.ARRAY):
                        v = v.value.get(x.ejecutar(metodos,ts).value)
                    elif(v.tipo == TIPO.STRING):
                        v = Valor(v.value[x.ejecutar(metodos,ts).value],TIPO.STRING)
                    else:
                        v = v
                val = v
            if(val.tipo== TIPO.PUNTERO):
                val = metodos.variables.get(val.value).valor
            return val
        except Exception as e:
            return Valor("Error Semantico: No se encontro la variable!",TIPO.ERROR)

        
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="Variable: '+ self.valor+'"] \n '
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>E  =>   ID <br/>| ID LCOR <br/> LCOR   => LCOR [E] <br/> | [E]  </p></td> 
        <td><p> t[0] = NodoVariable(t[1]) </p></td> 
        </tr>''')
        return v

    
    
class NodoPuntero(Nodo):
    #Esta clase representa cuando viene un valor entero
    def __init__(self, valor):
        self.valor = valor
    
    def ejecutar(self, metodos, ts):
        try:
            v = metodos.variables.get(self.valor).valor
            return Valor(self.valor,TIPO.PUNTERO)
        except Exception as e:
            return Valor("Error Semantico: No se encontro la variable!",TIPO.ERROR)

        
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label="PUNTERO : '+ self.valor+'"] \n '
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>E  =>  PUNTERO "&"  ID <br/> </p></td> 
        <td><p>t[0] = NodoPuntero(t[1],t[3]) </p></td> 
        </tr>''')
        return v