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
def mostrar_pagina(nombre):  # Define una función para cambiar entre páginas
    for widget in contenido_frame.winfo_children():  # Recorre todos los elementos dentro del frame de contenido
        widget.destroy()    # Elimina cada widget actual
        paginas[nombre]()  # Llama a la función de la página seleccionada

# paginas
def pagina_bienvenida():  # Función para mostrar la página de inicio
    tk.Label(contenido_frame, text= "Bienvenido a bienestar total", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=30)   # Muestra el título principal

    tk.Label(contenido_frame, text= "TU ESPACIO DE APOYO, INFO Y SLAUD EMOCIONAL.", bg=COLOR_FONDO, font= FUENTE_TEXTO).pack(pady=10)   # Muestra el subtítulo

def pagina_registro():  # Función para mostrar la página de registro
    tk.Label(contenido_frame, text="Registro de usuario", font=COLOR_FONDO).pack(pady=20)    # Muestra el título de registro

for campo in ["Nombre", "Edad", "correo",]:     # Recorre los campos que se quieren pedir

    tk.Label(contenido_frame, text=f"{campo}:", bg=COLOR_FONDO, font=FUENTE_TEXTO). pack()   # Crea una etiqueta para cada campo

    tk.Entry(contenido_frame, width=40).pack(pady=5)  # Crea una caja de texto para cada campo
             
def pagina_test():  # Función para mostrar la página del test

    tk.Label(contenido_frame,text="Test bienestar",font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)    # Muestra el título del test

    tk.Label(contenido_frame,text="Responde las siguientes preguntas para conocer tu nivel de bienestar.", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    ttk.Button(contenido_frame, text="iniciar test").pack(pady=20)


#diccionario de paginas 
paginas = {    # Diccionario que relaciona el nombre del botón con su función
    "Bienvenida":pagina_bienvenida,
    "Registro":pagina_registro,
    "Test":pagina_test,

}

#botones del menu lateral
for nombre in paginas: # Recorre el diccionario de páginas
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina (n)).pack(fill="x", pady=5, padx=10)  # Crea un botón por cada página y llama a la función correspondiente


ttk.Button(menu_frame, text="Salir", command=root.quit).pack(side ="bottom", pady=10) # Crea el botón para cerrar el programa


# mostrar pagina inicial
pagina_bienvenida()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
# Muestra la página de bienvenida al iniciar el programa

root.mainloop()   # Mantiene la ventana abierta en ejecución



