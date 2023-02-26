n = int(input())
tmp = n % 5
 
if n == 1 or n == 3:
    print(-1)
elif tmp % 2 == 0: 
    print((n // 5) + (tmp // 2))
else:
    print((n // 5) - 1 + (tmp + 5) // 2)
