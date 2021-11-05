# Stuk 2
stuk2 =  open("stuk2.txt").readlines()
def stuk2_options():
    print("")
    print("[ 8 ] er een nachtje over slapen")
    print("[ 3 ] nu actie nemen en meedoen aan de protesten")
    print("")

    stuk2_input = input("[?] Maak je keuze: ")

    if stuk2_input == "6":
        exec(open("6.py").read())
    elif stuk2_input == "5":
        exec(open("5.py").read())
    else:
        print("Dat is geen optie.")

print(*stuk2)
stuk2_options()