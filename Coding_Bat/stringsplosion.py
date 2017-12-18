def string_splosion(str):
    listed_string = list(str)
    empty_string = []
    for i in range(len(str)+1):
        empty_string.append(''.join(listed_string[0:i]))
    return ''.join(empty_string)
