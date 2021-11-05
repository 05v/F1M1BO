# Stuk 3
stuk3 =  open("stuk3.txt").readlines()
def stuk3_options():
    print("")
    print("[ 2 ] de tralies langzaam weg te snijden aan de buitenkant ( zodat de bewakers je niet zien)")
    print("[ 14 ] een van de bewakers neer te steken")
    print("")

    stuk3_input = input("[?] Maak je keuze: ")

    if stuk3_input == "2":
        exec(open("2.py").read())
    elif stuk3_input == "":
        exec(open("14.py").read())
    else:
        print("Dat is geen optie.")

print(*stuk3)
stuk3_options()