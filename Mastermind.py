#########################################
# groupe MI 1
# Pierre RATCLIFFE
# Yassine BAGHDAD-BEY
# Sephora TAHA
# Nique PRYSCIA
# https://github.com/uvsq22008849/projet_mastermind.git
#########################################


##################### Import des modules ##########################

import tkinter as tk
import random

##################### variables globales ##########################

racine = tk.Tk()

HEIGHT = 500
WIDTH = 490


######################### Fonctions ###############################


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
    canvas.create_oval((60 + (z * 100), 20, (((z + 1) * 100) + 30, 90)), outline = "black", width = 5)

canvas.create_line((60, 120), (430, 120), fill="black", width=2)

scroll_y.config(command = canvas.yview)


racine.mainloop()