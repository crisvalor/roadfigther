import tkinter as t
t.ventana = t.Tk()
t.ventana.geometry("600x400+500+200")
t.ventana.title("menu")
#Imagen del juego
imagenP = t.PhotoImage(file = "portada.png")
Imagen = t.Label(t.ventana, image = imagenP).place(x = 0, y = 0)
#Funciones de los botones
def nivel1():
    pass
Usuario1 = t.Label(text = "Usuario1:",font = ("Agency FB",14)).place(x = 200, y = 100)
#Creando un campo para texto de Usuario
entradaU1 = t.StringVar()
txtUsuario1 = t.Entry(t.ventana,textvariable = entradaU1).place(x = 260,y = 110)
Usuario2 = t.Label(text = "Usuario2:",font = ("Agency FB",14)).place(x = 200, y = 140)
entradaU2 = t.StringVar()
txtUsuario2 = t.Entry(t.ventana,textvariable = entradaU2).place(x = 260,y = 150)
#Crear los botones
btnStark = t.Button(t.ventana,text = "Lvl 1",command = nivel1,
                    font = ("Agency FB",14)).place(x = 70, y = 200)
btnStark = t.Button(t.ventana,text = "Lvl 2",
                    font = ("Agency FB",14)).place(x = 170, y = 200)
btnStark = t.Button(t.ventana,text = "Lvl 3",
                    font = ("Agency FB",14)).place(x = 270, y = 200)
btnStark = t.Button(t.ventana,text = "Lvl 4",
                    font = ("Agency FB",14)).place(x = 370, y = 200)
btnStark = t.Button(t.ventana,text = "Lvl 5",
                    font = ("Agency FB",14)).place(x = 470, y = 200)
t.ventana.mainloop()
 
