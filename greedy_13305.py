n = int(input())
dists = list(map(int, input().split(' ')))
costs = list(map(int, input().split(' ')))

c = costs[0]
res = c * dists[0]
for i, cost in enumerate(costs):
    if i == len(costs)-1:
        break
    elif i == 0:
        continue

    if c < cost:
        res += c * dists[i]
    else:
        c = cost
        res += c * dists[i]

print(res)
