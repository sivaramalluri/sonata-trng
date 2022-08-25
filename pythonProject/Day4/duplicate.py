def dup(i):
    j=[]
    for x in i:
        if x not in j:
            j.append(x)
    return j
def dup1(i):
    return list(set(i))

a=[1,2,3,4,4,3,6,7,41,8,9,10,2,8]
print(a)
print(dup(a))
print(dup1(a))