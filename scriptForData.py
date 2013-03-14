from tripDB.models import Destination, Route

file = open("data.txt")
while 1:
    line = file.readline()
    if not line:
        break
    line = line.strip()
    fields = line.split("*")
    newRow = Destination(name = fields[0], location = fields[2]+","+fields[3], description = fields[1])
    newRow.save()

yellowstone = Destination.objects.filter(name__icontains="yellowstone")[0]
rainier = Destination.objects.filter(name__icontains="rainier")[0]
grandteton = Destination.objects.filter(name__icontains="grand teton")[0]
yosemite = Destination.objects.filter(name__icontains="yosemite")[0]

newRow = Route(destA = yellowstone, destB = grandteton, driving_time = 2)
newRow.save()
newRow = Route(destA = yellowstone, destB = yosemite, driving_time = 12)
newRow.save()
newRow = Route(destA = yellowstone, destB = rainier, driving_time = 18)
newRow.save()
'''
#join
yellowstone_yosemite = Route.objects.filter(destA__name__icontains="yellowstone", destB__name__icontains="yosemite")
yellowstone_yosemite[0].driving_time

#update
yellowstone.description = "lalala"
yellowstone.save()
yellowstone = Destination.objects.filter(name__icontains="yellowstone")[0]
yellowstone.description
yellowstone.description = 'Yellowstone National Park, WY 82190, USA'
yellowstone.save()

#insertion and deletion
uiuc = Destination.objects.get(name="UIUC")
uiuc = Destination(name = "UIUC", location = "123,234", description = "University of Illinois at Urbana-Champaign")
uiuc = Destination.objects.get(name="UIUC")
uiuc.save()
uiuc = Destination.objects.get(name="UIUC")
uiuc.delete()
uiuc = Destination.objects.get(name="UIUC")
'''
