def cat_dog(str):
    listedstr = list(str)
    counter = [0,0]
    for i in range(len(str)-2):
        if str[i:i+3] == "cat":
            counter[0]= counter[0] + 1
        if str[i:i+3] == "dog":
            counter[1]= counter[1] + 1
    if counter[0] == counter[1]:
        return True
    else:
        return False
