if __name__ == '__main__':
    s = raw_input()
    listeds = list(s)
    for i in range(len(s)-1):
        if s[i].isalnum() == True:
            print True
            break
        if i == len(s)-1:
            print False

    for q in range(len(s)-1):
        if listeds[q].isalpha() == True:
            print True
            break
        if q == len(s)-1:
            print False

    for g in range(len(s)-1):
        if listeds[g].isdigit() == True:
            print True
            break
        if g == len(s)-1:
            print False

    for n in range(len(s)-1):
        if listeds[n].islower() == True:
            print True
            break
        if n == len(s)-1:
            print False

    for h in range(len(s)-1):
        if listeds[h].isupper() == True:
            print True
            break
        if  h == len(s)-1:
            print False
