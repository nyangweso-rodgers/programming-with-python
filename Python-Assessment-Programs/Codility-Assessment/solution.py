# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, K):
    # Implement your solution 
    N >= 1
    K >= 1
    # one glass and more than 2 litres of Water
    if (N == 1 and K >= 2):
        return -1
    # 
    if K % N == 2:
        return N
    
    # 
    if K % N == 3:
        return 2
    # K is divisible by N
    #if K % N == 0:
        #return 2
    if (N // K == 2):
        return 1
    # N is not divible by K and N >= K
    if (N % K != 0 and N >= K) or (K % N != 0 and N >= K):
        return 1
    
print(solution(5, 8))
#print(solution(6, 12))
#print(solution(4,10))