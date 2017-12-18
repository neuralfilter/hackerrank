def left2(str):
    listedstr = list(str)
    if len(str)<=2:
        return str
    return ''.join(listedstr[2:len(str)] + listedstr[0:2])
