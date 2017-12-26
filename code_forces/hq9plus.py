l = str(raw_input())
listedl = list(l)
executes = "NO"
for i in range(len(l)):
    if listedl[i] == "H":
        executes = "YES"
    if listedl[i] == "Q":
        executes = "YES"
    if (listedl[i] == 9) or (listedl[i] == "9"):
        executes = "YES"
    #if listedl[i] == "+":
        #executes = "NO"
print executes
