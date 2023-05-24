'''def tinhtong(n):
    if n==1:
        tong= 1
    else:
        tong= tinhtong(n-1)+1/n
    return tong 
    '''
def tinhtong(n):
    if n==1:
        return 1
    else:
        return tinhtong(n-1)+1/n
n=int(input('Nhập vào số nguyên n:'))
print(tinhtong(n))
