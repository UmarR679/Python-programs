def p(a,b):
    if b==0:
        return 1
    return a*p(a,b-1)
a,b=map(int,input().split())
print(p(a,b))