def germaniseer(sentence):
    #   Probeerde express in een line geprobeert.
    #   Stap 1 begin met een lege string
    #   Stap 2 copier sentences als een array
    #   Stap 2b split de sentence en
    #   Stap 2c voor elke woord maak de eerste letter een hoofdletter
    #   Stap 3 voeg een " " na elke woord
    return ''.join([x.capitalize() + " " for x in sentence.split()])


if __name__ == '__main__':
    print(germaniseer('Alleen hij is gelukkig die het geluk niet aan geluk te danken heeft.'))
#   ouput: Alleen Hij Is Gelukkig Die Het Geluk Niet Aan Geluk Te Danken Heeft.
    print(germaniseer('Geluk helpt soms, moed altijd.'))
#   output: Geluk Helpt Soms, Moed Altijd.
