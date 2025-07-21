# s='His name is ali, ali is astudent . '
# print(s.replace('ali','reza'))



# a=12
# b=34

# # s='{} X {}={}'

# # print(s.format(a,b,a*b))

# print(f'{a} x {b} = {a*b}')  # fstring 



# invoive =[
# ('pen','25,000'),
# ('notebook', '110,000')]
# for item,price in invoive:
#     print(item.center(10),price.rjust(7))


age= input('how old are you ?  ')
if age.isdigit():
    age= int(age)
else:
    print('please enter a valid age ')
