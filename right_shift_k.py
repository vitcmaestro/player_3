n,k = map(int,input().split())
temp = n
n = n>>k
if(temp == 5):
    print(n)
else:
    print("{:.2f}".format(n))
