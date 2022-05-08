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
import numpy as np
#from tkinter import ttk

##################### variables globales ##########################

racine = tk.Tk()
racine.configure(bg = '#53868B')

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


liste_cpt_cellule = [[0 for i in range(9)] for j in range(rows)]
liste_cpt_code = [0 for i in range(9)]

liste_nbre_indicateur_G = [0 for i in range(rows)]

liste_point_interrogation_code = [0 for i in range(cols)]


stop_clique_code = 0
cpt = 0
tvar = tk.StringVar()
var = "Cache moi ce code ;)"
tvar.set(var)

tvar2 = tk.StringVar()
var2 = "Mode 1 joueur"
tvar2.set(var2)
Alterner_nbr_joueurs = True
relancer_partie = False
stop_clique_code_ecran_defaite = 0
restaurer_point_interrogation = False

liste_couleur_fixe = [0 for i in range(rows)]

######################### Fonctions ###############################
def nombre_joueur():
    global stop_clique_code, cpt, Alterner_nbr_joueurs, var, var2
    if Alterner_nbr_joueurs == True and cpt == 0:
        var2 = "Mode 2 joueurs"
        tvar2.set(var2)
        var = "Effectuer le 1er essai"
        tvar.set(var)
        stop_clique_code = 1
        cpt = 1
        for i in range(cols):
            liste_DEFINITF_cellule_code_secret[i] = random.randint(1,8)
        #print(liste_DEFINITF_cellule_code_secret)
        nombre_couleur_ligne()
        #print(liste_cpt_code)
        for i in range(cols):
            liste_cellule_code_secret[i] = 0
            x0, y0, x1, y1 = canvas.coords(liste_cercle_code_secret[i])
            liste_point_interrogation_code[i] = canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text = "?", font =("copperplate", "50"))
        couleur_cellule()
        Alterner_nbr_joueurs = False
    elif Alterner_nbr_joueurs == False and cpt == 1:
        var2 = "Mode 1 joueur"
        var = "Cache moi ce code ;)"
        tvar2.set(var2)
        tvar.set(var)
        stop_clique_code = 0
        cpt = 0
        for i in range(cols):
            liste_DEFINITF_cellule_code_secret[i] = 0
            liste_cellule[0][i] = 0
            canvas.itemconfigure(liste_point_interrogation_code[i], state = 'hidden')
        couleur_cellule()
        for i in range(9):
            liste_cpt_code[i] = 0
        #print(liste_cpt_code)
        #print(liste_cellule_code_secret)
        Alterner_nbr_joueurs = True

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
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    for i in range(cols):
        x0, y0, x1, y1 = canvas.coords(liste_cercle_code_secret[i])
        if x > x0 and x < x1 and y > y0 and y < y1 and stop_clique_code == 0:
            liste_cellule_code_secret[i] += 1
            if liste_cellule_code_secret[i] > 8:
                liste_cellule_code_secret[i] = 1
    couleur_cellule()

