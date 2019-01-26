n,z = map(int,input().split())
ans = 0
for i in range(n,z+1):
    if(i%2 !=0):
        ans = ans+i
print(ans)
