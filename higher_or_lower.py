from art import logo,vs
import random
import os
# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')


datas = [
    {
        'name' : 'Instagram',
        'follower_count' : 345,
        'description' : 'Social media platform',
        'country' : 'US'
    },
    {
        'name' : 'Messi',
        'follower_count' : 430,
        'description' : 'Football player',
        'country' : 'Argentina'
    },
    {
        'name' : 'Aarina Grande',
        'follower_count' : 340,
        'description' : 'Artist',
        'country' : 'somewere'
    },
    {
        'name' : 'Ronaldhino',
        'follower_count' : 400,
        'description' : 'Football player',
        'country' : 'Brazil'
    },
    {
        'name' : 'Dwayen Johnson',
        'follower_count' : 420,
        'description' : 'Social media platform',
        'country' : 'US'
    },
    {
        'name' : 'facebook',
        'follower_count' : 346,
        'description' : 'Social media platform',
        'country' : 'US'
    }
]

def formate_data(data):
    """formating data in the printable order"""
    name = data["name"]
    follower = data["follower_count"]
    description = data["description"]
    country = data["country"]
    return(f"{name}, a {description}, from {country}.")

def check_ans(guess, follower_count_a, follower_count_b):
    if follower_count_a > follower_count_b:
        return guess == "a"
    else:
        return guess == "b"
   
    
score = 0
should_continue = True
data_b = random.choice(datas)
while should_continue:
    print(logo)
    # generating random data and comparing it
    data_a = data_b
    data_b = random.choice(datas)
    if data_a == data_b:
        data_b = random.choice(datas)
    

    print(f"Compare A: {formate_data(data_a)}")
    print(vs)
    print(f"Against B: {formate_data(data_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
    follower_count_a = data_a["follower_count"]
    follower_count_b = data_b["follower_count"]

    is_correct = check_ans(guess, follower_count_a, follower_count_b)
    os.system('cls')
    print(logo)
    if is_correct:
        score += 1
        print(f"You are Right!, Current score is {score}")
    else:
        should_continue = False
        print(f"Sorry! that's Worng!!, Your final score is {score}")
        
    
    
    
    
    
    
    
    
    