answer1 = input("school is over! where do you want to go? The mall, a cafe, the zoo?")
if answer1 == "The mall":
    answer2 = input("yay What store do you want to go to? brandy, aritzia, aero, or garage???") 
    if answer2 == "brandy":
        print ("Yay you got an adorable skirt! Cute find!")
    elif answer2 == "aritzia":
        print ("ooh everything is so cute but it's really expensive! We didn't get anything!")
    elif answer2 == "aero":
        print("Yay! you got the cutest sweatpants! Perfect for fall!")
    else:
        print ("OMG you found the perfect tank top! and you got the last one! Jealous!")
elif answer1 == "a cafe":
    answer3 = input ("Do you want a croissant or a hot chocolate, or both?")
    if answer3 == "croissant":
        print("Yum! So delicious!")
    elif answer3 == "hot chocolate":
        print ("Its the perfect temperature! So cozy!")
    else:
        print ("Yummy! I got both too!")
elif answer1 == "the zoo":
    answer4 = input ("OMG you randomly saw your friend there! Fun! What animals do you want to see? reptiles or zebras?")
    if answer4 == "zebras":
        print("OMG there so cool! You got to feed one!")
    else:
        print("Wow there so big! Kinda scary...")
else:
    print("We didn't do anything")