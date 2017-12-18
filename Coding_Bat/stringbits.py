def string_bits(str):
    listed = list(str)
    stringbi = list()
    for i in range(0, len(str), 2):
        stringbi.append(''.join(listed[i]))
    return ''.join(stringbi)
