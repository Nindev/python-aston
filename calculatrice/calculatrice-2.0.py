#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Calculatrice 2.0 Graphique")
label.pack()

# bouton de sortie
bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)

fenetre.mainloop()
