

# (5 points): As a developer, I want to make at least three commits with descriptive messages. 




# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists. 

destination = ['Mexico City', 'New York City', 'City of London', 'Rio de Janeiro', 'Barcelona', 'Hvar', 'Madrid', 'Berlin', 'Paris'] 
food = ['Happy Hour Tavern', 'Irish Delight' , 'Gionos Pizza', 'Mama Mia Italian', 'Hola Amigos Tacos', 'Pad Thai Hour', 'Jerk Chicken Restaurant']
transportation = ['motorcycle', 'bicycle', 'vehicle', 'train', 'moped','electric scooter']
entertainment = ['movies', 'bowling', 'hiking', 'magic show', 'musical', 'music feast', 'bus tour', 'zip line']




# (5 points): As a user, I want a destination to be randomly selected for my day trip. 


import random

def print_greeting():
    print("Hello and welcome to the day trip generator!")
    print("------------------------------------------------")
    print("Take a set and lets get this trip planned!")

def pick_destination():
    random_destination = random.choice(destination)
    user_input = input(f"How does {random_destination} sound for a destination? y/n: ")
    while user_input != "y":
        random_destination = random.choice(destination)
        user_input = input(f"Okay, well what do you think of {random_destination} instead? ")
    return random_destination
         


def pick_resturant():
    random_restaurant = random.choice(food)
    user_input = input(f"How does {random_restaurant} sound for a restaurant? y/n: ")
    while user_input != "y":
        random_restaurant = random.choice(food)
        user_input = input(f"Okay, well what do you think of {random_restaurant} instead? ")
    return random_restaurant
         


def pick_entertainment():
    random_entertainment = random.choice(entertainment)
    user_input = input(f"How does {random_entertainment} sound for a activitiy? y/n: ")
    while user_input != "y":
        random_entertainment = random.choice(entertainment)
        user_input = input(f"Okay, well what do you think of {random_entertainment} instead? ")
    return random_entertainment

def pick_transportation():
    random_transportation = random.choice(transportation)
    user_input = input(f"How does {random_transportation} sound for a activitiy? y/n: ")
    while user_input != "y":
        random_transportation = random.choice(transportation)
        user_input = input(f"Okay, well what do you think of {random_transportation} instead? ")
    return random_transportation

def confirm_trip(destination, transportation, entertainment, restaurant):
    print(f'You are going to {destination} by the way getting around in {transportation}')
    print(f"While you are there, you will be dining at {restaurant} and enjoying the activity of{entertainment} ")
    user_input = input(f"Are you happy with these choices? y/n: ")
    if user_input == "y":
        print('Have a great day trip!')
    elif user_input == 'n':
        run_day_trip()
    

def run_day_trip():
    print_greeting()
    confirmed_destination = pick_destination()
    confirmed_transportation = pick_transportation()
    confirmed_entertainment = pick_entertainment()
    confirmed_restaurant = pick_resturant()
    confirm_trip(confirmed_destination, confirmed_transportation, confirmed_entertainment, confirmed_restaurant)

run_day_trip()




 