from random import randint

#   lijst vullen met willekeurige zwart of wit, met lengte getal
def vullen(getal) -> list:
    urne_lijst = []
    for x in range(0, getal):
        #   randint gebruiken om een willekeurige nummer te vinden
        random_number = randint(1, 2)
        #   als de nummer 1 is voeg een wit toe, anders zwart
        #   randint gaat van 1 naar 2 dus 50%
        if random_number is 1:
            urne_lijst.append("wit")
        else:
            urne_lijst.append("zwart")
    return urne_lijst


def kiezen(lijst) -> tuple:
    #   maak een tuple met twee willekeurige cijfers
    #   de cijfers beginnen bij 0 en mag tot de lengte van de lijst gaan
    return tuple([randint(0, len(lijst)-1), randint(0, len(lijst)-1)])


def verwijderen(pos1, pos2, lijst) -> list:
    #   eerste regel van het spel
    if lijst[pos1] == "zwart" and lijst[pos2] == "zwart":
        lijst.append("zwart")
        lijst.pop(pos1)
        lijst.pop(pos2)
    #   tweede regel van het spel
    elif lijst[pos1] == "zwart" and lijst[pos2] == "wit" or lijst[pos1] == "wit" and lijst[pos2] == "zwart":
        lijst.append("wit")
        lijst.pop(pos1)
        lijst.pop(pos2)
    #   derde regel van het spel
    elif lijst[pos1] == "wit" and lijst[pos2] == "wit":
        lijst.append("zwart")
        lijst.pop(pos1)
        lijst.pop(pos2)
    #   we gebruiken pop om via de index een item te verwijderen van lijst
    return lijst


def laatste(lijst) -> str:
    #   we mogen de doorgevoerde lijst niet wijzigen
    urne = lijst
    #   ga door totdat de lijst lengte 1 is, daan zit er maar nog 1
    #   knikker in de vaas
    while len(urne) > 1:
        #   spelen
        knikker1, knikker2 = kiezen(urne)
        verwijderen(knikker1, knikker2, urne)
        #   als lengte 1 is (laatste knikker) pak de waarde van
        #   index 0 in de urne
        if len(urne) == 1:
            laatste = urne[0]
    #   geef laatste waarde terug in vorm van een string
    return laatste


if __name__ == "__main__":
    urne = vullen(10)
    print(urne)
    knikker1, knikker2 = kiezen(urne)
    print(knikker1, knikker2)
    verwijderen(knikker1, knikker2, urne)
    print(urne)
    print(laatste(urne))
