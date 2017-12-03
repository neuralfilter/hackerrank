def pos_neg(a, b, negative):
    if((negative == False)):
        return (((a < 0) and (b > 0)) or ((a > 0) and(b < 0)))
    if(negative == True):
        return ((a < 0) and (b < 0))
