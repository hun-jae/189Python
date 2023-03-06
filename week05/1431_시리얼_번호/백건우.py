n = int(input())
words = []
for _ in range(n): # 길이, 자리수의 합 비교, 사전순 알파벳순
    temp = list(input())
    wordLen = len(temp)  # 단어의 길이
    wordSum = 0          # 단어의 자리수의 합
    for ch in temp:
        if ch in ('1','2','3','4','5','6','7','8','9','0') :
            wordSum += int(ch)
    words.append([wordLen,wordSum,''.join(temp)])  # 단어 사전순
words.sort(key=lambda x:(x[0],x[1],x[2])) # 길이, 자리수의 합, 사전순으로 
for word in words :
    print(word[2])