def cliqueD_code_secret(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    for i in range(cols):
        x0, y0, x1, y1 = canvas.coords(liste_cercle_code_secret[i])
        if x > x0 and x < x1 and y > y0 and y < y1 and stop_clique_code == 0:
            liste_cellule_code_secret[i] -= 1
            if liste_cellule_code_secret[i] < 1:
                liste_cellule_code_secret[i] = 8
    couleur_cellule()

def cacher_code_secret():
    global liste_DEFINITF_cellule_code_secret, stop_clique_code, cpt, relancer_partie, var, restaurer_point_interrogation
    for y in range(rows):
        if cpt == 0 and stop_clique_code < 1 and liste_cellule_code_secret[0] != 0 and liste_cellule_code_secret[1] != 0 and liste_cellule_code_secret[2] != 0 and liste_cellule_code_secret[3] != 0:
            liste_DEFINITF_cellule_code_secret = list(liste_cellule_code_secret)
            for i in range(cols):
                liste_cellule_code_secret[i] = 0
                x0, y0, x1, y1 = canvas.coords(liste_cercle_code_secret[i])
                liste_point_interrogation_code[i] = canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text = "?", font =("copperplate", "50"))
            stop_clique_code = 1
            couleur_cellule()
            cpt += 1
            if cpt <= 1:
                var = 'Effectuer le ' + str(cpt) + 'er essai'
            elif cpt == 10:
                var = 'Attention dernier essai !'
            elif cpt > 10:
                var = 'Encore une partie ? :)'
            else:
                var = 'Effectuer le ' + str(cpt) + 'ème essai'
            tvar.set(var)
            #print(liste_cellule)
            indicateurs_D()
            nombre_couleur_ligne()
            indicateurs_G() 
            couleur_indicateurs()
    #print(liste_DEFINITF_cellule_code_secret)
        if cpt > 0 and y == (cpt - 1) and liste_cellule[y][0] != 0 and liste_cellule[y][1] != 0 and liste_cellule[y][2] != 0 and liste_cellule[y][3] != 0:
            couleur_cellule()
            if cpt < 11:
                cpt += 1
                #print(cpt)
            if cpt <= 1:
                var = 'Effectuer le ' + str(cpt) + 'er essai'
            elif cpt == 10:
                var = 'Attention dernier essai !'
            elif cpt == 11:
                var = 'Encore une partie ? :)'
            else:
                var = 'Effectuer le ' + str(cpt) + 'ème essai'
            tvar.set(var)
            indicateurs_D()
            nombre_couleur_ligne()
            indicateurs_G()
            couleur_indicateurs()
            victoire_defaite()
            #print(liste_cpt_code)
            #print(liste_DEFINITF_cellule_code_secret)
            #print(liste_indicateurs_D_haut)
    """"Code pour que lorsque la partie est chargé les points d'interogations s'affiche"""
    if liste_point_interrogation_code[0] != 0 and restaurer_point_interrogation == True:
        for i in range(cols):
            x0, y0, x1, y1 = canvas.coords(liste_cercle_code_secret[i])
            liste_point_interrogation_code[i] = canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text = "?", font =("copperplate", "50"))
    restaurer_point_interrogation = False
    #print(liste_point_interrogation_code)
    """boucle itère 10 fois seulement, grace à ce code je peux incrémenter la variable 'cpt' encore une fois pour ensuite appeler la fonction nouvelle_partie() sans qu'elle soit appellée dès que la partie se finit"""
    if cpt >= 11:
        cpt += 1
        #print(cpt)
    if cpt == 13:
        relancer_partie = True
        nouvelle_partie()

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

def indicateurs_D():
    for y in range(rows):
        for i in range(cols):
            #print(liste_cellule[y][i])
            #print(liste_DEFINITF_cellule_code_secret[i])
            if y == (cpt - 2) and liste_cellule[y][i] == liste_DEFINITF_cellule_code_secret[i]:
                #print(liste_cellule[y][i])
                #print(liste_DEFINITF_cellule_code_secret[i])
                #print(liste_cellule[y][i])
                if liste_indicateurs_D_haut[y][0] == 0:
                    liste_indicateurs_D_haut[y][0] += 1
                elif liste_indicateurs_D_haut[y][0] != 0 and liste_indicateurs_D_haut[y][1] == 0:
                    liste_indicateurs_D_haut[y][1] += 1
                elif liste_indicateurs_D_haut[y][0] != 0 and liste_indicateurs_D_haut[y][1] != 0 and liste_indicateurs_D_bas[y][0] == 0:
                    liste_indicateurs_D_bas[y][0] += 1
                else:
                    liste_indicateurs_D_bas[y][1] += 1

