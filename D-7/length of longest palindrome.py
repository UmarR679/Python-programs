s="abba"
m=0
for c in range(len(s)):
    l,r=c,c
    while l>=0 and r<len(s) and s[l]==s[r]:
        m=max(m,r-l+1)
        l-=1
        r+=1
    l,r=c,c+1
    while l>=0 and r<len(s) and s[l]==s[r]:
        m=max(m,r-l+1)
        l-=1
        r+=1
print(m)
 