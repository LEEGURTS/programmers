// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/140107

def solution(k, d):
    answer = 0
    now = 0
    while now <= d:
        yAxis = (d*d - now*now)**0.5
        answer += int(yAxis)//k + 1
        now+=k
    return answer