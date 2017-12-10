def front_back(str):
    if(str == ""):
        return ""
    temp = str[0]
    if(len(str) == 1):
        return str
    store = list(str)
    store[0] = str[len(str) - 1]
    store[len(str) - 1] = temp
    return "".join(store)
