import random



names = ["adeel","ahad" ,"asad","babar","danish","faizan"]
actions =["eating","sleeping","working","playing","running","coding"]
places =["park","mall","office","home","school","restaurant"]


while True:
    name = random.choice(names)
    action = random.choice(actions)
    place = random.choice(places)
    print(f"{name} is {action} at the {place}")
    user_input = input("press enter or type exit : ")
    if user_input.lower() == 'exit':
        break