n =int(input())
a = list(map(int,input().split()))
a.sort()
miner = 1000
for i in range(n-1):
    if(a[i+1]-a[i] <miner and a[i+1]-a[i]>0):
        miner = a[i+1]-a[i]
print(miner)
