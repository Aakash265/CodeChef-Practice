# cook your dish here
n = int(input())
lst = []
for i in range(n):
    ele = int(input())
    ele = str(ele)
    lst = list(ele)
    ans = int(lst[0])+int(lst[len(lst)-1])
    print(ans)