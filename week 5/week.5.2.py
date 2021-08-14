s = input()
l = []
for i in s:
    if i.isnumeric():
        l.append(i)
l = list(set(l))
l.sort()
for i in l:
    if int(i) % 2 == 0:
        n = i
        l.remove(i)
        l.sort(reverse=True)
        l.append(n)
        f = int(''.join(l))
        print(f)
        break
else:
    print(-1)