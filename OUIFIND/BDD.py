# -*- coding: utf-8 -*-
"""
Base de données SQL des objets trouvés.
"""

#Importation de modules
import sqlite3
import csv


# Commande utile pour visualiser les tables disponibles dans la base de données.
def voir_table():
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    l = cur.fetchall()
    print(l)


#Dans la suite CreateTable2, AddEntry2 et open_csv_file2 sont les fonctions relatives aux objets trouvés.

# def CreateTable(name):
#     cur.execute('''DROP perdu IF EXISTS''')
#     cur.execute('''CREATE TABLE IF NOT EXISTS perdu
#     (id INTEGER PRIMARY KEY, date TEXT, type TEXT, nature TEXT, enregistrement TEXT, gare TEXT, code TEXT)''')

def CreateTable2():
    cur.execute('''DROP TABLE IF EXISTS trouve''')
    cur.execute('''CREATE TABLE IF NOT EXISTS trouve
    (id INTEGER PRIMARY KEY, date TEXT, restitution TEXT, gare TEXT, code TEXT, nature TEXT, type TEXT, enregistrement TEXT)''')

# def AddEntry(id, date, type, nature, enregistrement, gare, code):
#     cur.execute('''INSERT INTO perdu
#      (id, date, type, nature, enregistrement, gare, code)
#     VALUES (?,?,?,?,?,?,?)''',(id, date, type, nature, enregistrement, gare, code))

def AddEntry2(id, date, restitution, gare, code, nature, type, enregistrement):
    cur.execute('''INSERT INTO trouve
     (id, date, restitution, gare, code, nature, type, enregistrement)
    VALUES (?,?,?,?,?,?,?,?)''',(id, date, restitution, gare, code, nature, type, enregistrement))

# def open_csv_file ( filename):
#     with open ( filename , newline ='') as csvfile :
#         file_reader = csv.reader ( csvfile , delimiter =';',quotechar ='"')
#         i = 0
#         for row in file_reader :
#             AddEntry( i, row[0], row[1], row[2], row[3], row[4], row[5])
#             i +=1
#         connection.commit()

def open_csv_file2 ( filename):
    with open ( filename , newline ='') as csvfile :
        file_reader = csv.reader ( csvfile , delimiter =';',quotechar ='"')
        i = 0
        for row in file_reader :
            AddEntry2( i, row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            i += 1
        connection.commit()

def CreateTable3():
    cur.execute('''DROP TABLE IF EXISTS ligne''')
    cur.execute('''CREATE TABLE IF NOT EXISTS ligne
    (id INTEGER PRIMARY KEY, gare TEXT)''')

def AddEntry3(id, gare):
    cur.execute('''INSERT INTO ligne
     (id,gare)
    VALUES (?,?)''',(id, gare))

def remplir ():
    ligne = ['Lille Flandres', 'Lille Europe', 'Arras', 'Paris Gare de Lyon', 'Paris Gare du Nord', 'Lyon Part Dieu', 'Grenoble']
    for i in range(len(ligne)) :
        AddEntry3(i, ligne[i])
        i += 1
    connection.commit()

#Nous avons à présent tous les éléments pour créer la base de données à partir des fonctions précédentes.



#Initialisation de l'environnement SQL
connection = sqlite3.connect('ikos.db')
cur = connection.cursor()

CreateTable2()
open_csv_file2("objets-trouves-restitution.csv")

CreateTable3()
remplir()

def test():
    cur.execute(''' 
    SELECT type, COUNT(id) FROM trouve GROUP BY type
    ''')

    l = cur.fetchall()

    liste = []
    for elem in l:
        liste.append(elem[0])
    return liste


def essai():
    cur.execute(''' 
    SELECT MIN(date) FROM trouve
    WHERE gare IN (SELECT gare FROM ligne) 
     ''')
    l = cur.fetchall()
    for elem in l:
        print(elem)

def retrouve(type, date):
    cur.execute(''' 
    SELECT id, code, gare, date, nature FROM trouve
    WHERE type = "{}" AND date > "{}" AND gare IN (SELECT gare FROM ligne)
    LIMIT 150
     '''.format(type, date) )


    l = cur.fetchall()

    liste = []
    for elem in l:
        liste.append(elem)
    return liste



types = ['Appareils Ã©lectroniques, informatiques, appareils photo', "Articles d'enfants, de puÃ©riculture", 'Articles de sport, loisirs, camping', 'Articles mÃ©dicaux', 'Bagagerie: sacs, valises, cartables', 'Bijoux, montres', 'ClÃ©s, porte-clÃ©s, badge magnÃ©tique', 'Divers', 'Instruments de musique', 'Livres, articles de papÃ©terie', 'Optique', 'Parapluies', "PiÃ¨ces d'identitÃ©s et papiers personnels", 'Porte-monnaie / portefeuille, argent, titres', 'VÃ©los, trottinettes, accessoires 2 roues', 'VÃªtements, chaussures']



