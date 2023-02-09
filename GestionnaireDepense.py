import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 


#-------------------------Noyau minimal-------------------------------------------------------------

#Fonction principale de notre projet. Elle regarde si le fichier csv existe et lance des fonctions en fonction.
def main():
    memstr = "0"
    try:
        with open('depense.csv', 'r') as file:
            print("Bonjour ! Voici vos récentes dépenses : \n")
            affichage()
            file.close()
            raj =  input("Voulez vous rajoutez une depense (o/n) : \n")
            if(((raj == 'o') or (raj == 'O') )):
                calcul()
                affichage()
                sup = input("Voulez-vous supprimer une dépense ? (o/n) \n")
                if(((sup == 'o') or (sup == 'O') )):
                    suppression()
                else:    
                    recherche()               
                exit()
            elif(((raj == 'n') or (raj == 'N'))):
                print("Vous ne voulez pas ajouter de dépenses. \n")
                sup = input("Voulez-vous supprimer une dépense ? (o/n) \n")
                if(((sup == 'o') or (sup == 'O') )):
                    suppression()
                else:    
                    recherche()               
                exit()
            else:
                print("Recommencez \n")
                main()
    except FileNotFoundError:
        create()
        addf() 
        affichage()
        recherche()
        exit()

#Fonction permettant de créé un fichier csv
def create():
    print("Bonjour, bienvenu sur ce gestionnaire de dépense : \n")
    with open('depense.csv', 'w', newline='') as csvfile:
      fieldnames = ['Date', 'Somme','Intitule','Categorie','Depense']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
    

#Fonction permettant d'ajouter la premiere dépense.
def addf():
    jour = int(input("Qu'elle est le jour de votre dépense ! \n"))
    if (jour <1) or (jour >31) :
        print("Ce n'est pas un jour valide")
        addf()
    jourc = str(jour)    
    mois = int(input("Qu'elle est le mois de votre dépense : \n"))
    if (mois <1) or (mois>12) :
        print("Ce n'est pas un mois valide")
        addf()
    moisc = str(mois)    
    annee = int(input("Qu'elle est l'année de votre dépense :\n"))
    if (annee <1940) or (annee>2022):
        print("Ce n'est pas une année valable")
        addf()
    anneec = str(annee)    
    date = jourc + "/" + moisc+ "/"+ anneec
    sum = input("Quel est la somme de votre dépense : \n")
    inti= input("Quel est l'intitulé de votre dépense : \n")
    cat= input("Quel est la catégorie associé à votre dépense : \n")  
    with open('depense.csv', 'a', newline='') as file:
        Données =(date,sum, inti,cat,sum )
        writer = csv.writer(file)
        writer.writerow(Données)


#Fonction qui ajoute les dépenses lorsqu'une dépense a été déjà enregistrer
def add(memoire):
    jour = int(input("Qu'elle est le jour de votre dépense : \n"))
    if (jour <1) or (jour >31) :
        print("Ce n'est pas un jour valide")
        add(memoire)
    jourc = str(jour)    
    mois = int(input("Qu'elle est le mois de votre dépense : \n"))
    if (mois <1) or (mois>12) :
        print("Ce n'est pas un mois valide")
        add(memoire)
    moisc = str(mois)    
    annee = int(input("Qu'elle est l'année de votre dépense :\n"))
    if (annee <1940) or (annee>2022):
        print("Ce n'est pas une année valable")
        add(memoire)
    anneec = str(annee)    
    date = jourc + "/" + moisc+ "/"+ anneec
    sum = float(input("Quel est la somme de votre dépense : \n"))
    dep = memoire + sum
    sumc = str(sum)
    depp = str(dep)
    inti= input("Quel est l'intitulé de votre dépense : \n")
    cat= input("Quel est la catégorie associé à votre dépense : \n")  
    with open('depense.csv', 'a', newline='') as file:
        Données =(date,sumc , inti,cat, depp )
        writer = csv.writer(file)
        writer.writerow(Données)
         
      
