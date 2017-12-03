def makes10(a, b):
    if(((a == 10) or (b == 10)) or ((a+b) == 10)):
       return True
    elif((a+b != 10) or ((a or b) or (b or a) != 10)):
        return False
