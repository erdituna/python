import random
                  
def name_to_number(name):
    
    if(name=="rock"):
        number = 0
    elif(name=="Spock"):
        number = 1
    elif(name=="paper"):
        number = 2
    elif(name=="lizard"):
        number = 3
    else:
        number = 4
    return number

    
def number_to_name(number):
  
    if(number == 0):
        name ="rock"
    elif(number == 1):
        name ="Spock"
    elif(number == 2):
        name ="paper"
    elif(number == 3):
        name ="lizard"
    else:
        name ="scissors"
    return name


def rpsls(player_choice):
  
    print ("")
    print ("Player Chooses", player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print ("Computer chooses ", comp_choice)
    difference = (player_number - comp_number) % 5
    if ((difference == 1) or (difference == 2)):
        print ("Player wins!")
    elif (difference == 0):
        print ("It's a tie!")
    else:
        print("Computer wins!")


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



                                                                                           