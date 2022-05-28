meine_liste = ["ich bin", "ein", "string in einer", "liste"]
zahlenliste = [1,2,3,4,5]


for element in meine_liste:
    print(element)
    
for i in range(0, 10, 1):
    print(i)
    
teilliste = meine_liste[1:3]
print(teilliste)

teilliste = zahlenliste[:4:2]
print(teilliste)

