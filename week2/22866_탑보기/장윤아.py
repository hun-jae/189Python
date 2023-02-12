'''
아직 오답
'''
n = int(input())
buildings = [0] + list(map(int, input().split()))

for i, building in enumerate(buildings):
    leftStack, rightStack = [], []
    for p in range(i):
        while leftStack and leftStack[-1][1] <= buildings[p]:
            leftStack.pop()
        if buildings[p] > building:
            leftStack.append((p,buildings[p]))

    for q in range(len(buildings)-1, i+1, -1):
        while rightStack and rightStack[-1][1] <= buildings[q]:
            rightStack.pop()
        if buildings[q] > building:
            rightStack.append((q,buildings[q]))


    stack = leftStack + rightStack
    visible = len(stack)
    if visible:
        if leftStack:
            res = leftStack.pop()[0]
        else:
            res = rightStack.pop()[0]
        print(visible, res)
    else:
        print(visible)