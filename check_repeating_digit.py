n = input("")
a = []
c = 0
for i in n:
    if i in a:
        c = 1
    else:
        a.append(i)
if(c == 0):
    print("no")
else:
    print("yes")
