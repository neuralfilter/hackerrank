def xyz_there(str):
   listedstr = list(str)
   if str == "xyz":
       return True
   for i in range(len(str)-2):
       print listedstr[i:i+3]
       if (''.join(listedstr[i:i+3]) == "xyz") and (''.join(listedstr[i-1:i]) !=
                                                            "."):
           return True
   return False
