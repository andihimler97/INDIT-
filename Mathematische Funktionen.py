
wert1 = float(input("Bitte wert1 eingeben: "))
wert2 = float(input("Bitte wert2 eingeben: "))

def fsumme(wert1, wert2):
    summe = wert1 + wert2
    return summe

def fdifferenz(wert1, wert2):
    differenz = wert1 - wert2
    return differenz
def fprodukt(wert1, wert2):
    produkt = wert1 * wert2
    return produkt

def fquotient(wert1, wert2):
    if wert2 == 0:
        print("Mathematisch unmöglich")
    quotient = wert1 / wert2
    return quotient

output1 = fsumme(wert1, wert2)
output2 = fdifferenz(wert1, wert2)
output3 = fprodukt(wert1, wert2)
output4 = fquotient(wert1, wert2)

print ("Summe: ", output1)
print ("Differenz: ", output2)
print ("Produkt: ", output3)
print ("Quotient: ", output4)