def nombre_couleur_ligne():
    for i in range(cols):
        if cpt < 2:
            if liste_DEFINITF_cellule_code_secret[i] == 0:
                liste_cpt_code[0] += 1
            elif liste_DEFINITF_cellule_code_secret[i] == 1:
                liste_cpt_code[1]  += 1
                #print(cpt1)
            elif liste_DEFINITF_cellule_code_secret[i] == 2:
                liste_cpt_code[2]+= 1
            elif liste_DEFINITF_cellule_code_secret[i] == 3:
                liste_cpt_code[3] += 1
            elif liste_DEFINITF_cellule_code_secret[i] == 4:
                liste_cpt_code[4] += 1
            elif liste_DEFINITF_cellule_code_secret[i] == 5:
                liste_cpt_code[5] += 1
            elif liste_DEFINITF_cellule_code_secret[i] == 6:
                liste_cpt_code[6] += 1
            elif liste_DEFINITF_cellule_code_secret[i] == 7:
                liste_cpt_code[7] += 1
            elif liste_DEFINITF_cellule_code_secret[i] == 8:
                liste_cpt_code[8] += 1
        #print(liste_cpt_code)
    
    for y in range(rows):
        for i in range(cols):
            if y == (cpt - 2):
                if liste_cellule[y][i] == 0:
                    liste_cpt_cellule[y][0] += 1
                elif liste_cellule[y][i] == 1:
                    liste_cpt_cellule[y][1] += 1
                elif liste_cellule[y][i] == 2:
                    liste_cpt_cellule[y][2] += 1
                elif liste_cellule[y][i] == 3:
                    liste_cpt_cellule[y][3] += 1
                elif liste_cellule[y][i] == 4:
                    liste_cpt_cellule[y][4] += 1
                elif liste_cellule[y][i] == 5:
                    liste_cpt_cellule[y][5] += 1
                elif liste_cellule[y][i] == 6:
                    liste_cpt_cellule[y][6] += 1
                elif liste_cellule[y][i] == 7:
                    liste_cpt_cellule[y][7] += 1
                elif liste_cellule[y][i] == 8:
                    liste_cpt_cellule[y][8] += 1
    #print(liste_cpt_cellule)
              
def indicateurs_G():
    for y in range(rows):
        if (cpt - 2) == y:
            if liste_indicateurs_D_haut[y][0] == 1:
                liste_nbre_indicateur_G[y] -= 1
            if liste_indicateurs_D_haut[y][1] == 1:
                liste_nbre_indicateur_G[y] -= 1
            if liste_indicateurs_D_bas[y][0] == 1:
                liste_nbre_indicateur_G[y] -= 1
            if liste_indicateurs_D_bas[y][1] == 1:
                liste_nbre_indicateur_G[y] -= 1
            for i in range(8):
                if liste_cpt_cellule[y][i + 1] <= liste_cpt_code[i + 1]:
                    liste_nbre_indicateur_G[y] += liste_cpt_cellule[y][i + 1]
                if liste_cpt_cellule[y][i + 1] > liste_cpt_code[i + 1]:
                    liste_nbre_indicateur_G[y] += liste_cpt_code[i + 1]
                if liste_nbre_indicateur_G[y] == 1:
                    liste_indicateurs_G_haut[y][0] = 1
                if liste_nbre_indicateur_G[y] == 2:
                    liste_indicateurs_G_haut[y][0] = 1
                    liste_indicateurs_G_haut[y][1] = 1
                if liste_nbre_indicateur_G[y] == 3:
                    liste_indicateurs_G_haut[y][0] = 1
                    liste_indicateurs_G_haut[y][1] = 1
                    liste_indicateurs_G_bas[y][0] = 1
                if liste_nbre_indicateur_G[y] == 4:
                    liste_indicateurs_G_haut[y][0] = 1
                    liste_indicateurs_G_haut[y][1] = 1
                    liste_indicateurs_G_bas[y][0] = 1
                    liste_indicateurs_G_bas[y][1] = 1
    #print(liste_nbre_indicateur_G)

