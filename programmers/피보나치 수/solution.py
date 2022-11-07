// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12945?itm_content=course14743

def solution(n):
    answer = 0
    array = [1,1]
    for i in range(1,n):
        array.append(array[i]+array[i-1])
    return array[n-1]%1234567