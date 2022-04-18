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


stop = 0
cpt = 0
#pivot = 0
cpt0, cpt1, cpt2, cpt3, cpt4, cpt5, cpt6, cpt7, cpt8 = 0, 0, 0, 0, 0, 0, 0, 0, 0
cpt0_cellule, cpt1_cellule, cpt2_cellule, cpt3_cellule, cpt4_cellule, cpt5_cellule, cpt6_cellule, cpt7_cellule, cpt8_cellule = 0, 0, 0, 0, 0, 0, 0, 0, 0
tvar = tk.StringVar()
tvar.set("Cache moi ce code ;)")

######################### Fonctions ###############################
def couleur_cellule():
    global cpt0, cpt1, cpt2, cpt3, cpt4, cpt5, cpt6, cpt7, cpt8
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
                    canvas.itemconfigure(liste_cercle_indicateurs_D_haut[y][0], fill = "red", outline = "red")
                    liste_indicateurs_D_haut[y][0] += 1
                elif liste_indicateurs_D_haut[y][0] != 0 and liste_indicateurs_D_haut[y][1] == 0:
                    canvas.itemconfigure(liste_cercle_indicateurs_D_haut[y][1], fill = "red", outline = "red")
                    liste_indicateurs_D_haut[y][1] += 1
                elif liste_indicateurs_D_haut[y][0] != 0 and liste_indicateurs_D_haut[y][1] != 0 and liste_indicateurs_D_bas[y][0] == 0:
                    canvas.itemconfigure(liste_cercle_indicateurs_D_bas[y][0], fill = "red", outline = "red")
                    liste_indicateurs_D_bas[y][0] += 1
                else:# liste_indicateurs_D_haut[y][0] != 0 and liste_indicateurs_D_haut[y][1] != 0 and liste_indicateurs_D_bas[y][0] != 0 and liste_indicateurs_D_bas[y][1] == 0:
                    canvas.itemconfigure(liste_cercle_indicateurs_D_bas[y][1], fill = "red", outline = "red")
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

'''Bonne couleur bonne place --> enlever  de indicateur gauche'''
"""def indicateurs_G():
    cpt2 = 0
    liste_verifiacation_couleur_differente = [0 for i in range(cols)]
    liste_cellule_deja_compté = [[0 for i in range(cols)] for j in range(rows)]
    liste_transitoire = [[0 for i in range(cols)] for j in range(rows)]
    liste_transitoire = list(liste_cellule)
    #print(liste_transitoire)
    for y in range(rows):
        for i in range(cols):
            if liste_DEFINITF_cellule_code_secret[i] == liste_cellule[y][i]:
                       liste_cellule_deja_compté[y][i] += 1
                       #print(liste_cellule_deja_compté)
                       #print(liste_cellule_deja_compté)
            #           cpt2 += 1
            #if liste_cellule_deja_compté[i] != 4:
            #    if liste_DEFINITF_cellule_code_secret[i] == liste_cellule_deja_compté
            for k in range(cols):
                #if liste_DEFINITF_cellule_code_secret[i] == liste_cellule[y][i]:
                #    liste_transitoire[y][i] = 9
                if y == (cpt - 2) and liste_DEFINITF_cellule_code_secret[i] == liste_cellule[y][k] and liste_cellule_deja_compté[y][k] < 1:# and liste_DEFINITF_cellule_code_secret[i] != liste_cellule[y][i]:# and k != liste_cellule_deja_compté[i]:
                    #if liste_cellule_deja_compté[i] != 4:
                        '''if liste_DEFINITF_cellule_code_secret[i] == liste_cellule[y][i]:
                        i_fixe = i'''
                        #if liste_DEFINITF_cellule_code_secret[i] == liste_cellule[y][i]:
                        #    liste_cellule_deja_compté[i] = liste_cellule[y][i]
                        liste_cellule_deja_compté[y][k] += 1
                        if liste_DEFINITF_cellule_code_secret[i] == liste_cellule[y][i]:
                            break
                        if liste_indicateurs_G_haut[y][0] == 0:
                            canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][0], fill = "red", outline = "red")
                            liste_indicateurs_G_haut[y][0] += 1
                            #t = liste_DEFINITF_cellule_code_secret[i]
                            #liste_verifiacation_couleur_differente[0] = t
                            break
                        elif liste_indicateurs_G_haut[y][0] != 0 and liste_indicateurs_G_haut[y][1] == 0:
                            canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][1], fill = "red", outline = "red")
                            liste_indicateurs_G_haut[y][1] += 1
                            #t = liste_DEFINITF_cellule_code_secret[i]
                            #liste_verifiacation_couleur_differente[1] = t
                            break
                        elif liste_indicateurs_G_haut[y][0] != 0 and liste_indicateurs_G_haut[y][1] != 0 and liste_indicateurs_G_bas[y][0] == 0:
                            canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][0], fill = "red", outline = "red")
                            liste_indicateurs_G_bas[y][0] += 1
                            #t = liste_DEFINITF_cellule_code_secret[i]
                            #liste_verifiacation_couleur_differente[2] = t
                            break
                        elif liste_indicateurs_G_haut[y][0] != 0 and liste_indicateurs_G_haut[y][1] != 0 and liste_indicateurs_G_bas[y][0] != 0:
                            canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][1], fill = "red", outline = "red")
                            liste_indicateurs_G_bas[y][1] += 1"""
              
