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
import tkinter.font as tkFont
#from tkinter import ttk

##################### variables globales ##########################

racine = tk.Tk()

HEIGHT = 540
WIDTH = 490

rows, cols = (10, 4)

liste_cellule = [[0 for i in range(cols)] for j in range(rows)]
liste_cercle = [[0 for i in range(cols)] for j in range(rows)]

liste_cellule_code_secret = [0 for i in range(cols)]
liste_cercle_code_secret = [0 for i in range(cols)]
liste_DEFINITF_cellule_code_secret = [0 for i in range(cols)]
#print(liste_cercle_code_secret)
#print(liste_cellule)

liste_indicateurs_G_haut = [[0 for i in range(2)] for j in range(rows)]
liste_cercle_indicateurs_G_haut = [[0 for i in range(2)] for j in range(rows)]
liste_indicateurs_G_bas = [[0 for i in range(2)] for j in range(rows)]
liste_cercle_indicateurs_G_bas = [[0 for i in range(2)] for j in range(rows)]
liste_indicateurs_D_haut = [[0 for i in range(2)] for j in range(rows)]
liste_cercle_indicateurs_D_haut = [[0 for i in range(2)] for j in range(rows)]
liste_indicateurs_D_bas = [[0 for i in range(2)] for j in range(rows)]
liste_cercle_indicateurs_D_bas = [[0 for i in range(2)] for j in range(rows)]

stop = 0
cpt = 0
pivot = 0
tvar = tk.StringVar()
tvar.set("Cache moi ce code ;)")

######################### Fonctions ###############################
def couleur_cellule():
    for i in range(cols):
        if liste_cellule_code_secret[i] == 0:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "white")
        elif liste_cellule_code_secret[i] == 1:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "blue")
        elif liste_cellule_code_secret[i] == 2:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "red")
        elif liste_cellule_code_secret[i] == 3:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "green")
        elif liste_cellule_code_secret[i] == 4:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "yellow")
        elif liste_cellule_code_secret[i] == 5:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "pink")
        elif liste_cellule_code_secret[i] == 6:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "black")
        elif liste_cellule_code_secret[i] == 7:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "grey")
        elif liste_cellule_code_secret[i] == 8:
            canvas.itemconfigure(liste_cercle_code_secret[i], fill = "orange")

    for y in range(rows):
        for i in range(cols):
            if liste_cellule[y][i] == 0:
                canvas.itemconfigure(liste_cercle[y][i], fill = "white")
            elif liste_cellule[y][i] == 1:
                canvas.itemconfigure(liste_cercle[y][i], fill = "blue")
            elif liste_cellule[y][i] == 2:
                canvas.itemconfigure(liste_cercle[y][i], fill = "red")
            elif liste_cellule[y][i] == 3:
                canvas.itemconfigure(liste_cercle[y][i], fill = "green")
            elif liste_cellule[y][i] == 4:
                canvas.itemconfigure(liste_cercle[y][i], fill = "yellow")
            elif liste_cellule[y][i] == 5:
                canvas.itemconfigure(liste_cercle[y][i], fill = "pink")
            elif liste_cellule[y][i] == 6:
                canvas.itemconfigure(liste_cercle[y][i], fill = "black")
            elif liste_cellule[y][i] == 7:
                canvas.itemconfigure(liste_cercle[y][i], fill = "grey")
            elif liste_cellule[y][i] == 8:
                canvas.itemconfigure(liste_cercle[y][i], fill = "orange")

    
def cliqueG_code_secret(event):
    #global x0, y0, x1, y1
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    for i in range(cols):
        x0, y0, x1, y1 = canvas.coords(liste_cercle_code_secret[i])
        if x > x0 and x < x1 and y > y0 and y < y1 and stop == 0:
            liste_cellule_code_secret[i] += 1
            if liste_cellule_code_secret[i] > 8:
                liste_cellule_code_secret[i] = 1
    couleur_cellule()

def cliqueD_code_secret(event):
    #global x0, y0, x1, y1
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    for i in range(cols):
        x0, y0, x1, y1 = canvas.coords(liste_cercle_code_secret[i])
        if x > x0 and x < x1 and y > y0 and y < y1 and stop == 0:
            liste_cellule_code_secret[i] -= 1
            if liste_cellule_code_secret[i] < 1:
                liste_cellule_code_secret[i] = 8
    couleur_cellule()
            #if x > j * 100 and x < j * 100 + 100 and y > i * 100 and y < i * 100 + 100:
            #    liste_cellule[i][j] += 1


