import tkinter as tk
from tkinter import messagebox




#iniciar tkinter
aplicacion = tk.Tk()

#tamaño de la ventana +0+0 ubicacion del sistema 
aplicacion.geometry("1020x630+0+0")
#titulo de la ventana
aplicacion.title("Gestor de Restaurantes")

# color del fondo 
aplicacion.config(bg="burlywood")

#layout app
#Panel superior
panel_superior = tk.Frame(aplicacion,bd=1,relief="flat")
panel_superior.pack(side="top")
etiqueta_titulo = tk.Label(panel_superior,text="Sistema de Facturacion",
                           fg="azure4",font=('Dosis',58),bg="burlywood",width=27)
etiqueta_titulo.grid(row=0,column=0)
#Panel izquierdo 
panel_izquierdo = tk.Frame(aplicacion,bd=1,relief="flat")
panel_izquierdo.pack(side="left")

#panel comida 
panel_comida = tk.LabelFrame(panel_izquierdo,text="Comida",font=("Dosis",19,"bold"),bd=1,relief="flat",fg="azure4")
panel_comida.pack(side="left")

#panel bebida 
panel_bebida = tk.LabelFrame(panel_izquierdo,text="Bebida",font=("Dosis",19,"bold"),bd=1,relief="flat",fg="azure4")
panel_bebida.pack(side="left")

#panel postres 
panel_postres = tk.LabelFrame(panel_izquierdo,text="Postres",font=("Dosis",19,"bold"),bd=1,relief="flat",fg="azure4")
panel_postres.pack(side="left")

#panel costos
panel_costos = tk.Frame(panel_izquierdo,bd=1,relief="flat")
panel_costos.pack(side="bottom")



#panel derecho
panel_derecho = tk.Frame(aplicacion,bd=1,relief="flat")
panel_derecho.pack(side="right")

#panel calculadora
panel_calculadora = tk.Frame(panel_derecho,bd=1,relief="flat",bg="burlywood")
panel_calculadora.pack(side="top")


#panel recibo
panel_recibo = tk.Frame(panel_derecho,bd=1,relief="flat",bg="burlywood")
panel_recibo.pack(side="bottom")


#panel botones
panel_botones = tk.Frame(panel_derecho,bd=1,relief="flat",bg="burlywood")
panel_botones.pack(side="bottom")


# lista de productos
lista_comida = ["pollo","camarones","tacos 1","tacos 2","tacos 3"]
lista_bebidas = ["jugo 1","jugo 2","jugo 3","jugo 4","jugo 5"]
lista_postres = ["helado 1","helado 2","helado 3","helado 4","helado 5"]

#crear un checkbutton
#generar items comida
var_comida = []
cuadros_comida = []
text_comida = []
contador = 0 
for comida in lista_comida:
    #crear check button
    var_comida.append("")
    var_comida[contador] = tk.IntVar()
    comida = tk.Checkbutton(panel_comida,
                            text=comida.title(),
                            font=("dosis",19,"bold"),
                            onvalue=1,
                            offvalue=0,
                            variable=var_comida[contador])
    comida.grid(row=contador,column=0,sticky="w")
    #crear cuadro de entrada 
    cuadros_comida.append("")
    text_comida.append("")
    cuadros_comida[contador] = tk.Entry(panel_comida,
                                        font=("dosis",18,"bold"),
                                        bd=1,
                                        width=6,
                                        state="disabled",
                                        textvariable=text_comida[contador])
    cuadros_comida[contador].grid(row=contador,column=1)

    contador += 1
#generar items bebida
var_bebida = []
cuadros_bebida = []
text_bebida = []
contador = 0 
for bebida in lista_bebidas:
    var_bebida.append("")
    var_bebida[contador] = tk.IntVar()
    bebida = tk.Checkbutton(panel_bebida,text=bebida.title(),font=("dosis",19,"bold"),
                            onvalue=1,offvalue=0,variable=var_bebida[contador])
    bebida.grid(row=contador,column=0,sticky="w")
    #crear cuadro de entrada 
    cuadros_bebida.append("")
    text_bebida.append("")
    cuadros_bebida[contador] = tk.Entry(panel_bebida,
                                        font=("dosis",18,"bold"),
                                        bd=1,
                                        width=6,
                                        state="disabled",
                                        textvariable=text_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,column=1)
    contador += 1
#generar items postres
var_postres = []
cuadros_postres = []
text_postres = []
contador = 0 
for postre in lista_postres:
    var_postres.append("")
    var_postres[contador] = tk.IntVar()
    postre = tk.Checkbutton(panel_postres,text=postre.title(),font=("dosis",19,"bold"),
                            onvalue=1,offvalue=0,variable=var_postres[contador])
    postre.grid(row=contador,column=0,sticky="w")
    #crear cuadro de entrada 
    cuadros_postres.append("")
    text_postres.append("")
    cuadros_postres[contador] = tk.Entry(panel_postres,
                                        font=("dosis",18,"bold"),
                                        bd=1,
                                        width=6,
                                        state="disabled",
                                        textvariable=text_postres[contador])
    cuadros_postres[contador].grid(row=contador,column=1)
    contador += 1






#evitar que la pantalla se cierre 
aplicacion.mainloop()





    

