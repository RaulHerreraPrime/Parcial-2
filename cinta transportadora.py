from tkinter import*
import time

global peq
global med
global grand

peq=0
med=0
grand=0

def entrocaja():
    si.config(state=DISABLED)
    no.config(state=DISABLED)
    time.sleep(1)
    h=Label(ventana,text="En terminal, ¿De que tamaño es la caja?",font=("arial 18")).grid(column=1,row=0)
    chico.config(state=NORMAL)
    mediano.config(state=NORMAL)
    grande.config(state=NORMAL)

def noentro():
    si.config(state=DISABLED)
    no.config(state=DISABLED)
    time.sleep(1)
    g=Label(ventana,text="\t\t¿Entró una caja\t\t",font=("arial 18")).grid(column=1,row=0)
    si.config(state=NORMAL)
    no.config(state=NORMAL)

def chico():
    global peq
    peq=peq+1
    time.sleep(1)
    h=Label(ventana,text="\t\t¿Entró una caja?\t\t",font=("arial 18")).grid(column=1,row=0)
    si.config(state=NORMAL)
    no.config(state=NORMAL)

def mediano():
    global med
    med=med+1
    time.sleep(1)
    h=Label(ventana,text="\t\t¿Entró una caja?\t\t",font=("arial 18")).grid(column=1,row=0)
    si.config(state=NORMAL)
    no.config(state=NORMAL)

def grande():
    global grand
    grand=grand+1
    time.sleep(1)
    h=Label(ventana,text="\t\t¿Entró una caja?\t\t",font=("arial 18")).grid(column=1,row=0)
    si.config(state=NORMAL)
    no.config(state=NORMAL)

def registro():
    global peq
    global med
    global grand
    l=Label(ventana,text="No. cajas chicas",font=("arial 18")).grid(column=0,row=3)
    w=Label(ventana,text=peq,font=("arial 18")).grid(column=2,row=3)
    r=Label(ventana,text="No. cajas medianas",font=("arial 18")).grid(column=0,row=4)
    y=Label(ventana,text=med,font=("arial 18")).grid(column=2,row=4)
    x=Label(ventana,text="No. cajas grandes",font=("arial 18")).grid(column=0,row=5)
    o=Label(ventana,text=grand,font=("arial 18")).grid(column=2,row=5)
    p=Label(ventana,text="No. cajas Totales",font=("arial 18")).grid(column=0,row=6)
    n=Label(ventana,text=peq+med+grand,font=("arial 18")).grid(column=2,row=6)

def salir():
    ventana.destroy()

ventana=Tk()
l=Label(ventana,text="¿Entró una caja?",font=("arial 18")).grid(column=1,row=0)
si=Button(ventana,text="si",bg="green",fg="black",command=entrocaja,width=7,height=1,font=("arial 18"))
si.grid(column=0,row=1)
no=Button(ventana,text="no",bg="red",fg="white",command=noentro,width=7,height=1,font=("arial 18"))
no.grid(column=1,row=1)
inv=Button(ventana,text="inventario",bg="blue",fg="white",command=registro,width=7,height=1,font=("arial 18"))
inv.grid(column=2,row=1)
grande=Button(ventana,text="grande",bg="red",fg="white",command=grande,width=7,height=1,font=("arial 18"),state=DISABLED)
grande.grid(column=2,row=2)
mediano=Button(ventana,text="mediana",bg="yellow",fg="black",command=mediano,width=7,height=1,font=("arial 18"),state=DISABLED)
mediano.grid(column=1,row=2)
chico=Button(ventana,text="chica",bg="blue",fg="white",command=chico,width=7,height=1,font=("arial 18"),state=DISABLED)
chico.grid(column=0,row=2)
salir=Button(ventana,text="salir",bg="gray",fg="white",command=salir,width=7,height=1,font=("arial 18"))
salir.grid(column=2,row=0)
ventana.mainloop()