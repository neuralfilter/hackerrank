def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)-len(sub_string)+1):
        print string[i:i+len(sub_string)]
        if string[i:i+len(sub_string)] == sub_string:
            counter+=1
    return counter
