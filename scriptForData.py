from tripDB.models import Destination

file = open("data.txt")
while 1:
    line = file.readline()
    if not line:
        break
    line = line.strip()
    fields = line.split("*")
    newRow = Destination(name = fields[0], location = fields[2]+","+fields[3], description = fields[1])
    newRow.save()
