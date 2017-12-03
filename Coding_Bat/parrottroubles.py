def parrot_trouble(talking, hour):
    if(talking == True and (20 < hour or hour < 7)):
        return True
    else:
        return False
    if(talking == False):
        return False