def indicateurs_G():
    liste_position_indice = [4 for i in range(cols)]
    liste_nbre_indicateur_G = [0 for i in range(rows)]
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
            '''if i < cols:
                if liste_DEFINITF_cellule_code_secret[i] == liste_cellule[y][i]:
                    liste_nbre_indicateur_G[y] -= 1'''
            """if liste_indicateurs_D_haut[y][0] == 1:
                liste_nbre_indicateur_G[y] -= 1
            if liste_indicateurs_D_haut[y][1] == 1:
                liste_nbre_indicateur_G[y] -= 1
            if liste_indicateurs_D_bas[y][0] == 1:
                liste_nbre_indicateur_G[y] -= 1
            if liste_indicateurs_D_bas[y][1] == 1:
                liste_nbre_indicateur_G[y] -= 1"""
            if liste_nbre_indicateur_G[y] == 1:
                canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][0], fill = "black", outline = "black")
            if liste_nbre_indicateur_G[y] == 2:
                canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][0], fill = "black", outline = "black")
                canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][1], fill = "black", outline = "black")
            if liste_nbre_indicateur_G[y] == 3:
                canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][0], fill = "black", outline = "black")
                canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][1], fill = "black", outline = "black")
                canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][0], fill = "black", outline = "black")
            if liste_nbre_indicateur_G[y] == 4:
                canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][0], fill = "black", outline = "black")
                canvas.itemconfigure(liste_cercle_indicateurs_G_haut[y][1], fill = "black", outline = "black")
                canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][0], fill = "black", outline = "black")
                canvas.itemconfigure(liste_cercle_indicateurs_G_bas[y][1], fill = "black", outline = "black") 
    #print(liste_nbre_indicateur_G)
    #nbre_indicateur_G = 0
        #print(nbre_indicateur_G)
    '''for i in range(cols):
        for k in range(cols):
            if liste_DEFINITF_cellule_code_secret[0] == liste_cellule[y][k]:
                liste_position_indice[0] = k
                break
            if liste_DEFINITF_cellule_code_secret[1] == liste_cellule[y][k] and liste_position_indice[0] == 4:# and k != liste_position_indice[0]:
                liste_position_indice[1] = k
                break
            if liste_DEFINITF_cellule_code_secret[1] == liste_cellule[y][k] and liste_position_indice[0] != 4 and k != liste_position_indice[0]:
                liste_position_indice[1] = k
                break '''
                        


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


ligne_separation = canvas.create_line((60, 120), (430, 120), fill="black", width=2)


bouton_iteration = tk.Button(racine, textvariable = tvar, command = cacher_code_secret, padx =16, pady =18, bd ='5', bg ='blue', font =("Optima", "23"))
bouton_iteration.grid(row = 1, column = 0)

scroll_y.config(command = canvas.yview)
canvas.bind("<Button-1>", cliqueG_code_secret)
canvas.bind("<Button-1>", cliqueG_iteration, add='+')
canvas.bind("<Button-2>", cliqueD_code_secret)
canvas.bind("<Button-2>", cliqueD_iteration, add='+')

racine.mainloop()