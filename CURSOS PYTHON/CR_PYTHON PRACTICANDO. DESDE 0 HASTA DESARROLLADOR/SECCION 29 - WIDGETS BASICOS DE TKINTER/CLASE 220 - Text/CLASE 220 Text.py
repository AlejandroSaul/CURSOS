import tkinter as tk

def mostarComentario():
    comentarioObtenido = comentario.get("1.0", tk.END).strip()
    resultado.config(text=f"comentario: {comentarioObtenido}")

ventana = tk.Tk()
ventana.title("Titulo")
ventana.geometry("500x500")
etiqueta = tk.Label(ventana,text = "Digite su comentario")
etiqueta.pack()

comentario = tk.Text(ventana, width= 40, height= 20, wrap="word")#Hace que el texto salte a la siguiente línea respetando palabras completas.
comentario.pack()
boton = tk.Button(ventana,text="Mostrar Comentario",command=mostarComentario)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()