n = int(input())
a = list(map(int,input().split()))
i =0
while(a[i]%2 != 0):
    i+=1
else:
    ans = a[i]
print(ans)
