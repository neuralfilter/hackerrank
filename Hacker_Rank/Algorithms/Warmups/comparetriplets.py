def solve(a0, a1, a2, b0, b1, b2):
    scorearr = [0 ,0]
    alicearr = [a0, a1, a2]
    bobarr = [b0, b1, b2]
    for i in range(3):
        if alicearr[i] > bobarr[i]:
            scorearr[0] = scorearr[0] + 1
        elif alicearr[i] < bobarr[i]:
            scorearr[1] = scorearr[1] + 1
    return scorearr[0], scorearr[1]
