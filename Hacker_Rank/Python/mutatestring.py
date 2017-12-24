def mutate_string(string, position, character):
    listedstr = list(string)
    strings = listedstr[:position] + list(character) + listedstr[position+1:]
    return ''.join(strings)
