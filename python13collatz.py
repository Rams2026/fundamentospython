print("CONJETURA DE COLLATZ")
print("introduzca un numero")
n = int(input())
while (n != 1):
    print("numero", n)
    if (n % 2 == 0):
        n = int(n / 2)
        print("numero en if", n)
    else:
        n = n * 3 + 1
        print("numero en else", n)
print("fin de programa")