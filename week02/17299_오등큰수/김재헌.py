n = int(input())
list_ = list(map(int, input().split()))
stack = []
count = {}

for i in list_: #값마다 count를 세준다.
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

result = [-1 for i in range(n)]
for idx, i in enumerate(list_):
    while stack and count[stack[-1][1]] < count[i]: #넣어줄 때 stack내부에 있는 애들중에 본인보다 count가 적은 애들이 있다면
        popIdx, popI = stack.pop() #뽑아서
        result[popIdx] = i #결과에 넣어준다
    stack.append([idx, i]) #이후 stack에 넣어줌
for i in result:
    print(i, end=" ")