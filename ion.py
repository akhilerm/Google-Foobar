def answer (h, q):
    root = pow(2, h) - 1
    p = []
    for i in q:
        if (i < root):
            p.append(find(root, i, root-1))
        else:
            p.append(-1)
    return p

def find(r, e, temp):
    temp/=2
    right = r-1
    left = r-1-temp
    if right == e or left == e:
        return r
    else:
        if e<=left:
            return find(left, e, temp)
        else:
            return find(right, e, temp)
height = 5
queue = [19,13,28]
print answer(height,queue)
