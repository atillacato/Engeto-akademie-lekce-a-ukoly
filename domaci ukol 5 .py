pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]

while pismena:
    print(", ".join(pismena))

    zadani = input("Ktere písmeno chceš vyhodit?")

    if zadani not in pismena:
        print(zadani + " není součástí písmen!")
    else:
        pismena.remove(zadani)

print("Konec hry!")