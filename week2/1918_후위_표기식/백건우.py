# https://www.acmicpc.net/board/view/54088 반례 참고해서 품
import sys

input = sys.stdin.readline

line = list(input().rstrip())
stack = []
for ch in line:
    if ch == '+':
        while stack and stack[-1] != '(':
            print(stack.pop(),end="")
        stack.append(ch)
    elif ch == '-':
        while stack and stack[-1] != '(':
            print(stack.pop(),end="")
        stack.append(ch)
    elif ch == '*':
        while stack and stack[-1] != '(' and stack[-1] != '+' and stack[-1] != '-':
            print(stack.pop(),end="")
        stack.append(ch)
    elif ch == '/':
        while stack and stack[-1] != '(' and stack[-1] != '+' and stack[-1] != '-':
            print(stack.pop(),end="")
        stack.append(ch)
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack[-1] != '(':
            print(stack.pop(),end="")
        stack.pop() #여는 괄호 pop
    else:
        print(ch,end="")

while stack:
    print(stack.pop(),end="")
