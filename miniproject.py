import math
print(' Enter the numbers with comma separation ')
n=input("enter the numbers:-")
list=n.split(',')
for h in range(len(list)):
    list[h]=int(list[h])
    s=5*list[h]**2 + 4
    p=math.sqrt(s)
    p=round(p)
    psqrt=p*p
    q=5*list[h]**2 - 4
    q=abs(q)
    t=math.sqrt(q)
    t=round(t)
    qsqrt=t*t
    if (s==psqrt or q==qsqrt):
        print(list[h],"valid")
    else:
        print(list[h],"invalid")



























