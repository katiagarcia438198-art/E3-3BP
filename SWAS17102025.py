import tkinter as tk 

from tkinter import ttk

# configuracion de colores 
COLOR_FONDO = "#5E5EF0"
COLOR_MENU  = "#696969"
COLOR_TEXTO = "#ECE4E4"
FUENTE_TITULO =("Arial", 16, "bold")
FUENTE_TEXTO =("Arial", 12)

#ventana principal
root = tk.Tk()
root.title("software para detectar la adiccion al streaming")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

#FRAME MENU LATERAL
menu_frame=tk.Frame(root,bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

#contenido del contenido
contenido_frame= tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# funcion para cambiar de pagina 
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
        paginas[nombre]()

# paginas
def pagina_bienvenida():
    tk.Label(contenido_frame, text= "Bienvenido a bienestar total", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=30)
    tk.Label(contenido_frame, text= "TU ESPACIO DE APOYO, INFO Y SLAUD EMOCIONAL.", bg=COLOR_FONDO, font= FUENTE_TEXTO).pack(pady=10)

def pagina_registro():
    tk.Label(contenido_frame, text="Registro de usuario", font=COLOR_FONDO).pack(pady=20)
for campo in ["Nombre", "Edad", "correo",]:
    tk.Label(contenido_frame, text=f"{campo}:", bg=COLOR_FONDO, font=FUENTE_TEXTO). pack()
    tk.Entry(contenido_frame, width=40).pack(pady=5)
             
def pagina_test():
    tk.Label(contenido_frame,text="Test bienestar",font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame,text="Responde las siguientes preguntas para conocer tu nivel de bienestar.", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    ttk.Button(contenido_frame, text="iniciar test").pack(pady=20)


#diccionario de paginas 
paginas = {
    "Bienvenida":pagina_bienvenida,
    "Registro":pagina_registro,
    "Test":pagina_test,

}

#botones del menu lateral
for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina (n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, text="Salir", command=root.quit).pack(side ="bottom", pady=10)

# mostrar pagina inicial
pagina_bienvenida()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

root.mainloop()

