n=int(input("          ?    "))
prime_number=[2]
for i in range(3,n):
    for p in prime_number:
        if i % p == 0:
            break               
    else:
       prime_number.append(i)
          
print(prime_number)

twin_prime=[]
for i in range(1,len(prime_number)):
    if prime_number[i]-prime_number[i-1] ==2:
        twin_prime.append((prime_number[i-1],prime_number[i])) 

print("اعداد اول دوقلو:")
for pair in twin_prime:
    print(pair)