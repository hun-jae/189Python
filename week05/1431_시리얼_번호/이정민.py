import queue

#정렬을 위해 priorityQueue 사용
q = queue.PriorityQueue()

#문자열의 길이가 같다면 모든 자리수의 합을 구하기
def sum (list):
    cnt = 0
    for l in list:
        if ord(l)<58 and ord(l)>47:
            cnt+=ord(l) - 48
    return cnt

#사전순으로 비교할 때 숫자가 알파벳보다 작다는 조건을 맞추기 위해서 각 문자를 아스키코드값으로 배열에 저장
def change(arr):
    val_arr = []
    for a in arr:
        val_arr.append(ord(a) - 48)
    return val_arr

class SerialNo :
    def __init__(self, str):
        self.str = str
        self.len = len(str)
        self.cnt = sum(str)
        self.arr = change(str)

    def __lt__(self, other):
        #문자열의 길이 비교
        if self.len == other.len:
            #문자열의 자리수 합 비교
            if self.cnt == other.cnt:
                #문자열의 사전순 비교
                for i in range(self.len):
                    if self.arr[i] != other.arr[i]:
                        return self.arr[i] < other.arr[i]
            return self.cnt < other.cnt
        return self.len < other.len

N = int(input())
#입력 받아서 바로 priorityQueue에 넣기
for i in range(N):
    str = input()
    q.put(SerialNo(str))

while not q.empty():
    tmp = q.get()
    print(tmp.Num)
