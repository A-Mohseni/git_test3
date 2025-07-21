# # l=['abc','def','ghi','jkl']
# # s=' - '.join(l)
# # print(s) 


# # s='abc def ghi jkl'

# # print(s.split(' '))   #


# s='''  a series of English language learning books designed for young learners, often used in preparation for Cambridge English Young Learners (YLE) exams. These books are known for their engaging stories and colorful pages, which make learning enjoyable. Each book in the series typically contains eight stories with accompanying activities. 
# Here's a more detailed breakdown:
# Target Audience:
# Storyfun books are aimed at young learners who are beginning to learn English, typically those preparing for the Cambridge YLE Starters, Movers, and Flyers exams. 
# Content:
# The books are filled with colorful illustrations and engaging stories that help children learn new vocabulary and grammar concepts. 
# Structure:
# Each book in the series includes a set of stories, usually eight in total, and each story is accompanied by a variety of activities to reinforce learning. 
# Focus on YLE Exams:
# The Storyfun series is specifically designed to support learners in preparing for the Cambridge English Young Learners (YLE) exams. 
# Example:
# One specific book in the series is "Storyfun for Starters," by Karen Saxby, which is available as a 62-page PDF. 
# '''
# # print(len(s.split()))
# # print(len(s.split('\n')))
# print(len(s.split('.')))
# print(len(s.replace('?','.').split('.')))


# s=0
# n=int(input('how many'))
# for i in range(n):
#     s+= int(input('???'))
#     print(s/n) 




# s=0
# c=0
# while True:
#     a=int(input(' ??'))
#     if a==0:
#         break
#     s+=a
#     c+=1
# print(s/c)


# s=[float(i)for i in input('?').split()]
print(sum(s:=[float(i)for i in input('?').split()])/len(s))


