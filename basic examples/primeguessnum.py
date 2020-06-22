# def yazdir(kelime,adet):
#     print(kelime * adet)

# yazdir('merhaba\n',10)

# def listeyeCevir(*params):
#     liste = []

#     for param in params:
#         liste.append(param)

#     return liste

# result = listeyeCevir(10,20,30,'merhaba')   
# print(result)


def asalSayiBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2):
        if sayi > 1:
            for i in range(2,sayi):
                if(sayi % i == 0):
                    break
            else:
                print(sayi)



sayi1 = int(input('1. sayi giriniz :'))
sayi2 = int(input('2. sayi giriniz :'))
asalSayiBul(sayi1,sayi2)
