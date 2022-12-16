import sqlite3

def CreerbaseDonne():
    con = sqlite3.connect(database="C:/Users/mathieu/Desktop/gestion de parc informatique/basedonne.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS employesalaire(
        code INTEGER PRIMARY KEY AUTOINCREMENT, entrepri text,nom text,prenom text,sexe text,
        email text,nationalite text,daj text,naissance text,experience text,
        idenfi text, tel text, statut text,adresse text,mois text,modepaie text,
        nobrheure text, tarif text,domaine text,anne text,recu text
        )""")
    
    con.commit()
    con.close()
    
CreerbaseDonne()