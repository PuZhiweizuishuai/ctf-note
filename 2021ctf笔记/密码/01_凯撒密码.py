a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
s='lrua{1uy3yj9l-yw9u-48j2-uuj8-36h03706y7u7}'
s='synt{5pq1004q-86n5-46q8-o720-oro5on0417r1}'

for j in range(0,26):
    t=[]
    for i,b in enumerate(s):
        n=a.find(s[i])
        if n==-1:
            t.append(s[i])
            continue
        if n%2==0:
           t.append(a[(n+j)%26])
        elif n%2!=0:
            t.append(a[(n+26-j)%26])
    for i,b in enumerate(t):
        print(t[i],end="")
    print('')
    
    
