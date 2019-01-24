m,n = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
i =0
j =0
le = min(m,n)
ans =[]
while(i<le and j<le):
    if(a[i]<b[j]):
        ans.append(a[i])
        i+=1
    elif(a[i]>b[j]):
        ans.append(b[j])
        j+=1
        
