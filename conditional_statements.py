#logic
#if, if-elif,if-elif-else

x = int(input('what is x?'))
y = int(input('what is y?'))

if x > y :
    print('x is greater than y')
elif x < y :
    print('x is lesser than y')
else:
    print('x is equal to y')

score = int(input('score:'))

if score >= 90 and score <= 100 :
    print('Grade A')
elif score <= 80 and score >= 90 :
    print('Grade B')
elif score <= 70 and score >= 80 :
    print('Grade C')
else:
    print('Grade D')