#Affiche le contenu du fichier csv.
def affichage():
    with open('depense.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
             print(row)

#Calcul de la dépense total
def calcul():
    memoire = 0
    with open("depense.csv") as infile :
        reader = csv.DictReader(infile)
        for row in reader:
            Sdepense =  (row['Somme'])
            Fdepense = float(Sdepense.strip('€'))
            memoire += Fdepense
    add(memoire)
        
         
          
  
#-------------------------------Noyau Bonus------------------------------------------------    

#Fonction de recherche d'une dépense.
def recherche():
    rech = input("Quel information cherchez-vous ? (somme/intitule/categorie/depense/rien/graphe) \n")
    if(rech.upper()=="GRAPHE"):
        graph()
    with open('depense.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if(rech.upper()=="SOMME"):
                print(row['Somme'])
            elif(rech.upper()=="INTITULE"):
                print(row['Intitule'],row['Somme'])
            elif(rech.upper()=="CATEGORIE"):
                print(row['Categorie'],row['Somme'])
            elif(rech.upper()=="DEPENSE"):
                print(row['Date'],row['Depense'])
            elif(rech.upper()=="RIEN"):
                print("Au revoir !")
                exit()
            else:
                print("Mauvaise saisie, veuillez recommencer : \n")
                recherche()
                  

#Affiche un graphe avec la date et les dépenses
def graph():
    csv = pd.read_csv("depense.csv")
    grap = input("Voulez-vous une sortie grpahique de vos dépenses dans le temps ? (o/n/exit)\n")
    if ((grap == 'o') or (grap == 'O') ):
        res = sns.lineplot(x="Date", y="Depense", data=csv)
        plt.show()
        exit()
    elif ((grap == 'n') or (grap == 'N') ):  
        grap2 = input("Voulez-vous une sortie grpahique de vos sommes dans le temps ? (o/n/exit)\n")
    else:
        exit()    
    if ((grap2 == 'o') or (grap2 == 'O') ):
        res = sns.lineplot(x="Date", y="Somme", data=csv)
        plt.show()
        exit()
    elif ((grap2 == 'n') or (grap2 == 'N')) :
        grap3 = input("Voulez-vous une sortie grpahique de vos sommes par rapport a vos catégories ? (o/n/exit)\n")
    else:
        exit()
    if ((grap3 == 'o') or (grap3 == 'O') ): 
        res = sns.relplot(x="Categorie", y="Somme", data=csv)
        plt.show()
        exit()
    elif ((grap3 == 'n') or (grap3 == 'N')) :
        grap4 = input("Voulez-vous une sortie grpahique de vos sommes par rapport a vos intitulés ? (o/n/exit)\n")
    else:
        exit()
    if ((grap4 == 'o') or (grap4 == 'O') ):
        res = sns.relplot(x="Intitule", y="Somme", data=csv)
        plt.show()
        exit()
    else:
        print("Au revoir !")
        exit()    

#Permet de supprimer une dépense en l'écrivant dans un autre fichier
def suppression():
    with open("depense.csv", 'r' ) as infile:
        sup = float(input("Quel somme voulez supprimer ? \n"))
        date = str(input("La date de votre achat (format 11/11/1111) : \n"))
        supc = str(sup)   
        datstr = str(date)    
        reader = csv.reader(infile)
        with open("depensebis.csv", 'w') as file :
            writer = csv.writer(file)
            for row in reader:
                if ( row[1] != supc  and row[0] != datstr) :
                    writer.writerow(row)
            file.close()
            revient()

#Mise a jour du csv principal apres supression avec saut de ligne entre chaque dépense.             
def revient():
    with open("depensebis.csv", 'r') as infile:
        reader = csv.reader(infile)
        with open("depense.csv", 'w') as file :
            writer = csv.writer(file)
            for row in reader:
                writer.writerow(row)
        print("La dépense a bien été supprimé. \n")        
        affichage()
        supligne()

#Enleve les saut de ligne dans le csv principale lors d'une supression d'une dépense. 
def supligne():
    df = pd.read_csv('depense.csv')
    df.dropna(axis=0, how='all',inplace=True)
    df.to_csv('depense.csv', index=False)
    recherche()

main()