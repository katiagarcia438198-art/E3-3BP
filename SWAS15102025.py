# importar las librerias 
import tkinter as tk

#creamos la funcion de mostrarventana2
def mostrar_ventana2():

    ventana1.withdraw() #esta funcion sirve para que oculte la ventana 1
    
    ventana2.deiconify()  # muestre la ventana 2

#creamos la funcion de regresar
def regresar ():
    
    #oculta la ventana2
    ventana2.withdraw()

    #muestra la ventana1
    ventana1.deiconify()

#creacion de ventana1
ventana1= tk.Tk()
label1=tk.Label(ventana1, text="bienvenida")
ventana1.geometry("700x500")
ventana1.config(bg="#131313")
label1.pack()

btn1=tk.Button(ventana1, text="ir a la ventana 2",command= mostrar_ventana2)
btn1.pack()


#creacion de ventanas 2
ventana2= tk.Tk()

label2=tk.Label(ventana2, text="pantalla con la informacion del streaming")
ventana2.geometry("700x500")

ventana2.config(bg="orange")
label2.pack()

btn2=tk.Button(ventana2, text="ir a la ventana 1",command= regresar)
btn2.pack()
ventana2.withdraw()

#creacion de ventanas (lanzar la interfaz)
ventana1.mainloop()



