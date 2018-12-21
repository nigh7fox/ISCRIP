# klopt niet
def vertaal(word, vertaling):
    new_word = ""
    if word.isupper():
        for k,v in vertalingen.items():
            if k == word:
                new_word += v.upper()
            else:
                new_word += k.upper()
    else:
        for k,v in vertalingen.items():
            if k == word:
                new_word += v
            else:
                new_word += k
    return new_word


def geslachtsveranderingen(zin, vertaling):
    new_zin = []
    for k, v in vertalingen.items():
        for word in zin:
            if word == k:
                new_zin.apppend(v.capitilize())
            else:
                new_zin.append(k.capitilize())
            if word == v:
                new_zin.append(k)
            else:
                new_zin.append(v)
    return ''.join([x for x in new_zin])


def geslachtsherstel(zin, vertaling):
    new_zin = []
    for k, v in vertalingen.items():
        for word in zin:
            if word == k:
                new_zin.apppend(k.capitilize())
            else:
                new_zin.append(v.capitilize())
            if word == v:
                new_zin.append(v)
            else:
                new_zin.append(k)
    return ''.join([x for x in new_zin])


if __name__ == "__main__":
    vertalingen = {'hij': 'zij', 'broer':'zus'}
    print(vertaal('hij', vertalingen))
    print(vertaal('HIJ', vertalingen))
    print(vertaal('Hij', vertalingen))
    print(vertaal('broer', vertalingen))
    print(vertaal('mijn', vertalingen))
    print(geslachtsverandering('Hij is mijn broer.', vertalingen))
    print(geslachtsherstel('Zij is mijn zus.', vertalingen))
