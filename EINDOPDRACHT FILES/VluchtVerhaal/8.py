# Stuk 8
stuk8 =  open("stuk8.txt").readlines()
def stuk8_options():
    print("")
    print("[ 5 ] verander van gedachte en blijf thuis")
    print("[ 12 ] ga op de vlucht")
    print("")

    stuk8_input = input("[?] Maak je keuze: ")

    if stuk8_input == "5":
        exec(open("5.py").read())
    elif stuk8_input == "12":
        exec(open("12.py").read())
    else:
        print("Dat is geen optie.")

print(*stuk8)
stuk8_options()