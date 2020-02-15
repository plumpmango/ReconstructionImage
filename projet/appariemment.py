import numpy as np
import sys
import math
import os

def eqm(bloc1,bloc2):
    l,h,c = bloc1.shape
    coefRGB = np.power((bloc2-bloc1),2)
    e = np.sum(coefRGB)
    EQM = e / (l*h*c)
    return EQM

#Recherche exhaustive
def calculMeilleurBloc1(windowIm1,bloc2):
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

def reconstruction(im1,im2,window,N):
    #parcours par fenetre 16*16
    t = window/2
    l,h,c = im1.shape
    im2C = np.zeros((l,h,c))
    for i in range(t,l-t,t):
        for j in range(t,h-t,t):
            # blocIm2 = [i-4:i+4][j-4:j+4]
            voisinIm1 = im1[i-t:i+t,j-t:j+t,:]
            blocIm2 = im2[i-4:i+4,j-4:j+4,:]
            im2C[i-4:i+4,j-4:j+4,:] = globals()['calculMeilleurBloc' + str(N)](voisinIm1,blocIm2)
            # print(str(i) + "," +str(j)+"\n")

    return im2C

#Recherche log2
def calculMeilleurBloc2(window,block):
    errqm = float("inf")
    windowSize = len(window)
    blockSize = len(block)
    midX = windowSize/2
    midY = windowSize/2
    pas = windowSize/4
    while pas >= 1:

        xL = midX-blockSize/2
        xR = midX+blockSize/2
        indexLineLeft =  [xL,xL,xL-pas,xL+pas,xL]
        indexLineRight = [xR,xR,xR-pas,xR+pas,xR]

        yL = midY-blockSize/2
        yR = midY+blockSize/2
        indexColumnLeft = [yL-pas,yL+pas,yL,yL,yL]
        indexColumRight = [yR-pas,yR+pas,yR,yR,yR]

        for i in range(0,len(indexLineLeft)):
            if (indexLineLeft[i] < 0) or (indexColumnLeft[i] < 0) or (indexLineRight[i] >= windowSize) or (indexColumRight[i] >= windowSize):
                continue

            temp = window[indexLineLeft[i]:indexLineRight[i],indexColumnLeft[i]:indexColumRight[i],:]
            tempEqm =  eqm(temp,block)

			#bloc gauche
            if tempEqm < errqm and i == 0:
                errqm = tempEqm
                res = temp
                midY = midY-pas
                break

			#bloc droite
            if tempEqm < errqm and i ==1:
                errqm = tempEqm
                res = temp
                midY=midY+pas
                break

			#bloc haut
            if tempEqm < errqm and i == 2:
                errqm = tempEqm
                res = temp
                midX = midX-pas
                break

			#bloc bas
            if tempEqm < errqm and i == 3:
                errqm = tempEqm
                res = temp
                midX = midX+pas
                break

			#bloc mid
            if tempEqm <= errqm and i == 4:
                errqm = tempEqm
                res = temp
                pas = pas/2
                break
    return(res)

#LUKas et Kanade
def calculerH(dx,dy,dxdy,i,j):
    A = sum(sum(sum(dx[i-1:i+1,j-1:j+1])))
    B = sum(sum(sum(dy[i-1:i+1,j-1:j+1])))
    C = sum(sum(sum(dxdy[i-1:i+1,j-1:j+1])))

    H = np.array([[A, B], [B, C]])

    return H

def calculerb(dxdt,dydt,i,j):
    bx = sum(sum(sum(dxdt[i-1:i+1,j-1:j+1])))
    by = sum(sum(sum(dydt[i-1:i+1,j-1:j+1])))

    b = np.array([bx, by])
    return b

def lukasKanade(im1,im2):
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

    dxdy = np.gradient(dx)[1]

    imS = np.zeros((l,h,2,))

    for i in range(1,l-8,8):
        for j in range(1,h-8,8):
            H = calculerH(dx,dy,dxdy,i,j)
            b = calculerb(dxdt,dydt,i,j)
            vp = np.linalg.eig(H)[0]
            if (vp[0] > 0.1) and (vp[1] > 0.1) :
                v = abs(np.linalg.lstsq(H,b)[0])
            else:
                v = np.zeros((2,))
            imS[i,j,:] = v

    return imS

def calculerIm(im1,im2,deltaIm):
    l,h,c = im1.shape
    # print im1.shape
    # newIm = np.zeros((l,h,c))
    newIm = im1
    for i in range(1,l-8,8):
        for j in range(1,h-8,8):
            # print type(deltaIm[0])
            indX = abs(int(math.floor(i-deltaIm[i,j,0])))
            indY = abs(int(math.floor(j-deltaIm[i,j,1])))

            if indX > l :
                indX = l-1
            if indX < 1 :
                indX = 1

            if indY < 1 :
                indY = 1
            if indY > h :
                indY = h-1

            newIm[i-1:i+1,j-1:j+1,:] = im2[indX-1:indX+1,indY-1:indY+1,:]

    return newIm

def casLK(img1,img2):
    deltaIm = lukasKanade(img1,img2);
    # print deltaIm.shape
    newIm = calculerIm(img2,img1,deltaIm)
    return newIm
