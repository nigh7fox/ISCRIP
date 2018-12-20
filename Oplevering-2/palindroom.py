def palindroom(txt_path):
    words = []
    #   open text file in dit geval woordenlijst.txt
    with open(txt_path) as woorden:
        for woord in woorden:
            left = woord[0:int(len(woord)/2-1)].replace("\n","")
            right = woord[int(len(woord)/2):len(woord)].replace("\n","")
            mid = woord[int(len(woord)/2-1)].replace("\n","")
            #   als de linker helft van de woord gelijk is aan
            #   de rechter helft omgedraaid dan is het een palindroom
            #   het middelste letter is niet van belang
            if left == right[::-1]:
                words.append(woord)
    return words


if __name__ == "__main__":
    #   print alle gevonden palindroom woorden, ps. savas is een extra test case
    for words in palindroom("woordenlijst.txt"):
        print(words.replace("\n", ""))
