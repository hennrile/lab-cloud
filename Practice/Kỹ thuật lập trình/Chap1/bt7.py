import time
def tuoi(ns):
    x = time.localtime()
    age = x[0] - ns
    return age

ns = int(input("Nhap nam sinh " ))
print(tuoi(ns))