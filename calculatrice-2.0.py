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
Button(fenetre, text='1', borderwidth=1).grid(row=1, column=1)
Button(fenetre, text='2', borderwidth=1).grid(row=1, column=2)
Button(fenetre, text='3', borderwidth=1).grid(row=1, column=3)
Button(fenetre, text='4', borderwidth=1).grid(row=2, column=1)
Button(fenetre, text='5', borderwidth=1).grid(row=2, column=2)
Button(fenetre, text='6', borderwidth=1).grid(row=2, column=3)
Button(fenetre, text='7', borderwidth=1).grid(row=3, column=1)
Button(fenetre, text='8', borderwidth=1).grid(row=3, column=2)
Button(fenetre, text='9', borderwidth=1).grid(row=3, column=3)
Button(fenetre, text='0', borderwidth=1).grid(row=4, column=2)

fenetre.mainloop()
