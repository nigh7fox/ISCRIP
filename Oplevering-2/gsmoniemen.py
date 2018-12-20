import time


def T9(woord) -> str:
    #   dictionary van de keypad van een gsm
    upper_keys_dict = {2: 'ABC', 3:'DEF', 4:'GHI', 5:'JKL', 6:'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ'}
    lower_keys_dict = {2: 'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    answer = []
    #   kijk in uppercase letters als de letter uppercase is anders lowercase
    for letter in woord:
        if letter.isupper():
            #   loop door de dictionary en kijk of de letter in een van de values zit
            #   in python zijn strings iterable dus geburik je if X in Y
            for key,values in upper_keys_dict.items():
                if letter in values:
                    answer.append(key)
        else:
            for key,values in lower_keys_dict.items():
                if letter in values:
                    answer.append(key)
    #   maak van de array een string
    answer = ''.join([str(x) for x in answer])
    return answer


def GSMoniemen(woord_1, woord_2) -> bool:
    #   als de eerste woord en de tweede woord dezelfde answer hebben return true
    return T9(woord_1) == T9(woord_2)


if __name__ == "__main__":
    print(T9('Hallo'))
    print(T9('aanbod'))
    print(T9('bamboe'))
    print(GSMoniemen('aanbod', 'bamboe'))
    print(GSMoniemen('maandag', 'vrijdag'))
