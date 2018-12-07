def caesarrotatie(n, txt):
    encrypted = ""
    for w in txt:
        for l in w:
            # not a letter
            if ord(l) < 65 or ord(l) > 122:
                encrypted += l
            encrypted += encrypt(l)
    return encrypted

# encryption gebeurt hier
def encrypt(letter):
    # alphabet in capital en lowercase
    # de for loop looped door de ascii tabel en vult de waardes
    uppercase_alphabet = [chr(i) for i in range(65, 90)]
    lowercase_alphabet = [chr(x) for x in range(97, 122)]
    # als letter is uppercase loop in uppercase array
    if letter.isupper():
        if letter in uppercase_alphabet:
            # index of current letter in uppercase alphabet
            letter_index = uppercase_alphabet.index(letter)
            new_letter_index = letter_index - 20
            if new_letter_index < 0:
                # maak cijfer postief
                new_letter_index = new_letter_index + 26
            return uppercase_alphabet[new_letter_index]
    else:
        if letter in lowercase_alphabet:
            # index of current letter in lowercase alphabet
            letter_index = lowercase_alphabet.index(letter)
            new_letter_index = letter_index - 20
            if new_letter_index < 0:
                # maak cijfer postief
                new_letter_index = new_letter_index + 26
            return lowercase_alphabet[new_letter_index]
    return ""


if __name__ == "__main__":
    print(caesarrotatie(20, "Ylluly boguhog ymn."))
