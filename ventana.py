
from tkinter import *

class Ventana(Frame):
       
    def __init__(self, master=None):
        super().__init__(master,width=680, height=260)
        self.master = master
        self.pack()
        self.create_widgets()

    def fNuevo():
        pass  

    def fModificar():
        pass     
    
    def fEliminar():
        pass  


    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=93,height=259)
   

        self.btnNuevo = Button(frame1, text="Nuevo", command=self.fNuevo, bg="Blue", fg="white")
        self.btnNuevo.place(x=5,y=50,width=80,height=30)

        self.btnModificar = Button(frame1, text="Modificar", command=self.fModificar, bg="Blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80,height=30)
        
        self.btnEliminar = Button(frame1, text="Eliminar", command=self.fEliminar, bg="Blue", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80,height=30)

        frame2 = Frame(self, bg="#3E91F6")
        frame2.place(x=95,y=0,width=150,height=259)

        lb1 = Label(frame2, text="Nombre:")
        lb1.place(x=3, y=5)
        self.txtNombre = Entry(frame2)
        self.txtNombre.place(x=3,y=25,width=100,height=20)

        lb2 = Label(frame2, text="Apellido:")
        lb2.place(x=3, y=55)
        self.txtApellido = Entry(frame2)
        self.txtApellido.place(x=3,y=75,width=100,height=20)

        lb3 = Label(frame2, text="Legajo:")
        lb3.place(x=3, y=105)
        self.txtLegajo = Entry(frame2)
        self.txtLegajo.place(x=3,y=125,width=100,height=20)