def cacher_code_secret():
    global liste_DEFINITF_cellule_code_secret, stop, cpt
    if stop < 1:
        liste_DEFINITF_cellule_code_secret = list(liste_cellule_code_secret)
    #print(liste_DEFINITF_cellule_code_secret)
    for i in range(cols):
        liste_cellule_code_secret[i] = 0
    stop = 1
    couleur_cellule()
    cpt += 1
    if cpt <= 1:
        var = 'Effectuer le ' + str(cpt) + 'er essai'
    elif cpt == 9:
        var = 'Attention dernier essai !'
    elif cpt > 9:
        var = 'Encore une partie ? :)'
    else:
        var = 'Effectuer le ' + str(cpt) + 'ème essai'
    tvar.set(var)
    #print(liste_cellule)
    indicateurs()

def cliqueG_iteration(event):
    x = canvas.canvasx(event.x)
    ya = canvas.canvasy(event.y)
    #print(x)
    for y in range(rows):
        for i in range(cols):
            x0, y0, x1, y1 = canvas.coords(liste_cercle[y][i])
            #print(x0, y0, x1, y1)
            if x > x0 and x < x1 and ya > y0 and ya < y1 and y == (cpt - 1):
                liste_cellule[y][i] += 1
                #print(liste_cellule[y][i])
                if liste_cellule[y][i] > 8:
                    liste_cellule[y][i] = 1
    couleur_cellule()

def cliqueD_iteration(event):
    x = canvas.canvasx(event.x)
    ya = canvas.canvasy(event.y)
    #print(x)
    for y in range(rows):
        for i in range(cols):
            x0, y0, x1, y1 = canvas.coords(liste_cercle[y][i])
            #print(x0, y0, x1, y1)
            if x > x0 and x < x1 and ya > y0 and ya < y1 and y == (cpt - 1):
                liste_cellule[y][i] -= 1
                #print(liste_cellule[y][i])
                if liste_cellule[y][i] < 1:
                    liste_cellule[y][i] = 8
    couleur_cellule()

def indicateurs():
    for y in range(rows):
        for i in range(cols):
            #print(liste_cellule[y][i])
            #print(liste_DEFINITF_cellule_code_secret[i])
            if y == (cpt - 2) and liste_cellule[y][i] == liste_DEFINITF_cellule_code_secret[i]:
                #print(liste_cellule[y][i])
                #print(liste_DEFINITF_cellule_code_secret[i])
                #print(liste_cellule[y][i])
                if i < 2:
                    canvas.itemconfigure(liste_cercle_indicateurs_D_haut[y][i], fill = "red", outline = "red")
                else:
                    canvas.itemconfigure(liste_cercle_indicateurs_D_bas[y][i - 2], fill = "red", outline = "red")



######################### Pogramme ################################

scroll_y = tk.Scrollbar(racine, orient = 'vertical')
scroll_y.grid(row = 0, column = 1, sticky = 'ns')

canvas = tk.Canvas(racine, bg = "white", height=HEIGHT, width=WIDTH, scrollregion = (0, 0, 490, 1140), yscrollcommand = scroll_y.set)
canvas.grid(row = 0, column = 0)

#print(tkFont.families())

for y in range(10):
    for i in range(4):
        cercle = canvas.create_oval((60 + (i * 100), 150 + (y * 100)), (((i + 1) * 100) + 30, ((y + 1) * 100) + 120), outline = "black", width = 5)
        liste_cercle[y][i] = cercle
#print(liste_cercle)
"""cercle des diametre 70, commence à 60 de la gauche et finit à 60 de la droite. Les 10 finissent à 1120"""

#60 150 130 220
#160 250 230 320
#90 à 150 donc ligne à y = 120
#1er cerlce commence à y = 150 et finit à y = 220
#Milieu 1er cercle à y = 185
#Dernier cercle se finit à x = 430
for z in range(4):
    cercle_code = canvas.create_oval((60 + (z * 100), 20, (((z + 1) * 100) + 30, 90)), outline = "black", width = 5)
    liste_cercle_code_secret[z] = cercle_code
