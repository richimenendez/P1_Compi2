"""
-------------------------------------
RichiBeans

por Ricardo Antonio Menéndez Tobías
201602916
-------------------------------------
"""

import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox


IDE = "RichiBeans"
archivo = None

# Configuración de Ventana
root = Tk()
root.geometry('1280x720')
root.title(IDE)

# Funciones Menu 
    #Archivo
def nuevo_archivo(): 
    a = 0 

def abrir_archivo(): 
    a = 0 

def exit_editor(event=None):
    if tkinter.messagebox.askokcancel("Salir","Seguro que quieres salir?"):
        root.destroy()

# Menu
barra_menu = Menu(root)
    #Archivo
archivo_menu = Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label="Nuevo", compound="left", underline=0,command=nuevo_archivo)
archivo_menu.add_command(label="Abrir", compound="left", underline=0,command=abrir_archivo)
archivo_menu.add_command(label="Guardar", compound="left", underline=0,command=nuevo_archivo)
archivo_menu.add_command(label="Guardar Como", compound="left", underline=0,command=nuevo_archivo)
archivo_menu.add_command(label="Cerrar", compound="left", underline=0,command=nuevo_archivo)
archivo_menu.add_command(label="Salir", compound="left", underline=0,command=exit_editor)
barra_menu.add_cascade(label="Archivo",menu=archivo_menu)

    #Editar
editar_menu = Menu(barra_menu,tearoff=0)
editar_menu.add_command(label="Copiar", compound ="left", underline = 0, command=nuevo_archivo)
editar_menu.add_command(label="Pegar", compound ="left", underline = 0, command=nuevo_archivo)
editar_menu.add_command(label="Buscar", compound ="left", underline = 0, command=nuevo_archivo)
editar_menu.add_command(label="Reemplazar", compound ="left", underline = 0, command=nuevo_archivo)
barra_menu.add_cascade(label="Editar", menu= editar_menu)

    #Ejecutar
ejecutar_menu = Menu(barra_menu, tearoff=0)
ejecutar_menu.add_command(label="Compilar Ascendente", compound="left", underline=0,command=nuevo_archivo)
ejecutar_menu.add_command(label="Compilar Descendente", compound="left", underline=0,command=nuevo_archivo)
ejecutar_menu.add_command(label="Reporte AST", compound="left", underline=0,command=nuevo_archivo)
ejecutar_menu.add_command(label="Reporte Tabla de Simbolos", compound="left", underline=0,command=nuevo_archivo)
ejecutar_menu.add_command(label="Reporte Gramatica", compound="left", underline=0,command=nuevo_archivo)
ejecutar_menu.add_command(label="Reporte Errores", compound="left", underline=0,command=nuevo_archivo)
barra_menu.add_cascade(label="Ejecutar",menu=ejecutar_menu)
    #Opciones
opcion_menu = Menu(barra_menu, tearoff=0)
opcion_menu.add_command(label="No", compound="left", underline=0,command=nuevo_archivo)
opcion_menu.add_command(label="No", compound="left", underline=0,command=nuevo_archivo)
opcion_menu.add_command(label="No", compound="left", underline=0,command=nuevo_archivo)
barra_menu.add_cascade(label="Opciones",menu=opcion_menu)

    #Ayuda
ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="No", compound="left", underline=0,command=nuevo_archivo)
ayuda_menu.add_command(label="No", compound="left", underline=0,command=nuevo_archivo)
ayuda_menu.add_command(label="No", compound="left", underline=0,command=nuevo_archivo)
barra_menu.add_cascade(label="Ayuda",menu=ayuda_menu)


root.config(menu=barra_menu)

# Texto
barra_numeros = Text(root, width=4, padx = 3, takefocus = 0, border=0,
            background ='#D1E7E0', state="disabled", wrap="none")

barra_numeros.pack(side='left', fill="y")

caja_texto =  Text(root, wrap='word', undo=1)
caja_texto.pack(expand="yes",fill="both")
scroll_bar = Scrollbar(caja_texto)
scroll_bar.config(command=caja_texto.yview)
scroll_bar.pack(side='right', fill='y')
cursor_info_bar = Label(caja_texto, text='Line: 1 | Column: 1')
cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')


"""
consola = Label(root,text="Hola")
consola.pack()
caja_texto2 =  Text(root, wrap='word', undo=1)
caja_texto2.pack(expand="yes",fill="both")
scroll_bar2 = Scrollbar(caja_texto2)
scroll_bar2.config(command=caja_texto2.yview)
scroll_bar2.pack(side="right",fill='y')
"""
# Consola


# Ejecución

root.protocol('WM_DELETE_WINDOW', exit_editor)
root.mainloop()