#시간 초과

N = int(input())
#input 저장 배열
lecture = []
#필요한 강의실 수를 저장할 배열
timeline = []

for i in range(N):
    lec = list(map(int, input().split()))
    #강의 시간 추가
    lec.append(lec[2]-lec[1])
    lecture.append(lec)

#강의 시간을 기준으로 내림차순 정렬
lecture.sort(key=lambda x:x[3], reverse=True)


for i in lecture:
    start = i[1]
    end = i[2]
    if(len(timeline) == 0):
        lec = [start, end]
        timeline.append(lec)
    else:
        check = False
        for j in timeline:
            t_start = j[0]
            t_end = j[1]
            #기존 강의의 시작 시간 보다 끝나는 시간이 앞이라면 추가
            if end <= t_start:
                j[0] = start
                check = True
                break
            #기존 강의가 끝난 후에 시작이라면 추가
            elif t_end <= start:
                j[1] = end
                check = True
                break
        #기존 강의들과 시간이 맞지 않으면 강의실 추가
        if check == False:
            lec = [start, end]
            timeline.append(lec)


print(len(timeline))
