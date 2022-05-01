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
#racine.configure(bg = 'black')

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

#liste_recommendation = [[0 for i in range(cols)] for j in range(rows)]


stop = 0
cpt = 0
#pivot = 0
tvar = tk.StringVar()
tvar.set("Cache moi ce code ;)")

tvar2 = tk.StringVar()
tvar2.set("Passer au mode 1 joueur")
bool = True

######################### Fonctions ###############################
def nombre_joueur():
    global stop, cpt, bool
    if bool == True:
        #var2 = "Passer au mode 2 joueurs"
        tvar2.set("Passer au mode 2 joueurs")
        tvar.set("Effectuer le 1er essai")
        stop = 1
        cpt = 1
        for i in range(cols):
            liste_DEFINITF_cellule_code_secret[i] = random.randint(1,8)
        #print(liste_DEFINITF_cellule_code_secret)
        nombre_couleur_ligne()
        #print(liste_cpt_code)
        for i in range(cols):
            liste_cellule_code_secret[i] = 0
        couleur_cellule()
        bool = False
    elif bool == False:
        tvar2.set("Passer au mode 1 joueur")
        tvar.set("Cache moi ce code ;)")
        stop = 0
        cpt = 0
        for i in range(cols):
            liste_DEFINITF_cellule_code_secret[i] = 0
            liste_cellule[0][i] = 0
        couleur_cellule()
        #print(liste_DEFINITF_cellule_code_secret)
        for i in range(9):
            liste_cpt_code[i] = 0
        #print(liste_cpt_code)
        #print(liste_cellule_code_secret)
        
        bool = True


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
    for y in range(rows):
        if cpt == 0 and stop < 1 and liste_cellule_code_secret[0] != 0 and liste_cellule_code_secret[1] != 0 and liste_cellule_code_secret[2] != 0 and liste_cellule_code_secret[3] != 0:
            liste_DEFINITF_cellule_code_secret = list(liste_cellule_code_secret)
            for i in range(cols):
                liste_cellule_code_secret[i] = 0
                x0, y0, x1, y1 = canvas.coords(liste_cercle_code_secret[i])
                canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text = "?", width = 50)
            stop = 1
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
            #print(cpt)

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
                '''if i < 2
                    canvas.itemconfigure(liste_cercle_indicateurs_D_haut[y][i], fill = "red", outline = "red")
                else:
                    canvas.itemconfigure(liste_cercle_indicateurs_D_bas[y][i - 2], fill = "red", outline = "red")'''
                if liste_indicateurs_D_haut[y][0] == 0:
                    #canvas.itemconfigure(liste_cercle_indicateurs_D_haut[y][0], fill = "red", outline = "red")
                    liste_indicateurs_D_haut[y][0] += 1
                elif liste_indicateurs_D_haut[y][0] != 0 and liste_indicateurs_D_haut[y][1] == 0:
                    #canvas.itemconfigure(liste_cercle_indicateurs_D_haut[y][1], fill = "red", outline = "red")
                    liste_indicateurs_D_haut[y][1] += 1
                elif liste_indicateurs_D_haut[y][0] != 0 and liste_indicateurs_D_haut[y][1] != 0 and liste_indicateurs_D_bas[y][0] == 0:
                    #canvas.itemconfigure(liste_cercle_indicateurs_D_bas[y][0], fill = "red", outline = "red")
                    liste_indicateurs_D_bas[y][0] += 1
                else:# liste_indicateurs_D_haut[y][0] != 0 and liste_indicateurs_D_haut[y][1] != 0 and liste_indicateurs_D_bas[y][0] != 0 and liste_indicateurs_D_bas[y][1] == 0:
                    #canvas.itemconfigure(liste_cercle_indicateurs_D_bas[y][1], fill = "red", outline = "red")
                    liste_indicateurs_D_bas[y][1] += 1

