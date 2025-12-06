# tuple-based sorting
scores = [
    (80, 100),
    (100, 50),
    (70, 100),
    (80, 90),
]

scores.sort(key=lambda x: (-x[0], -x[1]))

for s in scores:
    print(f"English score {s[0]}, Math score {s[1]}")

# dictionary-based sorting
scores = [
    {'english': 80, 'math': 100},
    {'english': 100, 'math': 50},
    {'english': 70, 'math': 100},
    {'english': 80, 'math': 90},
]

scores.sort(key=lambda x : (-x['english'], -x['math']))
for s in scores:
    print(s)


# two-dimensional array

# input
# 3 4
# 1 2 4
# 2 1 10
# 1 3 7
# 3 2 6
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e,w))

for nextNode, weight in graph[1]:
    print(f'next Node {nextNode}, weight = {weight}')
# output
# next Node 2, weight = 4
# next Node 3, weight = 7