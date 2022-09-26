def knuth(f):
    p=[]
    N=len(f)
    for i in range(N):
        if p==[]:
            p.append(f.pop())
        else:
            e = f.pop()
            if e >= p[-1]:
                p.append(e)
            else:
                np = []
                while not p==[] and e < p[-1]:
                    np.append(p.pop())
                p.append(e)
                while not np==[]:
                    p.append(np.pop())
    while not p==[]:
        f.append(p.pop())
    print(f)

knuth([2,1,3,5,12,11])