
#خیام پاسکال


# n=5
# L=[0]*(n+1)
# L[-1]=1
# while L[0] == 0:
#     m=[str(i) for i in L if i!=0]
#     print(' '.join(m).center(n*5))
#     for i in range(n):
#         L[i]+=L[i+1]

         




#مثلث سرپینسکی

n=14
L=[0]*(n+1)
L[-1]=1
c= n
while L[0] == 0:
    m=[['  ','##'][i%2==1] for i in L if i !=0]
    # print(' '.join(m).center(n*5))
    c-=1
    print((' '*c) + ''.join(m))
    for i in range(n):
        L[i]+=L[i+1]