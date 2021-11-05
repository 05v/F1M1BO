# Stuk 4
stuk4 =  open("stuk4.txt").readlines()
def stuk4_options():
    print("")
    print("[ 10 ] ga met hem mee")
    print("[ 20 ] wens hem succes en ga naar de moskee")
    print("")

    stuk4_input = input("[?] Maak je keuze: ")

    if stuk4_input == "10":
        exec(open("10.py").read())
    elif stuk4_input == "20":
        exec(open("20.py").read())
    else:
        print("Dat is geen optie.")