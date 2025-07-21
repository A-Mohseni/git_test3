l1=[3 ,4 ,5 ,6 ,7 ]
l2=[9 ,16 ,25 ,36 ,49 ]

l3=[]
for i in l1:
    if i%2==1:
        l3.append(i**2)
print(l3)



l4=[i**2 for i in l1 if i%2==1]  
print(l4)


