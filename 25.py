L=[3,4,5]

L.append(6)
L.insert(1,3.5)
L.insert(0,2)

L2=[9,8,7]

L.extend(L2)    # ezafe kardan aazaye yek list be list dige

L.append(3.5)


L.remove(3.5) #دستور remove اولین عبارتی که مشخص کردی که داخل لیست باشه رو پاک


# while 3.5 in L:
#     L.remove(3.5)

# ین حلقه میگه تا زمانیکه عبارت داخل لیسات هست پاک کن عبارت  رو

#L.pop(-1)   #metod pop addresi ke dadim ro pak mikone va mitone bema bar gardonash 
# x=L.pop(-1)
# print (x)

# L[3]=L[3]**2
L[3]=100
L[3]**=2
print(L)
