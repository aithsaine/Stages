import tkinter as tk
from classes import Stage
from tkinter import messagebox
from tkinter import ttk
import re




app = tk.Tk()


app.geometry("500x500")
app.iconbitmap("stage.ico")
app.title("Gestion Des Stage")
app['bg']='#5d8a82'

app.resizable(False,False)
lb_title = tk.Label(text="Gestion De Stage",font="5",bd=10,bg='#5d8a82')
lb_title.grid(column=0,row=0,columnspan=5,rowspan=3,pady=10,padx=120)
# id :
lb_id = tk.Label(text="Id",font=10,bg='#5d8a82')
lb_id.grid(column=0,row=4,padx=10,sticky=tk.W)
enId = tk.Entry(font=15,bd=2)
enId.grid(row=4,column=1,padx=20)
#  nom stage : 
lb_name = tk.Label(text="Nom de stage",font=10,bg='#5d8a82')
lb_name.grid(column=0,row=5,padx=10,sticky=tk.W)
enname = tk.Entry(font=15,bd=2)
enname.grid(row=5,column=1)
#  duree : 
lb_Duration = tk.Label(text="Duree",font=10,bg='#5d8a82')
lb_Duration.grid(column=0,row=6,padx=10,sticky=tk.W)
enDuration = tk.Entry(font=10,bd=2)
enDuration.grid(row=6,column=1)

# prix
lb_price = tk.Label(text="Prix",font=10,bg='#5d8a82')
lb_price.grid(column=0,row=7,padx=10,sticky=tk.W)
enPrice = tk.Entry(font=10,bd=2)
enPrice.grid(row=7,column=1)
# domaine
lb_Domaine = tk.Label(text="Domaine",font=10,bg='#5d8a82')
lb_Domaine.grid(column=0,row=8,padx=10,sticky=tk.W)
enDomaine = tk.Entry(font=10,bd=2)
enDomaine.grid(row=8,column=1)

# btns Function:

#    Inserer un Stage:
def Inserer():
    id = enId.get()
    nom = enname.get()
    duree = enDuration.get()
    prix = enPrice.get()
    domaine = enDomaine.get()
    if id=="" or nom =="" or duree=="" or prix == "" or domaine == "":
        messagebox.showerror("Error","entrer tout les information de stage")

    else:
        ok = True
        if not re.search(r"^[0-9]$",id) or not re.search(r"[-+]?\d*\.?\d+",prix) or not re.search(r"^[0-9]",duree):
            messagebox.showerror("Error","l'id et duree et le prix doit etre des numero")
            ok = False
        if ok:
            stg = Stage(int(id),nom,int(duree),float(prix),domaine)
            stg.insertToDb()
            messagebox.showinfo("congratulation", "data saved with success")



#Supprimer un stage
def Supprimer():
    app.destroy()
    import deletepage


btnInsert = tk.Button(text="Inserer",bg="#c1eeff",width=10,command=Inserer).grid(row=4, column=2,pady=5)
btnDelete = tk.Button(text="Supprimer",bg="#c1eeff",width=10,command=Supprimer).grid(row=5, column=2,pady=5)
btnSearsh = tk.Button(text="Chercher",bg="#c1eeff",width=10).grid(row=6, column=2,pady=5)
btnUpdate = tk.Button(text="Modifier",bg="#c1eeff",width=10).grid(row=7, column=2,pady=5)
dd = tk.Checkbutton()
table = ttk.Treeview(app,columns=(1,2,3,4,5),heigh=5,show="headings",padding=5)
table.heading(1,text="ID")
table.heading(2,text="nom")
table.heading(3,text="duration")
table.heading(4,text="prix")
table.heading(5,text="domaine")
table.column(1,width=50)
table.column(2,width=200)
table.column(3,width=60)
table.column(4,width=70)
table.column(5,width=100)
table.place(x=3,y=300)

stages = Stage.getAllStages()
liste_des_tupple_stage = []
for item in stages:
    liste_des_tupple_stage.append((item['id'],item['nom'],item['duree'],item['prix'],item['domaine']))
for item in liste_des_tupple_stage:
    table.insert("",tk.END,values=item)
app.mainloop()