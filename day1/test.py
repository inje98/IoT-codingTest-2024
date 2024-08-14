N = 17
K = 4

def sol99(N, K):
    count = 0
    while(N != 1):
        while (N % K == 0):
            N = int(N / K)
            count += 1
        if (N != 1):
            N = N - 1
            count += 1
    
    return count

        
print(sol99(N, K))