import tkinter as tk
from tkinter import messagebox
import random
import datetime
from tkinter import filedialog,messagebox

operador =""
precios_comida = [2,2,2,2,2,2,2,2]
precios_bebida = [1,1,1,1,1,1,1,1]
precios_postre = [3,3,3,3,3,3,3,3]



def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,tk.END)
    visor_calculadora.insert(tk.END,operador)


def borrar():
    global operador
    operador =""
    visor_calculadora.delete(0,tk.END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,tk.END)
    visor_calculadora.insert(0,resultado)
    operador = ""

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if var_comida[x].get() == 1:
            cuadros_comida[x].config(state = tk.NORMAL)
            if cuadros_comida[x].get() == "0":
                cuadros_comida[x].delete(0,tk.END)
            cuadros_comida[x].delete(0,tk.END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=tk.DISABLED)
            text_comida[x].set("0")
        x += 1
    x = 0
    for c in cuadros_bebida:
        if var_bebida[x].get() == 1:
            cuadros_bebida[x].config(state = tk.NORMAL)
            if cuadros_bebida[x].get() == "0":
                cuadros_bebida[x].delete(0,tk.END)
            cuadros_bebida[x].delete(0,tk.END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=tk.DISABLED)
            text_bebida[x].set("0")
        x += 1
    x = 0
    for c in cuadros_postres:
        if var_postres[x].get() == 1:
            cuadros_postres[x].config(state = tk.NORMAL)
            if cuadros_postres[x].get() == "0":
                cuadros_postres[x].delete(0,tk.END)
            cuadros_postres[x].delete(0,tk.END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=tk.DISABLED)
            text_postres[x].set("0")
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in text_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get())) * precios_comida[p]
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in text_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get())) * precios_bebida[p]
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in text_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get())) * precios_postre[p]
        p += 1

    sub_total = sub_total_comida+sub_total_bebida+sub_total_postres
    impuestos = sub_total * 0.16
    total = sub_total+impuestos

    var_costo_comida.set(f"$ {round(sub_total_comida,2)}")
    var_costo_bebida.set(f"$ {round(sub_total_bebida,2)}")
    var_costo_postres.set(f"$ {round(sub_total_postres,2)}")
    var_subtotal.set(f"$ {round(sub_total,2)}")
    var_impuestos.set(f"$ {round(impuestos,2)}")
    var_total.set(f"$ {round(total,2)}")