def couleur_indicateurs():
    for y in range(rows):
        if liste_indicateurs_G_haut[y][0] == 1:
            canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][0], fill = "#CD2626", outline = "#CD2626")
        if liste_indicateurs_G_haut[y][1] == 1:
            canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][1], fill = "#CD2626", outline = "#CD2626")
        if liste_indicateurs_G_bas[y][0] == 1:
            canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][0], fill = "#CD2626", outline = "#CD2626")
        if liste_indicateurs_G_bas[y][1] == 1:
            canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][1], fill = "#CD2626", outline = "#CD2626")
        if liste_indicateurs_D_haut[y][0] == 1:
            canvas.itemconfigure(liste_cercle_indicateurs_D_haut[y][0], fill = "#00CD66", outline = "#00CD66")
        if liste_indicateurs_D_haut[y][1] == 1:
            canvas.itemconfigure(liste_cercle_indicateurs_D_haut[y][1], fill = "#00CD66", outline = "#00CD66")
        if liste_indicateurs_D_bas[y][0] == 1:
            canvas.itemconfigure(liste_cercle_indicateurs_D_bas[y][0], fill = "#00CD66", outline = "#00CD66")
        if liste_indicateurs_D_bas[y][1] == 1:
            canvas.itemconfigure(liste_cercle_indicateurs_D_bas[y][1], fill = "#00CD66", outline = "#00CD66")
    
    for y in range(rows):
        if liste_indicateurs_G_haut[y][0] == 0:
            canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][0], fill = "white", outline = "white")
        if liste_indicateurs_G_haut[y][1] == 0:
            canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][1], fill = "white", outline = "white")
        if liste_indicateurs_G_bas[y][0] == 0:
            canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][0], fill = "white", outline = "white")
        if liste_indicateurs_G_bas[y][1] == 0:
            canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][1], fill = "white", outline = "white")
        if liste_indicateurs_D_haut[y][0] == 0:
            canvas.itemconfigure(liste_cercle_indicateurs_D_haut[y][0], fill = "white", outline = "white")
        if liste_indicateurs_D_haut[y][1] == 0:
            canvas.itemconfigure(liste_cercle_indicateurs_D_haut[y][1], fill = "white", outline = "white")
        if liste_indicateurs_D_bas[y][0] == 0:
            canvas.itemconfigure(liste_cercle_indicateurs_D_bas[y][0], fill = "white", outline = "white")
        if liste_indicateurs_D_bas[y][1] == 0:
            canvas.itemconfigure(liste_cercle_indicateurs_D_bas[y][1], fill = "white", outline = "white")


def recommendation():
    couleur_aleatoire = random.randint(1, 8)
    liste_couleur_fixe.append(couleur_aleatoire)
    couleur_aleatoire2 = random.randint(1, 8)
    liste_couleur_fixe.append(couleur_aleatoire2)
    for y in range(rows):
        for i in range(cols):
            if y == (cpt - 1):
                #if y == 0:
                if liste_indicateurs_G_haut[y - 1][0] == 0 and liste_indicateurs_D_haut[y - 1][0] == 0:
                    if i == 0:
                        liste_cellule[y][i] = couleur_aleatoire
                    elif i == 1:
                        liste_cellule[y][i] = couleur_aleatoire
                        liste_couleur_fixe[0] = couleur_aleatoire
                    elif i == 2:
                        liste_cellule[y][i] = couleur_aleatoire2
                    else:
                        liste_cellule[y][i] = couleur_aleatoire2
                        liste_couleur_fixe[1] = couleur_aleatoire2
                    #print(couleur_fixe)
                elif liste_indicateurs_D_haut[y - 1][0] == 1 and liste_indicateurs_G_haut[y - 1][0] == 0:
                    if i < 2:
                        liste_cellule[y][i] = liste_couleur_fixe[0]
                    else:
                        liste_cellule[y][i] = couleur_aleatoire
                elif liste_indicateurs_G_haut[y - 1][0] == 1:
                    liste_transitoire = list(liste_cellule[y - 1])
                    random.shuffle(liste_transitoire)
                    liste_cellule[y] = list(liste_transitoire)
    couleur_cellule()

