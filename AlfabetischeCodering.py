def geldigeSleutel(woord) -> bool:
    #   als de type van woord een int is return dan False
    if type(woord) is int:
        return False
    #   als de lengte van de woord en de lengte van een set van woord gelijk is aan 26
    #   dan zijn er alleen unique letters in woord en is het geldig.
    #   set geeft alleen unique waardes
    if len(woord) is 26 and len(woord) == len(set(woord)):
        return True
    return False


def codeer(woord, sleutel) -> str:
    #   magic
    new_woord = ""
    #   normale alfabet
    alfabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    #   index lijst
    letter_indexes = []
    #   voor elke letter in woord zet de index van elke letter in een lijst
    for letter in woord:
        letter_indexes.append(alfabet.index(letter))
    if geldigeSleutel(sleutel):
        #   niewe woord is gelijk aan de index van de letter in een normale alfabet
        #   ingevuld in de index van de sleutel, aldus B -> 2 in sleutel is index 2 -> f
        for indexes in letter_indexes:
            new_woord += sleutel[indexes]
    else:
        #   als de sleutel ongeldig is.
        raise AssertionError('Ongeldige Sleutel')
    return new_woord


def alfabetisch(woord) -> bool:
    alfabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    for i, letters in enumerate(woord):
        # als index van 't woord bij de voorlaatste letter komt wordt de laatste check gedaan
        # want elke cycle doen we ook index + 1 om de volgende index te krijgen
        if i is len(woord)-1:
            return True
        #   pak de index van i nu en de volgende i
        current_letter_index = alfabet.index(woord[i])
        next_letter_index = alfabet.index(woord[i+1])
        #   als i groter is dan i+1 (aldus index in de alfabet)
        #   dan is de woord niet op alfabetische volgorde
        if current_letter_index > next_letter_index:
            return False
    #   anders wel
    return True


def score(sleutel, bestand) -> int:
    return 0


if __name__ == "__main__":
    print(geldigeSleutel('jfbqpwcvuamozhilgrxtkndesy'))
    print(geldigeSleutel('jfbqpwcxvuamozhilgrxtkndesy'))
    print(geldigeSleutel('jfbqpwvuamozhilgrxtkndesy'))
    print(geldigeSleutel('jfbqpwxvuamozhilgrxtkndesy'))
    print(geldigeSleutel(123456789))

    print(codeer('bakker', 'jfbqpwcvuamozhilgrxtkndesy'))
    print(codeer('slager', 'jfbqpwcvuamozhilgrxtkndesy'))
    print(codeer('bullet', 'jfbqpwcvuamozhilgrxtkndesy'))
    # print(codeer('bakker', 'jfbqpwcvuamozhilgrxakndesy'))

    print(alfabetisch('bakker'))
    print(alfabetisch('fjmmpr'))
    print(alfabetisch('bullet'))
    print(alfabetisch('fkoopt'))

    print(score('jfbqpwcvuamozhilgrxtkndesy', 'zes-letter-woorden.txt'))
    print(score('idsxvaqtobuefpgcjwzrkmhnyl', 'zes-letter-woorden.txt'))
