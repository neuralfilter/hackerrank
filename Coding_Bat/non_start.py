def non_start(a, b):
    alisted = list(a)
    blisted = list(b)
    return ''.join(alisted[1:len(a)] + blisted[1:len(b)])
