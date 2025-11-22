import tkinter as tk
from tkinter import ttk

# configuracion de colores 
COLOR_FONDO = "#95B3EB"
COLOR_MENU  = "#423A68"
COLOR_TEXTO = "#080202DA"
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
    tk.Label(contenido_frame, text=" Bienvenido al software de deteccion del streaming", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=30)
    label0 = tk.Label(contenido_frame, text="¡Hola!", justify=tk.CENTER).pack(pady=10)
    label1 = tk.Label(contenido_frame, text= "Estamos aqui para ayudarte a encontrar un equilibrio saludable en tu consumo de contenido en linea", justify=tk.CENTER).pack(pady=10)
    label2 = tk.Label(contenido_frame, text= "El streaming nos conecta con historias increibles, pero el uso excesivo puede alejarnos de otras    ", justify=tk.CENTER).pack(pady=10)
    label3 = tk.Label(contenido_frame, text="cosas importantes: Tus metas, tus relaciones con tus seres queridos Este software te  ofrece las",justify=tk.CENTER).pack(pady=10)
    label4 = tk.Label(contenido_frame, text=" herramientas para: , Comprender tus habitos de visualizacion.Reflexionar sobre como utilizas",justify=tk.CENTER).pack(pady=10)
    label5 = tk.Label(contenido_frame, text="  tu tiempo. Retomar el control y hacer espacio para las actividades que realmente valoras,",justify=tk.CENTER).pack(pady=10)
    label6 = tk.Label(contenido_frame, text=" Tu privacidad es lo primero:todos los datos se procesan de forma confidencial. Da el primer paso",justify=tk.CENTER).pack(pady=10)
    label7 = tk.Label(contenido_frame, text="hacia un bienestar digital mas conciente",justify=tk.CENTER).pack(pady=10)
   # for campo in ["¡Hola!", "Estamos aqui para ayudarte a encontrar un equilibrio saludable en tu consumo de contenido en linea ", "El streaming nos conecta con historias increibles, pero el uso excesivo puede alejarnos de otras cosas importantes: Tus metas, tus relaciones con tus seres queridos.", "Este software te ofrece las herramientas para: ", "Comprender tus habitos de visualizacion.", "Reflexionar sobre como utilizas tu tiempo.", "Retomar el control y hacer espacio para las actividades que realmente valoras.", "Tu privacidad es lo primero:", "todos los datos se procesan de forma confidencial.", "Da el primer paso hacia un bienestar digital mas conciente"]:
     #   tk.Label(contenido_frame, text=f"{cam7po}:", bg=COLOR_FONDO, font=FUENTE_TEXTO). pack()
       # label = tk.Label(contenido_frame, text="["¡Hola!", "Estamos aqui para ayudarte a encontrar un equilibrio saludable en tu consumo de contenido en linea ", "El streaming nos conecta con historias increibles, pero el uso excesivo puede alejarnos de otras cosas importantes: Tus metas, tus relaciones con tus seres queridos.", "Este software te ofrece las herramientas para: ", "Comprender tus habitos de visualizacion.", "Reflexionar sobre como utilizas tu tiempo.", "Retomar el control y hacer espacio para las actividades que realmente valoras.", "Tu privacidad es lo primero:", "todos los datos se procesan de forma confidencial.", "Da el primer paso hacia un bienestar digital mas conciente"]:
        
    
def pagina_registro():
    tk.Label(contenido_frame, text="Registro de usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    for campo in ["Nombre", "Edad", "Correo", "Numero de telefono",]:
        tk.Label(contenido_frame, text=f"{campo}:", bg=COLOR_FONDO, font=FUENTE_TEXTO). pack()
        tk.Entry(contenido_frame, width=40).pack(pady=5)
    ttk.Button(contenido_frame, text="Registrarme").pack(pady=20)
             
def pagina_test():
    tk.Label(contenido_frame,text="Test sobre el streaming",font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame,text="Responde las siguientes prettguntas para conocer que tanto eres adicto al streaming", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    ttk.Button(contenido_frame, text="iniciar test").pack(pady=20)
    for campo in ["1. ¿Con qué frecuencia sientes la necesidad de ver contenido en streaming (Netflix, YouTube, etc.)?", "2. ¿Cuánto tiempo al día sueles pasar viendo contenido en streaming?", "3. ¿Has intentado reducir el tiempo que pasas en streaming sin éxito?", "4. ¿Te sientes irritable o ansioso cuando no puedes acceder a plataformas de streaming?", "5. ¿Prefieres ver contenido en streaming en lugar de pasar tiempo con amigos o familiares?", "6. ¿Has descuidado responsabilidades importantes (trabajo, estudios, tareas del hogar) debido al streaming?", "7. ¿Mientes a otros sobre la cantidad de tiempo que pasas viendo contenido en streaming?", "8. ¿Utilizas el streaming como una forma de escapar de tus problemas o emociones negativas?", "9. ¿Te sientes culpable o avergonzado por la cantidad de tiempo que pasas en streaming?", "10. ¿Has gastado más dinero del que puedes permitirte en suscripciones de streaming o datos móviles para ver contenido?"]:
        tk.Label(contenido_frame, text=f"{campo}:", bg=COLOR_FONDO, font=FUENTE_TEXTO). pack()
        tk.Entry(contenido_frame, width=40).pack(pady=5)

#diccionario de paginas 
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test,

}

#botones del menu lateral
for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina (n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, text="Salir", command=root.quit).pack(side ="bottom", pady=10)

# mostrar pagina inicial
pagina_bienvenida()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

root.mainloop()