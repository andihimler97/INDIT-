#Aufgabe: Wörter in DE--> EN

woerterbuch ={"Apfel":"apple", "Birne":"pear", "Kirsche": "cherry", "Melone":"melon", "Marille":"apricot", "Pfirsich":"peach"}


wort = input("Bitte Obstsorte auf Deutsch eingeben:")

i= 0
a= len(woerterbuch)

while i < a:
    if woerterbuch[i] == wort:
        print( "Übersetzung: " , woerterbuch[i])
        break
    i += 1
        
if i == a:
    print("Wort nicht im Wörterbuch vorhanden")
    
            


    
