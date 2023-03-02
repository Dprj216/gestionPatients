#coding:utf-8
import tkinter
from sqlite3 import IntegrityError, OperationalError
#from tkinter import*
from tkinter import ttk, END, TclError
from tkinter import messagebox
import sqlite3


#fonction observateur
def observateur(*args):
    if sexes.get():
        var_sexePatient.set("Masculin")
    else:
        var_sexePatient.set("Féminin")

#fonction ajouter



def ajouterPatient():
    #récupération des données du formulaire

    matricule = saisi_matriculePatient.get()
    nom = saisi_nomPatient.get()
    prenom = saisi_prenomPatient.get()
    age = saisi_agePatient.get()
    sexe = saisi_sexePatient.get()
    adresse = saisi_adressePatient.get()
    telephone = saisi_phonePatient.get()
    allergie = saisi_allergiePatient.get()

    #connexion à la base de données
    con = sqlite3.connect('gestionPatient.db')
    curseur = con.cursor()
    try:
        curseur.execute('INSERT INTO patient VALUES (?,?,?,?,?,?,?,?)', (matricule, nom, prenom, age, sexe, adresse, telephone, allergie))
        con.commit()
        con.close()
        messagebox.showinfo("Enregistrement", "Patient ajouté avec succès....")
        var_matriculePatient.set("")
        var_nomPatient.set("")
        var_prenomPatient.set("")
        var_agePatient.set("")
        var_sexePatient.set("")
        var_adrressePatient.set("")
        var_phonePatient.set("")
        var_allergiePatient.set("")

        # afficher ajout
        con = sqlite3.connect("gestionPatient.db")
        curseur = con.cursor()
        select = curseur.execute("select * from patient order by matricule desc")
        select = list(select)
        tableau.insert('', END, values=select[0])
        con.close()

    except (IntegrityError or OperationalError or IndexError):

        messagebox.showerror("Erreur", "Erreur de syntaxe, ou l'un des champs est vide")
        messagebox.showinfo("Info", "Veuillez remplire correctement les champs s'il vous plaît")
        var_matriculePatient.set("")
        var_nomPatient.set("")
        var_prenomPatient.set("")
        var_agePatient.set("")
        var_sexePatient.set("")
        var_adrressePatient.set("")
        var_phonePatient.set("")
        var_allergiePatient.set("")



#bouton quitter
def quitter():
    if messagebox.askyesno("Quitter", "Voullez-vous quitter l' application ?"):
        form1.quit()

"""
#fonction modifier
def modifier():
    matricule = saisi_matriculePatient.get()
    nom = saisi_nomPatient.get()
    prenom = saisi_prenomPatient.get()
    age = saisi_agePatient.get()
    sexe = saisi_sexePatient.get()
    adresse = saisi_adressePatient.get()
    telephone =saisi_phonePatient.get()
    allergie = saisi_allergiePatient.get()

    # connexion à la base de données
    con = sqlite3.connect('gestionPatient.db')
    curseur = con.cursor()
    curseur.execute("update patient set nom=?, prenom=?, age=?, sexe=?, adresse=?, telephone=?, allergie=? where matricule=?", (nom, prenom, age, sexe, adresse, telephone, allergie, matricule))
    con.commit()
    con.close()
    messagebox.showinfo("Modification", "Patient modifié avec succès....")

    #afficher modification
    con = sqlite3.connect("gestionPatient.db")
    curseur = con.cursor()
    select = curseur.execute("select * from patient order by matricule desc")
    select = list(select)
    tableau.insert('', END, values=select[0])
    con.close()
"""
#fonction supprimer
def supprimer():
    selectionner = tableau.item(tableau.selection())['values'][0]
    con = sqlite3.connect("gestionPatient.db")
    curseur = con.cursor()
    delete = curseur.execute("delete from patient where matricule = {}".format(selectionner))
    con.commit()
    tableau.delete(tableau.selection())

form1 = tkinter.Tk()
form1.title("Gestion des patients")
form1.minsize(1365, 800)




#titre
titre = tkinter.Label(form1, relief="ridge", text="GESTIONS DES PATIENTS", bg="darkblue", fg="white", bd=20, font=("Arial", 30))
titre.place(x=0, y=0, width=1370)


#les champs

#matricule du patient
matriculePatient = tkinter.Label(form1, text="Matricule Patient", font=("Arial", 16), bg="black", fg="white")
matriculePatient.place(x=10, y=150, width=200)

var_matriculePatient = tkinter.IntVar()
var_matriculePatient.set("")
saisi_matriculePatient = tkinter.Entry(form1, textvariable=var_matriculePatient)
saisi_matriculePatient.place(x=250, y=150, height=30, width=200)

#nom du patient
nomPatient = tkinter.Label(form1, text="Nom Patient", font=("Arial", 16), bg="black", fg="white")
nomPatient.place(x=10, y=200, width=200)

var_nomPatient =tkinter.StringVar()
saisi_nomPatient = tkinter.Entry(form1, textvariable=var_nomPatient)
saisi_nomPatient.place(x=250, y=200, height=30, width=200)

