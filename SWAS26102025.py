#importamos las librarias necesarias
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

#funcion que se ejecuta al presionar el boton
def iniciar_test():
    messagebox.showinfo("inicio del test",  "bienvenido al test de adiccion al streaming")
    ventanaprin.destroy()


#configurar la ventana
ventanaprin= tk.Tk()
ventanaprin.title("Software para detectar adicciones al streaming")
ventanaprin.geometry("600x400")
ventanaprin.config(bg="#FFADFB")

#configurar posicion de la pantalla
ancho_pantalla = ventanaprin.winfo_screenwidth()
alto_pantalla = ventanaprin.winfo_screenheight()
x=(ancho_pantalla // 2) - (600 // 2)
y=(alto_pantalla // 2) - (400 // 2)
ventanaprin.geometry(f"700x450+{x}+{y}")

#configurar los widges o elementos graficos

#bienvenida principal
titulo = tk.Label(
    ventanaprin,
    text="Bienvenido a mi software de deteccion de adiccion al streaming",
    font=("roboto", 18, "bold"),
    bg= "#751D6F",
    fg= "#7DDB6C",
    wraplength= 550,
    justify= "center"
  )
titulo.pack(pady=30)

#insertar una imagen
try:
    imagen=PhotoImage(file="streamin.adiccion.png")
    img_label= tk.Label (ventanaprin, image=imagen, bg= "#FB9B80")
    img_label.pack(pady=10)
except Exception:
    aviso = tk.label(ventanaprin,text=" no se encontro la imagen", bg= "#B3C3EC", fg= "gray")
    aviso.pack ()

#texto descriptivo
texto =tk.Label(
   ventanaprin,
   text=("Bienvenido a nuestro software, en este software te vamos a ayudar a identificar si eres adicto al streaming o que tanto de adicto eres. Nuestra mision es que los alumnos del CETis 151 se den cuenta si tienen adiccion al streaming, para eso hemos realizado este software que contiene un tes que te ayudara a saber que tanto eres adicto al streaming"
),
font= ("Roboto", 12),
bg= "#A2BAF7",
fg= "#190702",
wraplength=500,
justify="center",
)
texto.pack(pady=200)
#elemento boton para iniciar el test
boton_iniciar =tk.Button(
    ventanaprin,
    text="inicio test",
    font= ("Arial", 14, "bold"),
    bg="#8CA0E6",
    fg="white",
    relief= "raised",
    bd=3,
    padx= 20,
    pady=10,
    command= iniciar_test
)
#ejecutar la interfaz  de venta
ventanaprin.mainloop()