def maxi(p):
    if p==[]:
        return 0
    return max(p)

def partitions(n):
    if n==0:
        return [[]]
    return [[n-j]+p for j in range(n) for p in partitions(j) if n-j >= maxi(p)]

print(len(partitions(14)))