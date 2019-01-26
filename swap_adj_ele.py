n = int(input(""))
a = list(map(int,input().split()))
for i in range(0,(n-1),2):
    a[i],a[i+1] = a[i+1],a[i]
for i in range(n):
    if(i == (n-1)):
        print(a[i],end="")
    else:
        print(a[i],end = " ")
