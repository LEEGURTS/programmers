// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12918?itm_content=course14743#

def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        return False
    return s.isdigit()
