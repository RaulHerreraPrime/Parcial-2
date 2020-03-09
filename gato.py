from tkinter import*
global turno
global bo1
global bo2
global bo3
global bo4
global bo5
global bo6
global bo7
global bo8
global bo9

bo1=0
bo2=0
bo3=0
bo4=0
bo5=0
bo6=0
bo7=0
bo8=0
bo9=0

turno=0

def bot1():
    global turno
    global bo1
    if(turno==0):
        b1.config(text="X",state=DISABLED,bg="red",fg="white")
        turno=1
        bo1=3
        l=Label(ventana,text="player 2",font=("arial 24")).grid(column=1,row=4)  

    else:
        b1.config(text="O",state=DISABLED,bg="blue",fg="white")
        turno=0
        bo1=4
        l=Label(ventana,text="player 1",font=("arial 24")).grid(column=1,row=4) 
    ganador()
        
def bot2():
    global turno
    global bo2
    if(turno==0):
        b2.config(text="X",state=DISABLED,bg="red",fg="white")
        turno=1
        bo2=3
        l=Label(ventana,text="player 2",font=("arial 24")).grid(column=1,row=4)
        
    else:
        b2.config(text="O",state=DISABLED,bg="blue",fg="white")
        turno=0
        bo2=4
        l=Label(ventana,text="player 1",font=("arial 24")).grid(column=1,row=4)
    
    ganador()
        
def bot3():
    global turno
    global bo3
    if(turno==0):
        b3.config(text="X",state=DISABLED,bg="red",fg="white")
        turno=1
        bo3=3
        l=Label(ventana,text="player 2",font=("arial 24")).grid(column=1,row=4)
            
    else:
        b3.config(text="O",state=DISABLED,bg="blue",fg="white")
        turno=0
        bo3=4
        l=Label(ventana,text="player 1",font=("arial 24")).grid(column=1,row=4)

    ganador()

def bot4():
    global turno
    global bo4
    if(turno==0):
        b4.config(text="X",state=DISABLED,bg="red",fg="white")
        turno=1
        bo4=3
        l=Label(ventana,text="player 2",font=("arial 24")).grid(column=1,row=4)
        
    else:
        b4.config(text="O",state=DISABLED,bg="blue",fg="white")
        turno=0
        bo4=4
        l=Label(ventana,text="player 1",font=("arial 24")).grid(column=1,row=4)
    
    ganador()

def bot5():
    global turno
    global bo5
    if(turno==0):
        b5.config(text="X",state=DISABLED,bg="red",fg="white")
        turno=1
        bo5=3
        l=Label(ventana,text="player 2",font=("arial 24")).grid(column=1,row=4)
        
    else:
        b5.config(text="O",state=DISABLED,bg="blue",fg="white")
        turno=0
        bo5=4
        l=Label(ventana,text="player 1",font=("arial 24")).grid(column=1,row=4)

    ganador()

def bot6():
    global turno
    global bo6
    if(turno==0):
        b6.config(text="X",state=DISABLED,bg="red",fg="white")
        turno=1
        bo6=3
        l=Label(ventana,text="player 2",font=("arial 24")).grid(column=1,row=4)
        
    else:
        b6.config(text="O",state=DISABLED,bg="blue",fg="white")
        turno=0
        bo6=4
        l=Label(ventana,text="player 1",font=("arial 24")).grid(column=1,row=4)

    ganador()

def bot7():
    global turno
    global bo7
    if(turno==0):
        b7.config(text="X",state=DISABLED,bg="red",fg="white")
        turno=1
        bo7=3
        l=Label(ventana,text="player 2",font=("arial 24")).grid(column=1,row=4)
        
    else:
        b7.config(text="O",state=DISABLED,bg="blue",fg="white")
        turno=0
        bo7=4
        l=Label(ventana,text="player 1",font=("arial 24")).grid(column=1,row=4)

    ganador()

def bot8():
    global turno
    global bo8
    if(turno==0):
        b8.config(text="X",state=DISABLED,bg="red",fg="white")
        turno=1
        bo8=3
        l=Label(ventana,text="player 2",font=("arial 24")).grid(column=1,row=4)
        
    else:
        b8.config(text="O",state=DISABLED,bg="blue",fg="white")
        turno=0
        bo8=4
        l=Label(ventana,text="player 1",font=("arial 24")).grid(column=1,row=4)

    ganador()

def bot9():
    global turno
    global bo9
    if(turno==0):
        b9.config(text="X",state=DISABLED,bg="red",fg="white")
        turno=1
        bo9=3
        l=Label(ventana,text="player 2",font=("arial 24")).grid(column=1,row=4)
        
    else:
        b9.config(text="O",state=DISABLED,bg="blue",fg="white")
        turno=0
        bo9=4
        l=Label(ventana,text="player 1",font=("arial 24")).grid(column=1,row=4)
    
    ganador()

