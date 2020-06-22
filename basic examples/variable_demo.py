"""
1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz...

Müşteri adı 
Müşteri soyadı 
Müşteri ad + soyad
Müşteri cinsiyet
Müşteri tc kimlik
Müşteri Doğum Yılı
Müşteri adres bilgisi
Müşteri yaşı
"""

clientName = 'Erdi'
clientlastName = ' Tuna ' 
ClientNameSurname = clientName + ' ' + clientlastName
clientGender = True # Erkek
clientId = '1234567890'
ClientBirthdate = 1996
clientAdress = 'Ankara / Batıkent'
ClientAge= 2020 - ClientBirthdate
print(ClientAge)

"""
    2-Aşağıdaki  siparislerin toplam bilgisini hesaplayınız...


Sipariş 1 => 120 TL
Sipariş 2 => 1200.5 TL
Sipariş 3 => 366.95 TL

"""
order1 = 120
order2 = 1200.5
order3 = 366.95
total = order1 + order2 + order3
print("Total :",total)
#print(120+1200.5+366.95) #1687.45