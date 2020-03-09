from tkinter import*
def imprimir():
    kk=Label(ventana,text="joto el que presiono el boton",bg="red",fg="blue",font=("arial 64")).grid(column=0,row=1)  
    
ventana=Tk()
texto= Label(ventana,text="Hola mundo").grid(column=1,row=0)   #escribimos el texto en la ventana
boton=Button(ventana,text="B1",command = imprimir,bg="red",fg="blue",font=("arial 64")).grid(column=0,row=0)
ventana.mainloop()                        #abrimos la ventana