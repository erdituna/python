def format_name(first_name , last_name):
    if first_name == "":
        format_name = str(last_name)+", "+str(first_name)


    elif last_name =="":
        format_name = str(last_name)+", "+str(first_name)


    elif first_name != "" and last_name != "":
       format_name = str(last_name)+", "+str(first_name)


    else:
        format_name = str(last_name)+", "+str(first_name)


    



    return format_name


print(format_name("Ernst","Hemingway"))
print(format_name("","Madonna"))
print(format_name("Voltaire",""))
print(format_name("",""))