#print(liste_cercle_code_secret)

#Commencer à x=17 du bord avec des cercle de d=10 et x=6 d'ecart entre eux
#Commencer à y=172 avec meme d et meme écart
'''for y in range(10):
    for t in range(2):
        for i in range(2):
            cercle_indicateurs_G = canvas.create_oval((17 + (i * 16), 172 + (t * 16) + (y * 100)), (27 + (i * 16), 182 + (t * 16) + (y * 100)), outline = "white", width = 5, fill = 'white')
            liste_cercle_indicateurs_G[y][i] = cercle_indicateurs_G
"""Indicateurs gauche, cercles de diamètre 10 séparés de x et y = 6 pxl"""
#print(canvas.coords(liste_cercle_indicateurs[0][0]))
#print(canvas.coords(liste_cercle[0][0]))

for y in range(10):
    for t in range(2):
        for i in range(2):
            cercle_indicateurs_D = canvas.create_oval((447 + (i * 16), 172 + (t * 16) + (y * 100)), (457 + (i * 16), 182 + (t * 16) + (y * 100)), outline = "red", width = 5, fill = 'white')
            liste_cercle_indicateurs_D[y][i] = cercle_indicateurs_D'''

#print(cercle_indicateurs_D)

for y in range(10):
    for i in range(2):
        cercle_indicateurs_G_haut = canvas.create_oval((17 + (i * 16), 172 + (y * 100)), (27 + (i * 16), 182 + (y * 100)), outline = "white", width = 5, fill = 'white')
        liste_cercle_indicateurs_G_haut[y][i] = cercle_indicateurs_G_haut

for y in range(10):
    for i in range(2):
        cercle_indicateurs_G_bas = canvas.create_oval((17 + (i * 16), 188 + (y * 100)), (27 + (i * 16), 198 + (y * 100)), outline = "white", width = 5, fill = 'white')
        liste_cercle_indicateurs_G_bas[y][i] = cercle_indicateurs_G_bas


for y in range(10):
    for i in range(2):
        cercle_indicateurs_D_haut = canvas.create_oval((447 + (i * 16), 172 + (y * 100)), (457 + (i * 16), 182 + (y * 100)), outline = "white", width = 5, fill = 'white')
        liste_cercle_indicateurs_D_haut[y][i] = cercle_indicateurs_D_haut

for y in range(10):
    for i in range(2):
        cercle_indicateurs_D_bas = canvas.create_oval((447 + (i * 16), 188 + (y * 100)), (457 + (i * 16), 198 + (y * 100)), outline = "white", width = 5, fill = 'white')
        liste_cercle_indicateurs_D_bas[y][i] = cercle_indicateurs_D_bas


'''for y in range(20):
    for i in range(2):
        if pivot == 0 or f < r:
            cercle_indicateurs_D = canvas.create_oval((17 + (i * 16), 172 + pivot + (y * 100)), (27 + (i * 16), 182 + pivot + (y * 100)), outline = "red", width = 5, fill = 'red')
            pivot = -84 - y * 100
            r = pivot
        else:
            cercle_indicateurs_D = canvas.create_oval((17 + (i * 16), 172 + pivot + (y * 100)), (27 + (i * 16), 182 + pivot + (y * 100)), outline = "red", width = 5, fill = 'red')
            pivot = 0 - y * 100
            f = pivot
            #liste_cercle_indicateurs_D[y][i] = cercle_indicateurs_D'''

ligne_separation = canvas.create_line((60, 120), (430, 120), fill="black", width=2)


bouton_iteration = tk.Button(racine, textvariable = tvar, command = cacher_code_secret, padx =16, pady =18, bd ='5', bg ='blue', font =("Optima", "23"))
bouton_iteration.grid(row = 1, column = 0)

scroll_y.config(command = canvas.yview)
canvas.bind("<Button-1>", cliqueG_code_secret)
canvas.bind("<Button-1>", cliqueG_iteration, add='+')
canvas.bind("<Button-2>", cliqueD_code_secret)
canvas.bind("<Button-2>", cliqueD_iteration, add='+')

racine.mainloop()