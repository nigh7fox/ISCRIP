def samen(prijzen) -> float:
    #   initiale totale prijs
    total_zonder_korting = sum(prijzen)
    total_met_korting = total_zonder_korting
    #   kijk hoeveel items de klant krijgt van de deal
    amount_of_discount_items = round(len(prijzen)/4)
    #   sort de lijst van prijzen om de laagste waardes aan het begin te krijgen
    sorted_prijzen = sorted(prijzen)
    #   pak de som van de 0 tot amount_of_discount_items van de gesorteerde lijst
    discount_items = sum(sorted_prijzen[0:amount_of_discount_items])
    #   trek som van discount van total
    total_met_korting -= discount_items
    return total_met_korting


def groeperen(prijzen) -> tuple:
    #   sorteer prijzen
    sorted_prijzen = sorted(prijzen, reverse=True)
    grouped = []
    #   for alle prijzen in prijzen met een stap grote van i tot i + 4 voeg tot array als tuple
    for i in range(0, len(sorted_prijzen), 4):
        grouped.append(tuple(sorted_prijzen[i:i+4]))
    return grouped


def gegroepeerd(prijzen) -> float:
    total_arr = []
    discount = []
    #   tuples omdat ze nu gegroepeerd zijn in groepen van 4 of minder
    for tuples in prijzen:
        for t in tuples:
            #   voor het gebruiken van sum
            total_arr.append(t)
        if len(tuples) is 4:
            #   zoek kleinste waarde in alle tuples in gegroepeerde lijst
            discount.append(min(list(tuples)))
        else:
            pass
    #   zet alle waardes in een array zodat we sum functie kunnen gebruiken
    total_zonder_korting = sum(total_arr)
    return round(total_zonder_korting-sum(discount), 2)

def winst(prijzen) -> float:
    #   gewoon de prijs die samen zijn min de prijs met groepeerd prijzen
    return round(prijzen[0]-prijzen[1], 1)

if __name__ == "__main__":
    prijzen = [3.23, 5.32, 8.23, 2.23, 9.98, 7.43, 6.43, 8.23, 4.23]
    print(samen(prijzen))
    print(groeperen(prijzen))
    #   ik koos om een aparte variable aan te maken,omdat ik geen globable variable wil gebruiken
    grouped_prijzen = groeperen(prijzen)
    print(gegroepeerd(grouped_prijzen))
    prijzen = [samen(prijzen), gegroepeerd(grouped_prijzen)]
    print(winst(prijzen))
