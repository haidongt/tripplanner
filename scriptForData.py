from tripDB.models import Destination, Route

file = open("data/np_out.txt")
while 1:
    line = file.readline()
    if not line:
        break
    line = line.strip()
    fields = line.split("*")
    newRow = Destination(name = fields[0], location = fields[2]+","+fields[3], tag = "np")
    newRow.save()


file = open("data/zoo_out.txt")
while 1:
    line = file.readline()
    if not line:
        break
    line = line.strip()
    fields = line.split("*")
    newRow = Destination(name = fields[0], location = fields[2]+","+fields[3], tag = "zoo")
    newRow.save()
	
	
file = open("data/museums_out.txt")
while 1:
    line = file.readline()
    if not line:
        break
    line = line.strip()
    fields = line.split("*")
    newRow = Destination(name = fields[0], location = fields[2]+","+fields[3], tag = "museum")
    newRow.save()

file = open("data/city_out.txt")
while 1:
    line = file.readline()
    if not line:
        break
    line = line.strip()
    fields = line.split("*")
    newRow = Destination(name = fields[0], location = fields[2]+","+fields[3], tag = "city")
    newRow.save()
