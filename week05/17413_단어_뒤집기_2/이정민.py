S = input()

#괄호가 들어왔을 때 처리해 줄 stack
stack = []

#뒤집을 문자열
substring = ''

for i in S:
    if i == '<':
        #괄호 앞에 뒤집어야 되는 문자열이 있으면 뒤집어서 출력
        if len(substring) != 0 :
            print(substring[::-1], end='')
            substring = ''
        stack.append(i)
        print(i, end='')

    elif i == '>':
        stack.pop()
        print(i, end='')
    else :
        #len(stack) != 0 이면 '<'가 들어있다는 뜻이므로 출력
        if len(stack)!=0:
            print(i, end='')
        else:
            #공백이 들어오면 뒤집을 문자열 출력
            if i == ' ':
                print(substring[::-1], end = ' ')
                substring = ''
            else:
                substring += i
#남아있는 문자열 출력
if len(substring)!=0:
    print(substring[::-1], end='')
    substring = ''