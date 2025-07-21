# s='aBcDeF'
# s.lower()
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.strip()) #space ebteda va enteha
# print(s.rstrip())# space samt rast ro hazf milone
# print(s.lstrip()) # space samt chap ro hazf mikone
# print(s.startswith('a'))
# print(s.startswith('abcd'))
# print(s.endswith('ef'))
# print(s.endswith('eF')) 



# s='     Hello       '
# print(s.lower())
# print(s.strip())
# print(s.strip().lower())
# print(s.strip().lower().startswith('h') )




while True:
    a= input('are you sure?')
    if a.lower().strip().startswith("y") :
        print('ok')
   