def nombre_couleur_ligne():
    #global cpt0, cpt1, cpt2, cpt3, cpt4, cpt5, cpt6, cpt7, cpt8
    #global cpt0_cellule, cpt1_cellule, cpt2_cellule, cpt3_cellule, cpt4_cellule, cpt5_cellule, cpt6_cellule, cpt7_cellule, cpt8_cellule
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
            if y == (cpt - 2):# and cpt > 2:
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
    #liste_position_indice = [4 for i in range(cols)]
    #liste_nbre_indicateur_G = [0 for i in range(rows)]
    for y in range(rows):
        if liste_indicateurs_D_haut[y][0] == 1:
            liste_nbre_indicateur_G[y] -= 1
        if liste_indicateurs_D_haut[y][1] == 1:
            liste_nbre_indicateur_G[y] -= 1
        if liste_indicateurs_D_bas[y][0] == 1:
            liste_nbre_indicateur_G[y] -= 1
        if liste_indicateurs_D_bas[y][1] == 1:
            liste_nbre_indicateur_G[y] -= 1
        for i in range(8):
            #if y == (cpt - 2):
            if liste_cpt_cellule[y][i + 1] <= liste_cpt_code[i + 1]:
                liste_nbre_indicateur_G[y] += liste_cpt_cellule[y][i + 1]
            if liste_cpt_cellule[y][i + 1] > liste_cpt_code[i + 1]:
                liste_nbre_indicateur_G[y] += liste_cpt_code[i + 1]
            if liste_nbre_indicateur_G[y] == 1:
                #canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][0], fill = "black", outline = "black")
                liste_indicateurs_G_haut[y][0] = 1
            if liste_nbre_indicateur_G[y] == 2:
                #canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][0], fill = "black", outline = "black")
                #canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][1], fill = "black", outline = "black")
                liste_indicateurs_G_haut[y][0] = 1
                liste_indicateurs_G_haut[y][1] = 1
            if liste_nbre_indicateur_G[y] == 3:
                #canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][0], fill = "black", outline = "black")
                #canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][1], fill = "black", outline = "black")
                #canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][0], fill = "black", outline = "black")
                liste_indicateurs_G_haut[y][0] = 1
                liste_indicateurs_G_haut[y][1] = 1
                liste_indicateurs_G_bas[y][0] = 1
            if liste_nbre_indicateur_G[y] == 4:
                #canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][0], fill = "black", outline = "black")
                #canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][1], fill = "black", outline = "black")
                #canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][0], fill = "black", outline = "black")
                #canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][1], fill = "black", outline = "black") 
                liste_indicateurs_G_haut[y][0] = 1
                liste_indicateurs_G_haut[y][1] = 1
                liste_indicateurs_G_bas[y][0] = 1
                liste_indicateurs_G_bas[y][1] = 1
    #print(liste_nbre_indicateur_G)
    #nbre_indicateur_G = 0

def couleur_indicateurs():
    for y in range(rows):
        if (cpt - 2) == y:
            if liste_indicateurs_G_haut[y][0] == 1:
                canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][0], fill = "black", outline = "black")
            if liste_indicateurs_G_haut[y][1] == 1:
                canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][1], fill = "black", outline = "black")
            if liste_indicateurs_G_bas[y][0] == 1:
                canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][0], fill = "black", outline = "black")
            if liste_indicateurs_G_bas[y][1] == 1:
                canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][1], fill = "black", outline = "black")
            if liste_indicateurs_D_haut[y][0] == 1:
                canvas.itemconfigure(liste_cercle_indicateurs_D_haut[y][0], fill = "red", outline = "red")
            if liste_indicateurs_D_haut[y][1] == 1:
                canvas.itemconfigure(liste_cercle_indicateurs_D_haut[y][1], fill = "red", outline = "red")
            if liste_indicateurs_D_bas[y][0] == 1:
                canvas.itemconfigure(liste_cercle_indicateurs_D_bas[y][0], fill = "red", outline = "red")
            if liste_indicateurs_D_bas[y][1] == 1:
                canvas.itemconfigure(liste_cercle_indicateurs_D_bas[y][1], fill = "red", outline = "red")
    
    for y in range(rows):
        if (cpt - 2) == y:
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
    for y in range(rows):
        for i in range(cols):
            if y == (cpt - 1):
                if y == 0:
                    liste_cellule[y][i] = couleur_aleatoire
                elif y == 1 and liste_indicateurs_D_haut[y - 1][0] != 1 and liste_indicateurs_G_haut[y - 1][0] != 1:
                    liste_cellule[y][i] = couleur_aleatoire
                elif liste_indicateurs_G_haut[y - 1][0] == 1:
                    liste_transitoire = list(liste_cellule[y - 1])
                    random.shuffle(liste_transitoire)
                    liste_cellule[y] = list(liste_transitoire)
    couleur_cellule()

