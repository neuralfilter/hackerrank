def count_hi(str):
    listedstr = list(str)
    z = 0
    for i in range(len(str)-1):
        if str[i:i+2] == "hi":
            z+=1
    return z
