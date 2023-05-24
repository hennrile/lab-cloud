def tinhtong(n):
    if n == 1:
        return 1
    else:
        return tinhtong(n - 1) + 1/n