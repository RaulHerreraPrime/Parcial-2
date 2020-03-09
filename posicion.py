from tkinter import*

global m
global n
m=2
n=2

def up():
    global m,n

    if(n<1):
        n=4
    else:
        n=n-1
    bm.grid(column=m,row=n)

def down():
    global m,n
    
    if(n>3):
        n=0
    else:
        n=n+1
        
    bm.grid(column=m,row=n)

def right():
    global m,n

    if(m>3):
        m=0
       
    else:
        m=m+1
        
    bm.grid(column=m,row=n)

def left():
    global m,n
    
    if(m<1):
        m=4
        
    else:
        m=m-1
        
    bm.grid(column=m,row=n)

def exit():
    ventana.destroy()

ventana=Tk()
b0=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b0.grid(column=0,row=0)
b1=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b1.grid(column=1,row=0)
b2=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b2.grid(column=2,row=0)
b3=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b3.grid(column=3,row=0)
b4=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b4.grid(column=4,row=0)
b5=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b5.grid(column=0,row=1)
b6=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b6.grid(column=1,row=1)
b7=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b7.grid(column=2,row=1)
b8=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b8.grid(column=3,row=1)
b9=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b9.grid(column=4,row=1)
b10=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b10.grid(column=0,row=2)
b11=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b11.grid(column=1,row=2)
b12=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b12.grid(column=2,row=2)
b13=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b13.grid(column=3,row=2)
b14=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b14.grid(column=4,row=2)
b15=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b15.grid(column=0,row=3)
b16=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b16.grid(column=1,row=3)
b17=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b17.grid(column=2,row=3)
b18=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b18.grid(column=3,row=3)
b19=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b19.grid(column=4,row=3)
b20=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b20.grid(column=0,row=4)
b21=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b21.grid(column=1,row=4)
b22=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b22.grid(column=2,row=4)
b23=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b23.grid(column=3,row=4)
b24=Button(ventana,text="\t",bg="grey",state=DISABLED,width=6,height=3)
b24.grid(column=4,row=4)
bm=Button(ventana,text="\t",bg="yellow",state=DISABLED,width=6,height=3)
bm.grid(column=m,row=n)


up=Button(ventana,text="Up",bg="green",fg="white",width=6,height=3,font=("arial 9"),command=up).grid(column=8,row=1)
down=Button(ventana,text="Down",bg="green",fg="white",width=6,height=3,font=("arial 9"),command=down).grid(column=8,row=3)
left=Button(ventana,text="Left",bg="green",fg="white",width=6,height=3,font=("arial 9"),command=left).grid(column=7,row=2)
right=Button(ventana,text="Right",bg="green",fg="white",width=6,height=3,font=("arial 9"),command=right).grid(column=9,row=2)
ext=Button(ventana,text="EXIT",bg="red",fg="white",width=6,height=3,font=("arial 9"),command=exit).grid(column=8,row=2)

ventana.mainloop()