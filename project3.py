Blair_points = 0
Serena_points = 0
Jenny_points = 0
Vanessa_points = 0

answer1 = input("Do you prefer A-shopping, B-partying, C-doing a hobby, or D-going to a museum")
if answer1 == "A":
    Blair_points += 1
elif answer1 == "B":
    Serena_points += 1
elif answer1 == "C":
    Jenny_points += 1
else:
    Vanessa_points += 1
    Blair_points -=1

answer2 = input("Where would you vacation, A-Paris, B-South America, C-Hudson NY,or D-Greece")
if answer2 == "A":
    Blair_points += 1
elif answer2 == "B":
    Serena_points += 1
elif answer2 == "C":
    Jenny_points += 1
else:
    Vanessa_points += 1

answer3 = input(" What job would you want to have, A-President, B-Pursue social media, C-Fashion Designer, D-Director/Photographer")
if answer3 == "A"or "a":
    Blair_points += 1
elif answer3 == "B":
    Serena_points += 1
elif answer3 == "C":
    Jenny_points +=1
else:
    Vanessa_points +=1

answer4 = input("Which cake would you pick, A-Lava cake, B-Red velvet, C-Funfetti cake, or D-Oreo cake")
if answer4 == "A":
    Blair_points +=1
elif answer4 == "B":
    Serena_points +=1
elif answer4 == "C":
    Jenny_points +=1
else:
    Vanessa_points +=1

answer5 = input("What color would you dye your hair A-light pink, B-brown, C-Bleach blonde, D-Blue")
if answer5 == "A":
    Serena_points +=1
elif answer5 == "B":
    Blair_points +=1
elif answer5 == "C":
    Jenny_points +=1
else:
    Vanessa_points +=1

answer6 = input("What is the best part about yourself? A-Your money, B-Your power, C-Your personality, D-Your integrity")
if answer5 == "A":
    Serena_points +=1
elif answer5 =="B":
    Blair_points +=1
elif answer5 == "C":
    Jenny_points +=1
else:
    Vanessa_points +=1

#End of QUIZZZZZZZ
#Blair Ending
if Blair_points > Serena_points and Blair_points > Jenny_points and Blair_points > Vanessa_points:
    print("You are a Blair, you're popular, a great leader, and love to be in charge")
#Serena Ending    
elif Serena_points > Jenny_points and Serena_points > Vanessa_points:
    print("You are a Serena! The party dosen't start until you get there!The attention is always on you (Good or Bad ;))... And you'll do anything for your family")
#Jenny Ending
elif Jenny_points > Vanessa_points:
    print("You are a Jenny! You love doing a hobby, you hate being underestimated, and you have the coolest outfits")
#Vanessa Ending
else:
    print("You are a Vanessa! You don't follow stereotypes, You are very independent, and you always do the right thing")

