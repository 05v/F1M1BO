# Stuk 10
stuk10 =  open("stuk10.txt").readlines()
def stuk10_options():
    print("")
    print("[ 3 ] blijf hier")
    print("[ 18 ] probeer te vluchten")
    print("")

    stuk10_input = input("[?] Maak je keuze: ")

    if stuk10_input == "3":
        exec(open("3.py").read())
    elif stuk10_input == "18":
        exec(open("18.py").read())
    else:
        print("Dat is geen optie.")