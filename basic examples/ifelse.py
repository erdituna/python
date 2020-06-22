
'''
1.Örnek
'''

# isim = input('isminiz: ')
# yas = int(input('yasiniz: '))
# egitim = input('egitim: ')
# if (yas>=18) and (egitim=='lise' or egitim=='üniversite'):
#     print('ehliyet alabilirsiniz.')
# else:
#     print('ehliyet alamazsiniz.')
'''
2.Örnek
'''
# ogrnot1 = int(input('1.not : '))
# ogrnot2 = int(input('2.not : '))
# ogrnot3 = int(input('sözlü notu : '))
# avarage = (ogrnot1 + ogrnot2 + ogrnot3)/3
# if (avarage>=0) and (avarage<25):
#     print(f'ortalamananız: {avarage} notunuz : 0' )
# elif (avarage >=25 ) and (avarage <45):
#     print(f'ortalamananız: {avarage} notunuz : 1'  )
# elif (avarage >=45 ) and (avarage <55):
#     print(f'ortalamananız: {avarage} notunuz : 2'  )
# elif (avarage >=55 ) and (avarage <69):
#     print(f'ortalamananız: {avarage} notunuz : 3'  )    
# elif (avarage >=69 ) and (avarage <85):
#     print(f'ortalamananız: {avarage} notunuz : 4'  )
# elif (avarage >=85 ) and (avarage <=100):
#     print(f'ortalamananız: {avarage} notunuz : 5'  )
'''
3.Örnek
'''
# import datetime

# tarih = input('araciniz kac gündür trafikte: (2019/4/10) ')
# tarih = tarih.split('/')

# trafigeCikis = (datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2])))
# simdi = datetime.datetime.now()
# fark = simdi - trafigeCikis
# days = fark.days

# if days<=365:
#     print('1.servis aralığı')
# elif days > 365 and days <= 365*2:
#     print('2.servis aralığı')
# elif days > 365*2 and days <= 365*3:
#     print('3.servis aralığı')
# else:
#     print('hatalı süre.')



