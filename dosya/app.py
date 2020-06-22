def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    notlar = liste[1].split(',')

    ogrenciAdi = liste[0]
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    
    ortalama = (not1+not2+not3)/3

    if ortalama >= 90 and ortalama <=100:
        harf = "A1"
    elif ortalama >=80 and ortalama <=89:
        harf = "A2"
    elif ortalama >=70 and ortalama <=79:
        harf = "B1"
    elif ortalama >=65 and ortalama <=69:
        harf = "B2"
    elif ortalama >=60 and ortalama <=65:
        harf = "C"
    else:
        harf = "F3"
    return ogrenciAdi + " : " + harf + "\n"
    



def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input('Öğrenci adi  :')
    soyad = input('Öğrenci soyadi  :')
    not1 = input('1.notu giriniz  :')
    not2 = input('2.notu giriniz  :')
    not3 = input('3.notu giriniz  :')

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad + ' ' +soyad+ ' : '+not1+','+not2+','+not3+'\n')


def notlari_kayitet():
      with open("sinav_notlari.txt","r",encoding="utf-8") as file:
          liste = []

          for i in file:
            liste.append(not_hesapla(i))
          with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem = input('1- Notları oku\n2-Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n')
    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kayitet()
    else:
        break
