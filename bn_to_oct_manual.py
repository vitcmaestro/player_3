s = input()
n =0
a =[]
for i in range(len(s)-1,-1,-3):
    if(i-2 >=0):
        temp =s[i-2]+s[i-1]+s[i]
        a.insert(0,temp)
    elif(i-1 == 0):
        temp = '0'+s[i-1]+s[i]
        a.insert(0,temp)
    elif(i == 0):
        temp = "00"+s[i]
        a.insert(0,temp)
s =""
for j in a:
    x =2
    n =0
    for i in j:
        n = n +(int(i)*(2**x))
        x-=1
    s = s+str(n)
print(s)
    
