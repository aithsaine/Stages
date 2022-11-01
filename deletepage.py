from tkinter import *
from tkinter import messagebox
import re
from classes import Stage
import os

deletepage = Tk()
deletepage.geometry("500x200")
deletepage.iconbitmap("stage.ico")
deletepage.resizable(False,False)
deletepage.title("Supprimer un stage")
deletepage['bg']='#c5efff'
deletepage.focus()

# function valider la supprission

def valider_supprission():
    ids = list(map(lambda item : item["id"],Stage.getAllStages()))
    id = en_id.get()
    if id =="":
        messagebox.showerror("erreur","etre l'id de stage")
    if id != "" and not re.search(r"\d+",id):
        messagebox.showerror("erreur","l'id doit etre un nombre")
    elif id != "" and re.search(r"\d+",id):
        if int(id) not in ids:
            messagebox.showerror("erreur","Aucun Stage a cet id")
        else:
            ok = messagebox.askokcancel("Verification","est que vous ette sure de supprimer cet stage")
            if ok:
                Stage.DeleteFromDb(int(id))
                messagebox.showinfo("Congratulation","le stage ete supprimer avec success")
                deletepage.destroy()
                import main

def annuler_supprission():
    deletepage.destroy()
    os.startfile("main.py")



Label(deletepage ,text="Supprimer un Stage ",bg='#c5efff',font=15).grid(row=0,column=0,columnspan=3,rowspan=3,pady=10,padx=120)
Label(deletepage ,text="Id",bg='#c5efff',font=15).grid(row=5,column=0,pady=20,padx=10)
en_id = Entry(deletepage ,font=30)
en_id.grid(row=5,column=1)
en_id.focus()
btn_valide = Button(deletepage ,text="valider",command=valider_supprission)
btn_valide.grid(row=5,column=2)
btn_annuler = Button(text="annuler",command=annuler_supprission)
btn_annuler.grid(row=5,column=3)



deletepage.mainloop()
