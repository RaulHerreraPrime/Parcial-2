from tkinter import*

ventana = Tk()
ventana.geometry("300x225")  #tamaño de la ventana
i=PhotoImage(file="logo.gif")   #se importa la imagen
l=Label(ventana,image=i).pack()        #se imprime la imagen
ventana.mainloop()
