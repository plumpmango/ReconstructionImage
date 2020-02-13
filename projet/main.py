import cv2 as cv
import numpy as np
import time
import os
import appariemment as ap
import matplotlib.pyplot as plt


def ecrireImageFichier(img,nomFic):
    l,h = img.shape
    fichier = open(nomFic,"a")
    for i in range(0,l):
        for j in range(0,h):
            fichier.write(str(img2[i][j]) + " ")
        fichier.write("\n")

kaamelott1 = cv.imread('./images/kaamelott1.jpeg')
kaamelott2 = cv.imread('./images/kaamelott2.jpeg')

kaa1 = cv.imread('./images/kaa1.jpeg')
kaa2 = cv.imread('./images/kaa2.jpeg')


desert = cv.imread('./images/desert.jpeg')
desert2 = cv.imread('./images/desert2.jpeg')

friends1 = cv.imread('./images/friends1.jpeg')
friends2 = cv.imread('./images/friends2.jpeg')

westworld1 = cv.imread('./images/kaa1.jpeg')
westworld2 = cv.imread('./images/kaa2.jpeg')

result = cv.imread('./result.jpeg')
result2 = cv.imread('./result2.jpeg')
result3 = cv.imread('./result3.jpeg')
resultfriends = cv.imread('./resultfriends.jpeg')
resultwestword = cv.imread('./resultwestworld.jpeg')

window = 16
# result = ap.rechercheExhaustive(img1,img2,window)
# ecrireImageFichier(result,"result.txt")
# print "over"
# cv.imwrite('./resultwestworld.jpeg',result)
# cv.waitKey(20000)

print "Erreur quadratique moyenne kaamelott 1 : " + str(ap.eqm(friends1,resultfriends))

# cv.destroyAllWindows()
