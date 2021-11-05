# Stuk 18
stuk18 =  open("stuk18.txt").readlines()
def stuk18_options():
    print("")
    print("[ 19 ] blijf in Hongarije en bouw een leven op")
    print("[ 21 ] ga naar Nederland")
    print("")

    stuk18_input = input("[?] Maak je keuze: ")

    if stuk18_input == "19":
        exec(open("19.py").read())
    elif stuk18_input == "21":
        exec(open("21.py").read())
    else:
        print("Dat is geen optie.")