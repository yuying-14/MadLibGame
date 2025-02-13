print("Hello! Welcome to this simple MadLibs Game.")

while True:
    Version = input("Pick a number from 1 to 3: ")

    if Version == "1": 
        print("This Mad Lib is about a Day in New York City!")
        print("Please provide the following to fill in the story.")
        adjective = input("Adjective: ")
        place = input("Place in NYC: ")
        celebrity = input("Famous person: ")
        noun = input("Noun: ")
        verb = input("Verb: ")
        food = input("Food: ")
        transportation = input("Mode of transportation: ")

        madlibs1 = f"Today was a {adjective} day in New York City! I started my adventure at {place}, " \
                   f"where I unexpectedly ran into {celebrity}. They were holding a {noun} and trying to {verb}. " \
                   f"After that, I grabbed some {food} from a street vendor before hopping on a {transportation} " \
                   f"to explore the city. I love NYC <3!" 
        
        print("\nHere is your Wild Day in NYC story:")
        print(madlibs1)
    
    elif Version == "2": 
        print("This Mad Lib is about a nightmare story!")
        print("Please provide the following to fill in the story.")

        animals = input("Animal (plural): ")
        color = input("Color: ")
        body_part = input("Body part (plural): ")
        action = input("Action (verb): ")
        place = input("Place: ")
        obj = input("Object: ")
        adj2 = input("Adjective: ")

        madlibs2 = f"Last night, I had a nightmare about the {animals} in my {place}. " \
                   f"They were {color} with huge {body_part} and they {action} all around. It was terrifying! " \
                   f"I tried to fight them with {obj}, but they were too {adj2}."
        
        print("\nHere is your nightmare story:")
        print(madlibs2)
    
    elif Version == "3":  
        print("This Mad Lib is about a Day in College!")
        print("Please provide the following to fill in the story.")

        adjective = input("Adjective: ")
        college_name = input("College/University Name: ")
        professor_name = input("Professor's Name: ")
        subject = input("Class Subject: ")
        noun = input("Random Noun: ")
        verb = input("Verb: ")
        place_on_campus = input("Place on Campus: ")
        food = input("Food: ")

        madlibs3 = f"Today was a {adjective} day at {college_name}. I woke up late and had to rush to my {subject} class, " \
                   f"taught by Professor {professor_name}. I forgot my {noun} at home, so I had to {verb} my way through class. " \
                   f"After that, I headed to {place_on_campus} to grab some {food}, which was surprisingly delicious! " \
                   f"I hope my day is even better tomorrow!"  

        print("\nHere is your college campus story:")
        print(madlibs3)

    else:
        print("\nInvalid choice! Please enter 1, 2, or 3.\n")
        continue  

    # Option to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break 