def recibo():
    texto_recibo.delete(1.0,tk.END)
    num_recibo = f"N# - {random.randint(1000,9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year}-{fecha.hour}:{fecha.minute}"
    texto_recibo.insert(tk.END,f"Datos: \t{num_recibo}\t\t{fecha_recibo}")
    texto_recibo.insert(tk.END,f"*"*47+"\n")
    texto_recibo.insert(tk.END,"Items\t\tCant.\tCosto Items")
    texto_recibo.insert(tk.END,f"-"*54+"\n")
    x = 0 
    for comida in text_comida:
        if comida.get() != "0":
            texto_recibo.insert(tk.END,f"{lista_comida[x]}\t\t{comida.get()}\t"
                                        f"$ {int(comida.get())*precios_comida[x]}\n")    
        x += 1
    x = 0 
    for bebida in text_bebida:
        if bebida.get() != "0":
            texto_recibo.insert(tk.END,f"{lista_bebidas[x]}\t\t{bebida.get()}\t"
                                        f"$ {int(bebida.get())*precios_bebida[x]}\n")    
        x += 1
    x = 0
    for postre in text_postres:
        if postre.get() != "0":
            texto_recibo.insert(tk.END,f"{lista_postres[x]}\t\t{postre.get()}\t"
                                        f"$ {int(postre.get())*precios_postre[x]}\n")    
        x += 1

    texto_recibo.insert(tk.END,f"-"*54+"\n")
    texto_recibo.insert(tk.END,f"Costo de la comida: \t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(tk.END,f"Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n")
    texto_recibo.insert(tk.END,f"Costo de la postres: \t\t\t{var_costo_postres.get()}\n")
    texto_recibo.insert(tk.END,f"Costo de la subtotal: \t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(tk.END,f"Costo de la impuestos: \t\t\t{var_impuestos.get()}\n")
    texto_recibo.insert(tk.END,f"Costo de la total: \t\t\t{var_total.get()}\n")

def guardar():
    info_recibo = texto_recibo.get(1.0,tk.END)
    archivo = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Informacion","Su recibo ha sido guardado")


def reset():
    texto_recibo.delete(0.1,tk.END)
    for text in text_comida:
        text.set("0")
    for text in text_bebida:
        text.set("0")
    for text in text_postres:
        text.set("0")
    for cuadro in cuadros_comida:
        cuadro.config(state=tk.DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=tk.DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=tk.DISABLED)
    for var in var_comida:
        var.set(0)
    for var in var_bebida:
        var.set(0)
    for var in var_postres:
        var.set(0)
    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postres.set("")
    var_subtotal.set("")
    var_impuestos.set("")
    var_total.set("")



#iniciar tkinter
aplicacion = tk.Tk()

#tamaño de la ventana +0+0 ubicacion del sistema 
aplicacion.geometry("1020x631+0+0")
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

#panel costos
panel_costos = tk.Frame(panel_izquierdo,bd=1,relief="flat",bg="azure4",padx=40,pady=30)
panel_costos.pack(side="bottom")

#panel comida 
panel_comida = tk.LabelFrame(panel_izquierdo,text="Comida",font=("Dosis",19,"bold"),bd=1,relief="flat",fg="azure4",pady=20)
panel_comida.pack(side="left")

#panel bebida 
panel_bebida = tk.LabelFrame(panel_izquierdo,text="Bebida",font=("Dosis",19,"bold"),bd=1,relief="flat",fg="azure4",pady=20)
panel_bebida.pack(side="left")

#panel postres 
panel_postres = tk.LabelFrame(panel_izquierdo,text="Postres",font=("Dosis",19,"bold"),bd=1,relief="flat",fg="azure4",pady=20)
panel_postres.pack(side="left")





#panel derecho
panel_derecho = tk.Frame(aplicacion,bd=1,relief="flat")
panel_derecho.pack(side="right")

#panel calculadora
panel_calculadora = tk.Frame(panel_derecho,bd=1,relief="flat",bg="burlywood")
panel_calculadora.pack(side="top")

#panel recibo
panel_recibo = tk.Frame(panel_derecho,bd=1,relief="flat",bg="burlywood")
panel_recibo.pack(side="top")

#panel botones
panel_botones = tk.Frame(panel_derecho,bd=1,relief="flat",bg="burlywood")
panel_botones.pack(side="bottom")




# lista de productos
lista_comida = ["tacos -1","tacos 0","tacos 1","tacos 2","tacos 3","tacos 4","tacos 5","tacos 6"]
lista_bebidas = ["jugo 1","jugo 2","jugo 3","jugo 4","jugo 5","jugo 6","jugo 7","jugo 8"]
lista_postres = ["helado 1","helado 2","helado 3","helado 4","helado 5","helado 6","helado 7","helado 8"]

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
                            variable=var_comida[contador],
                            command=revisar_check)
    comida.grid(row=contador,column=0,sticky="w")
    #crear cuadro de entrada 
    cuadros_comida.append("")
    text_comida.append("")
    text_comida[contador] = tk.StringVar()
    text_comida[contador].set("0")

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
    bebida = tk.Checkbutton(panel_bebida,
                            text=bebida.title(),
                            font=("dosis",19,"bold"),
                            onvalue=1,
                            offvalue=0,
                            variable=var_bebida[contador],
                            command=revisar_check)
    bebida.grid(row=contador,column=0,sticky="w")
    #crear cuadro de entrada 
    cuadros_bebida.append("")
    text_bebida.append("")
    text_bebida[contador] = tk.StringVar()
    text_bebida[contador].set("0")
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
    postre = tk.Checkbutton(panel_postres,
                            text=postre.title(),
                            font=("dosis",19,"bold"),
                            onvalue=1,
                            offvalue=0,
                            variable=var_postres[contador],
                            command=revisar_check)
    postre.grid(row=contador,column=0,sticky="w")
    #crear cuadro de entrada 
    cuadros_postres.append("")
    text_postres.append("")
    text_postres[contador] = tk.StringVar()
    text_postres[contador].set("0")
    cuadros_postres[contador] = tk.Entry(panel_postres,
                                        font=("dosis",18,"bold"),
                                        bd=1,
                                        width=6,
                                        state="disabled",
                                        textvariable=text_postres[contador])
    cuadros_postres[contador].grid(row=contador,column=1)
    contador += 1

# costos y campos de entrada 
#variables
var_costo_comida = tk.StringVar()
var_costo_bebida = tk.StringVar()
var_costo_postres = tk.StringVar()
var_subtotal = tk.StringVar()
var_impuestos = tk.StringVar()
var_total = tk.StringVar()
#costo comida
etiqueta_costo_comida = tk.Label(panel_costos,
                                 text="Costo Comida",
                                 font=("Dosis",12,"bold"),
                                 bg="azure4",
                                 fg="White"
                                 )
etiqueta_costo_comida.grid(row=0,column=0)
texto_costo_comida = tk.Entry(panel_costos,
                              font=("Dosis",12,"bold"),
                              bd=1,
                              width=10,
                              state="readonly",
                              textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1,padx=41)
#costo bebida
etiqueta_costo_bebida = tk.Label(panel_costos,
                                 text="Costo Bebida",
                                 font=("Dosis",12,"bold"),
                                 bg="azure4",
                                 fg="White"
                                 )

etiqueta_costo_bebida.grid(row=1,column=0)
texto_costo_bebida = tk.Entry(panel_costos,
                              font=("Dosis",12,"bold"),
                              bd=1,
                              width=10,
                              state="readonly",
                              textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1,padx=41)
#costo postres
etiqueta_costo_postres = tk.Label(panel_costos,
                                 text="Costo Postres",
                                 font=("Dosis",12,"bold"),
                                 bg="azure4",
                                 fg="White"
                                 )

etiqueta_costo_postres.grid(row=2,column=0)
texto_costo_postres = tk.Entry(panel_costos,
                              font=("Dosis",12,"bold"),
                              bd=1,
                              width=10,
                              state="readonly",
                              textvariable=var_costo_postres)
texto_costo_postres.grid(row=2,column=1,padx=41)
#subtotal
etiqueta_costo_subtotal = tk.Label(panel_costos,
                                 text="Subtotal",
                                 font=("Dosis",12,"bold"),
                                 bg="azure4",
                                 fg="White"
                                 )

etiqueta_costo_subtotal.grid(row=0,column=2)
texto_costo_subtotal = tk.Entry(panel_costos,
                              font=("Dosis",12,"bold"),
                              bd=1,
                              width=10,
                              state="readonly",
                              textvariable=var_subtotal)
texto_costo_subtotal.grid(row=0,column=3,padx=41)
#impuestos
etiqueta_costo_impuestos = tk.Label(panel_costos,
                                 text="Impuestos",
                                 font=("Dosis",12,"bold"),
                                 bg="azure4",
                                 fg="White"
                                 )

etiqueta_costo_impuestos.grid(row=1,column=2)
texto_costo_impuestos = tk.Entry(panel_costos,
                              font=("Dosis",12,"bold"),
                              bd=1,
                              width=10,
                              state="readonly",
                              textvariable=var_impuestos)
texto_costo_impuestos.grid(row=1,column=3,padx=41)
#total
etiqueta_costo_total = tk.Label(panel_costos,
                                 text="Total",
                                 font=("Dosis",12,"bold"),
                                 bg="azure4",
                                 fg="White"
                                 )

etiqueta_costo_total.grid(row=2,column=2)
texto_costo_total = tk.Entry(panel_costos,
                              font=("Dosis",12,"bold"),
                              bd=1,
                              width=10,
                              state="readonly",
                              textvariable=var_total)
texto_costo_total.grid(row=2,column=3,padx=41)

# botones

botones = ["Total","Recibo","Guardar","Reset"]
botones_creados = []
columnas = 0
for boton in botones:
    boton = tk.Button(panel_botones,
                      text=boton.title(),
                      font=("Dosis",14,"bold"),
                      fg="black",
                      bg="azure4",
                      bd=1,
                      width=7,
                      cursor="hand2",
                      disabledforeground="red")
    botones_creados.append(boton)
    boton.grid(row=0,column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=reset)

# area de recibo 
texto_recibo = tk.Text(panel_recibo,
                       font=("Dosis",14,"bold"),
                       bd=1,
                       width=42,
                       height=10)
texto_recibo.grid(row=0,column=0)

# area de calculadora 
visor_calculadora = tk.Entry(panel_calculadora,
                             font=("Dosis",14,"bold"),
                             width=32,
                             bd=1
                             )
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ["7","8","9","+",
                       "4","5","6","-",
                       "1","2","3","x",
                       "=","Borrar","0","/"]

botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = tk.Button(panel_calculadora,
                      text=boton.title(),
                      font=("Dosis",14,"bold"),
                      fg="black",
                      bg="azure4",
                      bd=1,
                      width=8
                      )
    botones_guardados.append(boton)
    boton.grid(row=fila,
               column=columna)
    
    if columna == 3:
        fila += 1
    
    columna += 1

    if columna == 4:
        columna = 0 


botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=lambda : obtener_resultado())
botones_guardados[13].config(command=lambda : borrar())
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))




#evitar que la pantalla se cierre 
aplicacion.mainloop()





    


