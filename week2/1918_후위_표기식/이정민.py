input = list(map(str, input()))

stack = []
answer = ""

sign=["+", "-", "*", "/", "(", ")"]

for i in range(len(input)):
    tmp = input[i]

    if tmp not in sign:
        answer = answer+tmp
    else:
        if tmp=='(':
            stack.append(tmp)
        elif tmp==')':
            while len(stack)!=0 and stack[-1]!='(':
                answer = answer+stack.pop()
            stack.pop()
        elif tmp=='*' or tmp=='/':
            while len(stack)!=0 and (stack[-1]=='*' or stack[-1]=='/'):
                answer = answer+stack.pop()
            stack.append(tmp)
        elif tmp=='+' or tmp=='-':
            while len(stack)!=0 and stack[-1]!='(':
                answer = answer+stack.pop()
            stack.append(tmp)

while len(stack)!=0:
    answer = answer+stack.pop()

print(answer)
