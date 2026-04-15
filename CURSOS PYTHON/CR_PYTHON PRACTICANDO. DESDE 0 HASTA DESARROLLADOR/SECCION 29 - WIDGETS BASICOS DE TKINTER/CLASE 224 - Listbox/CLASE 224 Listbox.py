import tkinter as tk

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("500x500")

def mostrarSeleccion():
    seleccion = lista.get(lista.curselection())
    resultado.config(text="Seleccionaste: {}".format(seleccion))

lista = tk.Listbox(ventana,selectmode=tk.SINGLE)
lista.pack()

opciones = ["Azul","Rojo","Negro","Amarillo"]

for i in opciones:
    lista.insert(tk.END,i)

boton = tk.Button(ventana,text="Mostrar Seleccion del Usuario",command=mostrarSeleccion)
boton.pack()


resultado = tk.Label(ventana,text = "")
resultado.pack()

ventana.mainloop()