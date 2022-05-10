def eingabe():
    correct = False
    while correct == False:
        v_str = input("Radius: ")
        try:
            v = float(v_str)
            if v > 0:
                correct = True
            else:
                print("Eingabe ist ungültig (v <= 0)")
        except ValueError:
                print(" Eingabe ist ungültig (keine Zahl)")
    return v

def kreisumfang(radius):
    umfang = 2*radius*3.14159265
    return umfang

kreisradius = eingabe()
print("eingegebener Radius: ", kreisradius)

umfang = kreisumfang(kreisradius)
print("Kreisumfang: ", umfang)