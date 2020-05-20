namedel = ['k','a','z']
namelist = ['Kevin','Coco','Anita','Zobro','Jack']
namedels = []
names = []
print(namelist)
for n in namedel:
    for na in namelist: 
        if n in na.lower():
            namelist.remove(na)
print(namelist)