from tkinter import *
import BDD
root = Tk()
root.title('OUIFIND')


train_number = StringVar()
train_number.set("")
object_description = StringVar()
object_description.set("")
day = StringVar()
day.set("")
month = StringVar()
month.set("")
year = StringVar()
year.set("")

# frame_train = Frame(root, padx=10, pady=10)
# frame_train.grid(row=0, column=0)
# label_train = Label(frame_train, text="Numéro du train :")
# label_train.grid(row=0, column=0)
# entree_train = Entry(frame_train, textvariable=train_number, width=20)
# entree_train.grid(row=0, column=1)

frame_date = Frame(root, padx=10, pady=10)
frame_date.grid(row=1, column=0)
label_jour = Label(frame_date, text="Jour : ")
label_jour.grid(row=0, column=0)
entree_jour = Entry(frame_date, textvariable=day, width=3)
entree_jour.grid(row=0, column=1)
label_mois = Label(frame_date, text="Mois : ")
label_mois.grid(row=0, column=2)
entree_mois = Entry(frame_date, textvariable=month, width=3)
entree_mois.grid(row=0, column=3)
label_year = Label(frame_date, text="Année : ")
label_year.grid(row=0, column=4)
entree_year = Entry(frame_date, textvariable=year, width=5)
entree_year.grid(row=0, column=5)

frame_type = Frame(root, padx=10, pady=10)
frame_type.grid(row=2, column=0)
label_type = Label(frame_type, text="Type de l'objet :     ")
label_type.grid(row=0, column=0)
choix_type = Variable(frame_type, ('Vêtements', 'Bagage', 'Portefeuille', 'Livre', 'Electronique', 'Divers'))
choix_types = Listbox(frame_type, listvariable=choix_type, width=20, relief='groove', height=6, selectborderwidth=3)
choix_types.grid(row=0, column=1)

# frame_description = Frame(root, padx=10, pady=10)
# frame_description.grid(row=3, column=0)
# label_description = Label(frame_description, text="Rapide description de l'objet :")
# label_description.grid(row=8, column=0)
# entree_description = Entry(frame_description, textvariable=object_description, width=40)
# entree_description.grid(row=8, column=1)


def object_search():
    annee = entree_year.get()
    mois = entree_mois.get()
    jour = entree_jour.get()
    date = annee+'-'+mois+'-'+jour
    types = {0:'VÃªtements, chaussures', 1:'Bagagerie: sacs, valises, cartables', 2:'Porte-monnaie / portefeuille, argent, titres', 3:'Livres, articles de papÃ©terie', 4:'Appareils Ã©lectroniques, informatiques, appareils photo', 5:'Divers'}
    type = types[choix_types.curselection()[0]]

    global tableau1
    tableau = BDD.retrouve(type, date)

    root2 = Tk()
    root2.title('Objets trouvés')

    def sort_objects(indice):
        for j in range(1, len(tableau)):
            temp = tableau[j]
            i = j
            while i > 0 and tableau[i-1][indice] > temp[indice]:
                tableau[i] = tableau[i-1]
                i = i - 1
            tableau[i] = temp

    def sort():
        consigne_int = choice_sortbox.curselection()[0]
        consigne = {0: "Code UIC", 1: 'Gare', 2: "Date"}[consigne_int]
        if consigne == 'Code UIC':
            sort_objects(1)
        if consigne == 'Gare':
            sort_objects(2)
        if consigne == 'Date':
            sort_objects(3)
        list_of_objects = []
        for x in tableau:
            list_of_objects.append("UIC : "+str(x[1])+', '+str(x[2])+', '+str(x[3])+', '+str(x[4]))
        frame_list = Frame(root2, padx=10, pady=10)
        frame_list.grid(row=1, column=0)
        object_list = Variable(frame_list, tuple(list_of_objects))
        object_listbox = Listbox(frame_list, listvariable=object_list, width=120, relief='groove', height=25)
        object_listbox.grid(row=0, column=1)



    frame_sort = Frame(root2, padx=10, pady=10)
    label_sort = Label(frame_sort, text="Trier par : ")
    label_sort.grid(row=0, column=0)
    choice_sort = Variable(frame_sort, ('Code UIC', 'Gare', 'Date'))
    choice_sortbox = Listbox(frame_sort, listvariable=choice_sort, width=10, relief='groove', height=3)
    choice_sortbox.grid(row=0, column=1)
    button_sort = Button(frame_sort, text="Envoyer", command=sort)
    button_sort.grid(row=0, column=2)
    frame_sort.grid(row=0)






    root2.mainloop()



frame_buttons = Frame(root, padx=10, pady=10)
frame_buttons.grid(row=4, column=0)
submit = Button(frame_buttons, text="Envoyer", padx=10, pady=5, bd=2, command=object_search)
submit.grid(row=0, column=1)

root.mainloop()



