def printName(i, n):
    if i > n:
        return
    print("park")
    printName(i + 1, n)

printName(1, 5)