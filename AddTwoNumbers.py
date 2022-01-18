N = int(input())
lst = []
for i in range(N):
    (a, b) = map(int, input().split())
    ans = a + b
    lst.append(ans)

for i in range(len(lst)):
    print(lst[i])