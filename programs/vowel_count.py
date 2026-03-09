# Write a program to count vowels in a string

s = input('Enter a string to count vowels : ')
s = s.lower()
count = 0
for i in s:
    if(i in 'aeiou'):
        count += 1
print(f'Total vowel present in given string is : {count}')