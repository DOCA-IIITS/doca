import csv
from .models import spec
path = './'

file=open( path +"xyz.CSV", "r")
reader = csv.reader(file)
for line in reader:
    t=line[1]
    a=spec(spec=t)
    a.save()
    
    
