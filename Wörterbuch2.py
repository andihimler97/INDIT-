#Wörterbuch Matrix
di = {"apple":"Apfel", "pear":"Birne", "cherry":"Kirsche", "melon":"Melone", "apricot":"Marille", "peach":"Pfirsich"}

print("Welcome to Dictionary2, please select from the following functions")
print("Choose [A] to translate")
print("Choose [B] to add new word")
    

    
correct = False
    
while correct == False:                                             #Eingabe solange bis korrekte Eingabe
    eingabe = input("Enter a function: ")    
    
    if eingabe == "A":
                                                                    #correct = True ---  korrekte Eingabe
        word=input("Please write your word: ")                      #Auslesen der Eingabe
        if word in di:
            print("translation: ",di[word])                         #Übersetzung
        else:
            print('sorry error')
    elif eingabe == "B":
                                                                    #correct = True ----- korrekte Eingabe
        di [input('English word:')] = [input('German translation:')] #durch hinzufügen neuer Wörter wächst das Wörterbuch
        
    else:
        print("wrong answer")
