sayi = int(input('sayi giriniz : '))
asalmi = True

if sayi == 1:
    print('1 asal sayi değildir.')

for i in range(2,sayi):
    if (sayi % i == 0) :
        asalmi = False
        break
if asalmi:
        print('asaldır.')
else:
        print('asal degildir.')