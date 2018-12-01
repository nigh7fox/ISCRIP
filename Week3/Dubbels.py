def dubbels(numbers):
    if type(numbers[0]) is not int:
        return list(set([i for i in numbers if numbers.count(i) > 1]))
    return list(set([x for x in numbers if numbers.count(x) > 1]))


if __name__ == "__main__":
    print(dubbels([3, 9, 4, 3, 8, 7, 3, 4, 2]))
    print(dubbels([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(dubbels([8, 6, 9, 5, 7, 4, 8, 3]))
    print(dubbels(['0476-987394', '0498-837493', '0476-987394']))
