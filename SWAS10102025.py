#importar la biblioteca

import tkinter as tk 
from tkinter import ttk



#crear la ventana en python 
ventana=tk.Tk()
#configuramos la ventana 
ventana.title("Esta es mi primera ventana")
ventana.geometry("700x800")




#agregamos  los widgets
#colocando la informacion en columnas y filas para
organizarla




ttk.Label(ventana,text="APLICA METODOLOGIAS AGILES PARA EL DESARROLLO DE SOFTWARE").grid(column=0,row=1)
ttk.Label(ventana,text="Equipo numero 3").grid(column=0,row=2)
ttk.Label(ventana,text="Karla sanchez Morales").grid(column=0,row=3)
ttk.Label(ventana,text="Katia Garcia Yañez").grid(column=0,row=4)
ttk.Label(ventana,text="Yosany Gonzalez Perez").grid(column=0,row=5)
ttk.Label(ventana,text="Evelyn Juarez Perez").grid(column=0,row=6)






#Activamos la ventana
ventana.resizable(0,0)
ventana.mainloop()

