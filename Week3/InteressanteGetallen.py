def interessante_getallen(a, b, c):
    for x in range(50, 0, -1):
        if a % b == 0:
            kleinste_deelbaar = b
    count = 0
    while True:
        numbers = [int(n) for n in str(count)]
        if sum(numbers) == c:
            if sum(numbers) % kleinste_deelbaar == 0:
                if sum(numbers) % c == 0:
                    if count % c == 0:
                        return str(kleinste_deelbaar) + "\n" + str(count)
        count += 1
    return 0


if __name__ == "__main__":
    print(interessante_getallen(2, 1, 10))

