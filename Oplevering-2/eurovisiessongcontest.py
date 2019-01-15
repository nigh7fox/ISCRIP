from collections import Counter, OrderedDict


def scoresToevoegen(current_bord, new_bord):
    updated_bord = dict(Counter(current_bord)+Counter(new_bord))
    return updated_bord


def scoresTonen(current_bord, top=0):
    sorted_dict = OrderedDict(sorted(current_bord.items(), key=lambda x: x[1]))
    if top is 0:
        return list(sorted_dict.items())[::-1]
    return list(sorted_dict.items())[len(sorted_dict):len(sorted_dict)-1-top:-1]


if __name__ == "__main__":
    scorebord = {}
    scores_UK = {'Lithuania': 7, 'Russia': 3, 'Estonia': 4, 'Azerbaijan': 2, 'Sweden': 12, 'Turkey': 1, 'Spain': 8, 'Germany': 6, 'Malta': 5, 'Ireland': 10}
    scorebord = scoresToevoegen(scorebord, scores_UK)
    print(scoresTonen(scorebord))
    scores_HU = {'Albania': 8, 'Russia': 7, 'Iceland': 6, 'Italy': 5, 'Sweden': 12, 'Turkey': 3, 'Spain': 1, 'Germany': 10, 'Serbia': 4, 'Moldova': 2}
    scorebord = scoresToevoegen(scorebord, scores_HU)
    print(scoresTonen(scorebord, 3))
