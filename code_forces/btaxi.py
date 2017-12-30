l = int(raw_input())
child =raw_input().split()
def taxi(passengers, other):
    print passengers
    print other
    if passengers == 1:
        return 1
    if (passengers in child) and (other in child):
        child.remove(passengers)
        child.remove(other)
        child.append(5)
    else:
        return taxi(--passengers, ++other)
print taxi(4,1)
