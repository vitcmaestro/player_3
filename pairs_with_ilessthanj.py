n = int(input())
a = list(map(int,input().split()))
c=0
for i in range(n-1):
    for j in range(1,n):
        if(a[i]<a[j]):
            c+=1
print(c)
