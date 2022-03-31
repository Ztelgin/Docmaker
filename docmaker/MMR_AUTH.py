import re
import pandas as pd

save_file = open('hereisthedata.csv', 'w')
#data = open('PAK MMR TEST.txt','r')
to_add = open('New Text Document.txt','r', encoding="utf8")
#data = open('New Text Document.txt','r')


authlist = []

for line in to_add:
    auth = re.findall('by (.*)\(',line)
    if not len(auth) == 0:
        auth = auth[0].split(' and ')
        authlist.append(auth)

print(authlist)

for entry in authlist:
    for name in entry:
        name = name.split()
        for part in name:
            print(part)
            save_file.write(part+",")
        save_file.write("\n")
