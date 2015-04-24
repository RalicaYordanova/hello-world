##################################################################
# 24.04.2015 Created by Ralica Yordanova                         #
##################################################################

ziel = int(raw_input("Geben Sie eine Zahl von 1 bis 100 ein! \t"))
print ziel

unterschranke = 0
oberschranke = 100

autoversuch = (unterschranke + oberschranke) / 2
print "Autoversuch: \t", autoversuch


while (autoversuch != ziel):
    if (autoversuch < ziel):
        print autoversuch
        print "Ich brauche eine Zahl groesser", autoversuch
        unterschranke = autoversuch
        autoversuch = (oberschranke + autoversuch) / 2
    else:
        print autoversuch
        print "Ich brauche eine Zahl kleiner", autoversuch
        oberschranke = autoversuch
        autoversuch = (unterschranke + autoversuch) / 2
        
        
print "Richtig: ", autoversuch


