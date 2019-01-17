def vierkant(cells, n=1) -> [[]]:
    answer = []
    curr_cells = []
    #   add first row
    for y in range(cells):
        curr_cells.append(n)
    for cell in range(cells):
        #   begin bij de eerste cell en verander de current naar de nieuwe cell als laats/
        new_cells = [n]
        #   voor alle cijfers in de grote van de cells(gegeven) voeg een nieuwe cijfer toe
        #   waarbij de cijfer gelijk is aan de (index + 1) + new_cells[index]
        #   hier doen we de kruis plus -> [x+1] naar x == nieuwe cijfer
        for x in range(cells-1):
            new_cells.append(curr_cells[x+1] + new_cells[x])
        #   voeg nieuwe cijfers toe aan antwoord
        answer.append(curr_cells)
        #   ga een stap verder en verander de current_cells met de nieuwe voor volgende
        #   stap in de for loop
        curr_cells = new_cells
    return answer


def paden(rijen, n=1) -> str:
    #   we hebben een methode al gemaakt om vierkant van pascal te berekenen
    vierkanten = vierkant(rijen, n)
    antwoord = ""
    #   pak de laatste row in de lijst
    last_row = vierkanten[rijen - 1]
    #   pak laatste cijfer van dat lijst
    last_number_width = len(str(last_row[rijen-1])) + 1
    for rij in vierkanten:
        for i, cijfers in enumerate(rij):
            #   gebruik .format samen met align en width om de cijfers mooi
            #   onder elkaar te plaatsen aan de hand van de laatste cijfer
            antwoord += '{:{align}{width}}'.format(str(cijfers), align='>', width=last_number_width)
            if i == len(rij)-1:
                #   voeg een enter toe aan bij het laatste cijfer
                antwoord += "\n"
    return antwoord

if __name__ == "__main__":
    print(vierkant(3))
    print(vierkant(3, 100))
    print(vierkant(4))
    print(paden(3))
    print(paden(3, 100))
    print(paden(4))
    print(paden(6))
    print(paden(8))
    print(paden(10))
