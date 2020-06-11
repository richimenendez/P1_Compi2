from ast import *
from ast_operacion import *
def reporteErrores():
    pass

def reporteAST():
    pass

def gramaticalASC(lista):
    html = ''' <html>
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
<body>
	<h1>Reporte Gramatical: Gramatica Ascendente</h1>
	<h3> Ricardo Menéndez - 201602916 </h3>
	<br/><br/>
<table width="800" border="1" align="center">'''
    for x,y in lista.items():
        html+= y.grammarASC()
    html+="</body></html>"
    print(html)


def gramaticalDES():
    pass