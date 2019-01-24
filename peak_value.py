n = int(input(""))
a = list(map(int,input().split()))
ans =-1
i=0
while(i<(n-1) and ans==-1):
    if(a[i]<=a[i+1]):
        i+=1
    else:
        ans = a[i]
print(ans)
