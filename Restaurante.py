from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ''
precios_comida = [6.75, 8.95, 12.85, 9.10, 8.90, 7.80, 10, 12.50]
precios_bebida = [12, 12, 2, 3, 0.80, 1.50, 1.50, 2]
precios_postre = [3.50, 3.50, 3.50, 4, 4, 4, 4, 6]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')

        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')

        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')

        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postre[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    iva = sub_total * 0.21
    total = sub_total + iva

    var_precio_comida.set(f'{round(sub_total_comida, 2)}€')
    var_precio_bebida.set(f'{round(sub_total_bebida, 2)}€')
    var_precio_postre.set(f'{round(sub_total_postre, 2)}€')
    var_subtotal.set(f'{round(sub_total, 2)}€')
    var_precio_iva.set(f'{round(iva, 2)}€')
    var_precio_total.set(f'{round(total, 2)}€')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 60 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tPrecio Items\n')
    texto_recibo.insert(END, f'-' * 58 + ' \n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'{int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0

    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'{int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0

    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t'
                                     f'{int(postre.get()) * precios_postre[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 58 + ' \n')
    texto_recibo.insert(END, f'Precio de la comida: \t\t\t{var_precio_comida.get()}\n')
    texto_recibo.insert(END, f'Precio de la bebida: \t\t\t{var_precio_bebida.get()}\n')
    texto_recibo.insert(END, f'Precio de los postres: \t\t\t{var_precio_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 58 + ' \n')
    texto_recibo.insert(END, f'Sub-Total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'IVA: \t\t\t{var_precio_iva.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_precio_total.get()}\n')
    texto_recibo.insert(END, f'*' * 60 + '\n')
    texto_recibo.insert(END, 'Gracias. Vuelva Pronto')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado')



def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')

    for texto in texto_bebida:
        texto.set('0')

    for texto in texto_postre:
        texto.set('0')


    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)

    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)

    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)


    for v in variables_comida:
        v.set(0)

    for v in variables_bebida:
        v.set(0)

    for v in variables_postre:
        v.set(0)


    var_precio_comida.set('')
    var_precio_bebida.set('')
    var_precio_postre.set('')
    var_subtotal.set('')
    var_precio_iva.set('')
    var_precio_total.set('')




# Iniciar tkinter
aplicacion = Tk()



# Tamaño de la ventana
aplicacion.geometry('1420x830+0+0')


# Evitar maximizar
aplicacion.resizable(0, 0)


# Titulo de la ventana
aplicacion.title('Restaurante Python - Sistema de Facturación')

# color de fondo de la ventana
aplicacion.config(bg='chartreuse3')


# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4',
                        font=('Dosis', 48), bg='burlywood', width=27)

etiqueta_titulo.grid(row=0, column=0)


# Panel Izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)


# Panel precios
panel_precios = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=150)
panel_precios.pack(side=BOTTOM)


# Panel Carta
panel_carta = LabelFrame(panel_izquierdo, text='Carta', font=('Dosis', 14, 'bold'),
                         bd=1, relief=FLAT, fg='azure4')

panel_carta.pack(side=LEFT)


# Panel Bebidas
panel_bebida = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 14, 'bold'),
                         bd=1, relief=FLAT, fg='azure4')

panel_bebida.pack(side=LEFT)

# Panel Postres
panel_postre = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 14, 'bold'),
                         bd=1, relief=FLAT, fg='azure4')

panel_postre.pack(side=LEFT)


# Panel Derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)


# Panel Calculadora
panel_calculadora = LabelFrame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# Panel recibo
panel_recibo = LabelFrame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel botones
panel_botones = LabelFrame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()


# Lista de productos
lista_comidas = ['Pollo', 'Cordero', 'Salmón', 'Merluza', 'Kebab', 'Pizza Carbonara', 'Hamburguesa', 'Hamburguesa completa']
lista_bebidas = ['Vino tinto', 'Vino blanco', 'Coca-Cola', 'Cerveza', 'Agua', 'Zumo', 'Café', 'Seven-Up']
lista_postres = ['Yogurt', 'Helado', 'Tarta de queso', 'Tarta de la abuela', 'Fruta', 'Natillas', 'Arroz con leche', 'Flan']


# Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    # Crear checkbuttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_carta,
                         text=comida.title(),
                         font=('Dosis', 15, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_carta,
                                     font=('Dosis', 14, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])

    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador += 1



# Generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:

    # Crear checkbuttons
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebida, text=bebida.title(), font=('Dosis', 15, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador, column=0, sticky=W)

    # Crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebida,
                                     font=('Dosis', 14,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])

    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador += 1


# Generar items postres
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:

    # Generar Checkbuttons
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postre, text=postre.title(), font=('Dosis', 15, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador, column=0, sticky=W)


    # Generar cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postre,
                                     font=('Dosis', 14, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])

    cuadros_postre[contador].grid(row=contador,
                                  column=1)
    contador += 1



# Variables
var_precio_comida = StringVar()
var_precio_bebida = StringVar()
var_precio_postre = StringVar()
var_subtotal = StringVar()
var_precio_iva = StringVar()
var_precio_total = StringVar()


# Establecer etiquetas de precios y campos de entrada
etiqueta_precio_comida = Label(panel_precios,
                               text='Precio comida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_precio_comida.grid(row=0,
                            column=0)

texto_precio_comida = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_comida)

texto_precio_comida.grid(row=0,
                         column=1,
                         padx=41)


etiqueta_precio_bebida = Label(panel_precios,
                               text='Precio Bebida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_precio_bebida.grid(row=1,
                            column=0)

texto_precio_bebida = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_bebida)

texto_precio_bebida.grid(row=1,
                         column=1,
                         padx=41)


etiquvar_precio_postre = Label(panel_precios,
                               text='Precio Postres',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiquvar_precio_postre.grid(row=2,
                            column=0)

tevar_precio_postre = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_postre)

tevar_precio_postre.grid(row=2,
                         column=1,
                         padx=41)



etiqueta_subtotal = Label(panel_precios,
                               text='Subtotal',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_subtotal.grid(row=0,
                        column=2)

texto_subtotal = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_subtotal)

texto_subtotal.grid(row=0,
                    column=3,
                    padx=41)



etiqueta_iva = Label(panel_precios,
                               text='IVA',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_iva.grid(row=1,
                  column=2)

texto_iva = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_iva)

texto_iva.grid(row=1,
                column=3,
               padx=41)


etiqueta_total = Label(panel_precios,
                               text='Total',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_total.grid(row=2,
                    column=2)

texto_total = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_total)

texto_total.grid(row=2,
                column=3,
                 padx=41)


# Botones
botones = ['total', 'recibo', 'guardar', 'reset']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)


# Área de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12,'bold'),
                    bd=1,
                    width=49,
                    height=10)

texto_recibo.grid(row=0,
                  column=0)



# Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=37,
                          bd=1)

visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+',
                       '4', '5', '6', '-',
                       '1', '2', '3', 'x',
                       '=', 'Borrar', '0', '/']

botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0


botones_guardados[0].config(command=lambda  : click_boton('7'))
botones_guardados[1].config(command=lambda  : click_boton('8'))
botones_guardados[2].config(command=lambda  : click_boton('9'))
botones_guardados[3].config(command=lambda  : click_boton('+'))
botones_guardados[4].config(command=lambda  : click_boton('4'))
botones_guardados[5].config(command=lambda  : click_boton('5'))
botones_guardados[6].config(command=lambda  : click_boton('6'))
botones_guardados[7].config(command=lambda  : click_boton('-'))
botones_guardados[8].config(command=lambda  : click_boton('1'))
botones_guardados[9].config(command=lambda  : click_boton('2'))
botones_guardados[10].config(command=lambda  : click_boton('3'))
botones_guardados[11].config(command=lambda  : click_boton('*'))
botones_guardados[12].config(command=resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda  : click_boton('0'))
botones_guardados[15].config(command=lambda  : click_boton('/'))

# Evitar que la pantalla se cierre
aplicacion.mainloop()
