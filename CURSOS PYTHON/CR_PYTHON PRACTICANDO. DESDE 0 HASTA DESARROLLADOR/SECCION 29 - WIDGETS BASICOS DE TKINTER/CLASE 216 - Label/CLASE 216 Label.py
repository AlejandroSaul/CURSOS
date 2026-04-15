import tkinter as tk

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("500x500")

etiqueta = tk.Label(ventana,text="Texto")
etiqueta.pack()

etiqueta2 =tk.Label(ventana,text="Texto 2")
etiqueta2.pack()

ventana.mainloop()