def retour_en_arriere():
    global cpt, var
    for y in range(rows):
        for i in range(9):
            if y == (cpt - 1):
                liste_cpt_cellule[y - 1][i] = 0
        for i in range(cols):
            if y == (cpt - 1):
                liste_cellule[y][i] = 0
                liste_cellule[y - 1][i] = 0
                couleur_cellule()
                if liste_indicateurs_G_haut[y - 1][0] == 1:
                    liste_indicateurs_G_haut[y - 1][0] = 0
                    liste_nbre_indicateur_G[y - 1] = 0
                if liste_indicateurs_G_haut[y - 1][1] == 1:
                    liste_indicateurs_G_haut[y - 1][1] = 0
                    liste_nbre_indicateur_G[y - 1] = 0
                if liste_indicateurs_G_bas[y - 1][0] == 1:
                    liste_indicateurs_G_bas[y - 1][0] = 0
                    liste_nbre_indicateur_G[y - 1] = 0
                if liste_indicateurs_G_bas[y - 1][1] == 1:
                    liste_indicateurs_G_bas[y - 1][1] = 0
                    liste_nbre_indicateur_G[y - 1] = 0
                if liste_indicateurs_D_haut[y - 1][0] == 1:
                    liste_indicateurs_D_haut[y - 1][0] = 0
                if liste_indicateurs_D_haut[y - 1][1] == 1:
                    liste_indicateurs_D_haut[y - 1][1] = 0
                if liste_indicateurs_D_bas[y - 1][0] == 1:
                    liste_indicateurs_D_bas[y - 1][0] = 0
                if liste_indicateurs_D_bas[y - 1][1] == 1:
                    liste_indicateurs_D_bas[y - 1][1] = 0
                couleur_indicateurs()
                if i == 3 and cpt > 1:
                    cpt -= 1
                    #print(cpt)
                    if cpt <= 1:
                        var = 'Effectuer le ' + str(cpt) + 'er essai'
                    elif cpt == 10:
                        var = 'Attention dernier essai !'
                    elif cpt > 10:
                        var = 'Encore une partie ? :)'
                    else:
                        var = 'Effectuer le ' + str(cpt) + 'ème essai'
                    tvar.set(var)

    if cpt == 11:
        for i in range(9):
            liste_cpt_cellule[9][i] = 0
        for i in range(cols):
            liste_cellule[9][i] = 0
            couleur_cellule()
            if liste_indicateurs_G_haut[9][0] == 1:
                liste_indicateurs_G_haut[9][0] = 0
                liste_nbre_indicateur_G[9] = 0
            if liste_indicateurs_G_haut[9][1] == 1:
                liste_indicateurs_G_haut[9][1] = 0
                liste_nbre_indicateur_G[9] = 0
            if liste_indicateurs_G_bas[9][0] == 1:
                liste_indicateurs_G_bas[9][0] = 0
                liste_nbre_indicateur_G[9] = 0
            if liste_indicateurs_G_bas[9][1] == 1:
                liste_indicateurs_G_bas[9][1] = 0
                liste_nbre_indicateur_G[9] = 0
            if liste_indicateurs_D_haut[9][0] == 1:
                liste_indicateurs_D_haut[9][0] = 0
            if liste_indicateurs_D_haut[9][1] == 1:
                liste_indicateurs_D_haut[9][1] = 0
            if liste_indicateurs_D_bas[9][0] == 1:
                liste_indicateurs_D_bas[9][0] = 0
            if liste_indicateurs_D_bas[9][1] == 1:
                liste_indicateurs_D_bas[9][1] = 0
            couleur_indicateurs()
            if i == 3 and cpt > 1:
                cpt -= 1
                var = 'Attention dernier essai !'
                tvar.set(var)


