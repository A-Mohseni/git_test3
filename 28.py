from time import time


tic= time()
n=2000
prime_number=[2]
for i in range (3,n,2):
    #for p in [j for j in prime_number if j <=sqrt(i)]:
    for p in prime_number:
        if i%p==0:
            break
    else:
        prime_number.append(i) 
print(prime_number) 
toc=time()
print(toc-tic)
print(len(prime_number))