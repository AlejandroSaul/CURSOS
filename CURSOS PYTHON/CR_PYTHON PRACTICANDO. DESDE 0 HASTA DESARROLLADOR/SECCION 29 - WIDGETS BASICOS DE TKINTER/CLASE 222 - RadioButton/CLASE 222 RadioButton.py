import tkinter as tk

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("500x500")

def mostrarSeleccion():
    resultado.config(text = f"Opcion seleccionada: {selectionVar.get()}")

selectionVar = tk.StringVar()
selectionVar.set("")


radio = tk.Radiobutton(ventana,text="Opcion 1", variable=selectionVar, value = "Opcion 1",state="normal")
radio.pack()
radio2 = tk.Radiobutton(ventana,text="Opcion 2", variable=selectionVar, value = "Opcion 2")
radio2.pack()
radio3 = tk.Radiobutton(ventana,text="Opcion 3", variable=selectionVar, value = "Opcion 3")
radio3.pack()

boton = tk.Button(ventana,text="Mostrar Seleccion", command=mostrarSeleccion)
boton.pack( )

resultado = tk.Label(ventana,text="")
resultado.pack()

ventana.mainloop()