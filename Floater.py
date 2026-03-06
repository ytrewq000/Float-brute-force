import numpy
n = 0
u = 1.797
e = 308
while True:
    n += 1
    p = numpy.longdouble(f"{u}{n}")
    q = p *10**e
    if q == numpy.longdouble('inf'):
        n -= 1
        u = numpy.longdouble(f"{u}{n}")
        n = 0
        print(u)
    else:
        print(q,p)
    if len(str(p)) == 18:
        break

    
