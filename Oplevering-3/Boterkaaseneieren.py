from collections import Counter


def leesBord(path):
    bord_arr = []
    #   open txt file met bord lees alle lines en verander \n aldus enter
    #   met een lege lijn zodat ze niet opgeslagen worden in de uiteindelijke array.
    with open(path) as bord:
        bord_data = [x.replace("\n", "") for x in bord.readlines()]
    print(bord_data)
    return bord_data


def toonBord(rooster) -> str:
    rooster_arr = []
    for i, row in enumerate(rooster):
        #   voeg elke row toe en replace spaties en X en O met ". " en "X " "O "
        rooster_arr.append(row.replace(" ", ". ").replace("X", "X ").replace("O", "O "))
    #   geef een string terug met goeie changes
    return str('\n'.join(rooster_arr))


def winnaar(rooster) -> str:
    #   twee arrays om index van O en X bij te houden
    player_x = []
    player_o = []
    for index, rows in enumerate(rooster):
        #   als er in een row alleen hetzelfde type heeft aldus X of O dan win je. vb. OOO
        if rows == 'OOO':
            return 'O wint'
        elif rows == 'XXX':
            return 'X wint'
        #   voeg de index (waar de X of O) licht op de rooster
        for index, row in enumerate(rows):
            if row == 'X':
                player_x.append(index)
            elif row == 'O':
                player_o.append(index)
    #   maak dictionaries met counts met gebruik van collections
    x_counter = Counter(player_x)
    o_counter = Counter(player_o)
    #   zoek voor nummer 3 dat betekent dat er 3 van X op dezelfde rij zitten
    for k, v in x_counter.items():
        if v is 3:
            return 'X wint'
    #   zoek voor nummer 3 dat betekent dat er 3 van O op dezelfde rij zitten
    for k, v in o_counter.items():
        if v is 3:
            return 'O wint'
    return 'gelijkspel'


if __name__ == "__main__":
    leesBord('tictactoe1.txt')
    leesBord('tictactoe2.txt')
    leesBord('tictactoe3.txt')
    print(toonBord(['OX ', 'OX ', ' X ']))
    print('"{}"'.format(str(toonBord(['OX ', 'OX ', ' X ']).replace("\n", "\\n"))))
    print(toonBord(['XXO', 'OOX', 'XOX']))
    print(winnaar(['OX ', 'OX ', ' X ']))
    print(winnaar(['OOO', ' XX', 'X  ']))
    print(winnaar(['XXO', 'OOX', 'XOX']))
