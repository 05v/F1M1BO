# Stuk 16
stuk16 =  open("stuk16.txt").readlines()
def stuk16_options():
    print("")
    print("[ 12 ] ga naar het dorp toe")
    print("[ 7 ] blijf doorlopen door het bos")
    print("")

    stuk16_input = input("[?] Maak je keuze: ")

    if stuk16_input == "12":
        exec(open("12.py").read())
    elif stuk16_input == "7":
        exec(open("7.py").read())
    else:
        print("Dat is geen optie.")