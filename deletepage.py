from tkinter import *
from tkinter import messagebox
import re
from classes import Stage

deletepage = Tk()
deletepage.geometry("500x500")
deletepage.iconbitmap("stage.ico")
deletepage.resizable(False,False)
deletepage.title("Supprimer un stage")
deletepage['bg']='#5d8a82'

# function valider la supprission

def valider_supprission():
    ids = list(map(lambda item : item["id"],Stage.getAllStages()))
    id = en_id.get()
    clean = True
    if not re.search(r"\d+",id):
        messagebox.showerror("erreur","l'id doit etre un nombre")
        clean = True
    else:
        if int(id) not in ids:
            messagebox.showerror("erreur","Aucun Stage a cet id")
        else:
            ok = messagebox.askokcancel("est que vous ette sure de supprimer cet stage")
            if ok:
                Stage.DeleteFromDb(int(id))
                messagebox.showinfo("Congratulation","le stage ete supprimer avec success")
                deletepage.destroy()
                import main

Label(text="Supprimer un Stage ",bg='#5d8a82',font=15).grid(row=0,column=0,pady=20,padx=10)
Label(text="Id",bg='#5d8a82',font=15).grid(row=2,column=0,pady=20,padx=10)
en_id = Entry(font=20)
en_id.grid(row=2,column=1)
en_id.focus()
btn_valide = Button(text="valider la supprission",command=valider_supprission)
btn_valide.grid(row=3,column=0,padx=30,pady=30)
btn_annuler = Button(text="annuler la supprission")
btn_annuler.grid(row=3,column=1)


deletepage.mainloop()
