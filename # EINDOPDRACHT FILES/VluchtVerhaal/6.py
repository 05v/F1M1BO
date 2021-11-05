# Stuk 6
stuk7 =  open("stuk7.txt").readlines()
def stuk7_options():
    print("")
    print("[ 7 ] ga slapen, en morgen door")
    print("[ 16 ] probeer eten te vinden")
    print("")

    stuk7_input = input("[?] Maak je keuze: ")

    if stuk7_input == "7":
        exec(open("7.py").read())
    elif stuk7_input == "16":
        exec(open("16.py").read())
    else:
        print("Dat is geen optie.")