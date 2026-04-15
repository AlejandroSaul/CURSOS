import tkinter as tk

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("500x500")

def mostrarNombre():
    nombreObtenido = nombre.get()
    resultado.config(text=f"Hola, {nombreObtenido}")

etiqueta = tk.Label(ventana,text="Ingresa tu nombre: ")
etiqueta.pack()

nombre =  tk.StringVar()
entradaNombre = tk.Entry(ventana,width= 25, textvariable=nombre)
entradaNombre.pack()
#numero = tk.IntVar()

boton = tk.Button(ventana,text="boton",command=mostrarNombre)
boton.pack()

resultado = tk.Label(ventana,text="")
resultado.pack()

ventana.mainloop()