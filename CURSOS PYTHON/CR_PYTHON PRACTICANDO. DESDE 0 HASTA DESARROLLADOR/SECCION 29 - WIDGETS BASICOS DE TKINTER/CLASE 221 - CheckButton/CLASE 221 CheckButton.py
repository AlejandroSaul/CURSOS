import tkinter as tk

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("500x500")

opcionVar = tk.IntVar()

chekOpciones = tk.Checkbutton(
    ventana,
    text = "¿Desea recibir notificaciones?",
    variable = opcionVar,
    onvalue=1,
    offvalue=0
)

chekOpciones.pack()

def mostrarEstado():
    if opcionVar.get() == 1 :
        resultado.config(text = "Notificaciones Activadas")
        print(opcionVar.get())
    elif opcionVar.get() == 0 :
        resultado.config(text = "Notificaciones Desctivadas")
        print(opcionVar.get())

boton = tk.Button(ventana,text= "Cambiar", command=mostrarEstado)
boton.pack()

resultado = tk.Label(ventana,text="")
resultado.pack()
ventana.mainloop()