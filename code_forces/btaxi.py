def answer():
    counter = 0
    N = input()
    a = map(int,raw_input().split())
    g = 4
    while(len(a) > 0):
        k = 0
        for k in range(len(a)):
            if a[k] == 5:
                counter+=1
                a.remove(5)
            if a[k] == g:
                for m in range(len(a)):
                    if a[m] == (5-g):
                        a.remove(g)
                        a.remove(5-g)
                        counter+=1
                m = 0
                g-=1
            if len(a) == 1:
                a.remove(a[0])
    print(counter)
