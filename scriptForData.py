file = open("data.txt")

while 1:
    line = file.readline()
    if not line:
        break
    print line
