def schrikkeljaar(num):
    #   In psuedo code -> return de string schrikkeljaar,
    #   Als de module van 4 gelijk is aan nul (dus is deelbaar door 4) EN!
    #   Is ook deelbaar door 400.
    #   Anders geef de string niet schrikkeljaar terug.
    return 'Schrikkeljaar' if num % 4 == 0 and num % 400 == 0 else 'Niet Schrikkeljaar'


if __name__ == '__main__':
    print(schrikkeljaar(1800))
