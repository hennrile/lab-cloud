def tongbinhphuong(n):
    if(n<=1):
        return 1
    else:   
        return n*n+tongbinhphuong(n-1)
    
n = int(input('Nhập giá trị n:'))
print(tongbinhphuong(n))
