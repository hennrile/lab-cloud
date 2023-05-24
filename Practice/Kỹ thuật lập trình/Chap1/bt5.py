def sx(x):
    for i in range(len(ds) - 1):
        for j in range (i + 1, len(ds)):
            if ds [i] > ds [j]:
                temp = ds[i]
                ds[i] = ds[j]
                ds[j] = temp
    return ds
ds = [3,2,4,6,7]
print(sx(ds)) 