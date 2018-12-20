def levensverwachting(geslacht, roker, sport, alcohol, fastfood):
    leeftijd = 70
    if geslacht == 'vrouw':
        leeftijd += 4
    elif geslacht == 'man':
        leeftijd -= 2
    if roker is True:
        leeftijd -= 5
    else:
        leeftijd +=5
    if sport < 1:
        leeftijd -= 3
    else:
        leeftijd += sport
    if alcohol > 7:
        leeftijd -= (alcohol-7)*0.5
    else:
        leeftijd += 2
    if fastfood is False:
        leeftijd += 3
    return leeftijd

if __name__ == "__main__":
    print(levensverwachting('man', True, 2, 10, True))
    print(levensverwachting('man', True, 5, 5, True))
    print(levensverwachting('vrouw', False, 5, 0, False))
    print(levensverwachting('vrouw', False, 3, 14, True))
    print(levensverwachting('man', False, 4, 4, False))
