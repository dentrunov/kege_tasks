with open('04.txt') as f:
    n = int(f.readline())
    s = list(map(int,f.readlines()))

min_summa = 100000000000000000
for i in range(n):
    summa = 0
    for j in range(n):
        summa += min(abs(j-i),n-abs(j-i)) * s[j]
    if summa < min_summa:
        min_summa = summa
print(min_summa)
    



'''with open('03.txt') as f:
    n = int(f.readline())
    s = list(map(int,f.readlines()))

max_sum = 0
min_l = 1000000
for i in range(n):
    summa = 0
    for j in range(i,n):
        summa = sum(s[i:j+1])
        if summa % 89 == 0:
            if summa > max_sum:
                max_sum = summa
                min_l = j - i + 1
print(min_l)
            
                


with open('02.txt') as f:
    n = int(f.readline())
    s = list(map(int,f.readlines()))

min_x = 10**10
for i in range(n-1):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if (s[i] + s[j] + s[k]) % 3 == 0 and (s[i] + s[j] + s[k]) < min_x:
                min_x = s[i] + s[j] + s[k]
print(min_x)
                
with open('01.txt') as f:
    n = int(f.readline())
    s = list(map(int,f.readlines()))

max_x = 0
for i in range(n-1):
    for j in range(i+1,n):
        x = s[i] * s [j]
        if x % 14 == 0 and x > max_x:
            max_x = x

print(max_x)'''
