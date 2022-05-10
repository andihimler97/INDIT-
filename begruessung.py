namen = ["Franz", "Sven", "Andi", "Anna", "Lukas"]

def begruessung(name):
    print("Servus" , name)
    print("Es freut mich das du heute dabei bist")
    print("Ich wünsche dir viel Spaß mit dem Programm")
    return

def begruessung2(namensliste):
    for ein_name in namensliste:
        print("Servus" , ein_name)
        print("Es freut mich das du heute dabei bist")
        print("Ich wünsche dir viel Spaß mit dem Programm")
    return

print ("Version 1")
for name in namen:
    begruessung(name)
    
print ("Version 2")
begruessung2(name) 