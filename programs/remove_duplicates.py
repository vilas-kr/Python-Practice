#  Write a program to remove duplicates from a list

n = int(input('Enter number of elements : '))
lst = []
for i in range(n):
    lst.append(input())
unique = set()
for i in lst:
    unique.add(i)
print(f'lst : {lst}')
print(f'unique : {unique}')