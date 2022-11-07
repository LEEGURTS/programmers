// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12930?itm_content=course14743

def solution(s):
    answer = ''
    count = 0
    for word in s:
        if word == ' ':
            answer+=' '
            count = 0
        elif count%2 == 0:
            answer+=(word.upper())
            count+=1
        else:
            count+=1
            answer+=(word.lower())
    return answer