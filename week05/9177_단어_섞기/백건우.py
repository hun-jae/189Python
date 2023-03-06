# dfs로 단어 순서 경우의 수 모두 구해서 풀려고 했는데 시간초과남 문제유형보니까 dp로 풀래서 dp로 풀어볼 예정

from collections import deque

n = int(input())

def dfs(wordsLen, word3Len):
    global word3, canMake
    if len(ch) == word3Len:
        temp = ''
        for i in ch:
            if i == 0 :
                cur = word1.popleft()
                temp += cur
                word1.append(cur)
            elif i == 1 :
                cur = word2.popleft()
                temp += cur
                word2.append(cur)

        if word3 == temp:
            canMake = True
        return
    for i in range(2):
        if not canMake:
            if wordsLen[i] > 0 :
                ch.append(i)
                wordsLen[i] -= 1
                dfs(wordsLen, word3Len)
                wordsLen[i] += 1
                ch.pop()

for tc in range(1, n+1):
    canMake = False
    word1, word2, word3 = input().split(' ')
    word1 = deque(word1)
    word2 = deque(word2)
    ch = deque()
    dfs([len(word1), len(word2)], len(word3))

    if canMake : print('Data set {}: yes'.format(tc))
    else : print('Data set {}: no'.format(tc))
