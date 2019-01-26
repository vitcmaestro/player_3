s = input()
n =0
a =[]
for i in range(len(s)-1,-1,-4):
    if(i-3 >=0):
        temp =s[i-3:i+1]
        a.insert(0,temp)
    elif(i-2 == 0):
        temp = '0'+s[i-2:i+1]
        a.insert(0,temp)
    elif(i-1 == 0):
        temp = '00'+s[i-1:i+1]
        a.insert(0,temp)
    elif(i == 0):
        temp = "000"+s[i]
        a.insert(0,temp)
s =""
for j in a:
    x =3
    n =0
    for i in j:
        n = n +(int(i)*(2**x))
        x-=1
    if(n<=9):
        s = s+str(n)
    else:
        t = chr(n+55)
        s = s +t
print(s)
    
