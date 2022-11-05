// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/133501

def solution(distance, scope, times):
    answer = 0
            
    detection = []
    
    for i in range(len(scope)):
        start,end = sorted(scope[i])
        watch,rest = times[i]
        time = start
        while time<=end:
            if 0<time%(watch+rest)<=watch:
                detection.append(time)
                break
            time+=1
    return distance if not detection else sorted(detection)[0]