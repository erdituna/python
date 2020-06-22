# error handling => hata yöntemi

while True:
        
    try:
        x = int(input('x : '))
        y = int(input('y : '))
        print(x/y)
    except (ZeroDivisionError,ValueError):
        print('yanlis bilgi girdiniz')
        
    else:
        break