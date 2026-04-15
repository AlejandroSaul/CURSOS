import tkinter as tk

def cambiarTexto():
    mensajeCambiante.config(text="Texto Cambiado")

def restalecerTexto():
    mensajeCambiante.config(text="Texto Original")

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("500x500")

texto = tk.Label(ventana,text="Texto")
texto.pack()

texto.config(text="Funcionalidades")

mensajeCambiante = tk.Label(ventana,text="Texto Original ")
mensajeCambiante.pack()

boton1 = tk.Button(ventana, text = "Cambiar Texto", command=cambiarTexto)
boton1.pack()

boton2 = tk.Button(ventana, text = "Restablecer Texto", command=restalecerTexto)
boton2.pack()

ventana.mainloop()