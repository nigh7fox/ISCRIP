def formule_1(l, a ,t):
    # constantes
    MAX_KM = 305
    MAX_T = 120
    r = MAX_KM / a
    # round om afteronden
    k = round(r) * a
    if((r * t) > MAX_T):
        # als je over de tijd limiet gaat
        over_t = (r * t) - MAX_T
        over_r = over_t / t
        # neem dan de aantal die te veel is min de R (max)
        r = r - over_r
        k = round(r) * a
    # vaste waarde voor monaco
    if l is "Monaco":
        r = 78
        k = 260.52
    # en de antwoord is
    ans = "De grote prijs van " + l + " wordt verreden over " + str(round(r))  + " ronden (" + str(round(k, 3)) + "km)"
    return ans


if __name__ == "__main__":
    print(formule_1("Belgie", 7.004, 2.88772))
    print(formule_1("Monaco", 3.340, 1.13895))
    print(formule_1("Brazilie", 5.031, 1.54178))
