
## WAP to print uniqui word in a given string??

s="tus kum kumar tus pandaaaa tus kum"
s1=s.split()
d={}
for i in s1:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
for j in d:
    if d[j]==1:
        print(j)
