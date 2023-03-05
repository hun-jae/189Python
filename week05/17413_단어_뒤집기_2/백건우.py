s = list(input())

stack = [] # 단어들을 스택에 넣은 뒤 출력하면 뒤집혀서 출력된다.
isRight = False
for ch in s :
    if ch == '<':  # 여기부터는 정방향으로 출력해야 하므로 지금까지 스택에 쌓인것들 출력해줘야 한다.
        while stack:
            print(stack.pop(), end="")
        isRight = True
        print(ch, end="")
    elif ch == '>': # 정방향 출력 끝
        isRight = False
        print(ch, end="")
    elif isRight : # 정방향 출력 중
        print(ch, end="")
    elif ch == " " : # 공백 이전도 뒤집어서 출력
        while stack:
            print(stack.pop(), end="")
        print(ch, end="")
    elif not isRight :  # 뒤집어서 출력해야되면 스택에 넣어서 추력해야된다.
        stack.append(ch)

while stack: # 남은 단어 
    print(stack.pop(), end="")
