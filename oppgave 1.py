import random
import os

SPILLERE_FIL = 'spillere.txt'

def last_spillere():
    """Last spillere fra flat fil."""
    if os.path.exists(SPILLERE_FIL):
        with open(SPILLERE_FIL, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    return []

def lagre_spillere(spillere):
    """Lagre spillere til flat fil."""
    with open(SPILLERE_FIL, 'w', encoding='utf-8') as f:
        for spiller in spillere:
            f.write(spiller + '\n')

def legg_til_spiller(spillere):
    """Legg til en ny spiller."""
    navn = input("Skriv inn spillernavn: ").strip()
    if navn and navn not in spillere:
        spillere.append(navn)
        lagre_spillere(spillere)
        print(f"Spiller '{navn}' lagt til.")
    else:
        print("Ugyldig navn eller allerede finnes.")

def fjern_spiller(spillere):
    """Fjern en spiller."""
    navn = input("Skriv inn spillernavn å fjerne: ").strip()
    if navn in spillere:
        spillere.remove(navn)
        lagre_spillere(spillere)
        print(f"Spiller '{navn}' fjernet.")
    else:
        print("Spiller ikke funnet.")

def vis_spillere(spillere):
    """Vis alle spillere."""
    if spillere:
        print("Spillere:")
        for i, spiller in enumerate(spillere, 1):
            print(f"{i}. {spiller}")
    else:
        print("Ingen spillere registrert.")

def lag_laguttak(spillere):
    """Lag et tilfeldig laguttak for kampen."""
    if len(spillere) < 5:
        print("Trenger minst 5 spillere for å lage laguttak.")
        return

    # Velg 5 spillere til banen
    bane_spillere = random.sample(spillere, 5)
    innbyttere = [p for p in spillere if p not in bane_spillere]

    # Posisjoner: 1 Målvakt, 2 Forsvarere, 2 Angripere
    posisjoner = ['Målvakt'] + ['Forsvarer'] * 2 + ['Angriper'] * 2
    random.shuffle(posisjoner)

    # Tildel posisjoner tilfeldig
    laguttak = list(zip(bane_spillere, posisjoner))

    print("\nLaguttak:")
    for spiller, posisjon in laguttak:
        print(f"{spiller}: {posisjon}")

    if innbyttere:
        print("\nInnbyttere:")
        for innbytter in innbyttere:
            print(innbytter)

def hoved():
    """Hovedmeny løkke."""
    spillere = last_spillere()
    while True:
        print("\n--- Lagstyringsprogram ---")
        print("1. Legg til spiller")
        print("2. Fjern spiller")
        print("3. Vis spillere")
        print("4. Lag laguttak")
        print("5. Avslutt")
        valg = input("Velg et alternativ: ").strip()

        if valg == '1':
            legg_til_spiller(spillere)
        elif valg == '2':
            fjern_spiller(spillere)
        elif valg == '3':
            vis_spillere(spillere)
        elif valg == '4':
            lag_laguttak(spillere)
        elif valg == '5':
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg. Prøv igjen.")

if __name__ == "__main__":
    hoved()