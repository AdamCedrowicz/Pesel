from ast import Import
import random
# birth year
v1 = random.randrange(0,9)
v2 = random.randrange(0,9)
#birth month
v4 = random.randrange(0,9)
if v4 == 0:
    v3 = 1
elif v4 <= 2:
     v3 = random.randrange(0,2)
else:
    v3 = 0
# birth day
v6 = random.randrange(0,9)
if v6 == 0 and v4 == 2:
    v5 = random.randrange(1,3)
elif v6 == 1 and v4 in [1,3,5,7,8,0] or v3 == 0 and v4 == 2:
    v5 = random.randrange(0,4)
else:
    v5 = random.randrange(1,3)
# 4 random
v7 = random.randrange(0,9)
v8 = random.randrange(0,9)
v9 = random.randrange(0,9)
v10 = random.randrange(0,9)
# v11 
numbers = [      
        (v1 * 1) % 10
        ,(v2 * 3) % 10
        ,(v3 * 7) % 10
        ,(v4 * 9) % 10
        ,(v5 * 1) % 10
        ,(v6 * 3) % 10
        ,(v7 * 7) % 10
        ,(v8 * 9) % 10
        ,(v9 * 1) % 10
        ,(v10 *3) % 10
        ]
values_sum = sum(numbers) % 10
v11 = 10 - values_sum
v11 = v11 % 10
#printing
l = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11]
pesel = (''.join(str(i) for i in l))
pesel_file = open('pesel.txt', 'a')
pesel_file.write(pesel)
pesel_file.close()