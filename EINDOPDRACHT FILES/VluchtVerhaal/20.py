# Stuk 20
stuk20 =  open("stuk20.txt").readlines()
def stuk20_options():
    print("")
    print("[ 18 ] ga met hun mee")
    print("[ 3 ] blijf hier")
    print("")

    stuk20_input = input("[?] Maak je keuze: ")

    if stuk20_input == "18":
        exec(open("18.py").read())
    elif stuk20_input == "3":
        exec(open("3.py").read())
    else:
        print("Dat is geen optie.")