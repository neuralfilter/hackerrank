def make_out_word(out, word):
    listedout = list(out)
    return ''.join(listedout[0:2] + list(word) + listedout[2:4])
