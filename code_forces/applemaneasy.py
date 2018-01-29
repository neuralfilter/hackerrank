board = [list(str(raw_input())) for i in xrange(int(raw_input()))]
count = 0
for i in xrange(len(board)):
    for j in xrange(len(board)):
        temps = [0, -1, 0, 1, 0]
        for x in xrange(4):
            ai = i + temps[x]
            aj = j + temps[x+1]
            if (0 <= ai < len(board)) and (0 <= aj < len(board)) and (board[ai][aj] == "o"):
                count += 1
        if (count % 2 > 0):
            print "NO"
            exit()
print "YES"
