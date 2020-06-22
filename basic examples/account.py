
ErdiHesap = {
    'ad' : 'Erdi Tuna',
    'hesapNo' : '3548967',
    'bakiye'  : 4000,
    'ekHesap'  : 2500
}
AhmetHesap = {
    'ad' : 'Ahmet Turna',
    'hesapNo ' : '3341267',
    'bakiye'  : 3000,
    'ekHesap'  : 1500
}
MuratHesap = {
    'ad' : 'Murat Gümüş',
    'hesapNo' : '1241237',
    'bakiye'  : 6000,
    'ekHesap'  : 1500
}


def paraCek(hesap,miktar):
    print(f"Merhaba {hesap ['ad']}")
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -=miktar    
        print('paranızı alabilirsiniz.')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanımı = input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanımı == 'e':
               eKhesapCekilcekMiktar = miktar - hesap['bakiye']
               hesap['bakiye'] = 0
               hesap['ekHesap'] -= eKhesapCekilcekMiktar
               print('paranızını alabilirsiniz...')
            else:
                print(f"{hesap['hesapNo']} nolu {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüm hesabınızda yeterli bakiye bulunmamaktadır...')

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']}nolu hesabınızda {hesap['bakiye']} TL Bulunmaktadır. Ek hesap liminitiz ise {hesap['ekHesap']} TL dir...")


paraCek(ErdiHesap,2500)
bakiyeSorgula(ErdiHesap)
print('*****************')
paraCek(ErdiHesap,4001)
bakiyeSorgula(ErdiHesap)


