def fascinating(n):
    D = 2 * n
    T = 3 * n
    combined = str(n) + str(D) + str(T)

    if len(combined) != 9:
        return False
    return sorted(combined) == list('123456789')

v = int(input("Enter a number:"))
print(fascinating(v))