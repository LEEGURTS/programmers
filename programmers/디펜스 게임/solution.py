// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/142085?language=python3

def solution(n, k, enemy):
    def isPossible(mid):
        if sum(enemy[:mid+1])-sum(sorted(enemy[:mid+1])[::-1])<=n:
            return True
        else:
            return False
        
    left=0
    right=len(enemy)
    while left<right:
        mid = (left+right)//2
        if isPossible(mid):
            left = mid+1
        else:
            right = mid
    return left