no_num = input()
arr = []
answer_arr = []

for num in range(no_num):
    arr.append(long(input()))

for numbers in range(no_num):
    while(True):
        (arr[numbers]) += 1
        if(str(arr[numbers])[::-1] == str(arr[numbers])):
            print(arr[numbers])
            break