def sauvegarde():
    fic = open("Sauvegarde Mastermind", "w")
    for i in range(cols):
        if i < 3:
            fic.write(str(liste_DEFINITF_cellule_code_secret[i]) + ' ')
        else:
            fic.write(str(liste_DEFINITF_cellule_code_secret[i]) + "\n")
    for i in range(cols):
        if i < 3:
            fic.write(str(liste_cercle_code_secret[i]) + ' ')
        else:
            fic.write(str(liste_cercle_code_secret[i]) + "\n")
    for y in range(rows):
        for i in range(cols):
            if i < 3:
                fic.write(str(liste_cellule[y][i]) + " ")
            else:
                fic.write(str(liste_cellule[y][i]) + "\n")
    for y in range(rows):
        for i in range(cols):
            if i < 3:
                fic.write(str(liste_cercle[y][i]) + " ")
            else:
                fic.write(str(liste_cercle[y][i]) + "\n")
    for y in range(rows):
        for i in range(2):
            if i == 0:
                fic.write(str(liste_indicateurs_D_haut[y][i]) + " ")
            else:
                fic.write(str(liste_indicateurs_D_haut[y][i]) + "\n")
    for y in range(rows):
        for i in range(2):
            if i == 0:
                fic.write(str(liste_cercle_indicateurs_D_haut[y][i]) + " ")
            else:
                fic.write(str(liste_cercle_indicateurs_D_haut[y][i]) + "\n")
    for y in range(rows):
        for i in range(2):
            if i == 0:
                fic.write(str(liste_indicateurs_D_bas[y][i]) + " ")
            else:
                fic.write(str(liste_indicateurs_D_bas[y][i]) + "\n")
    for y in range(rows):
        for i in range(2):
            if i == 0:
                fic.write(str(liste_cercle_indicateurs_D_bas[y][i]) + " ")
            else:
                fic.write(str(liste_cercle_indicateurs_D_bas[y][i]) + "\n")
    for y in range(rows):
        for i in range(2):
            if i == 0:
                fic.write(str(liste_indicateurs_G_haut[y][i]) + " ")
            else:
                fic.write(str(liste_indicateurs_G_haut[y][i]) + "\n")
    for y in range(rows):
        for i in range(2):
            if i == 0:
                fic.write(str(liste_cercle_indicateurs_G_haut[y][i]) + " ")
            else:
                fic.write(str(liste_cercle_indicateurs_G_haut[y][i]) + "\n")
    for y in range(rows):
        for i in range(2):
            if i == 0:
                fic.write(str(liste_indicateurs_G_bas[y][i]) + " ")
            else:
                fic.write(str(liste_indicateurs_G_bas[y][i]) + "\n")
    for y in range(rows):
        for i in range(2):
            if i == 0:
                fic.write(str(liste_cercle_indicateurs_G_bas[y][i]) + " ")
            else:
                fic.write(str(liste_cercle_indicateurs_G_bas[y][i]) + "\n")
    for y in range(rows):
        for i in range(9):
            if i < 8:
                fic.write(str(liste_cpt_cellule[y][i]) + " ")
            else:
                fic.write(str(liste_cpt_cellule[y][i]) + "\n")
    for i in range(9):
            if i < 8:
                fic.write(str(liste_cpt_code[i]) + " ")
            else:
                fic.write(str(liste_cpt_code[i]) + "\n")
    for i in range(rows):
            if i < 9:
                fic.write(str(liste_nbre_indicateur_G[i]) + " ")
            else:
                fic.write(str(liste_nbre_indicateur_G[i]) + "\n")
    for i in range(cols):
            if i < 3:
                fic.write(str(liste_point_interrogation_code[i]) + " ")
            else:
                fic.write(str(liste_point_interrogation_code[i]) + "\n")
    fic.write(str(stop_clique_code) + "\n")
    fic.write(str(cpt) + "\n")
    fic.write(str(Alterner_nbr_joueurs) + "\n")
    fic.write(str(relancer_partie) + "\n")
    fic.write(str(var) + "\n")
    fic.write(str(var2))
    fic.close()

def charger_partie():
    global cpt, stop_clique_code, var, var2, Alterner_nbr_joueurs, relancer_partie, liste_DEFINITF_cellule_code_secret, liste_cercle_code_secret, liste_cpt_code, liste_nbre_indicateur_G, liste_point_interrogation_code, restaurer_point_interrogation

    liste_transitoire = []
    i = 0
    fic = open("Sauvegarde Mastermind","r")
    for ligne in fic:
        liste_transitoire.append(ligne.split())
    
    stop_clique_code = 0
    cpt = 0
    Alterner_nbr_joueurs = False
    relancer_partie = False
    var = ''
    var2 = ''

    stop_clique_code = liste_transitoire[115][0]
    stop_clique_code = int(stop_clique_code)
    cpt = liste_transitoire[116][0]
    cpt = int(cpt)
    Alterner_nbr_joueurs = liste_transitoire[117][0]
    if Alterner_nbr_joueurs == 'True':
        Alterner_nbr_joueurs = True
    else:
        Alterner_nbr_joueurs = False
    relancer_partie = liste_transitoire[118][0]
    if relancer_partie == 'True':
        relancer_partie = True
    else:
        relancer_partie = False
    for i in range(len(liste_transitoire[119])):
        var += (liste_transitoire[119][i]) + ' '
    for i in range(len(liste_transitoire[120])):
        var2 += (liste_transitoire[120][i]) + ' '
    
    for i in range(1, 7):
        liste_transitoire.remove(liste_transitoire[-1])
    liste_transitoire = [list(map(int,i)) for i in liste_transitoire]

    liste_DEFINITF_cellule_code_secret = liste_transitoire[0]
    liste_cercle_code_secret = liste_transitoire[1]
    liste_cpt_code = liste_transitoire[112]
    liste_nbre_indicateur_G = liste_transitoire[113]
    liste_point_interrogation_code = liste_transitoire[114]
    for y in range(rows):
        liste_cellule[y] = liste_transitoire[y + 2]
        liste_cercle[y] = liste_transitoire[y + 12]
        liste_indicateurs_D_haut[y] = liste_transitoire[y + 22]
        liste_cercle_indicateurs_D_haut[y] = liste_transitoire[y + 32]
        liste_indicateurs_D_bas[y] = liste_transitoire[y + 42]
        liste_cercle_indicateurs_D_bas[y] = liste_transitoire[y + 52]
        liste_indicateurs_G_haut[y] = liste_transitoire[y + 62]
        liste_cercle_indicateurs_G_haut[y] = liste_transitoire[y + 72]
        liste_indicateurs_G_bas[y] = liste_transitoire[y + 82]
        liste_cercle_indicateurs_G_bas[y] = liste_transitoire[y + 92]
        liste_cpt_cellule[y] = liste_transitoire[y + 102]
    
    restaurer_point_interrogation = True

    fic.close()

    tvar.set(var)
    tvar2.set(var2)
    
    couleur_cellule()
    couleur_indicateurs()
    cacher_code_secret()
    nombre_joueur
    #print(liste_transitoire)
    #print(var2, var, Alterner_nbr_joueurs, relancer_partie, cpt, stop_clique_code)
    #print(type(Alterner_nbr_joueurs), type(relancer_partie))
    #print(liste_DEFINITF_cellule_code_secret)
    #print(liste_cercle_code_secret)
    #print(liste_cellule)
    #print(liste_cercle)
    #print(liste_indicateurs_D_haut)
    #print(liste_cercle_indicateurs_D_haut)
    #print(liste_cpt_code)
    #print(liste_nbre_indicateur_G) 

