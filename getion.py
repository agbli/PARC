

from tkinter import *
from tkinter import messagebox, ttk
import time
from tkcalendar import * 
import sqlite3
import os
import tempfile



class Gestion:
    def __init__(self,root):
        self.root = root
        self.root.title("Gestion de parc informatique")
        self.root.geometry("1920x1080+0+0")
        
        
        title = Label(self.root, text="GESTION DE PARC INFORMATIQUE", bd=10, relief=RAISED, font=('Algerian',18), bg='Teal', fg='black')
        title.pack(side=TOP, fill=X)
        
        ########################frame0
        
        Frame0= Frame(self.root, bd=2, relief=RIDGE, bg='Teal')
        Frame0.place(x=0,y=50, width=1700,height=60) 
        
        lbl_Gestion = Label(Frame0, text="Gestion de parc informatique - Liste des machines",bg='Teal', font=("times new roman", 18)).place(x=10,y=10)
        
        
        self.btn_nouveau = Button(Frame0, text="Nouveau",command=self.nouveau, font=('times new roman',15), bg='Silver')
        self.btn_nouveau.place(x=1130,y=10,width=100)
        
        
        self.btn_modifier = Button(Frame0, text="Modifier",command=self.modifier, font=('times new roman',15), bg='Silver')
        self.btn_modifier.place(x=1270,y=10,width=100)
        
        self.btn_supprimer = Button(Frame0, text="Supprimer", font=('times new roman',15), bg='Silver')
        self.btn_supprimer.place(x=1400,y=10,width=100)
        
        self.btn_imprimer = Button(Frame0, text="Imprimer", font=('times new roman',15), bg='Silver')
        self.btn_imprimer.place(x=1530,y=10,width=100)
        
        
        ##########################frame01
        Frame01= Frame(self.root, bd=2, relief=RIDGE, bg='Silver')
        Frame01.place(x=0,y=120, width=1700,height=60) 
        lbl_Affichage = Label(Frame01, text="Affichage des machine :",bg='Silver', font=("times new roman", 18)).place(x=10,y=10)
        lbl_Affichage = Label(Frame01, text="Toutes les machines",bg='Silver', font=("times new roman", 18)).place(x=300,y=10)
        self.btn_Affichage = Button(Frame01, text="Affichage de toutes les machines",command=self.affichage, font=('times new roman',14), bg='Silver')
        self.btn_Affichage.place(x=1270,y=10,width=400)
        
        
        #################################frame1
        
        Frame1 = Frame(self.root, bd=2, relief=RIDGE)
        Frame1.place(x=10,y=190, width=400,height=750)
        
        Framec = Frame(self.root, bd=2, relief=RIDGE,bg='Teal')
        Framec.place(x=10,y=190, width=400,height=50)
        lbl_Machine = Label(Framec, text="Machine",bg='Teal', font=("times new roman", 18)).place(x=10,y=10)
        lbl_Utilisateur = Label(Framec, text="Utilisateur",bg='Teal', font=("times new roman", 18)).place(x=250,y=10)
        
        scroll_y = Scrollbar(Frame1, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)
        
        #########################frame2
        Frame2 = Frame (self.root, bd=2, relief=RIDGE)
        Frame2.place(x=430, y=190, width=150, height=300)
        
        #########################frame3
        Frame3 = Frame (self.root, bd=2, relief=RIDGE)
        Frame3.place(x=590, y=190, width=150, height=300)
        
        #########################frame4
        Frame4 = Frame (self.root, bd=2, relief=RIDGE)
        Frame4.place(x=750, y=190, width=250, height=140)
        
        #########################frame5
        Frame5 = Frame (self.root, bd=2, relief=RIDGE)
        Frame5.place(x=750, y=350, width=250, height=140)
        
        #########################frame6
        Frame6 = Frame (self.root, bd=2, relief=RIDGE)
        Frame6.place(x=1010, y=190, width=150, height=300)
        
        #########################frame7
        Frame7 = Frame (self.root, bd=2, relief=RIDGE)
        Frame7.place(x=1170, y=190, width=150, height=300)
        
        #########################frame8
        Frame8 = Frame (self.root, bd=2, relief=RIDGE)
        Frame8.place(x=1330, y=190, width=150, height=140)
        
        #########################frame9
        Frame9 = Frame (self.root, bd=2, relief=RIDGE)
        Frame9.place(x=1330, y=350, width=150, height=140)
        
        #########################frame10
        Frame10 = Frame (self.root, bd=2, relief=RIDGE)
        Frame10.place(x=430, y=550, width=150, height=300)
        
        #########################frame11
        Frame11 = Frame (self.root, bd=2, relief=RIDGE)
        Frame11.place(x=590, y=550, width=150, height=300)
        
        #########################frame12
        Frame12 = Frame (self.root, bd=2, relief=RIDGE)
        Frame12.place(x=750, y=550, width=250, height=140)
        
        #########################frame13
        Frame13 = Frame (self.root, bd=2, relief=RIDGE)
        Frame13.place(x=750, y=710, width=250, height=140)
        
        #########################frame14
        Frame14 = Frame (self.root, bd=2, relief=RIDGE)
        Frame14.place(x=1010, y=550, width=150, height=300)
        
        #########################frame15
        Frame15 = Frame (self.root, bd=2, relief=RIDGE)
        Frame15.place(x=1170, y=550, width=150, height=300)
        
        #########################frame16
        Frame16 = Frame (self.root, bd=2, relief=RIDGE)
        Frame16.place(x=1330, y=550, width=150, height=140)
        
        #########################frame17
        Frame17 = Frame (self.root, bd=2, relief=RIDGE)
        Frame17.place(x=1330, y=710, width=150, height=140)
        
        ########################frame18
        Frame18 = Frame (self.root, bd=2, relief=RIDGE)
        Frame18.place(x=600, y=880, width=600, height=65)
        self.btn_modif = Button(Frame18, text="Locaux",command=self.temple, font=('times new roman',15), bg='Silver')
        self.btn_modif.place(x=10,y=10,width=100)
        
        self.btn_modif = Button(Frame18, text="utilisateur",command=self.plan, font=('times new roman',15), bg='Silver')
        self.btn_modif.place(x=150,y=10,width=100)
        
        self.btn_modif = Button(Frame18, text="utilisateur",command=self.boot, font=('times new roman',15), bg='Silver')
        self.btn_modif.place(x=300,y=10,width=100)
        
        self.btn_modif = Button(Frame18, text="utilisateur",command=self.toop, font=('times new roman',15), bg='Silver')
        self.btn_modif.place(x=450,y=10,width=100)
        

        
        
        
        
        ###########################root2
        
    def temple(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Modifier le plan des locaux")
        self.root2.geometry("1300x900+0+0")
        title = Label(self.root2, text="Modifier le plan des locaux", bd=10, relief=RAISED, font=('Algerian',18), bg='Teal', fg='black')
        title.pack(side=TOP, fill=X)
        
        Framed= Frame(self.root2, bd=2, relief=RIDGE, bg='Teal')
        Framed.place(x=0,y=50, width=1700,height=60) 
        
        lbl_Gestion = Label(Framed, text="Gestion des lieux",bg='Teal', font=("times new roman", 18)).place(x=10,y=10)
        
        
        self.btn_nouveau = Button(Framed, text="Nouveau", font=('times new roman',15), bg='Silver')
        self.btn_nouveau.place(x=1130,y=10,width=100)
        
        
        self.btn_modifier = Button(Framed, text="Modifier", font=('times new roman',15), bg='Silver')
        self.btn_modifier.place(x=1270,y=10,width=100)
        
        self.btn_supprimer = Button(Framed, text="Supprimer", font=('times new roman',15), bg='Silver')
        self.btn_supprimer.place(x=1400,y=10,width=100)
        
        self.btn_imprimer = Button(Framed, text="Imprimer", font=('times new roman',15), bg='Silver')
        self.btn_imprimer.place(x=1530,y=10,width=100)
        
        
         #########################frame2
        Frame2 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame2.place(x=10, y=190, width=150, height=300)
        
        #########################frame3
        Frame3 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame3.place(x=200, y=190, width=150, height=300)
        
        #########################frame4
        Frame4 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame4.place(x=390, y=190, width=250, height=140)
        
        #########################frame5
        Frame5 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame5.place(x=390, y=350, width=250, height=140)
        
        #########################frame6
        Frame6 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame6.place(x=670, y=190, width=150, height=300)
        
        #########################frame7
        Frame7 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame7.place(x=860, y=190, width=150, height=300)
        
        #########################frame8
        Frame8 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame8.place(x=1050, y=190, width=150, height=140)
        
        #########################frame9
        Frame9 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame9.place(x=1050, y=350, width=150, height=140)
        
        #########################frame10
        Frame10 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame10.place(x=10, y=550, width=150, height=300)
        
        #########################frame11
        Frame11 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame11.place(x=200, y=550, width=150, height=300)
        
        #########################frame12
        Frame12 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame12.place(x=390, y=550, width=250, height=140)
        
        #########################frame13
        Frame13 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame13.place(x=390, y=710, width=250, height=140)
        
        #########################frame14
        Frame14 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame14.place(x=670, y=550, width=150, height=300)
        
        #########################frame15
        Frame15 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame15.place(x=860, y=550, width=150, height=300)
        
        #########################frame16
        Frame16 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame16.place(x=1050, y=550, width=150, height=140)
        
        #########################frame17
        Frame17 = Frame (self.root2, bd=2, relief=RIDGE)
        Frame17.place(x=1050, y=710, width=150, height=140)
        ##########################frame18
        Frame18 = Frame (self.root2, bd=2, relief=RIDGE,bg='Silver')
        Frame18.place(x=1230,y=190, width=400,height=750)
        
        lbl_Affichage = Label(Frame18, text="Affichage des machine :",bg='Silver', font=("times new roman", 18)).place(x=10,y=10)
        
        lbl_Affichage = Label(Frame18, text="Affichage des machine :",bg='Silver', font=("times new roman", 14)).place(x=10,y=100)
        self.txt_adresse = Text (Frame18, font=("times new roman", 18), bg="lightyellow",)
        self.txt_adresse.place(x=10,y=120, width=350, height=50)
        
        lbl_Affichage = Label(Frame18, text="Affichage des machine :",bg='Silver', font=("times new roman", 14)).place(x=10,y=200)
        self.txt_adresse = Text (Frame18, font=("times new roman", 18), bg="lightyellow",)
        self.txt_adresse.place(x=10,y=220, width=350, height=150)
        
        self.txt_adresse = Text (Frame18, font=("times new roman", 18), bg="lightyellow",)
        self.txt_adresse.place(x=10,y=390, width=350, height=150)
        
        
        lbl_Affichage = Label(Frame18, text="Affichage des machine :",bg='Silver', font=("times new roman", 14)).place(x=10,y=550)
        self.txt_adresse = Text (Frame18, font=("times new roman", 18), bg="lightyellow",)
        self.txt_adresse.place(x=10,y=580, width=350, height=50)
        
        
        
        self.root2.mainloop() 
        
        
        
        
        #########root3
        
    def plan(self):
        self.root3 = Toplevel(self.root)
        self.root3.title("Modifier le plan des locaux")
        self.root3.geometry("1300x900+0+0")
        title = Label(self.root3, text="Modifier ", bd=10, relief=RAISED, font=('Algerian',18), bg='Teal', fg='black')
        title.pack(side=TOP, fill=X)
        
        Framep= Frame(self.root3, bd=2, relief=RIDGE, bg='Teal')
        Framep.place(x=0,y=50, width=1700,height=60) 
        
        lbl_Gestion = Label(Framep, text="Gestion des lieux",bg='Teal', font=("times new roman", 18)).place(x=10,y=10)
        
        
        self.btn_nouveau = Button(Framep, text="Nouveau", font=('times new roman',15), bg='Silver')
        self.btn_nouveau.place(x=1130,y=10,width=100)
        
        
        self.btn_modifier = Button(Framep, text="Modifier", font=('times new roman',15), bg='Silver')
        self.btn_modifier.place(x=1270,y=10,width=100)
        
        self.btn_supprimer = Button(Framep, text="Supprimer", font=('times new roman',15), bg='Silver')
        self.btn_supprimer.place(x=1400,y=10,width=100)
        
        self.btn_imprimer = Button(Framep, text="Imprimer", font=('times new roman',15), bg='Silver')
        self.btn_imprimer.place(x=1530,y=10,width=100)
        
        Framec = Frame(self.root3, bd=2, relief=RIDGE,bg='Teal')
        Framec.place(x=10,y=190, width=800,height=50)
        lbl_Machine = Label(Framec, text="Machine",bg='Teal', font=("times new roman", 18)).place(x=10,y=10)
        lbl_Utilisateur = Label(Framec, text="Utilisateur",bg='Teal', font=("times new roman", 18)).place(x=250,y=10)
        
        Frame1 = Frame(self.root3, bd=2, relief=RIDGE)
        Frame1.place(x=10,y=240, width=800,height=700)
        
        scroll_y = Scrollbar(Frame1, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)
        
        Frame18 = Frame (self.root3, bd=2, relief=RIDGE,bg='Silver')
        Frame18.place(x=1000,y=190, width=650,height=750)
        lbl_Affichage = Label(Frame18, text="Affichage des machine :",bg='Silver', font=("times new roman", 18)).place(x=10,y=10)
        
        lbl_nom = Label(Frame18, text="Nom:",bg='Silver', font=("times new roman", 18)).place(x=10,y=60)
        lbl_prenom = Label(Frame18, text="Prenom:",bg='Silver', font=("times new roman", 18)).place(x=10,y=100)
        lbl_sexe = Label(Frame18, text="Sexe:",bg='Silver', font=("times new roman", 18)).place(x=10,y=140)
        lbl_email = Label(Frame18, text="Email:",bg='Silver', font=("times new roman", 18)).place(x=10,y=180)
        lbl_nationalite = Label(Frame18, text="Nationalité:",bg='Silver', font=("times new roman", 18)).place(x=10,y=220)
        lbl_adresse = Label(Frame18, text="Adresse:",bg='Silver', font=("times new roman", 18)).place(x=10,y=260)
        
        
        txt_nom = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_nom.place(x=120,y=60, width=240)
        
        txt_prenom = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_prenom.place(x=120,y=100, width=240)
        
        self.ecri_sexe = ttk.Combobox(Frame18, font=('times new roman',18), state="readonly")
        self.ecri_sexe["values"] = ("Homme", "Femme")
        self.ecri_sexe.place(x=120, y=140, width=240)
        self.ecri_sexe.current(0)
        
        txt_email = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_email.place(x=120,y=180, width=240)
        
        txt_nationalite = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_nationalite.place(x=120,y=220, width=240)
        
        self.txt_adresse = Text (Frame18, font=("times new roman", 18), bg="lightyellow",)
        self.txt_adresse.place(x=120,y=260, width=240, height=50)
        
    
   
        
        self.root3.mainloop()
        
        
    def boot(self):
        self.root4 = Toplevel(self.root)
        self.root4.title("Modifier le plan des locaux")
        self.root4.geometry("1300x900+0+0")
        title = Label(self.root4, text="Le plan ", bd=10, relief=RAISED, font=('Algerian',18), bg='Teal', fg='black')
        title.pack(side=TOP, fill=X)
        
        Framed= Frame(self.root4, bd=2, relief=RIDGE, bg='Teal')
        Framed.place(x=0,y=50, width=1700,height=60) 
        
        lbl_Gestion = Label(Framed, text="Gestion des lieux",bg='Teal', font=("times new roman", 18)).place(x=10,y=10)
        
        
        self.btn_nouveau = Button(Framed, text="Nouveau", font=('times new roman',15), bg='Silver')
        self.btn_nouveau.place(x=1130,y=10,width=100)
        
        
        self.btn_modifier = Button(Framed, text="Modifier", font=('times new roman',15), bg='Silver')
        self.btn_modifier.place(x=1270,y=10,width=100)
        
        self.btn_supprimer = Button(Framed, text="Supprimer", font=('times new roman',15), bg='Silver')
        self.btn_supprimer.place(x=1400,y=10,width=100)
        
        self.btn_imprimer = Button(Framed, text="Imprimer", font=('times new roman',15), bg='Silver')
        self.btn_imprimer.place(x=1530,y=10,width=100)
        
        Framec = Frame(self.root4, bd=2, relief=RIDGE,bg='Teal')
        Framec.place(x=10,y=190, width=800,height=50)
        lbl_Machine = Label(Framec, text="Machine",bg='Teal', font=("times new roman", 18)).place(x=10,y=10)
        lbl_Utilisateur = Label(Framec, text="Utilisateur",bg='Teal', font=("times new roman", 18)).place(x=250,y=10)
        
        Frame1 = Frame(self.root4, bd=2, relief=RIDGE)
        Frame1.place(x=10,y=240, width=800,height=700)
        
        scroll_y = Scrollbar(Frame1, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)
        
        Frame18 = Frame (self.root4, bd=2, relief=RIDGE,bg='Silver')
        Frame18.place(x=1000,y=190, width=650,height=750)
        lbl_Affichage = Label(Frame18, text="Affichage des machine :",bg='Silver', font=("times new roman", 18)).place(x=10,y=10)
        
        lbl_nom = Label(Frame18, text="Nom:",bg='Silver', font=("times new roman", 18)).place(x=10,y=60)
        lbl_prenom = Label(Frame18, text="Prenom:",bg='Silver', font=("times new roman", 18)).place(x=10,y=100)
        lbl_sexe = Label(Frame18, text="Sexe:",bg='Silver', font=("times new roman", 18)).place(x=10,y=140)
        lbl_email = Label(Frame18, text="Email:",bg='Silver', font=("times new roman", 18)).place(x=10,y=180)
        lbl_nationalite = Label(Frame18, text="Nationalité:",bg='Silver', font=("times new roman", 18)).place(x=10,y=220)
        lbl_adresse = Label(Frame18, text="Adresse:",bg='Silver', font=("times new roman", 18)).place(x=10,y=260)
        
        
        txt_nom = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_nom.place(x=120,y=60, width=240)
        
        txt_prenom = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_prenom.place(x=120,y=100, width=240)
        
        self.ecri_sexe = ttk.Combobox(Frame18, font=('times new roman',18), state="readonly")
        self.ecri_sexe["values"] = ("Homme", "Femme")
        self.ecri_sexe.place(x=120, y=140, width=240)
        self.ecri_sexe.current(0)
        
        txt_email = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_email.place(x=120,y=180, width=240)
        
        txt_nationalite = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_nationalite.place(x=120,y=220, width=240)
        
        self.txt_adresse = Text (Frame18, font=("times new roman", 18), bg="lightyellow",)
        self.txt_adresse.place(x=120,y=260, width=240, height=50)
        
        Framec = Frame(self.root4, bd=2, relief=RIDGE,bg='Teal')
        Framec.place(x=10,y=190, width=800,height=50)
        lbl_Machine = Label(Framec, text="Machine",bg='Teal', font=("times new roman", 18)).place(x=10,y=10)
        lbl_Utilisateur = Label(Framec, text="Utilisateur",bg='Teal', font=("times new roman", 18)).place(x=250,y=10)
        
        Frame1 = Frame(self.root4, bd=2, relief=RIDGE)
        Frame1.place(x=10,y=240, width=800,height=700)
        
        scroll_y = Scrollbar(Frame1, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)
        
        Frame18 = Frame (self.root4, bd=2, relief=RIDGE,bg='Silver')
        Frame18.place(x=1000,y=190, width=650,height=750)
        lbl_Affichage = Label(Frame18, text="Affichage des machine :",bg='Silver', font=("times new roman", 18)).place(x=10,y=10)
        
        lbl_nom = Label(Frame18, text="Nom:",bg='Silver', font=("times new roman", 18)).place(x=10,y=60)
        lbl_prenom = Label(Frame18, text="Prenom:",bg='Silver', font=("times new roman", 18)).place(x=10,y=100)
        lbl_sexe = Label(Frame18, text="Sexe:",bg='Silver', font=("times new roman", 18)).place(x=10,y=140)
        lbl_email = Label(Frame18, text="Email:",bg='Silver', font=("times new roman", 18)).place(x=10,y=180)
        lbl_nationalite = Label(Frame18, text="Nationalité:",bg='Silver', font=("times new roman", 18)).place(x=10,y=220)
        lbl_adresse = Label(Frame18, text="Adresse:",bg='Silver', font=("times new roman", 18)).place(x=10,y=260)
        
        
        txt_nom = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_nom.place(x=120,y=60, width=240)
        
        txt_prenom = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_prenom.place(x=120,y=100, width=240)
        
        self.ecri_sexe = ttk.Combobox(Frame18, font=('times new roman',18), state="readonly")
        self.ecri_sexe["values"] = ("Homme", "Femme")
        self.ecri_sexe.place(x=120, y=140, width=240)
        self.ecri_sexe.current(0)
        
        txt_email = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_email.place(x=120,y=180, width=240)
        
        txt_nationalite = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_nationalite.place(x=120,y=220, width=240)
        
        self.txt_adresse = Text (Frame18, font=("times new roman", 18), bg="lightyellow",)
        self.txt_adresse.place(x=120,y=260, width=240, height=50)
        
        self.root4.mainloop()
        
        
        ##############################root5
        
    def toop(self):
        self.root5 = Toplevel(self.root)
        self.root5.title("Modifier le plan des locaux")
        self.root5.geometry("1300x900+0+0")
        title = Label(self.root5, text="Le plan ", bd=10, relief=RAISED, font=('Algerian',18), bg='Teal', fg='black')
        title.pack(side=TOP, fill=X)
        
        Framed= Frame(self.root5, bd=2, relief=RIDGE, bg='Teal')
        Framed.place(x=0,y=50, width=1700,height=60) 
        
        lbl_Gestion = Label(Framed, text="Gestion des lieux",bg='Teal', font=("times new roman", 18)).place(x=10,y=10)
        
        
        self.btn_nouveau = Button(Framed, text="Nouveau", font=('times new roman',15), bg='Silver')
        self.btn_nouveau.place(x=1130,y=10,width=100)
        
        
        self.btn_modifier = Button(Framed, text="Modifier", font=('times new roman',15), bg='Silver')
        self.btn_modifier.place(x=1270,y=10,width=100)
        
        self.btn_supprimer = Button(Framed, text="Supprimer", font=('times new roman',15), bg='Silver')
        self.btn_supprimer.place(x=1400,y=10,width=100)
        
        self.btn_imprimer = Button(Framed, text="Imprimer", font=('times new roman',15), bg='Silver')
        self.btn_imprimer.place(x=1530,y=10,width=100)
        
        Framec = Frame(self.root5, bd=2, relief=RIDGE,bg='Teal')
        Framec.place(x=10,y=190, width=800,height=50)
        lbl_Machine = Label(Framec, text="Machine",bg='Teal', font=("times new roman", 18)).place(x=10,y=10)
        lbl_Utilisateur = Label(Framec, text="Utilisateur",bg='Teal', font=("times new roman", 18)).place(x=250,y=10)
        
        Frame1 = Frame(self.root5, bd=2, relief=RIDGE)
        Frame1.place(x=10,y=240, width=800,height=700)
        
        scroll_y = Scrollbar(Frame1, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)
        
        Frame18 = Frame (self.root5, bd=2, relief=RIDGE,bg='Silver')
        Frame18.place(x=1000,y=190, width=650,height=750)
        lbl_Affichage = Label(Frame18, text="Affichage des machine :",bg='Silver', font=("times new roman", 18)).place(x=10,y=10)
        
        lbl_nom = Label(Frame18, text="Nom:",bg='Silver', font=("times new roman", 18)).place(x=10,y=60)
        lbl_prenom = Label(Frame18, text="Prenom:",bg='Silver', font=("times new roman", 18)).place(x=10,y=100)
        lbl_sexe = Label(Frame18, text="Sexe:",bg='Silver', font=("times new roman", 18)).place(x=10,y=140)
        lbl_email = Label(Frame18, text="Email:",bg='Silver', font=("times new roman", 18)).place(x=10,y=180)
        lbl_nationalite = Label(Frame18, text="Nationalité:",bg='Silver', font=("times new roman", 18)).place(x=10,y=220)
        lbl_adresse = Label(Frame18, text="Adresse:",bg='Silver', font=("times new roman", 18)).place(x=10,y=260)
        
        
        txt_nom = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_nom.place(x=120,y=60, width=240)
        
        txt_prenom = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_prenom.place(x=120,y=100, width=240)
        
        self.ecri_sexe = ttk.Combobox(Frame18, font=('times new roman',18), state="readonly")
        self.ecri_sexe["values"] = ("Homme", "Femme")
        self.ecri_sexe.place(x=120, y=140, width=240)
        self.ecri_sexe.current(0)
        
        txt_email = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_email.place(x=120,y=180, width=240)
        
        txt_nationalite = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_nationalite.place(x=120,y=220, width=240)
        
        self.txt_adresse = Text (Frame18, font=("times new roman", 18), bg="lightyellow",)
        self.txt_adresse.place(x=120,y=260, width=240, height=50)
        
        Framec = Frame(self.root5, bd=2, relief=RIDGE,bg='Teal')
        Framec.place(x=10,y=190, width=800,height=50)
        lbl_Machine = Label(Framec, text="Machine",bg='Teal', font=("times new roman", 18)).place(x=10,y=10)
        lbl_Utilisateur = Label(Framec, text="Utilisateur",bg='Teal', font=("times new roman", 18)).place(x=250,y=10)
        
        Frame1 = Frame(self.root5, bd=2, relief=RIDGE)
        Frame1.place(x=10,y=240, width=800,height=700)
        
        scroll_y = Scrollbar(Frame1, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)
        
        Frame18 = Frame (self.root5, bd=2, relief=RIDGE,bg='Silver')
        Frame18.place(x=1000,y=190, width=650,height=750)
        lbl_Affichage = Label(Frame18, text="Affichage des machine :",bg='Silver', font=("times new roman", 18)).place(x=10,y=10)
        
        lbl_nom = Label(Frame18, text="Nom:",bg='Silver', font=("times new roman", 18)).place(x=10,y=60)
        lbl_prenom = Label(Frame18, text="Prenom:",bg='Silver', font=("times new roman", 18)).place(x=10,y=100)
        lbl_sexe = Label(Frame18, text="Sexe:",bg='Silver', font=("times new roman", 18)).place(x=10,y=140)
        lbl_email = Label(Frame18, text="Email:",bg='Silver', font=("times new roman", 18)).place(x=10,y=180)
        lbl_nationalite = Label(Frame18, text="Nationalité:",bg='Silver', font=("times new roman", 18)).place(x=10,y=220)
        lbl_adresse = Label(Frame18, text="Adresse:",bg='Silver', font=("times new roman", 18)).place(x=10,y=260)
        
        
        txt_nom = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_nom.place(x=120,y=60, width=240)
        
        txt_prenom = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_prenom.place(x=120,y=100, width=240)
        
        self.ecri_sexe = ttk.Combobox(Frame18, font=('times new roman',18), state="readonly")
        self.ecri_sexe["values"] = ("Homme", "Femme")
        self.ecri_sexe.place(x=120, y=140, width=240)
        self.ecri_sexe.current(0)
        
        txt_email = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_email.place(x=120,y=180, width=240)
        
        txt_nationalite = Entry(Frame18,font=("times new roman",18), bg="lightyellow")
        txt_nationalite.place(x=120,y=220, width=240)
        
        self.txt_adresse = Text (Frame18, font=("times new roman", 18), bg="lightyellow",)
        self.txt_adresse.place(x=120,y=260, width=240, height=50)
        
        self.root5.mainloop()
        
    def nouveau(self):
        self.root6 = Toplevel(self.root)
        self.root6.title("Modifier le plan des locaux")
        self.root6.geometry("1300x900+0+0")
        title = Label(self.root6, text="Le plan ", bd=10, relief=RAISED, font=('Algerian',18), bg='Teal', fg='black')
        title.pack(side=TOP, fill=X)
        
        #############Frame1
        
        #Variable
        self.var_codeemplo = StringVar()
        self.var_entrepri = StringVar()
        self.var_nom = StringVar()
        self.var_marque = StringVar()
        self.var_sexe = StringVar()
        self.var_email = StringVar()
        self.var_adresse = StringVar()
        self.var_nationalite = StringVar()
        self.var_daj = StringVar()
        self.var_naissance = StringVar()
        self.var_experience = StringVar()
        self.var_idenfi = StringVar()
        self.var_tel = StringVar()
        self.var_statut = StringVar()
        
        Frame1 = Frame(self.root6, bd=2, relief=RIDGE)
        Frame1.place(x=10,y=120, width=880,height=850)
        
        title2 = Label(Frame1,text="Nouvelle machine", bd=20, relief=RAISED, font=("Algerian",30),bg="lightgray", fg="black")
        title2.pack(side=TOP, fill=X)
        
        lbl_code = Label(Frame1,text="Numero de table de la machine", font=("time new roman", 20)).place(x=10,y=150)
        self.txt_code = Entry(Frame1, textvariable=self.var_codeemplo, font=('times new roman',20), bg="lightyellow")
        self.txt_code.place(x=390, y=155, width=200)
        
        btn_recher = Button(Frame1, text="Recherche", font=("times new roman",15), bg="gray").place(x=600,y=150)
        
        lbl_entreprise = Label(Frame1, text="Entreprise", font=("times new roman", 18)).place(x=10,y=240)
        lbl_nom = Label(Frame1, text="Nom complet", font=("times new roman", 18)).place(x=10,y=310)
        lbl_marque = Label(Frame1, text="Marque", font=("times new roman", 18)).place(x=10,y=370)
        lbl_sexe = Label(Frame1, text="Sexe", font=("times new roman", 18)).place(x=10,y=430)
        lbl_email = Label(Frame1, text="Email", font=("times new roman", 18)).place(x=10,y=490)
        lbl_indentifiant = Label(Frame1, text="Identifiant", font=("times new roman", 18)).place(x=10,y=550)
        
        
        lbl_annee = Label(Frame1, text="Année de livraison", font=("times new roman", 18)).place(x=400,y=240)
        lbl_naissance = Label(Frame1, text="Date d'espiration", font=("times new roman", 18)).place(x=400,y=310)
        
        
        
        
        txt_entreprise = Entry(Frame1,textvariable=self.var_entrepri,font=("times new roman",18), bg="lightyellow")
        txt_entreprise.place(x=120,y=240, width=240)
        
        txt_nom = Entry(Frame1,textvariable=self.var_nom,font=("times new roman",18), bg="lightyellow")
        txt_nom.place(x=120,y=310, width=240)
        
        
        
        self.ecri_marque = ttk.Combobox(Frame1,textvariable=self.var_marque, font=('times new roman',18), state="readonly")
        self.ecri_marque["values"] = ("DELL", "AZUS","HP","LENOVO","SAMSUNG","APPL","TUCHIBA")
        self.ecri_marque.place(x=120,y=370, width=240)
        self.ecri_marque.current(0)
        
        self.ecri_sexe = ttk.Combobox(Frame1,textvariable=self.var_sexe, font=('times new roman',18), state="readonly")
        self.ecri_sexe["values"] = ("Homme", "Femme")
        self.ecri_sexe.place(x=120, y=430, width=240)
        self.ecri_sexe.current(0)
        
        txt_email = Entry(Frame1,textvariable=self.var_email,font=("times new roman",18), bg="lightyellow")
        txt_email.place(x=120,y=490, width=240)
        
        
        
          
        self.txt_daj = ttk.Combobox(Frame1, textvariable=self.var_daj,font=("times new roman", 18), state="readonly")
        self.txt_daj["values"] = ("2022-2023", "2023-2024","2024-2025","2025-2026","2026-2027")
        self.txt_daj.place(x=600, y=240)
        self.txt_daj.current(0)
        
        self.ecri_date = DateEntry(Frame1, font=("times new roman",18), bg="lightgray", state="readonly", date_pattern ='dd/mm/yy')
        self.ecri_date.place(x=600, y=310, width= 260)
        
        
        txt_identifiant = Entry(Frame1,textvariable=self.var_idenfi,font=("times new roman",18), bg="lightyellow")
        txt_identifiant.place(x=120,y=550, width=240)
        
        
        
        
        
        
        
        #####################################Frame2
        
        #Variable
        self.var_mois= StringVar()
        self.var_modepaie = StringVar()
        self.var_nbrHeure = StringVar()
        self.var_tarif= StringVar()
        self.var_domne = StringVar()
        self.var_anne = StringVar()
        self.var_salairenet = StringVar()
        
        Frame2 = Frame (self.root6, bd=2, relief=RIDGE)
        Frame2.place(x=900, y=120, width=760, height=475)
        
        title3 = Label(Frame2,text="Total des machine", bd=20, relief=RAISED, font=("Algerian",30),bg="lightgray", fg="black")
        title3.pack(side=TOP, fill=X)
        
        lbl_mois = Label(Frame2, text="Mois", font=("times new roman", 18)).place(x=10,y=150)
        
        
        lbl_anne = Label(Frame2, text="Année", font=("times new roman", 18)).place(x=400,y=150)
        lbl_domaine = Label(Frame2, text="Domaine", font=("times new roman", 18)).place(x=10,y=200)
        
        
        txt_mois= Entry(Frame2,textvariable=self.var_mois,font=("times new roman",18), bg="lightyellow")
        txt_mois.place(x=180,y=150, width=160)
        
        
        
        txt_anne= Entry(Frame2,textvariable=self.var_anne,font=("times new roman",18), bg="lightyellow")
        txt_anne.place(x=510,y=150, width=160)
        
        txt_domaine = Entry(Frame2,textvariable=self.var_domne,font=("times new roman",18), bg="lightyellow")
        txt_domaine.place(x=180,y=200, width=160)
        
        
        
        self.btn_calcul = Button(Frame2, text="Calculer",command=self.calcule, font=('times new roman',18, "bold"), bg='orange')
        self.btn_calcul.place(x=100,y=350,width=170)
        
        self.btn_sauvegarde = Button(Frame2, text="Sauvegarde",command=self.sauvegarde, font=('times new roman',18, "bold"), bg='green')
        self.btn_sauvegarde.place(x=300,y=350,width=170)
        
        self.btn_rreini = Button(Frame2, text="Reinitialiser", font=('times new roman',18, "bold"), bg='gray')
        self.btn_rreini.place(x=500,y=350,width=170)
        
        self.btn_modifier = Button(Frame2, text="Modifier", font=('times new roman',18, "bold"), bg='yellow')
        self.btn_modifier.place(x=200,y=420,width=180)
        
        self.btn_supprimer = Button(Frame2, text="Supprimer", font=('times new roman',18, "bold"), bg='red')
        self.btn_supprimer.place(x=400,y=420,width=180)
        
        ##########################Frame3
        
        Frame3 = Frame(self.root6, bd=2, relief=RIDGE)
        Frame3.place(x=900, y=600, width=760,height=370)
        
        ##########################Calculatrice
        cal_Frame = Frame(Frame3, bd=2, relief=RIDGE)
        cal_Frame.place(x=5, y=5, width=285, height=315)
        self.var_txt = StringVar()
        self.var_operation = ""
        
        def btn_click(nombre):
            self.var_operation = self.var_operation+str(nombre)
            self.var_txt.set(self.var_operation)
            
        def resultat():
            result = str(eval(self.var_operation))
            self.var_txt.set(result)
            self.var_operation = ""
            
        def clear():
            self.var_txt.set("")
            self.var_operation = ""
        
        txt_resultat = Entry(cal_Frame,textvariable=self.var_txt, state="readonly", font=("times new roman", 20, "bold"),justify=RIGHT).place(x=0, y=0, relwidth=1, height=50)
        
        btn_7 = Button(cal_Frame, text="7",command=lambda:btn_click(7), font=("times new roman", 18, "bold")).place(x=0, y=50, height=50, width=60)
        btn_8 = Button(cal_Frame, text="8",command=lambda:btn_click(8), font=("times new roman", 18, "bold")).place(x=71, y=50, height=50, width=60)
        btn_9 = Button(cal_Frame, text="9",command=lambda:btn_click(9), font=("times new roman", 18, "bold")).place(x=142, y=50, height=50, width=60)
        btn_dev = Button(cal_Frame, text="/",command=lambda:btn_click('/'), font=("times new roman", 18, "bold")).place(x=213, y=50, height=50, width=60)
        
        btn_4 = Button(cal_Frame, text="4",command=lambda:btn_click(4), font=("times new roman", 18, "bold")).place(x=0, y=120, height=50, width=60)
        btn_5 = Button(cal_Frame, text="5",command=lambda:btn_click(5), font=("times new roman", 18, "bold")).place(x=71, y=120, height=50, width=60)
        btn_6 = Button(cal_Frame, text="6",command=lambda:btn_click(6), font=("times new roman", 18, "bold")).place(x=142, y=120, height=50, width=60)
        btn_mul = Button(cal_Frame, text="*",command=lambda:btn_click('*'), font=("times new roman", 18, "bold")).place(x=213, y=120, height=50, width=60)
        
        btn_1 = Button(cal_Frame, text="1",command=lambda:btn_click(1), font=("times new roman", 18, "bold")).place(x=0, y=190, height=50, width=60)
        btn_2= Button(cal_Frame, text="2",command=lambda:btn_click(2), font=("times new roman", 18, "bold")).place(x=71, y=190, height=50, width=60)
        btn_3 = Button(cal_Frame, text="3",command=lambda:btn_click(3), font=("times new roman", 18, "bold")).place(x=142, y=190, height=50, width=60)
        btn_soustr = Button(cal_Frame, text="-",command=lambda:btn_click('-'), font=("times new roman", 18, "bold")).place(x=213, y=190, height=50, width=60)
        
        btn_0 = Button(cal_Frame, text="0",command=lambda:btn_click(0), font=("times new roman", 18, "bold")).place(x=0, y=260, height=50, width=60)
        btn_c = Button(cal_Frame, text="C",command=clear, font=("times new roman", 18, "bold")).place(x=71, y=260, height=50, width=60)
        btn_addition = Button(cal_Frame, text="+",command=lambda:btn_click('+'), font=("times new roman", 18, "bold")).place(x=142, y=260, height=50, width=60)
        btn_egal = Button(cal_Frame, text="=",command=resultat, font=("times new roman", 18, "bold")).place(x=213, y=260, height=50, width=60)
        
        ########################Frame Salaire
        FrameSalaire = Frame(Frame3, bd=2, relief=RIDGE)
        FrameSalaire.place(x=300, y=0, width=450, height=365)
        
        title4 = Label(FrameSalaire, text="Reçu de Salaire", bd=5, relief=RIDGE, font=("Algerian",18), bg="lightgray", fg="black")
        title4.pack(side=TOP, fill=X)
        
        FrameSalaire2 = Frame(FrameSalaire, bg="white", bd=2, relief=RIDGE)
        FrameSalaire2.place(x=0, y=55, relwidth=1, height=260)
        
        self.recu = f'''\t\tUhtman DevSEc \n\tAdresse : Medine, jokko FC, Mbour
        -----------------------------------------------
        Numero de table de la machine \t\t: ***
        Nom complet     \t\t: ***
        Marque \t\t: ***
        Année de livraison \t\t: ***
        Générer le \t\t: JJ/MM/AAAA
        ----------------------------------------------
        Par Mathieu
        uthman@gmail.com
        789456123
        '''
        
        scroll_y = Scrollbar(FrameSalaire2, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)
        
        self.txt_recuSalaire = Text(FrameSalaire2, font=('times new roman', 15), bg="lightyellow", yscrollcommand=scroll_y.set)
        self.txt_recuSalaire.pack(fill=BOTH, expand=1)
        
        scroll_y.config(command=self.txt_recuSalaire.yview)
        
        self.txt_recuSalaire.insert(END, self.recu)
        
        self.btn_imprime = Button(FrameSalaire, text="Imprimer",command=self.imprimer, font=('times new roman',18, "bold"), bg='cyan')
        self.btn_imprime.place(x=310,y=316,width=135)
        
        ##############Fonction
        
    def calcule(self):
            if self.var_tarif.get()=="" or self.var_mois.get()=="" or self.var_nbrHeure.get()=="" :
                messagebox.showerror("Erreur", "Remplir les champs obligatoir")
            else:
                taux_horaire = int(self.var_tarif.get())
                nombre_heur = int(self.var_nbrHeure.get())
                salaire_net = nombre_heur * taux_horaire
                self.var_salairenet.set(str(round(salaire_net,2)))
                
            #recu
            nouveau_recu = f'''\t\tUhtman DevSEc \n\tAdresse : Medine, jokko FC, Mbour
        -----------------------------------------------
        Numero de table de la machine \t\t: {self.var_codeemplo.get()}
        Nom complet \t\t: {self.var_nom.get()}
        Marque \t\t: {self.var_marque.get()}
        Année de livraison \t\t: {self.var_anne.get()}
        Générer le \t\t: {str(time.strftime("%d-%m-%y"))}
        ----------------------------------------------
        Par Mathieu
        uthman@gmail.com
        789456123
        '''
        
            self.txt_recuSalaire.delete("1.0", END)
            self.txt_recuSalaire.insert(END, nouveau_recu)
            
     
     
    def imprimer(self):
        fichier = tempfile.mktemp(".txt")
        open(fichier, "w").write(self.txt_recuSalaire.get("1.0", END))
        os.startfile(fichier, 'print')
        
        
    def sauvegarde(self):
        if self.var_codeemplo.get()=="" or self.var_salairenet.get()=="":
            messagebox.showerror("Erreur", "Remplir tous les champs obligatoires", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="C:/Users/mathieu/Desktop/projet/basedonne.db")
                cur = con.cursor()
                cur.execute("select * from employesalaire where code = ?",(self.var_codeemplo.get(),))
                row = cur.fetchone()
                
                if row!=None:
                    messagebox.showerror("Erreur", "code existe", parent=self.root)
                else:
                    cur.execute("""insert into employesalaire(code, entrepri,
                                nom,prenom,sexe,email,nationalite,daj,naissance,
                                experience,idenfi,tel,statut,adresse,mois,modepaie,
                                nobrheure,tarif,domaine,anne,recu ) 
                                values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                   (self.var_codeemplo.get(),
                    self.var_entrepri.get(),
                    self.var_nom.get(),
                    self.var_prenom.get(),
                    self.var_sexe.get(),
                    self.var_email.get(),
                    self.var_naissance.get(),
                    self.var_daj.get(),
                    self.var_experience.get(),
                    self.var_idenfi.get(),
                    self.var_tel.get(),
                    self.var_statut.get(),
                    self.var_adresse.get(),
                    self.var_mois.get(),
                    self.var_modepaie.get(),
                    self.var_nbrHeure.get(),
                    self.var_tarif.get(),
                    self.var_domne.get(),
                    self.var_anne.get(),  
                    self.var_salairenet.get(),
                    self.var_codeemplo.get()+".txt"          
                    ))
                    con.commit()
                    con.close()
                    fichier = open("C:/Users/mathieu/Desktop/projet/Recupaiement/"+str(self.var_codeemplo.get())+".txt", "w")
                    fichier.write(self.txt_recuSalaire.get("1.0", END))
                    fichier.close()
                    messagebox.showinfo("Succèss", "Vous avez enregistrer le dossier", parent=self.root)
                
            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(ex)}")   
      
    def recherche(self):
        try :
            con = sqlite3.connect(database="C:/Users/mathieu/Desktop/projet/basedonne.db")
            cur = con.cursor()
            cur.execute("select * from employesalaire where code = ?", (self.var_codeemplo.get(),))
            row = cur.fetchone()
            if row ==None:
                messagebox.showerror("Erreur", "Le code n'existe pas", parent=self.root)
            else:
                self.var_codeemplo.set(row[0])
                self.var_entrepri.set(row[1])
                self.var_nom.set(row[2])
                self.var_prenom.set(row[3])
                self.var_sexe.set(row[4])
                self.var_email.set(row[5])
                self.var_naissance.set(row[6])
                self.var_daj.set(row[7])
                self.var_experience.set(row[8])
                self.var_idenfi.set(row[9])
                self.var_tel.set(row[10])
                self.var_statut.set(row[11])
                self.var_adresse.delete("1.0", END)
                self.var_adresse.insert(END, row[12])
                self.var_mois.set(row[13])
                self.var_modepaie.set(row[14])
                self.var_nbrHeure.set(row[15])
                self.var_tarif.set(row[16])
                self.var_domne.set(row[17])
                self.var_anne.set(row[18])
                self.var_salairenet.set(row[19])
                self.var_codeemplo.set(row[20])
                
                fichier = open("C:/Users/mathieu/Desktop/projet/Recupaiement/"+str(row[21]),"r")
                self.txt_recuSalaire.delete("1.0", END)
                for i in fichier:
                    self.txt_recuSalaire.insert(END, i)
                fichier.close
                
                    
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreu de connextion : {str(ex)}")

        
        
        self.root6.mainloop()
        
        
        
    def modifier(self):
        self.root7 = Toplevel(self.root)
        self.root7.title("Modifier le plan des locaux")
        self.root7.geometry("1300x900+0+0")
        title = Label(self.root7, text="Le plan ", bd=10, relief=RAISED, font=('Algerian',18), bg='Teal', fg='black')
        title.pack(side=TOP, fill=X)
        
        
        self.root7.mainloop()  
        
    def affichage(self):
        self.root8 = Toplevel(self.root)
        self.root8.title("Modifier le plan des locaux")
        self.root8.geometry("1300x900+0+0")
        title = Label(self.root8, text="Le plan ", bd=10, relief=RAISED, font=('Algerian',18), bg='Teal', fg='black')
        title.pack(side=TOP, fill=X)
        
        
        self.root8.mainloop()
        
    
        
        
    



        


root=Tk()
obj = Gestion(root)
root.mainloop()        

