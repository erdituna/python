
def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("parola en az 7 karakter olmalı")
    elif not re.search("[a-z]",psw):
        raise Exception("parola küçük harf içermelidir.")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola Büyük harf içermelidir.")
    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam içermelidir.")
    elif not re.search("[_@$.]",psw):
        raise Exception("parola alpha numeric harf içermelidir.")
    elif re.search("\s",psw):
        raise Exception("parola boşluk içermemelidir.")
    else:
        print("password is created...")

password = "12345678aB_"

try:
    check_password(password)
except Exception as ex:
    print(ex)
finally:
    print("validation completed...")