def victoire_defaite():
    global ecran_defaite, ecran_victoire, cpt, var, stop_clique_code_ecran_defaite
    for y in range(rows):
        if liste_indicateurs_D_bas[y][1] == 1 and y < 4:
            ecran_victoire = canvas.create_window(WIDTH/2, HEIGHT/2, window = label_victoire)
            cpt = 11
            var = "Encore une partie ? :)"
            tvar.set(var)
        elif liste_indicateurs_D_bas[y][1] == 1:
            x0, y0, x1, y1 = canvas.coords(liste_cercle[y][0])
            #print(y0, y1)
            ecran_victoire = canvas.create_window(WIDTH/2, (y0 + y1)/2, window = label_victoire)
            #print(ecran_victoire)
            cpt = 11
            var = "Encore une partie ? :)"
            tvar.set(var)
            stop_clique_code_ecran_defaite = 1
        if cpt == 11 and liste_cellule[9][0] != 0 and stop_clique_code_ecran_defaite == 0:
            ecran_defaite = canvas.create_window(WIDTH/2, 1140 - (HEIGHT/2), window = label_defaite)

def nouvelle_partie():
    global cpt, stop_clique_code, relancer_partie, Alterner_nbr_joueurs, var, var2, stop_clique_code_ecran_defaite
    if relancer_partie == True:
        if cpt == 13 and liste_cellule[9][0] != 0 and stop_clique_code_ecran_defaite != 1:
            canvas.itemconfigure(ecran_defaite, state = 'hidden')
        else:
            canvas.itemconfigure(ecran_victoire, state = 'hidden')
        for i in range(cols):
            liste_DEFINITF_cellule_code_secret[i] = 0
            canvas.itemconfigure(liste_point_interrogation_code[i], state = 'hidden')
            liste_point_interrogation_code[i] = 0
            #print(liste_point_interrogation_code)
        for y in range(rows):
            liste_nbre_indicateur_G[y] = 0
            for i in range(cols):
                liste_cellule[y][i] = 0
            for i in range(2):
                liste_indicateurs_D_haut[y][i] = 0
                liste_indicateurs_D_bas[y][i] = 0
                liste_indicateurs_G_haut[y][i] = 0
                liste_indicateurs_G_bas[y][i] = 0
            for i in range(9):
                liste_cpt_cellule[y][i] = 0
        for i in range(9):
            liste_cpt_code[i] = 0
        couleur_cellule()
        couleur_indicateurs()
        var = "Cache moi ce code ;)"
        tvar.set(var)
        var2 = "Mode 1 joueur"
        tvar2.set(var2)
        Alterner_nbr_joueurs = True
        relancer_partie = False
        cpt = 0
        stop_clique_code = 0
        stop_clique_code_ecran_defaite = 0

