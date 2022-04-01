#Programm, das in 10° - Schritten 0° und 180° den jew. Cosinus-Wert berechnet und ausgibt

import math      #import math lib


winkel_grad = 0              #Laufvariable

while (True):    #beginn Schleife
    
    winkel = winkel_grad *(math.pi/180)        #umrechnung in Rad
    
    print("cos(" , winkel_grad , ")" ,round(math.cos(winkel),4))   #berechnung Winkel und runden 
    
    winkel_grad += 10      #ändern der Laufvariable
    
    if winkel_grad == 190:    
        break      #Ende der Schleife
    

