def ExG(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        return ExG(n - 1) + 2 * ExG(n - 2) + 3 * ExG(n - 3)

Resultado = ExG(4)
print(Resultado)



