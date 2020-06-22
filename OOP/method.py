class Circle:
    pi = 3.14

    def __init__(self,yaricap=1):
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return 2 * self.pi + self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)


c1 = Circle()
c2 = Circle(5)

print(f'c1 circle area : {c1.alan_hesapla()} c1 circumference : {c1.cevre_hesapla()}')

print(f'c2 circle area : {c2.alan_hesapla()} c2 circumference : {c2.cevre_hesapla()}')