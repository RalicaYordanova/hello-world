##################################################################
# 24.04.2015 Created by Ralica Yordanova                         #
##################################################################

goal = int(raw_input("Geben Sie eine Zahl von 1 bis 100 ein! \t"))
print goal


autoversuch = 50
print "Autoversuch: \t", autoversuch

lower = 0
upper = 100


while (autoversuch != goal):
    if (autoversuch < goal):
        print autoversuch
        print "Ich brauche eine Zahl groesser", autoversuch
        lower = autoversuch
        autoversuch = (upper + autoversuch) / 2
    else:
        print autoversuch
        print "Ich brauche eine Zahl kleiner", autoversuch
        upper = autoversuch
        autoversuch = (lower + autoversuch) / 2
        
        
print "Richtig: ", autoversuch


