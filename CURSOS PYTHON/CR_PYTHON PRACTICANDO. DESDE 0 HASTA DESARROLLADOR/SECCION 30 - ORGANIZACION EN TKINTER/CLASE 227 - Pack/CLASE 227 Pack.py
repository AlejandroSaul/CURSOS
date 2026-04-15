import tkinter as tk

ventana  = tk.Tk()
ventana.geometry("500x500")
ventana.title("Pack")

etiqueta1 = tk.Label(ventana,text = "Arriba",bg ="lightblue")
etiqueta1.pack(side = "top", fill = "x")

etiqueta2 = tk.Label(ventana,text = "Abajo",bg ="lightgreen")
etiqueta2.pack(side = "bottom", fill = "x")

etiqueta3 = tk.Label(ventana,text = "Izquierda",bg ="lightcoral")
etiqueta3.pack(side = "left", fill = "y")

etiqueta3 = tk.Label(ventana,text = "Derecha",bg ="lightyellow")
etiqueta3.pack(side = "right", fill = "y")

tk.mainloop()