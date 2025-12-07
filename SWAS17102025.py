import tkinter as tk #Importa la librería principal de Tkinter y la renombra como "tk"


from tkinter import ttk   # Importa los widgets modernos de Tkinter (botones mejorados, etc.)


# configuracion de colores 
COLOR_FONDO = "#5E5EF0"     # Define el color de fondo principal de la ventana

COLOR_MENU  = "#696969"   # Define el color del menú lateral
COLOR_TEXTO = "#ECE4E4"    
FUENTE_TITULO =("Arial", 16, "bold")  # Define la fuente del título (Arial, tamaño 16, en negrita)

FUENTE_TEXTO =("Arial", 12)

#ventana principal
root = tk.Tk()    # Crea la ventana principal de la aplicación
root.title("software para detectar la adiccion al streaming")   # Coloca el título de la ventana
root.geometry("900x500")  # Define el tamaño de la ventana (ancho x alto)
root.config(bg=COLOR_FONDO) 

#FRAME MENU LATERAL
menu_frame=tk.Frame(root,bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")  # Coloca el menú a la izquierda y lo estira verticalmente


#contenido del contenido
contenido_frame= tk.Frame(root, bg=COLOR_FONDO)  # Crea el frame principal donde se mostrará el contenido

contenido_frame.pack(side="right", fill="both", expand=True)  # Posiciona el frame a la derecha y permite que se expanda


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


