import sys
sys.setrecursionlimit(10000)
l = int(raw_input())
def luckycheck(divi, base):
    if(divi % base == 0) and (("4" == str(base)) or ("7" == str(base))):
        return "YES"
    elif (divi % base == 0) and ( ("4" in list(str(base))) and ("7" in
                                                              list(str(base))) ):
        stringed = str(base)
        listed = list(stringed)
        i=0
        for i in range(len(stringed)):
            if (listed[i] != "7") and (listed[i] != "4"):
                return "NO"
        return "YES"
    elif base == divi:
       return "NO"
    elif divi == 1:
        return "NO"
    else:
        return luckycheck(divi, base+1)

print luckycheck(l, 1)
