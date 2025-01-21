import random
def get_user_input():
    user_input=input("Please your play choice: ")
    return user_input


def get_cpu_input():
    choices = ['r','p','s']
    cpu_input = random.choice(choices)
    return cpu_input

def play(user,cpu):
    print(f"User choice is {user}")
    print(f"Computer choice is {cpu}")
    if user == cpu:
        return "draw"
    elif user == 'r' and cpu =='p':
        return "Computer wins"

    elif user == 'r' and cpu=='s':
        return "Human wins"

    elif user == 'p' and cpu=='s':
        return "Computer wins"

    elif user == 'p' and cpu=='r':
        return "Computer wins" 

    elif user == 's' and cpu=='r':
        return "Computer wins"   

    elif user == 's' and cpu=='p':
        return "Human wins"        

    else:
        return "game crashed, wrong input from user" 

u=get_user_input()
c=get_cpu_input()

winner=play(u,c)
print(winner)

