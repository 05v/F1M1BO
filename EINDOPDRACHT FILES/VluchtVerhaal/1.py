# Stuk 1
stuk1 =  open("stuk1.txt").readlines()
def stuk1_options():
    print("")
    print("[ 8 ] er een nachtje over slapen")
    print("[ 3 ] nu actie nemen en meedoen aan de protesten")
    print("")

    stuk1_input = input("[?] Maak je keuze: ")

    if stuk1_input == "8":
        exec(open("8.py").read())
    elif stuk1_input == "3":
        exec(open("3.py").read())
    else:
        print("Dat is geen optie.")

print(*stuk1)
stuk1_options()