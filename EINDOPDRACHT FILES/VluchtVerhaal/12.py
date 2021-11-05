# Stuk 12
stuk12 =  open("stuk12.txt").readlines()
def stuk12_options():
    print("")
    print("[ 20 ] de moskee")
    print("[ 4 ] je beste vriend zijn huis")
    print("")

    stuk12_input = input("[?] Maak je keuze: ")

    if stuk12_input == "20":
        exec(open("20.py").read())
    elif stuk12_input == "4":
        exec(open("4.py").read())
    else:
        print("Dat is geen optie.")

print(*stuk12)
stuk12_options()