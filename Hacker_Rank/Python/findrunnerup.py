if __name__ == '__main__':
    n = int(raw_input())

    h = map(int, raw_input().split())
    h = set(h)
    h.remove(max(set(h)))

    print max(h)
