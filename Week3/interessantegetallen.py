def interessante_getallen(a, b, c):
    # zoek kleinste deelbare getal, begin van 50 en ga naar 0
    for x in range(50, 0, -1):
        if a % b == 0:
            kleinste_deelbaar = b
    counter = 0
    while True:
        # maak een lijst van de cijfer (individuele cijfers)
        numbers = [int(n) for n in str(counter)]
        # als de som van de cijfers gelijk is aan de ingevoerde getal
        if sum(numbers) == c:
            # als de som deelbaar is door de kleinste deelbare getal
            if sum(numbers) % kleinste_deelbaar == 0:
                # als de som deelbaar is door de gegeven getal
                if sum(numbers) % c == 0:
                    # als de counter deelbaar is door c (anders geeft hij 19 terug)
                    if counter % c == 0:
                        return str(kleinste_deelbaar) + "\n" + str(counter)
        counter += 1
    return 0


if __name__ == "__main__":
    print(interessante_getallen(2, 1, 10))

