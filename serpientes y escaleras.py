from tkinter import*
from random import randint
import time

global turno,dado1,dado2,x1,y1,x2,y2
turno=1
x1=-50
x2=-50
y1=450
y2=475

def dados():
    global turno,dado1,dado2,x1,y1,x2,y2
    dado1= randint(1,6)
    dado2= randint(1,6)
    d1=Label(ventana,text=dado1,font="arial 18",bg="yellow").place(x=50,y=550,width=50,height=50)
    d2=Label(ventana,text=dado2,font="arial 18",bg="yellow").place(x=400,y=550,width=50,height=50)
    if(turno==1):
        x1=x1+(dado1*50)+(dado2*50)
        while(x1>450):
            y1=y1-50
            x1=x1-500
        print("1 ",x1,y1)
        pl=Label(ventana,text="player 2",font="arial 18").place(x=150,y=510,width=200,height=50)
        ganador()
        serpyesc()
        p1.place(x=x1,y=y1)
        turno=0
        time.sleep(.3)
        
    elif(turno==0):
        x2=x2+(dado1*50)+(dado2*50)
        while(x2>450):
            y2=y2-50
            x2=x2-500
        print("2 ",x2,y2)
        pl=Label(ventana,text="player 1",font="arial 18").place(x=150,y=510,width=200,height=50)
        ganador()
        serpyesc()
        p2.place(x=x2,y=y2)
        turno=1
        time.sleep(.3)

def serpyesc():
    global turno,x1,x2,y1,y2
    if(turno==0):
        if(x1==200 and y1==350):
            x1=250
            y1=450
            l=Label(ventana,text="serpiente :(",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p1.place(x=250,y=450)
        elif(x1==250 and y1==250):
            x1=50
            y1=400
            l=Label(ventana,text="serpiente :(",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p1.place(x=50,y=400)
        elif(x1==150 and y1==100):
            x1=50
            y1=200
            l=Label(ventana,text="serpiente :(",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p1.place(x=50,y=200)
        elif(x1==350 and y1==50):
            x1=250
            y1=100
            l=Label(ventana,text="serpiente :(",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p1.place(x=250,y=100)
        elif(x1==400 and y1==400):
            x1=250
            y1=150
            l=Label(ventana,text="escalera :)",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p1.place(x=250,y=150)
        elif(x1==50 and y1==300):
            x1=100
            y1=200
            l=Label(ventana,text="escalera :)",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p1.place(x=100,y=200)
        elif(x1==100 and y1==100):
            x1=0
            y1=0
            l=Label(ventana,text="escalera :)",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p1.place(x=0,y=0)
        elif(x1==300 and y1==150):
            x1=450
            y1=0
            l=Label(ventana,text="escalera :)",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p1.place(x=450,y=0)
            ganador()

        else:
            l=Label(ventana,text="\t\t",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            

    elif(turno==1):
        if(x2==200 and y2==375):
            x2=250
            y2=475
            l=Label(ventana,text="serpiente :(",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            
        elif(x2==250 and y2==275):
            x2=50
            y2=425
            l=Label(ventana,text="serpiente :(",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p2.place(x=50,y=425)
        elif(x2==150 and y2==125):
            x2=50
            y2=225
            l=Label(ventana,text="serpiente :(",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p2.place(x=50,y=225)
        elif(x2==350 and y2==75):
            x2=250
            y2=125
            l=Label(ventana,text="serpiente :(",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p2.place(x=250,y=125)
        elif(x2==400 and y2==425):
            x2=250
            y2=175
            l=Label(ventana,text="escalera :)",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p2.place(x=250,y=175)
        elif(x2==50 and y2==325):
            x2=100
            y2=225
            l=Label(ventana,text="escalera :)",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p2.place(x=100,y=225)
        elif(x2==100 and y2==125):
            x2=0
            y2=25
            l=Label(ventana,text="escalera :)",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p2.place(x=0,y=25)
        elif(x2==300 and y2==175):
            x2=450
            y2=25
            l=Label(ventana,text="escalera :)",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)
            p2.place(x=450,y=25)
            ganador()
        else:
            l=Label(ventana,text="\t\t",font="arial 18")
            l.place(x=150,y=650,width=200,height=20)



def ganador():
    global x1,y1,x2,y2
    if((x1==450 and y1==0) or y1<0):
        pl=Label(ventana,text="player 1 wins",font="arial 18",bg="orange").place(x=150,y=510,width=200,height=50)
        x1=450
        y1=0
        dados.config(state=DISABLED)
    elif((x2==450 and y2==25) or y2<0): 
        pl=Label(ventana,text="player 2 wins",font="arial 18",bg="orange").place(x=150,y=510,width=200,height=50)
        x2=450
        y2=0
        dados.config(state=DISABLED)

def reinicio():
    global turno,x1,y1,x2,y2
    x1=x2=-50
    y1=450
    y2=475
    turno=1
    pl=Label(ventana,text="player 1     ",font="arial 18").place(x=150,y=510,width=200,height=50)
    p1.place(x=0,y=y1)
    p2.place(x=0,y=y2)
    dados.config(state=NORMAL)

def funcion1():
    otra_ventana = Toplevel()
    otra_ventana.geometry("300x225")
    i=PhotoImage(file="logo.gif")
    l=Label(otra_ventana,image=i).place(x=0,y=0)
    otra_ventana.mainloop()
    
    

def funcion2():
    otra_ventana = Toplevel()
    otra_ventana.geometry("300x225")
    i=PhotoImage(file="logo1.gif")
    l=Label(otra_ventana,image=i).place(x=0,y=0)
    otra_ventana.mainloop()

def exit():
    ventana.destroy()

    

ventana=Tk()
ventana.geometry("700x700")
tablero=PhotoImage(file="tablero-500x500.gif")
ds=PhotoImage(file="decepticon.gif")
au=PhotoImage(file="autobot.gif")

l1=Label(ventana,image=tablero).place(x=0,y=0)

p1=Button(ventana,image=au,command=funcion1)
p1.place(x=0,y=450)
p2=Button(ventana,image=ds,command=funcion2)
p2.place(x=0,y=475)
dados=Button(ventana,text="Tirar Dados",bg="blue",fg="white",font="arial 14",command=dados)
dados.place(x=150,y=575,width=200,height=70)
pl=Label(ventana,text="player 1",font="arial 18").place(x=150,y=510,width=200,height=50)
reinicio=Button(ventana,text="reinicio",bg="pink",fg="white",font="arial 14",command=reinicio)
reinicio.place(x=550,y=100,width=100,height=50)
exit=Button(ventana,text="Exit",bg="gold",fg="black",font="arial 14",command=exit)
exit.place(x=550,y=200,width=100,height=50)
ventana.mainloop()

