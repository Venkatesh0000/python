l = [0, 2, 4, 6, 8]
t = (1, 3, 5, 7)
t1 = list(t)
m = len(l)
n = len(t)
res = []
for i in range(m + n):
    if i % 2 == 0:
        res.append(l[0])
        l.remove(l[0])
    else:
        res.append(t1[0])
        t1.remove(t1[0])
print(res)