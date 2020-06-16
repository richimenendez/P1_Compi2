from ast import *
from ast_operacion import *

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

def reporteErrores():
    pass

def reporteAST():
    pass

def gramaticalASC(lista):
    html = '''
	<h1>Reporte Gramatical: Gramatica Ascendente</h1>
	<h3> Ricardo Menéndez - 201602916 </h3>
	<br/><br/>
<table width="800" border="1" align="center">
    '''
    for x,y in lista.items():
        html+= y.grammarASC()
    html+="</body></html>"
    print(html)


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
        <tr><td>'''+x+"</td><td>"+y.valor.value+ '''</td><td>'''+y.valor.tipo.name+"</td></tr>"
        except:
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
    print(html)

