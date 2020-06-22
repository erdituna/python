# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#        print('inner')
#        return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1,num2)

# outer(10)


# def factorial(number):
    
#     def inner_factorial(number):
#         if number <= 1:
#             return 1
#         return number * inner_factorial(number-1)
    
#     return inner_factorial(number)


# print(factorial(5))


def yetki_sorgula(page):
    def inner(role):
        if role == 'Admin':
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)

    return inner

user1 = yetki_sorgula("Product Edit")
print(user1("Admin"))
print(user1('User')) 