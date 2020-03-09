from tkinter import*
global contador
global resultado
global operacion

resultado=0
contador=0
operacion=0


def acu0():
    global contador
    contador=10*contador+0
    l=Label(ventana,text=contador,font=("arial 18")).grid(column=1, row=0)

def acu1():
    global contador
    contador=10*contador+1
    l=Label(ventana,text=contador,font=("arial 18")).grid(column=1, row=0)

def acu2():
    global contador
    contador=10*contador+2
    l=Label(ventana,text=contador,font=("arial 18")).grid(column=1, row=0)

def acu3():
    global contador
    contador=10*contador+3
    l=Label(ventana,text=contador,font=("arial 18")).grid(column=1, row=0)

def acu4():
    global contador
    contador=10*contador+4
    l=Label(ventana,text=contador,font=("arial 18")).grid(column=1, row=0)

def acu5():
    global contador
    contador=10*contador+5
    l=Label(ventana,text=contador,font=("arial 18")).grid(column=1, row=0)

def acu6():
    global contador
    contador=10*contador+6
    l=Label(ventana,text=contador,font=("arial 18")).grid(column=1, row=0)

def acu7():
    global contador
    contador=10*contador+7
    l=Label(ventana,text=contador,font=("arial 18")).grid(column=1, row=0)

def acu8():
    global contador
    contador=10*contador+8
    l=Label(ventana,text=contador,font=("arial 18")).grid(column=1, row=0)

def acu9():
    global contador
    contador=10*contador+9
    l=Label(ventana,text=contador,font=("arial 18")).grid(column=1, row=0)

def mas():
    global contador
    global resultado
    global operacion
    resultado=contador
    contador=0
    operacion=0
    l=Label(ventana,text="\t",font=("arial 18")).grid(column=1, row=0)

def menos():
    global contador
    global resultado
    global operacion
    resultado=contador
    contador=0
    operacion=1
    l=Label(ventana,text="\t",font=("arial 18")).grid(column=1, row=0)

def por():
    global contador
    global resultado
    global operacion
    resultado=contador
    contador=0
    operacion=2
    l=Label(ventana,text="\t",font=("arial 18")).grid(column=1, row=0)

def div():
    global contador
    global resultado
    global operacion
    resultado=contador
    contador=0
    operacion=3
    l=Label(ventana,text="\t",font=("arial 18")).grid(column=1, row=0)

def igual():
    global contador
    global resultado
    global operacion
    l=Label(ventana,text="\t ",font=("arial 18")).grid(column=1, row=0)
    if(operacion==0):
        resultado=resultado+contador
    elif(operacion==1):
        resultado=resultado-contador
    elif(operacion==2):
        resultado=resultado*contador
    elif(operacion==3):
        try:
            resultado=resultado/contador
        except ZeroDivisionError:
            resultado="MATh ERROR"
            contador=0
    l=Label(ventana,text=resultado,font=("arial 18")).grid(column=1, row=0)
    contador=resultado
   

def c():
    global contador
    global resultado
    global operacion

    operacion=0
    resultado=0
    contador=0
    w=Label(ventana,text="\t ").grid(column=1, row=0)
    



ventana=Tk()
b0=Button(ventana,text="0",command=acu0,bg="blue",fg="white").grid(column=1,row=4)
b1=Button(ventana,text="1",command=acu1,bg="blue",fg="white").grid(column=0,row=3)
b2=Button(ventana,text="2",command=acu2,bg="blue",fg="white").grid(column=1,row=3)
b3=Button(ventana,text="3",command=acu3,bg="blue",fg="white").grid(column=2,row=3)
b4=Button(ventana,text="4",command=acu4,bg="blue",fg="white").grid(column=0,row=2)
b5=Button(ventana,text="5",command=acu5,bg="blue",fg="white").grid(column=1,row=2)
b6=Button(ventana,text="6",command=acu6,bg="blue",fg="white").grid(column=2,row=2)
b7=Button(ventana,text="7",command=acu7,bg="blue",fg="white").grid(column=0,row=1)
b8=Button(ventana,text="8",command=acu8,bg="blue",fg="white").grid(column=1,row=1)
b9=Button(ventana,text="9",command=acu9,bg="blue",fg="white").grid(column=2,row=1)
bmas=Button(ventana,text="+",command=mas,bg="red",fg="white").grid(column=3,row=1)
bmenos=Button(ventana,text="-",command=menos,bg="red",fg="white").grid(column=3,row=2)
bpor=Button(ventana,text="x",command=por,bg="red",fg="white").grid(column=3,row=3)
bdiv=Button(ventana,text="÷",command=div,bg="red",fg="white").grid(column=3,row=4)
beq=Button(ventana,text="=",command=igual,bg="yellow",fg="black").grid(column=0,row=4)
bc=Button(ventana,text="c",command=c,bg="red",fg="white").grid(column=2,row=4)



ventana.mainloop()

    