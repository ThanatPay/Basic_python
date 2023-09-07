def factor(n):
    for val in range(1,n+1):
        if n%val==0:
            yield val

f=factor(10)
print(next(f))
print(next(f))
print(next(f))
print(next(f))

def gen_num():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for g in gen_num():
    if g>100:
        break
    print(g)