def ganador():
    global bo1
    global bo2
    global bo3
    global bo4
    global bo5
    global bo6
    global bo7
    global bo8
    global bo9
    w=0
    if(bo1+bo2+bo3==9 or bo4+bo5+bo6==9 or bo7+bo8+bo9==9 or bo1+bo4+bo7==9 or bo2+bo5+bo8==9 or bo3+bo6+bo9==9 or bo1+bo5+bo9==9 or bo3+bo5+bo7==9):
        l=Label(ventana,text="player 1 wins",bg="red",fg="blue",font=("arial 24")).grid(column=1,row=4)  
        w=1
        
    elif (bo1+bo2+bo3==12 or bo4+bo5+bo6==12 or bo7+bo8+bo9==12 or bo1+bo4+bo7==12 or bo2+bo5+bo8==12 or bo3+bo6+bo9==12 or bo1+bo5+bo9==12 or bo3+bo5+bo7==12):
        l=Label(ventana,text="player 2 wins",bg="blue",fg="red",font=("arial 24")).grid(column=1,row=4) 
        w=1
    
    elif (bo1+bo2+bo3+bo4+bo5+bo6+bo7+bo8+bo9>=31):
        l=Label(ventana,text="  Gato  ",bg="yellow",fg="black",font=("arial 24")).grid(column=1,row=4)
        w=1
    if(w==1):
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
def salir():
    ventana.destroy()

def reset():
    global turno
    global bo1
    global bo2
    global bo3
    global bo4
    global bo5
    global bo6
    global bo7
    global bo8
    global bo9

    bo1=0
    bo2=0
    bo3=0
    bo4=0
    bo5=0
    bo6=0
    bo7=0
    bo8=0
    bo9=0
    turno=0

    b1.config(state=NORMAL,text="T",bg="black",fg="white")
    b2.config(state=NORMAL,text="T",bg="black",fg="white")
    b3.config(state=NORMAL,text="T",bg="black",fg="white")
    b4.config(state=NORMAL,text="I",bg="black",fg="white")
    b5.config(state=NORMAL,text="A",bg="black",fg="white")
    b6.config(state=NORMAL,text="O",bg="black",fg="white")
    b7.config(state=NORMAL,text="C",bg="black",fg="white")
    b8.config(state=NORMAL,text="C",bg="black",fg="white")
    b9.config(state=NORMAL,text="E",bg="black",fg="white")
    l=Label(ventana,text="     \t     ",bg="white",fg="white",font=("arial 24")).grid(column=1,row=4)
    l=Label(ventana,text="player 1",font=("arial 24")).grid(column=1,row=4)

ventana=Tk()
l=Label(ventana,text="player 1",font=("arial 24")).grid(column=1,row=4)
b1=Button(ventana,text="T",bg="black",fg="white",command=bot1,width=15,height=5,font=("arial 18"))
b1.grid(column=0,row=0)
b2=Button(ventana,text="T",bg="black",fg="white",command=bot2,width=15,height=5,font=("arial 18"))
b2.grid(column=0,row=1)
b3=Button(ventana,text="T",bg="black",fg="white",command=bot3,width=15,height=5,font=("arial 18"))
b3.grid(column=0,row=2)
b4=Button(ventana,text="I",bg="black",fg="white",command=bot4,width=15,height=5,font=("arial 18"))
b4.grid(column=1,row=0)
b5=Button(ventana,text="A",bg="black",fg="white",command=bot5,width=15,height=5,font=("arial 18"))
b5.grid(column=1,row=1)
b6=Button(ventana,text="O",bg="black",fg="white",command=bot6,width=15,height=5,font=("arial 18"))
b6.grid(column=1,row=2)
b7=Button(ventana,text="C",bg="black",fg="white",command=bot7,width=15,height=5,font=("arial 18"))
b7.grid(column=2,row=0)
b8=Button(ventana,text="C",bg="black",fg="white",command=bot8,width=15,height=5,font=("arial 18"))
b8.grid(column=2,row=1)
b9=Button(ventana,text="E",bg="black",fg="white",command=bot9,width=15,height=5,font=("arial 18"))
b9.grid(column=2,row=2)
salir=Button(ventana,text="salir",bg="grey",fg="black",command=salir,width=10,height=3,font=("arial 10"))
salir.grid(column=0,row=4)
reset=Button(ventana,text="reset",bg="grey",fg="black",command=reset,width=10,height=3,font=("arial 10"))
reset.grid(column=2,row=4)


ventana.mainloop()
