# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:34:51 2022

@author: coren
"""

import tkinter as tk 
import numpy as np
import matplotlib.pyplot as pp
import copy
from mpl_toolkits.mplot3d import Axes3D

def Calcul():
    A = np.array([[float(A_e11.get()),float(A_e12.get())],[float(A_e12.get()),float(A_e22.get())]])
    b = np.array([[float(B_e1.get())],[float(B_e1.get())]])
    c = float(C_e1.get())
    print(A)
    print(b)
    print(c)
    x,y = np.arange(-10,10,.01),np.arange(-10,10,.01)
    xx,yy = np.meshgrid(x,y)
    f = 0.5*(A[0,0]*xx**2) 
    f += 0.5*(A[1,1]*yy**2 )
    f += A[1,0]*xx*yy -b[0]*xx-b[1]*yy + c
    fig = pp.figure()
    ax = Axes3D(fig)
    ax.plot_surface(xx,yy,f)
    pp.show()

fen = tk.Tk()
fen.geometry('500x500') 
can1 = tk.Canvas(fen,width = 500,height = 500)
can1.pack()
# --------------
# Get A
# --------------

can1.create_text(10,100,anchor=tk.NW,text = "A = ")
A_E11 = tk.IntVar() ; A_E12 = tk.IntVar() ; A_E22 = tk.IntVar() 
A_e11 = tk.Entry(can1,textvariable = A_E11,width = 5) ; A_e12 = tk.Entry(can1,textvariable = A_E12,width = 5); A_e22 = tk.Entry(can1,textvariable = A_E22,width = 5)
A_e11.place(x = 50 , y = 70) ; A_e12.place(x = 100 , y = 70) ; A_e22.place(x = 100 , y = 120)
l1 = tk.Label(can1,textvariable = A_E12)
l1.place(x =50 , y = 120)

# --------------
# Get b
# --------------

can1.create_text(210 , 100 ,text = "b = ", anchor = tk.NW)
B_E1,B_E2 = tk.IntVar(), tk.IntVar()
B_e1 = tk.Entry(can1,textvariable = B_E1,width = 5) ; B_e2 = tk.Entry(can1,textvariable = B_E2,width = 5)
B_e1.place(x = 250 , y = 70) ; B_e2.place(x = 250 , y = 120)

# --------------
# Get c
# --------------

can1.create_text(310, 100, text = "c = ",anchor = tk.NW)
C_E1 = tk.IntVar()
C_e1 = tk.Entry(can1,textvariable = C_E1,width = 5)
C_e1.place(x = 350, y = 100)

# --------------
# Button de calcul
# --------------

B1 = tk.Button(can1,text = "Calcul",command = Calcul)
B1.place(x = 300, y = 250)


fen.mainloop()




