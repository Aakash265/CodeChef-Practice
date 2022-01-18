wd, bal = map(float, input().split())
if (wd % 5 == 0 and wd + 0.5 <= bal):
    bal = bal-wd-0.5
    print("%.2f"%bal)
else:
    print("%.2f"%bal)
