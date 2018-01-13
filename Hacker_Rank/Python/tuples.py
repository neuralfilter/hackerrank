if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    k = []
    for i in range(len(integer_list)):
        k.append(integer_list[i])
k = tuple(k)
print hash(k)