######################### Pogramme ################################
scroll_y = tk.Scrollbar(racine, orient = 'vertical')
scroll_y.grid(row = 0, rowspan = 5, column = 2, sticky = 'ns')

canvas = tk.Canvas(racine, bg = "#53868B", height=HEIGHT, width=WIDTH, scrollregion = (0, 0, 490, 1140), yscrollcommand = scroll_y.set, bd = 5)#, highlightthickness = 0)
canvas.grid(row = 0, rowspan = 5, column = 1)
scroll_y.config(command = canvas.yview)

label_victoire = tk.Label(racine, text = "Félicitations !" + "\n\n" + "Vous avez remporté la partie :)", font =("Optima", "30"), bg = 'yellow', borderwidth = 10)
label_defaite = tk.Label(racine, text = "Quel dommage, c'était pas loin !" + "\n\n" + "Pourquoi pas retenter ta chance ?", font =("Optima", "30"), bg = '#98FB98', borderwidth = 10)

#Cercles iterations :
for y in range(10):
    for i in range(4):
        cercle = canvas.create_oval((60 + (i * 100), 150 + (y * 100)), (((i + 1) * 100) + 30, ((y + 1) * 100) + 120), outline = "black", width = 5)
        liste_cercle[y][i] = cercle
"""cercles de diametre 70, commence à 60 pxl de la gauche et finit à 60 pxl de la droite. Les 10 finissent à y = 1120"""

#Quelques coordonnées utiles pour le positionnement des cerlces et des indicateurs dans le canevas
#60 150 130 220 : 1er cercle
#160 250 230 320 : 2eme cercle
#90 à 150 donc ligne à y = 120
#1er cerlce commence à y = 150 et finit à y = 220
#Milieu 1er cercle à y = 185
#Dernier cercle se finit à x = 430

#Cercles code secret :
for z in range(4):
    cercle_code = canvas.create_oval((60 + (z * 100), 20, (((z + 1) * 100) + 30, 90)), outline = "black", width = 5)
    liste_cercle_code_secret[z] = cercle_code

#Cercles indicateurs G et D :
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


ligne_separation = canvas.create_line((60, 120), (430, 120), fill="black", width=2)


bouton_iteration = tk.Button(racine, textvariable = tvar, command = cacher_code_secret, padx =16, pady =18, bd ='3', font =("Optima", "23"), width = 14)
bouton_iteration.grid(row = 6, column = 1, pady =25)

bouton_recommendation = tk.Button(racine, text = "Besoin d'aide ?", command = recommendation, padx =16, pady =18, bd ='3', bg ='blue', font =("Comic Sans MS", "23"), width = 9)
bouton_recommendation.grid(row = 1, column = 0)

bouton_retour_en_arriere = tk.Button(racine, text = "Retour en arrière", command = retour_en_arriere, padx =16, pady =18, bd ='3', bg ='blue', font =("Optima", "23"), width = 10)
bouton_retour_en_arriere.grid(row = 2, column = 0)

bouton_sauvegarde = tk.Button(racine, text = "Sauvegarder", command = sauvegarde, padx =16, pady =18, bd ='3', bg ='blue', font =("Optima", "23"), width = 10)
bouton_sauvegarde.grid(row = 3, column = 0)

bouton_charger = tk.Button(racine, text = "Charger la partie", command = charger_partie, padx =18, pady =18, bg ='blue', font =("Optima", "23"), width = 10, bd = '3')
bouton_charger.grid(row = 4, column = 0)

bouton_nbre_joueur = tk.Button(racine, textvariable = tvar2, command = nombre_joueur, padx =27, pady =18, bd ='3', bg ='yellow', font =("Optima", "23"), width = 9)
bouton_nbre_joueur.grid(row = 0, column = 0, padx =25)

canvas.bind("<Button-1>", cliqueG_code_secret)
canvas.bind("<Button-1>", cliqueG_iteration, add='+')
canvas.bind("<Button-2>", cliqueD_code_secret)
canvas.bind("<Button-2>", cliqueD_iteration, add='+')

couleur_cellule()

racine.mainloop()