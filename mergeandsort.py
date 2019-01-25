m,n = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
i =0
j =0
le = min(m,n)
ans =[]
while(i<le and j<le):
    if(a[i] == b[j]):
        ans.append(a[i])
        ans.append(b[j])
        i+=1
        j+=1
    elif(a[i]<b[j]):
        ans.append(a[i])
        i+=1
    elif(a[i]>b[j]):
        ans.append(b[j])
        j+=1
if(m>n):
    for x in range(i,m):
        ans.append(a[x])
elif(m<n):
    for x in range(j,n):
        ans.append(b[x])
for z in range(len(ans)):
    if(z == len(ans)-1):
        print(ans[z],end ="")
    else:
        print(ans[z],end =" ")
    
