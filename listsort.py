from random import randint

p = []

for i in range(6):
    p.append(randint(0, 100))


def insertsort(lists):
    if lists[0] > lists[1]:
        buffer = lists[0]
        lists[0] = lists[1]
        lists[1] = buffer
    else:
        None
    c = 0
    while c != 100:
        a = 1
        if lists[a] > lists[a+1]:
            buffer = lists[a]
            lists[a] = lists[a+1]
            lists[a+1] = buffer

            if lists[a] < lists[0]:
                x = lists[0]
                lists[0] = lists[a]
                lists[a] = x

            c += 1
            a += 1
        else:
            a += 1
            c += 1


print(p)
insertsort(p)
print(p)
            