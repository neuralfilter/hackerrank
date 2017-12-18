def extra_end(str):
    listedstr = list(str)
    return ''.join(listedstr[len(str)-2:len(str)]*3)
