MAX = 1000000

def dp():
    """
    Body:
        sum of euler_phi(N) over [1,N]
    Return:
        None; save cumulative sum as global var
    """
    global S

    memo = [0] * (MAX + 1)
    S    = [0] * (MAX + 1) # cumulative sum until i

    for i in range(1, MAX+1):
        j = 1
        while i * j <= MAX:
            memo[i*j] += i
            j += 1
        S[i] = S[i-1] + memo[i] 
    
if __name__ == "__main__":
    dp()

    T = int(input())
    
    ans = []
    for _ in range(T):
        ans.append(S[int(input())])
    print('\n'.join(map(str,ans))+'\n')
    
