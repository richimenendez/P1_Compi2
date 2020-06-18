from values import * 

class Expresion():
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
        
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" Cast (Int) "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        return v   
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  LEFTPAR "("  int   DERPAR ")"  E <br/> </p></td> 
        <td><p> t[0]  = Cast2Int(t[2]) </p></td> 
        </tr>'''+self.val1.grammarASC())
        return v

def calcularDouble(val1):
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
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" Cast (Double) "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        return v
        
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  LEFTPAR "("  double   DERPAR ")"  E <br/> </p></td> 
        <td><p> t[0]  = Cast2Int(t[2]) </p></td> 
        </tr>'''+self.val1.grammarASC())
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
        
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" Cast (Char) "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        return v

    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  LEFTPAR "("  char   DERPAR ")"  E <br/> </p></td> 
        <td><p> t[0]  = Cast2Int(t[2]) </p></td> 
        </tr>'''+self.val1.grammarASC())
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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" + "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v


    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E + E <br/> </p></td> 
        <td><p> if(t[2]=="+")<br>
        t[0]  = Suma(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v

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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" - "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v

        
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E - E <br/> </p></td> 
        <td><p> if(t[2]=="-")<br>
        t[0]  = Resta(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v

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
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" * "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v

    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E * E <br/> </p></td> 
        <td><p> if(t[2]=="*")<br>
        t[0]  = Multi(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v


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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" / "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v

        
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E / E <br/> </p></td> 
        <td><p> if(t[2]=="/")<br>
        t[0]  = Divi(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v


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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" - E "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  => - E  <br/> </p></td> 
        <td><p> if(t[1]=="-")<br>
        t[0]  = Negativo(t[1]) </p></td> 
        </tr>'''+self.val1.grammarASC())
        return v


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


    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label= "abs" ] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        return v

    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  => abs "(" E ")" <br/> </p></td> 
        <td><p> if(t[1]=="abs")<br>
        t[0]  = abs(t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC())
        return v
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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" == "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E == E <br/> </p></td> 
        <td><p> if(t[2]=="==")<br>
        t[0]  = Igual(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v

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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" != "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E != E <br/> </p></td> 
        <td><p> if(t[2]=="!=")<br>
        t[0]  = DesIgual(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v

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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" > "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E > E <br/> </p></td> 
        <td><p> if(t[2]==">")<br>
        t[0]  = Mayor(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v

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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" < "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E < E <br/> </p></td> 
        <td><p> if(t[2]=="<")<br>
        t[0]  = Menor(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v

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
        
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" >= "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v 
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E >= E <br/> </p></td> 
        <td><p> if(t[2]==">=")<br>
        t[0]  = MayorI(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v


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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" <= "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E <= E <br/> </p></td> 
        <td><p> if(t[2]=="<=")<br>
        t[0]  = MenorI(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v


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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" ! E "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  => ! E  <br/> </p></td> 
        <td><p> if(t[1]=="!")<br>
        t[0]  = Not(t[2]) </p></td> 
        </tr>'''+self.val1.grammarASC())
        return v

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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" AND & "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E && E <br/> </p></td> 
        <td><p> if(t[2]=="&&")<br>
        t[0]  = And(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v

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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" OR | "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E || E <br/> </p></td> 
        <td><p> if(t[2]=="||")<br>
        t[0]  = Or(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v

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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" XOR ^ "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E ^ E <br/> </p></td> 
        <td><p> if(t[2]=="^")<br>
        t[0]  = Xor(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v



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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" BitWise Not !E "] \n '
        v+="n"+str(node)+"->"+self.val1.ast() 
        return v
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  => ! E  <br/> </p></td> 
        <td><p> if(t[1]=="!")<br>
        t[0]  = BNot(t[2]) </p></td> 
        </tr>'''+self.val1.grammarASC())
        return v


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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" BitWise Or | "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E || E <br/> </p></td> 
        <td><p> if(t[2]=="||")<br>
        t[0]  = Bor(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v

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
 
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" BitWise AND & "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E && E <br/> </p></td> 
        <td><p> if(t[2]=="&&")<br>
        t[0]  = BAnd(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v

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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" BitWise Xor ^ "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E ^ E <br/> </p></td> 
        <td><p> if(t[2]=="^")<br>
        t[0]  = BXor(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v
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

    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" BitWise Left << "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E << E <br/> </p></td> 
        <td><p> if(t[2]=="<<")<br>
        t[0]  = BLeft(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v

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
    def ast(self):
        node = abs(hash(self))
        v = "n"+str(node)+"\nn"+str(node)+'[label=" BitWise Right >> "] \n '
        v+="n"+str(node)+"->"+self.val1.ast()
        v+="n"+str(node)+"->"+self.val2.ast()
        return v
    
    def grammarASC(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E >> E <br/> </p></td> 
        <td><p> if(t[2]==">>")<br>
        t[0]  = BRight(t[1],t[3]) </p></td> 
        </tr>'''+self.val1.grammarASC()+self.val2.grammarASC())
        return v