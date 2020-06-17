from ast import *
from ast_operacion import *
import webbrowser
import os

head = ''' <html>
<head>

<style>
.et {background-color: powderblue;}
</style>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>'''

def reporteErrores(eL,eS,eSem):
    html = '''
	<h1>Reporte de Errores: </h1>
	<h3> Ricardo Menéndez - 201602916 </h3>
    <h4> Errores Lexicos </h4>
<table width="800" border="1" align="center">
    '''
    for x in eL:
        try:
            html+= '<tr><td> '+x+'</td></tr>'
        except Exception as e:
            print("Error generando linea de reporte gramatical  "+ str(e))
    html+='''</table>
    <h4> Errores Sintacticos </h4>
<table width="800" border="1" align="center">'''
    for x in eS:
        try:
            html+= '<tr><td> '+x+'</td></tr>'
        except Exception as e:
            print("Error generando linea de reporte gramatical  "+ str(e))
    html+='''</table>
    <h4> Errores Semanticos </h4>
<table width="800" border="1" align="center">'''
    for x in eSem:
        try:
            html+= '<tr><td> '+x.valor +"    en linea: "+ str(x.linea)+'</td></tr>'
        except Exception as e:
            print("Error generando linea de reporte gramatical  "+ str(e))
    html+="</body></html>"
    try:
        contenido = head + html
        with open('reporte_Errores.html','w') as rep:
            rep.write(contenido)
    except Exception as e:
        print("No se pudo generar el reporte: " + str(e))

def reporteAST(root):
    dot = "digraph {\n"
    dot += root.ast()
    dot += "\n}"
    try:
        contenido = dot
        with open('AST.dot','w') as rep:
            rep.write(contenido)
        os.system('dot "AST.dot" -o "AST.pdf" -Tpdf')
    except:
        print("No se pudo")

def gramaticalASC(lista):
    html = '''
	<h1>Reporte Gramatical: Gramatica Ascendente</h1>
	<h3> Ricardo Menéndez - 201602916 </h3>
<table width="1000" border="1" align="center">
    '''
    for x,y in lista.items():
        try:
            html+= y.grammarASC()
        except Exception as e:
            print("Error generando linea de reporte gramatical  "+ str(e))
    html+="</body></html>"
    try:
        contenido = head + html
        with open('reporte_GAsc.html','w') as rep:
            rep.write(contenido)
    except Exception as e:
        print("No se pudo generar el reporte: " + str(e))


def gramaticalDES():
    pass

def reporteTS(vars,metods):
    html = '''
	<h1>Reporte Tabla de Simbolos: </h1>
	<h3> Ricardo Menéndez - 201602916 </h3>
	<br/><br/>
    <h3> Variables:</h3>
    <table width="800" border="1" align="center">
    <tr class="et"><th> Variable </th> <th> Valor </th> <th> Tipo </th></tr> 
    '''
    for x,y in vars.items():
        try:
            html += '''
        <tr><td>'''+x+"</td><td>"+str(y.valor.value)+ '''</td><td>'''+y.valor.tipo.name+"</td></tr>"
        except Exception as e:
            print(e)
            html += '''
        <tr><td>'''+x+"</td><td> Array   </td> <td> "+ y.valor.tipo.name+"</tr>"
    html+="</table>"
    html+='''
    <h3> Metodos </h3>
    <table width="800" border="1" align="center">
    <tr class="et"><th> Metodo </th> </tr> 
    '''
    for x,y in metods.items():
        html += '''
        <tr><td>'''+x+"</td></tr>"
    html+="</table></body></html>"
    try:
        contenido = head + html
        with open('reporte_TS.html','w') as rep:
            rep.write(contenido)
    except Exception as e:
        print("No se pudo generar el reporte: " + str(e))

