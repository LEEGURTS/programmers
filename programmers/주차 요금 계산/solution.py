// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/92341

import collections
import math
def solution(fees, records):
    answer = []
    timeSet = collections.defaultdict(int)
    sumSet = collections.defaultdict(int)
    def calculate(time):
        if time <= fees[0]:
            return fees[1]
        else:
            return fees[1] + fees[3]*math.ceil(((time-fees[0])/fees[2]))
    
    for item in records:
        time,number,inout = item.split()
        if inout == "IN":
            timeSet[number] = time
        else:
            t1h,t1m = timeSet[number].split(":")
            t2h,t2m = time.split(":")
            t1 = 60*int(t1h) + int(t1m)
            t2 = 60*int(t2h) + int(t2m)
            sumSet[number] += t2-t1
            timeSet[number] = 0
    for item in timeSet.items():
        if item[1] != 0:
            t2h,t2m = item[1].split(":")

            sumSet[item[0]]+=(60*23)+59 - (60*int(t2h) + int(t2m))
            
    result = []
    for i in sorted(sumSet.items()):
        result.append(calculate(i[1]))
    return result