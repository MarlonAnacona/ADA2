def backspack(w, b, M):
    numElm = len(w)
    bmax = [[0] * numElm for _ in range(M + 1)]

    # Llenar cuando solo hay un elemento
    for i in range(M + 1):
        bmax[i][0] = b[0] if i >= w[0] else 0

    for j in range(1, numElm):
        for i in range(M + 1):
            bmax[i][j] = max(
                bmax[i][j - 1],  # No llevarlo
                bmax[i - w[j]][j - 1] + b[j] if i - w[j] >= 0 else 0  # Llevarlo
            )

    x = [False] * numElm
    i = M
    j = numElm - 1

    while j > 0:
        x[j] = bmax[i][j] != bmax[i][j - 1]
        i = i if bmax[i][j] == bmax[i][j - 1] else i - w[j]
        j = j - 1

    x[0] = bmax[i][0] > 0

    for k in range(M + 1):
        print(bmax[k])

    print(x)

# Ejemplo de uso
weights = [7, 5, 6, 8]
values = [3, 2, 1, 4]
max_weight = 20

backspack(weights, values, max_weight)


def backspack2(w, b, M):
    numElm = len(w)
    bmin = [[0] * numElm for _ in range(M + 1)]

    # Llenar cuando solo hay un elemento
    for i in range(M + 1):
        bmin[i][0] = b[0] if i >= w[0] else 0

    for j in range(1, numElm):
        for i in range(M + 1):
            bmin[i][j] = min(  # Cambio a min en lugar de max
                bmin[i][j - 1],  # No llevarlo
                bmin[i - w[j]][j - 1] + b[j] if i - w[j] >= 0 else 0  # Llevarlo
            )

    x = [False] * numElm
    i = M
    j = numElm - 1

    while j > 0:
        x[j] = bmin[i][j] != bmin[i][j - 1]  # Cambio a bmin en lugar de bmax
        i = i if bmin[i][j] == bmin[i][j - 1] else i - w[j]
        j = j - 1

    x[0] = bmin[i][0] > 0

    for k in range(M + 1):
        print(bmin[k])

    print(x)

# Ejemplo de uso
weights = [7, 5, 6, 8]
values = [3, 2, 1, 4]
max_weight = 20

backspack2(weights, values, max_weight)

