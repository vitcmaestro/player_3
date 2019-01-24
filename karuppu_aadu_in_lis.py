n = int(input())
a = list(map(int,input().split()))
i =0
b = [str(a[i]%2) for i in range(n)]
c = b.count('1')
if(c ==1):
    check = '1'
else:
    check = '0'
for i in range(n):
    if(b[i] == check):
        print(a[i])
        break
