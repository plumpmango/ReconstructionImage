import cv2 as cv
import numpy as np
import time
import os
import appariemment as ap
import matplotlib.pyplot as plt



kaamelott1 = cv.imread('./images/kaamelott1.jpeg')
kaamelott2 = cv.imread('./images/kaamelott2.jpeg')

kaa1 = cv.imread('./images/kaa1.jpeg')
kaa2 = cv.imread('./images/kaa2.jpeg')


desert = cv.imread('./images/desert.jpeg')
desert2 = cv.imread('./images/desert2.jpeg')

friends1 = cv.imread('./images/friends1.jpeg')
friends2 = cv.imread('./images/friends2.jpeg')

westworld1 = cv.imread('./images/westworld1.jpeg')
westworld2 = cv.imread('./images/westworld2.jpeg')


#Recherche exhaustive

window = 16

result = ap.reconstruction(kaamelott1,kaamelott2,window,1)
cv.imwrite('./result.jpeg',result)

result2 = ap.reconstruction(kaa1,kaa2,window,1)
cv.imwrite('./result2.jpeg',result2)

result3 = ap.reconstruction(desert,desert2,window,1)
cv.imwrite('./result3.jpeg',result3)

resultfriends = ap.reconstruction(friends1,friends2,window,1)
cv.imwrite('./resultfriends.jpeg',resultfriends)

resultwestworld = ap.reconstruction(westworld1,westworld2,window,1)
cv.imwrite('./resultwestworld.jpeg',resultwestworld)

result = cv.imread('./result.jpeg')
result2 = cv.imread('./result2.jpeg')
result3 = cv.imread('./result3.jpeg')
resultfriends = cv.imread('./resultfriends.jpeg')
resultwestworld = cv.imread('./resultwestworld.jpeg')

print "Erreur quadratique moyenne kaamelott 1 : " + str(ap.eqm(kaamelott2,result))
print "Erreur quadratique moyenne kaamelott 2 : " + str(ap.eqm(kaa2,result2))
print "Erreur quadratique moyenne kaamelott 3 : " + str(ap.eqm(desert2,result3))
print "Erreur quadratique moyenne friends : " + str(ap.eqm(friends2,resultfriends))
print "Erreur quadratique moyenne westworld : " + str(ap.eqm(westworld2,resultwestworld))



#Recherche en log2
resultLog2 = ap.reconstruction(kaamelott1,kaamelott2,16,2)
cv.imwrite('./resultLog2.jpeg',resultLog2)

result2Log2 = ap.reconstruction(kaa1,kaa2,16,2)
cv.imwrite('./result2Log2.jpeg',result2Log2)

result3Log2 = ap.reconstruction(desert,desert2,16,2)
cv.imwrite('./result3Log2.jpeg',result3Log2)

resultfriendsLog2 = ap.reconstruction(friends1,friends2,16,2)
cv.imwrite('./resultfriendsLog2.jpeg',resultfriendsLog2)


resultwestworldLog2 = ap.reconstruction(westworld1,westworld2,16,2)
cv.imwrite('./resultwestworldLog2.jpeg',resultwestworldLog2)


resultLog2 = cv.imread('./resultLog2.jpeg')
result2Log2 = cv.imread('./result2Log2.jpeg')
result3Log2 = cv.imread('./result3Log2.jpeg')
resultfriendsLog2 = cv.imread('./resultfriendsLog2.jpeg')
resultwestworldLog2 = cv.imread('./resultwestworldLog2.jpeg')

print "Erreur quadratique moyenne kaamelott 1 : " + str(ap.eqm(kaamelott2,resultLog2))
print "Erreur quadratique moyenne kaamelott 2 : " + str(ap.eqm(kaa2,result2Log2))
print "Erreur quadratique moyenne kaamelott 3 : " + str(ap.eqm(desert2,result3Log2))
print "Erreur quadratique moyenne friends : " + str(ap.eqm(friends2,resultfriendsLog2))
print "Erreur quadratique moyenne westworld : " + str(ap.eqm(westworld2,resultwestworldLog2))


#Lukas et kanade
resultLK = ap.casLK(kaamelott1,kaamelott2)
cv.imwrite('./resultLKv2.jpeg',resultLK)

resultLK2 = ap.casLK(kaa1,kaa2)
cv.imwrite('./resultLK2v2.jpeg',resultLK2)

resultLK3 = ap.casLK(desert,desert2)
cv.imwrite('./resultLK3v2.jpeg',resultLK3)

resultLKfriends = ap.casLK(friends1,friends2)
cv.imwrite('./resultLKfriendsv2.jpeg',resultLKfriends)

resultLKwestworld = ap.casLK(westworld1,westworld2)
cv.imwrite('./resultLKwestworldv2.jpeg',resultLKwestworld)



# resultLK = cv.imread('./resultLKv2.jpeg')
# resultLK2 = cv.imread('./resultLK2v2.jpeg')
# resultLK3 = cv.imread('./resultLK3v2.jpeg')
# resultLKfriends = cv.imread('./resultLKfriendsv2.jpeg')
# resultLKwestworld = cv.imread('./resultLKwestworldv2.jpeg')


print "Erreur quadratique moyenne kaamelott 1 : " + str(ap.eqm(kaamelott2,resultLK))
print "Erreur quadratique moyenne kaamelott 2 : " + str(ap.eqm(kaa2,resultLK2))
print "Erreur quadratique moyenne kaamelott 3 : " + str(ap.eqm(desert2,resultLK3))
print "Erreur quadratique moyenne friends : " + str(ap.eqm(friends2,resultLKfriends))
print "Erreur quadratique moyenne westworld : " + str(ap.eqm(westworld2,resultLKwestworld))
