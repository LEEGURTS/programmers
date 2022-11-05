// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/92342

def solution(n, info):
    answer = []
    result = []
    def getFullScore(lion,appeach):
        score = 0
        for i in reversed(range(1,11)):
            multipier = 0
            if (lion[10-i]-appeach[10-i])>0:
                multipier = 1
            elif lion[10-i] == 0 and appeach[10-i] == 0:
                multipier = 0
            else:
                multipier = -1
            score+=multipier*i
        return score

    def dfs(lion,depth):
        summation = sum(lion)
        if summation > n or depth > 11:
            return False
        if summation == n and getFullScore(lion,info)>0:
            result.append(lion[:])
            
        for i in range(depth,11):
            temp = lion[i]
            lion[i] = n-summation if n-summation < info[i]+1 else info[i]+1
            dfs(lion,i+1)
            lion[i] = temp
            
    dfs([0 for i in range(11)],0)
    
    return [-1] if not result else sorted(list(result),key=lambda x:(getFullScore(x,info),x[::-1]),reverse=True)[0]