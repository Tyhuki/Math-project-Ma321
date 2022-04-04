# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 13:46:25 2022

@author: coren
"""
import numpy as np 
import matplotlib.pyplot as pp
import copy
from mpl_toolkits.mplot3d import Axes3D



def DescenteGradient_PFixe(A,b,x_0,nitermax,pas,tol ):
    xit = [x_0]
    Niter = 0
    x = x_0
    R_k = tol*2
    while Niter < nitermax and np.linalg.norm(R_k) > tol : 
        Niter += 1
        R_k = A@x - b
        x += -pas*R_k
        xit.append(x)
    print("On obtient un vecteur x = ",x," avec ",Niter," itérations.")
    return x,xit,Niter

def DescenteGradient_POptimal(A,b,x_0,nitermax,tol):
    xit = list()
    xit.append(copy.copy(x_0))
    Niter = 0
    x = x_0
    pas = float()
    R_k = tol*2
    while Niter < nitermax and np.linalg.norm(R_k) > tol :
        Niter += 1
        R_k = A@x - b
        pas = np.linalg.norm(R_k)**2/(np.transpose(R_k)@A@R_k)
        x += -pas*R_k
        print(x)
        xit.append(copy.copy(x))
    print("On obtient un vecteur x = ",x," avec ",Niter," itérations.")
    return x,xit,Niter

def DescenteGradient_Conjugue(A,b,x_0,Nitermax,tol):
    xit = list()
    xit.append(copy.copy(x_0))
    Niter = 0
    x = x_0
    pas = float() ; d = float() ; B = float()
    R_km1 = tol*2
    R_k = tol*2
    while Niter < Nitermax and np.linalg.norm(A@x - b) > tol : # Bon 
        R_km1 = R_k
        Niter += 1
        R_k = A@x - b
        if Niter == 1 :
            d = -R_k
        else : 
            B = np.linalg.norm(R_k)**2/np.linalg.norm(R_km1)**2
            d =  - R_k + B*d
        pas = (np.transpose(R_k)@R_k)/(np.transpose(d)@A@d)
        x += pas*d
        xit.append(copy.copy(x))
    print("On obtient un vecteur x = ",x," avec ",Niter," itérations.")
    return x,xit,Niter

dataP = np.loadtxt("data/dataP.dat")
dataQ = np.loadtxt("data/dataQ.dat")
# print(dataP)
# print(dataQ)

X = list()
for i in range(len(dataP)):
    X.append([1,dataP[i]])
# print(X)
A = np.transpose(X)@X
b = np.transpose(X)@dataQ
# c0 = np.transpose(np.array([-9.,-7.]))
# c1 = np.transpose(np.array([-10.,-10.]))
# Resol2 = DescenteGradient_POptimal(A, b, c0, 10000, 10**-6)
# Resol = DescenteGradient_Conjugue(A, b, c1, 10000, 10**-6)
# # Tracage graphique
x = np.arange(-10,10,.01)
y = np.arange(-10,10,.01)

xx,yy = np.meshgrid(x,y)

# f = 0.5*(A[0][0]*xx**2 + A[1][1]*yy**2+ 2*A[1][0]*xx*yy +b[0]*xx+b[1]*yy + np.transpose(dataQ)@dataQ)
# h = pp.contour(x,y,f,[50*i**3 for i in range(15)])
# a11,b11 = list(),list()
# for i in range(len(Resol[1])) :
#     print(Resol[1][i])
#     a11.append(Resol[1][i][0])
#     b11.append(Resol[1][i][1])
# # pp.plot(a11,b11,color='cyan')
# pp.show()
def Trace_3d(A,b,c,x,y):
    xx,yy = np.meshgrid(x,y)
    f = 0.5*(A[0][0]*xx**2) 
    f += 0.5*(A[1][1]*yy**2 )
    f += A[1][0]*xx*yy -b[0]*xx-b[1]*yy + c
    fig = pp.figure()
    ax = Axes3D(fig)
    ax.plot_surface(xx,yy,f)
    pp.show()

def Trace_beta(A,b,c,b1,b2,n):
    x,y = np.arange(-10,10,0.01),np.arange(-10,10,0.01)
    xx,yy = np.meshgrid(x,y)
    f = 0.5*(A[0][0]*xx**2 + A[1][1]*yy**2+ 2*A[1][0]*xx*yy) -b[0]*xx-b[1]*yy + c
    # print(f)
    h = pp.contour(x,y,f,[b1+i**4*(b2-b1)/n**4 for i in range(n)])
    if (h == UserWarning) : 
        print("Ces betas n'adment pas de contour !")
    pp.show()
print(b)
# Trace_beta(A,b,np.transpose(dataQ)@dataQ,-10000,10000,10)
Trace_3d(A,b,np.transpose(dataQ)@dataQ,np.arange(-10,10,.01),np.arange(-10,10,.01))




