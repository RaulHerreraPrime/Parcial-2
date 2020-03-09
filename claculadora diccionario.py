class calcu:
    def __init__(self):
        pass

    def menu(self):
        a=0
        while(a!=9):
            try:
                a=int(input("selecciona: \n\t0 == Suma\n\t1 == Resta\n\t2 == multiplicacion\nu otro valor para salir\n\t"))
            except ValueError:
                a=9
            if(a>-1 and a<4):

                state=True
                state1=True
                while(state==True):
                    try:
                        b=int(input("ingresa primer número\t"))
                        state=False
                    except ValueError:
                        state=True

                while(state1==True):
                    try:
                        c=int(input("ingresa segundo número\t"))
                        state1=False
                    except ValueError:
                        state1=True

                z=self.diccionario(a,b,c)
                print(z)
            
        print("adios")


    def diccionario(self,x,b,c):
        w={
            0: b+c,
            1: b-c,
            2: b*c,
        }
        return w.get(x,"Adios")     #si no se obtiene el valor marcado hace lo de la derecha de la coma

#instrucciones
cal=calcu()
cal.menu()