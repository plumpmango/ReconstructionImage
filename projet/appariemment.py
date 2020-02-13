import numpy as np
import sys

def eqm(bloc1,bloc2):
    l,h,c = bloc1.shape
    coefRGB = np.power((bloc2-bloc1),2)
    e = np.sum(coefRGB)
    EQM = e / (l*h*c)
    return EQM

def calculMeilleurBloc(windowIm1,bloc2):
    errqm = float("inf")
    lig,col,c1 = windowIm1.shape
    ligBloc,colBloc,c2 = bloc2.shape
    blocf = np.zeros((ligBloc,colBloc))
    for i in range(4,lig-4):
        for j in range(4,col-4):
            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            bloctmp = windowIm1[i-4:i+4,j-4:j+4,:]
            errCur = eqm(bloctmp,bloc2)
            if errqm > errCur :
                errqm = errCur
                blocf = bloctmp
    return blocf

def rechercheExhaustive(im1,im2,window):
    #parcours par fenetre 16*16
    t = window/2
    l,h,c = im1.shape
    im2C = np.zeros((l,h,c))
    for i in range(t,l-t,t):
        for j in range(t,h-t,t):
            # blocIm2 = [i-4:i+4][j-4:j+4]
            voisinIm1 = im1[i-t:i+t,j-t:j+t,:]
            blocIm2 = im2[i-4:i+4,j-4:j+4,:]
            im2C[i-4:i+4,j-4:j+4,:] = calculMeilleurBloc(voisinIm1,blocIm2)
            # print(str(i) + "," +str(j)+"\n")

    return im2C

def calculerH(dx,dy,dxdy,i,j):
    a = dx[i-1:i+1,j-1:j+1]
    A = sum(a)
    B = sum(dy[i-1:i+1,j-1:j+1])
    C = sum(dxdy[i-1:i+1,j-1:j+1])

    H = np.array([[A, B]; [B, C]])

    return H

def calculerb(dxdt,dydt,i,j):
    bx = sum(dxdt[i-1:i+1,j-1:j+1])
    by = sum(dydt[i-1:i+1,j-1:j+1])

    b = np.array([bx; by])
    return b

def lucasKanade(im1,Iim2):
    l,h,c = im1.shape

    # Gradient
    dx = np.zeros((l,h,c))
    dy = np.zeros((l,h,c))

    for j in range(2,h):
        dx[:,j] = im1[:,j,:]-im1[:,j-1,:]

    for i in range(2,l):
        dy[i,:] = im1[i,:]-im1[i-1,:]

    dxdt = (im2-im1)*dx
    dydt = (im2-im1)*dy
    dx = np.power(dx,2)
    dy = np.power(dy,2)

    xx,dxdy = np.gradient(dx)

    imS = np.zeros(l,h,2,1)

    for i in range(2,l):
        for j in range(2,h):
            H = calculerH(dx,dy,dxdy,i,j)
            b = calculerb(dxdt,dydt,i,j)
            vp,vectp = abs(np.linalg.eig(H))
            v = np.linalg.lstsq(H,b)
            imS[i,j,:,:] = v

    return imS
