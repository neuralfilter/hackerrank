l = list(raw_input())
vowels = ["a", "e", "i", "o", "u"]
actual = []
for i in range(len(l)):
    if l[i] not in vowels:
        actual.append(l[i])

print "".join(actual)

