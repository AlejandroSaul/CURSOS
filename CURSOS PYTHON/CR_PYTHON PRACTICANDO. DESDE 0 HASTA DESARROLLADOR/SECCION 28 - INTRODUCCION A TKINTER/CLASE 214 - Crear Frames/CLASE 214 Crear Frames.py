import tkinter as tk

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("500x500")
ventana.resizable(False, False)

marco = tk.Frame(ventana, height=200,width = 200, bg="gray", borderwidth= 5, relief='solid')
marco.propagate()
marco.pack(pady=50)

ventana.mainloop()