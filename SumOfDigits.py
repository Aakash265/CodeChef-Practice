n = int(input())
ans = []

for i in range(n):
    lst = []
    ele = int(input())
    ele = str(ele)
    for j in ele:
        lst.append(int(j))
    ans.append(sum(lst))

for i in ans:
    print(i)