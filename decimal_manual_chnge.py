s = input()
n =0
x = (len(s)-1)
for i in s:
    n = n +(int(i)*(2**x))
    x-=1
print(n)
