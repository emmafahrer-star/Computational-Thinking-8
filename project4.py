print("Welcome to the Good Life physical therapy app")
activity = "no activity logged yet"
achievements ="you are getting stronger!"
progress = "You  are so close to getting some more challenging exercises! Good job!"
exercises = "25 pushups, IT band stretch, and 1 min plank"

# for loop starts here line 8-21
for i in range (5):
    choice = input("would you like to look at your progress, achievements, see exercises or log activity")

    if choice == "progress":
        print(f"{progress}")
    elif choice == "achievements":
        print(f"your achievements are that {achievements}")
    elif choice == "see exercises" or choice == "exercises":
        print(f"your exercises are {exercises}")
    elif choice == "log activity" or choice == "activity":
        print(f"{activity}")
        activity = input("Type here to input any activity you have done")
    else:
        print("HUH? Thats not an option, silly. Pick again")
print("Thank you for using the Good Life physical therapy app! Have and AMAZING day!")
