l = raw_input()
l = l.lower()
listedl = list(l)
counter = 0
vowels = ["a", "o", "y", "e", "u", "i"]
newarr = []
for i in range(len(l)):
    if(l[i] not in vowels):
        newarr.append( ".")
        newarr.append(listedl[i])
print(''.join(newarr))
