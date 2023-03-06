inputStr = input()
stack = []
ans = ""
flag = False
for i in inputStr:
    if i=="<":
        while stack:
            ans+= stack.pop()
        stack = ["<"]
        flag = True
    elif i==">":
       stack.append(">")
       ans+="".join(stack[:])
       stack = []
       flag = False
    elif i == " ":
        if flag:
            stack.append(" ")
        else:
            while stack:
                ans+= stack.pop()
            ans += " "
    else:
        stack.append(i)
while stack:
    ans += stack.pop()
print(ans)
