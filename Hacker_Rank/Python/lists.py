if __name__ == "__main__":
    N = int(raw_input())
    counter = 0
    arr = []
    while(counter <= N):
        inputted = raw_input()
        inputted = list(inputted)
        if(inputted[0:6] == "insert"):
            del inputted[0:7]
            counted = 0
            for i in range(len(inputted)):
                if((isinstance(inputted[i],int)) and (counted == 0)):
                   if(isinstance(inputted[i+1], int)):
                       i = inputted[i:i+1]
                       counted+=1
                   else:
                       i = inputted[i]
                       counted+=1
                if((isinstance(inputted[i], int)) and (counted == 1)):
                   if(isinstance(inputted[i+1], int)):
                       e = inputted[i:i+1]
                       counted+=1
                   else:
                       e = inputted[i]
                       counted+=1
            arr.insert(i, e)
            print arr
        if(inputted == "print"):
            print arr
        if(inputted == "remove"):
            e = int(raw_input())
            arr.remove(e)
        if(inputted == "append"):
            e = int(raw_input())
            arr.append(e)
        if(inputted == "sort"):
            arr.sort()
        if(inputted == "pop"):
            arr.pop()
        if(inputted == "reverse"):
            arr.reverse()
        counter+=1
