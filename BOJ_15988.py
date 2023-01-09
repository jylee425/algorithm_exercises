

def dp(T):
    """
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    """
    memo = [1] + [2] + [4] + [0] * 1000000
    
    for i in range(3, 1000000 + 3):
       memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
       memo[i] = memo[i] % 1000000009

    for _ in range(T):
        N = int(input())
        print(memo[N-1])
        


if __name__ == '__main__':
    T = int(input())

    dp(T)
