import random

sayi = random.randint(1,100)
can = int(input('kac hak kullanmak istersiniz  : '))
hak = can
print(sayi)
sayac = 0
puan=100

while  hak > 0:
        
        hak -=1
        sayac=sayac+1
        
        tahmin = int(input('tahmin:'))

        if sayi==tahmin:
            print(f'tebriler {sayac}.defada bildiniz. Toplam puanınız : {100- (100/can) * (sayac-1)}')
            break
        elif sayi > tahmin:
            print('yukari')
          
        else:
            print('asagi')
           
        if hak ==0:
            print(f'hakkiniz bitti. puanınız : 0')
