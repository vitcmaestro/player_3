n = int(input())
s =""
while(n>0):
    r = str(n%2)
    s = s+r
    n = n//2
print(s[::-1])
