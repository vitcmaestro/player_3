n = int(input())
a = list(map(int,input().split()))
c = 1
maxer = 0
for j in range(n-1):
    if(a[j]<a[j+1]):
        c+=1
        if(c>maxer):
            maxer = c
    else:
        c = 0
print(maxer)