#prenom du patient
prenomPatient = tkinter.Label(form1, text="Prenom Patient", font=("Arial", 16), bg="black", fg="white")
prenomPatient.place(x=10, y=250, width=200)

var_prenomPatient = tkinter.StringVar()
saisi_prenomPatient = tkinter.Entry(form1, textvariable=var_prenomPatient)
saisi_prenomPatient.place(x=250, y=250, height=30, width=200)

#age du patient
agePatient = tkinter.Label(form1, text="Age Patient", font=("Arial", 16), bg="black", fg="white")
agePatient.place(x=10, y=300, width=200)

var_agePatient = tkinter.IntVar()
saisi_agePatient = tkinter.Spinbox(form1, from_=1, to=100, textvariable=var_agePatient)
saisi_agePatient.place(x=250, y=300, height=30, width=200)

#sexe du patient
sexePatient = tkinter.Label(form1, text="Sexe Patient", font=("Arial", 16), bg="black", fg="white")
sexePatient.place(x=10, y=350, width=200)

sexes = tkinter.IntVar()
sexes.trace("w", observateur)
masculinPatient = tkinter.Radiobutton(form1, text="Masculin", value=1, variable=sexes, font=("Arial", 10))
masculinPatient.place(x=245, y=340)
femininPatient = tkinter.Radiobutton(form1, text="Féminin", value=0, variable=sexes, font=("Arial", 10))
femininPatient.place(x=380, y=340)

var_sexePatient = tkinter.StringVar()
saisi_sexePatient = tkinter.Entry(form1, textvariable=var_sexePatient)
saisi_sexePatient.place(x=250, y=360, width=200)

#adresse du patient
adressePatient = tkinter.Label(form1, text="Adresse Patient", font=("Arial", 16), bg="black", fg="white")
adressePatient.place(x=10, y=405, width=200)

var_adrressePatient = tkinter.StringVar()
saisi_adressePatient = tkinter.Entry(form1, textvariable=var_adrressePatient)
saisi_adressePatient.place(x=250, y=405, height=30, width=200)

#telephone du patient
phonePatient = tkinter.Label(form1, text="Téléphone Patient", font=("Arial", 16), bg="black", fg="white")
phonePatient.place(x=10, y=455, width=200)

var_phonePatient = tkinter.StringVar()
saisi_phonePatient = tkinter.Entry(form1, textvariable=var_phonePatient)
saisi_phonePatient.place(x=250, y=455, height=30, width=200)

#remarque du patient
allergiePatient = tkinter.Label(form1, text="Allergie Patient", font=("Arial", 16), bg="black", fg="white")
allergiePatient.place(x=10, y=505, width=200)

var_allergiePatient = tkinter.StringVar()
saisi_allergiePatient = tkinter.Entry(form1, textvariable=var_allergiePatient)
saisi_allergiePatient.place(x=250, y=505, height=30, width=200)

#bouton enregistrer
btnEnregistrer = tkinter.Button(form1, text="Enregistrer", font=("Arial", 16), bg="green", fg="white", command=ajouterPatient)
btnEnregistrer.place(x=10, y=600, width=200)

#bouton modifier
btnquitter = tkinter.Button(form1, text="Quitter", font=("Arial", 16), bg="blue", fg="white", command=quitter)
btnquitter.place(x=250, y=600, width=200)

#bouton supprimer
btnSupprimer = tkinter.Button(form1, text="Supprimer", font=("Arial", 16), bg="red", fg="white", command=supprimer)
btnSupprimer.place(x=130, y=650, width=200)


#titre tableau
listePatient = tkinter.Label(form1, text="LISTE DES PATIENTS", font=("Arial", 16), bg="darkblue", fg="white")
listePatient.place(x=600, y=100, width=750)

#tableau pour la liste des patients
tableau = ttk.Treeview(form1, columns=(1, 2, 3, 4, 5, 6, 7, 8), height=5, show="headings")
tableau.place(x=600, y=150, height=450, width=750)

#entête du tableau
tableau.heading(1, text="MATRICULE")
tableau.heading(2, text="NOM")
tableau.heading(3, text="PRENOM")
tableau.heading(4, text="AGE")
tableau.heading(5, text="SEXE")
tableau.heading(6, text="ADRESSE")
tableau.heading(7, text="TELEPHONE")
tableau.heading(8, text="ALLERGIE")

#dimenssions
tableau.column(1, width=80)
tableau.column(2, width=100)
tableau.column(3, width=100)
tableau.column(4, width=50)
tableau.column(5, width=100)
tableau.column(6, width=100)
tableau.column(7, width=100)
tableau.column(8, width=100)

#afficher  les infos la liste
con = sqlite3.connect("gestionPatient.db")
curseur = con.cursor()
select = curseur.execute("select * from patient")
select = list(select)
for row in select:
    tableau.insert('', "end", values=row)
con.close()


form1.mainloop()