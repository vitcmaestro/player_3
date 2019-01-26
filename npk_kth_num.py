def fact(n):
    if(n == 0):
        return 1
    x = 1
    for i in range(2,n+1):
        x = x *i
    return x
n,p,k = map(int,input().split())
ans = (fact(n)//fact(n-k))
a = str(ans)
print(a[k+1])
