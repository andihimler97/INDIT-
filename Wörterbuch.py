#Aufgabe: Wörter in DE--> EN

woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]

woerterbuch_englisch = ["apple", "pear", "cherry", "melon", "apricot", "peach"]


wort = input("Bitte Obstsorte auf Deutsch eingeben:")

i= 0
a= len(woerterbuch_deutsch)

while i < a:
    if woerterbuch_deutsch[i] == wort:
        print( "Übersetzung: " , woerterbuch_englisch[i])
        break
    i += 1
        
if i == a:
    print("Wort nicht im Wörterbuch vorhanden")
    
            


    
