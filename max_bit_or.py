n = int(input())
a = list(map(int,input().split()))
maxer = 0
for i in range(n):
    for j in range(n):
        if(a[i]|a[j] > maxer):
            maxer = a[i]|a[j]
print(maxer)
