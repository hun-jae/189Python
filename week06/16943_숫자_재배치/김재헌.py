from itertools import permutations as p
a, b = map(list, input().split())
b = int(''.join(b))
per = list(p(sorted(a,reverse=True), len(a)))
ans = -1
for i in per:
    if i[0]=="0":
        break
    if int(''.join(i)) < b:
        ans = int(''.join(i))
        break
print(ans)
