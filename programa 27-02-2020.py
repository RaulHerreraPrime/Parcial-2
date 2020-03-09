from tkinter import*

def obtener():
    texto=t.get()
    l=Label(ventana,text=texto,font=("arial 18")).grid(column=0,row=2)
    cuadro.config(state=NORMAL)

ventana=Tk()
ventana.config(height=500)
b=Button(ventana,text="Enter",bg="blue",fg="white",command=obtener,width=5,height=1,font=("arial 18"))
b.grid(column=0,row=1)
t=StringVar()
cuadro=Entry(ventana,textvariable=t,show="*",font=("arial 18"),state=DISABLED,bd=15,width=50)
cuadro.place(x=100,y=100)
ventana.mainloop()

