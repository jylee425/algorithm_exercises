N = int(input())

ans = 0
for _ in range(N):
    tap = int(input())
    ans += tap
ans -= N-1
print(ans)