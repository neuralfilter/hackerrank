count = 5
def helloworld(count):
    if count == 1:
        return
    print "hello"
    helloworld(count-1)

helloworld(count)
