def fact(n):
    if(n == 0):
        return 1
    x = 1
    for i in range(2,n+1):
        x = x *i
    return x
n,k = map(int,input().split())
ans = (fact(n)//(fact(k)*fact(n-k)))
print(ans)
