def sayHello(name='user'):
    return 'hello '+ name

msg = sayHello('ahmet')
msg = sayHello('ada')


print(msg)

def total(num1,num2):
    return num1 + num2

result = total(10,20)
print(result)

def yasHesapla(dogumYili):
    return 2020- dogumYili

ageErdi = yasHesapla(1996)

print(ageErdi)


def EmekliligeKacyilKaldi(dogumYili,isim):
        yas=yasHesapla(dogumYili)
        emeklilik = 65-yas

        if emeklilik >0:
            print(f'{isim} bey emekliliğinize {emeklilik} yıl kaldi')
        else:
            print('Emekli Oldunuz...')

EmekliligeKacyilKaldi(1996,'erdi')
EmekliligeKacyilKaldi(1965,'mehmet')
EmekliligeKacyilKaldi(1950,'musa')


                