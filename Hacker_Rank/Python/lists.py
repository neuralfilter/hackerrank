if __name__ == "__main__":
    N = int(raw_input())
    arr = []
    for i in range(N):
        com = map(str, raw_input().split())
        if com[0] == "insert":
            arr.insert(int(com[1]), int(com[2]))
        elif com[0] == "print":
            print arr
        elif com[0] == "remove":
            arr.remove(int(com[1]))
        elif com[0] == "append":
            arr.append(int(com[1]))
        elif com[0] == "sort":
            arr.sort()
        elif com[0] == "pop":
            arr.pop()
        elif com[0] == "reverse":
            arr = arr[::-1]

