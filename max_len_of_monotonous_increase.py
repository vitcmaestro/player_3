n = int(input())
a = list(map(int,input().split()))
c = 0
maxer = 0
for j in range(n-1):
    if(a[j]<a[j+1]):
        c+=1
    else:
        if(c>maxer):
            maxer = c+1
        c = 0
print(maxer)
