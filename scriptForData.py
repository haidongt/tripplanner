from tripDB.models import Destination

file = open("data.txt")
count = 0
while 1:
    count = count + 1
    line = file.readline()
    if not line:
        break
    line = line.strip()
    fields = line.split("*")
    newRow = Destination(dest_ID = count, name = fields[0], location = fields[2]+","+fields[3], description = fields[1])
    newRow.save()
