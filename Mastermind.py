#########################################
# groupe MI 1
# Pierre RATCLIFFE
# Yassine BAGHDAD-BEY
# Sephora TAHA
# Nique PRYSCIA
# https://github.com/uvsq22008849/projet_tas_de_sable.git
#########################################


##################### Import des modules ##########################

import tkinter as tk
import random

##################### variables globales ##########################

racine = tk.Tk()

HEIGHT = 540
WIDTH = 490

rows, cols = (10, 4)

liste_cellule = [[0 for i in range(cols)] for j in range(rows)]
liste_cercle = [[0 for i in range(cols)] for j in range(rows)]
liste_cellule_code_secret = [0 for i in range(cols)]
liste_cercle_code_secret = [0 for i in range(cols)]
#print(liste_cercle_code_secret)
#print(liste_cellule)

######################### Fonctions ###############################
def couleur_cellule():
    for i in range(cols):
        if liste_cellule_code_secret[i] == 1:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "blue")
        if liste_cellule_code_secret[i] == 2:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "red")
        if liste_cellule_code_secret[i] == 3:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "green")
        if liste_cellule_code_secret[i] == 4:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "yellow")
        if liste_cellule_code_secret[i] == 5:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "pink")
        if liste_cellule_code_secret[i] == 6:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "black")
        if liste_cellule_code_secret[i] == 7:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "grey")
        if liste_cellule_code_secret[i] == 8:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "orange")

    
def cliqueG_code_secret(event):
    global x0, y0, x1, y1
    x = event.x
    y = event.y
    for i in range(4):
        x0, y0, x1, y1 = canvas.coords(liste_cercle_code_secret[i])
        if x > x0 and x < x1 and y > y0 and y < y1:
            liste_cellule_code_secret[i] += 1
            if liste_cellule_code_secret[i] > 8:
                liste_cellule_code_secret[i] = 1
    couleur_cellule()

def cliqueD_code_secret(event):
    global x0, y0, x1, y1
    x = event.x
    y = event.y
    for i in range(4):
        x0, y0, x1, y1 = canvas.coords(liste_cercle_code_secret[i])
        if x > x0 and x < x1 and y > y0 and y < y1:
            liste_cellule_code_secret[i] -= 1
            if liste_cellule_code_secret[i] == 0:
                liste_cellule_code_secret[i] = 8
    couleur_cellule()
            #if x > j * 100 and x < j * 100 + 100 and y > i * 100 and y < i * 100 + 100:
            #    liste_cellule[i][j] += 1

        

#def code_secret():


######################### Pogramme ################################

scroll_y = tk.Scrollbar(racine, orient = 'vertical')
scroll_y.grid(row = 0, column = 1, sticky = 'ns')

canvas = tk.Canvas(racine, bg = "white", height=HEIGHT, width=WIDTH, scrollregion = (0, 0, 490, 1140), yscrollcommand = scroll_y.set)
canvas.grid(row = 0, column = 0)

for y in range(10):
    for i in range(4):
        canvas.create_oval((60 + (i * 100), 150 + (y * 100)), (((i + 1) * 100) + 30, ((y + 1) * 100) + 120), outline = "black", width = 5)
        #canvas.create_oval((0, i *  100), (500, i * 100), outline = "blue", width = 5)
"""cercle des diametre 70, commence à 60 de la gauche et finit à 60 de la droite. Les 10 finissent à 1120"""

#60 150 130 220
#160 250 230 320
#90 à 150 donc ligne à y = 120
for z in range(4):
    cercle = canvas.create_oval((60 + (z * 100), 20, (((z + 1) * 100) + 30, 90)), outline = "black", width = 5)
    liste_cercle_code_secret[z] = cercle
#print(liste_cercle_code_secret)

canvas.create_line((60, 120), (430, 120), fill="black", width=2)

bouton_iteration = tk.Button(racine, text = "Prochaine étape", padx = 20, pady = 20, font =("Helvetica", "20"))
bouton_iteration.grid(row = 1, column = 0)

scroll_y.config(command = canvas.yview)
canvas.bind("<Button-1>", cliqueG_code_secret)
canvas.bind("<Button-2>", cliqueD_code_secret)


racine.mainloop()