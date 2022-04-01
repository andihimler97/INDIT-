
i = 0                                              #Laufvariable 
floatPi = 0                                        #Brechnungsvariable
summe = 0                                          #Variable für Reihensumme


strTerme = input("Anzahl der Terme eingeben: ")    #Eingabe Funktion
floatTerme = float(strTerme)                       

while i <= floatTerme:                             #while-Schleife
    floatPi = ((-1)** i)/ (2*i+1)                  #Leibniz Formel
    summe += floatPi                               #entspricht summe = summe + floatPi
    i += 1                                         #Laufvariable wird erhöht


print("Pi :", summe*4)                             #Ausgabe Ergebnis (Pi/4)