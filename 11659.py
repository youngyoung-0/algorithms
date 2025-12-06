import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number_list = list(map(int, input().split()))

prefix_sum = [0]
temp = 0

for i in number_list:
    temp += i
    prefix_sum.append(temp)

for _ in range(M):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start - 1])