def retour_en_arriere():
    global cpt
    for y in range(rows):
        for i in range(9):
            if y == (cpt - 1):# and cpt > 2:
                liste_cpt_cellule[y - 1][i] = 0
        for i in range(cols):
            if y == (cpt - 1):
                liste_cellule[y][i] = 0
                liste_cellule[y - 1][i] = 0
                couleur_cellule()
                if liste_indicateurs_G_haut[y - 1][0] == 1:
                    liste_indicateurs_G_haut[y - 1][0] = 0
                    #liste_indicateurs_G_haut[y][0] = 0
                    liste_nbre_indicateur_G[y - 1] = 0
                if liste_indicateurs_G_haut[y - 1][1] == 1:
                    liste_indicateurs_G_haut[y - 1][1] = 0
                    #liste_indicateurs_G_haut[y][1] = 0
                    liste_nbre_indicateur_G[y - 1] = 0
                if liste_indicateurs_G_bas[y - 1][0] == 1:
                    liste_indicateurs_G_bas[y - 1][0] = 0
                    #liste_indicateurs_G_bas[y][0] = 0
                    liste_nbre_indicateur_G[y - 1] = 0
                if liste_indicateurs_G_bas[y - 1][1] == 1:
                    liste_indicateurs_G_bas[y - 1][1] = 0
                    #liste_indicateurs_G_bas[y][1] = 0
                    liste_nbre_indicateur_G[y - 1] = 0
                if liste_indicateurs_D_haut[y - 1][0] == 1:
                    liste_indicateurs_D_haut[y - 1][0] = 0
                    #liste_indicateurs_D_haut[y][0] = 0
                if liste_indicateurs_D_haut[y - 1][1] == 1:
                    liste_indicateurs_D_haut[y - 1][1] = 0
                    #liste_indicateurs_D_haut[y][1] = 0
                if liste_indicateurs_D_bas[y - 1][0] == 1:
                    liste_indicateurs_D_bas[y - 1][0] = 0
                    #liste_indicateurs_D_bas[y][0] = 0
                if liste_indicateurs_D_bas[y - 1][1] == 1:
                    liste_indicateurs_D_bas[y - 1][1] = 0
                    #liste_indicateurs_D_bas[y][1] = 0
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

def sauvegarde():
    fic = open("Sauvegarde Mastermind", "w")
    fic.write(str(liste_DEFINITF_cellule_code_secret) + "\n")
    #for y in range(rows):
    fic.write(str(liste_cellule) + "\n")
    #for y in range(rows):
    #    for i in range(2):
    fic.write(str(liste_indicateurs_D_haut) + "\n")
    fic.write(str(liste_indicateurs_D_bas) + "\n")
    fic.write(str(liste_indicateurs_G_haut) + "\n")
    fic.write(str(liste_indicateurs_G_bas) + "\n")
    fic.close()


######################### Pogramme ################################

scroll_y = tk.Scrollbar(racine, orient = 'vertical')
scroll_y.grid(row = 0, rowspan = 5, column = 2, sticky = 'ns')

canvas = tk.Canvas(racine, bg = "white", height=HEIGHT, width=WIDTH, scrollregion = (0, 0, 490, 1140), yscrollcommand = scroll_y.set)
canvas.grid(row = 0, rowspan = 5, column = 1)
scroll_y.config(command = canvas.yview)

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


bouton_iteration = tk.Button(racine, textvariable = tvar, command = cacher_code_secret, padx =16, pady =18, bd ='5', bg ='blue', font =("Optima", "23"), width = 14)
bouton_iteration.grid(row = 6, column = 1)

bouton_recommendation = tk.Button(racine, text = "Besoin d'aide ?", command = recommendation, padx =16, pady =18, bd ='5', bg ='blue', font =("Optima", "23"))
bouton_recommendation.grid(row = 1, column = 0)

bouton_retour_en_arriere = tk.Button(racine, text = "Retour en arrière", command = retour_en_arriere, padx =16, pady =18, bd ='5', bg ='blue', font =("Optima", "23"), width = 10)
bouton_retour_en_arriere.grid(row = 2, column = 0)

bouton_sauvegarde = tk.Button(racine, text = "Sauvegarder", command = sauvegarde, padx =16, pady =18, bd ='5', bg ='blue', font =("Optima", "23"), width = 10)
bouton_sauvegarde.grid(row = 3, column = 0)

bouton_charger = tk.Button(racine, text = "Charger la partie", command = retour_en_arriere, padx =16, pady =18, bd ='5', bg ='blue', font =("Optima", "23"), width = 10)
bouton_charger.grid(row = 4, column = 0)

bouton_nbre_joueur = tk.Button(racine, textvariable = tvar2, command = nombre_joueur, padx =30, pady =18, bd ='5', bg ='blue', font =("Optima", "23"), width = 14)
bouton_nbre_joueur.grid(row = 0, column = 0)

canvas.bind("<Button-1>", cliqueG_code_secret)
canvas.bind("<Button-1>", cliqueG_iteration, add='+')
canvas.bind("<Button-2>", cliqueD_code_secret)
canvas.bind("<Button-2>", cliqueD_iteration, add='+')

racine.mainloop()