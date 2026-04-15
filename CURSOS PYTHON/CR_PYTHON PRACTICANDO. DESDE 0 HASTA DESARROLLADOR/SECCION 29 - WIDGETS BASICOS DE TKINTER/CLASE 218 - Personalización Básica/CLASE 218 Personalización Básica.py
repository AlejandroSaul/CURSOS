import tkinter as tk

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("500x500")

etiqueta = tk.Label(ventana, 
                    text="Bienvenido a tkinter",
                    bg="red",
                    fg="darkblue",
                    width=50,
                    height=4,
                    font=("Helvetica",24,"italic")
                    )
etiqueta.pack(pady =50)
etiqueta.pack(padx =10)
#etiqueta.config(bg="red")
#etiqueta.config(fg="darkblue")

def actionBoton():
    etiqueta.config(text="Boton Presionado", bg="green")

boton = tk.Button(text="Haz click aca",
                  font=("Arial",20,"bold"),
                  bg = "orange",
                  fg = "white",
                  activebackground="red",
                  activeforeground="blue",
                  width=10,
                  command=actionBoton
                  )
boton.pack()

ventana.mainloop()