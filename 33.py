# s='d:\new folder'
# s='d:\new folder\text.txt'
# s='d:\new folder\backup.txt'
# s='d:\new folder\red.txt'
# s='it\'s my bag'
# s="it\"s my bag"
# s='d:\\new folder'

# print(s)


#end = vaghti karet tamom shd akharesh chikar kne!. 
# sep = joda konande, dar dastor print.
from time import sleep
from datetime import datetime

while True:
    t=datetime.now().strftime('%H:%M:%S')
    print(t,end='\r')
    sleep(1)



