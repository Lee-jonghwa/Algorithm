N = int(input())
weights = list(map(int,input().split()))

times = 0

while len(weights) > 1:
    weights.sort()
    times += weights[0] + weights[1]
    weights.append(weights[0] + weights[1])
    weights.pop(0)
    weights.pop(0)

print(times)