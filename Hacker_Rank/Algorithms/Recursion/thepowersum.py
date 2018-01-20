
def powersum(i, j, n):
    if n ** j < i:
        return powersum(i, j, n+1) + powersum(i - n ** j, j, n+1)
    elif n ** j == i:
        return 1
    else:
        return 0


def main():
    m = int(raw_input())
    n = int(raw_input())
    print powersum(int(m), int(n), 1)
    return 0

main()
