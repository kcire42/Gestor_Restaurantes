import tkinter as tk
from tkinter import messagebox



#Funciones
# def mensaje():
#     nombre = entrada.get()
#     etiqueta.config(text = f"Hola, {nombre}")


#iniciar tkinter
aplicacion = tk.Tk()

#tamaño de la ventana +0+0 ubicacion del sistema 
aplicacion.geometry("1020x630+0+0")
#titulo de la ventana
aplicacion.title("Gestor de Restaurantes")

# color del fondo 
aplicacion.config(bg="burlywood")
#caja de texto output
# etiqueta = tk.Label(aplicacion,text="Ingresa tu nombre ")
# etiqueta.pack(padx=10,pady=5)
#caja de input
# entrada = tk.Entry(aplicacion)
# entrada.pack(padx=10,pady=5)

# boton = tk.Button(aplicacion,text="Haz click aqui",command=mensaje)
# boton.pack(padx=10,pady=10)



#evitar que la pantalla se cierre 
aplicacion.mainloop()





    

