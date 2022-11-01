from pymongo import MongoClient

class Stage:
    cnx = MongoClient("localhost",27017)
    db = cnx["db_stages"]
    stages_collection = db["stage"]


    def __init__(self,id:int, nom:str, duree:int,prix:float,domaine:str) -> None:
        self.__id = id
        self.__nom = nom
        self.__duree = duree
        self.__prix = prix
        self.__domaine = domaine

    def getId(self):
        return self.__id
    property(getId)

    def getNom(self):
        return self.__nom

    def setNom (self,new_name):
        self.__nom = new_name

    property(getNom,setNom)

    def getDuree(self):
        return self.__duree
    def setDuree (self,new_duree):
        self.__duree=new_duree    
    property(getDuree, setDuree)    


    def getPrix(self):
        return self.__prix
    def setPrix (self,new_prix):
        self.__prix=new_prix    
    property(getPrix, setPrix)    

    def getDomaine(self):
        return self.__domaine
    def setDomaine (self,new_d__domaine):
        self.__domaine=new_d__domaine    
    property(getDomaine, setDomaine)

# 
    def insertToDb(self):
        Stage.stages_collection.insert_one({"id":self.__id,"nom":self.__nom,"duree":self.__duree,"prix":self.__prix,"domaine":self.__domaine})

    @staticmethod
    def getAllStages()->list:
        res = list(Stage.stages_collection.find({}))
        return res
    
    @staticmethod
    def UpdateFromDb(id:int,new_data:dict=None):
        Stage.stages_collection.update_one({"id":id},{"$set":new_data})

    @staticmethod
    def DeleteFromDb(id:int)->bool:
        ids = list(map(lambda item : item["id"],Stage.getAllStages()))
        if id in ids:
            Stage.stages_collection.delete_one({"id":id})
            return True
        else:
            return False



""" stages = Stage.getAllStages()
for item in stages:
    for key,value in dict(item).items():
        print(key,value,sep="  :  ")
    print() """

""" res = Stage.UpdateFromDb(2,{"nom":"Generate DataBases SQL"}) """

