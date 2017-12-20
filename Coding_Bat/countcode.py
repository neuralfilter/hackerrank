def count_code(str):
    listedstr = list(str)
    counter = 0
    for i in range(len(str)-3):
        if (''.join(listedstr[i:i+2]) == "co"):
            if(''.join(listedstr[i+3:i+4]) == "e"):
                counter+=1
    return counter
