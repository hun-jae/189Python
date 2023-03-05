# 후위표기식 : 알파벳 들어올때 넣어주고 stack에서 뺄때 넣어줌(괄호는 넣지말고)
# priorityStack : 연산자 들어올때 자기보다 우선순위가 크거나 같은 연산자를 쭉 빼자
#                빼면서 후위표기식에 넣어준다(괄호는 빼고 넣어줌)
#                뺄때 주의할것은 괄호 내의 있는건 따로 해줘야함
#                즉 괄호가 나올 때 괄호의 cnt를 체크하면서 빼주자 while(cnt > 0)
# 연산자우선순위 : 1 : )
#              2 : -, +
#              3 : *, /
#              4 : (

midNotation = list(input())
prefix = ""
prior = {")": 0, "*": 1, "/": 1, "+": 2, "-": 2, "(": 3} #여는 괄호에 연산자를 넣기 위해 우선순위를 최하위로
operStack = []
for s in midNotation:
    bracketCnt = 0 #현재 연산자스택에 괄호가 있을때
    if s.isupper(): #문자가 들어왔을때
        prefix += s
    else:
        if len(operStack) == 0 or s=="(" or s==")": #여는 괄호의 우선순위가 최하위지만 operStack에 넣어줄때 이전 연산자가 빠지면 안되니 따로 처리
            operStack.append(s)
            continue
        while(prior[operStack[-1]] <= prior[s] or bracketCnt > 0): #스택에 있는 연산자가 우선순위가 높거나 현재 괄호가 열려있다면 빼는작업 필요
            if operStack[-1] == ")":
                bracketCnt += 1
                operStack.pop()
            elif operStack[-1] == "(":
                bracketCnt -= 1
                operStack.pop()
            else: #연산자
                prefix += operStack.pop()

            if len(operStack) == 0:
                break

        #스택에 있는 연산자가 우선순위가 낮을때 혹은 아무것도 없을때
        operStack.append(s)

#모든 문자열이 들어갔음
while(operStack): #연산자 남아있는 상황
    if operStack[-1] == "(" or operStack[-1] == ")":
        operStack.pop()
    else:
        prefix+=operStack.pop()
print(prefix)