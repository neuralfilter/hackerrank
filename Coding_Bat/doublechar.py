def double_char(str):
    listedstr = list(str)
    doublestr = []
    for i in range(len(str)):
        doublestr.append(''.join(listedstr[i])*2)
    return ''.join(doublestr)
