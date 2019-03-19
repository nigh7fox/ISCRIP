from random import randint


def vullen(getal) -> list:
    urne_lijst = []
    for x in range(0, getal):
        random_number = randint(1, 2)
        if random_number is 1:
            urne_lijst.append("wit")
        else:
            urne_lijst.append("zwart")
    return urne_lijst


def kiezen(lijst) -> tuple:
    return tuple([randint(0, len(lijst)-1), randint(0, len(lijst)-1)])


def verwijderen(pos1, pos2, lijst) -> list:
    if lijst[pos1] == "zwart" and lijst[pos2] == "zwart":
        lijst.append("zwart")
        lijst.pop(pos1)
        lijst.pop(pos2)
    elif lijst[pos1] == "zwart" and lijst[pos2] == "wit" or lijst[pos1] == "wit" and lijst[pos2] == "zwart":
        lijst.append("wit")
        lijst.pop(pos1)
        lijst.pop(pos2)
    elif lijst[pos1] == "wit" and lijst[pos2] == "wit":
        lijst.append("zwart")
        lijst.pop(pos1)
        lijst.pop(pos2)
    return lijst


def laatste(lijst) -> str:
    urne = lijst
    while len(urne) > 1:
        knikker1, knikker2 = kiezen(urne)
        verwijderen(knikker1, knikker2, urne)
        if len(urne) == 1:
            laatste = urne[0]
    return laatste


if __name__ == "__main__":
    urne = vullen(10)
    print(urne)
    knikker1, knikker2 = kiezen(urne)
    print(knikker1, knikker2)
    verwijderen(knikker1, knikker2, urne)
    print(urne)
    print(laatste(urne))
