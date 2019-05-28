a = [4,2,3,2,1,1]
t = len(a)
b = [1] * 8
for i in range(t):
    b[i] = a[i]

candi = []
for i0 in range(b[0]):
    for i1 in range(b[1]):
        for i2 in range(b[2]):
            for i3 in range(b[3]):
                for i4 in range(b[4]):
                    for i5 in range(b[5]):
                        for i6 in range(b[6]):
                            for i7 in range(b[7]):
                                tmp = (i0,i1, i2, i3, i4, i5, i6, i7)
                                print(tmp[:t])

