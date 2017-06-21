start_story = '''
    Once up on a time, there was a little person named Little Blue Riding Hood.
    That's you! Your grandmother is stuck in her house in the woods and she's extremely hungry.
    She needs your help. Go to the store and get food.
    '''

buy_food = '''
    You paid with counterfeit bills. The storeowners called the cops. They're coming to arrest you.
    '''



steal_food = '''
    You're on the security camera tape and the storeowner called the cops.
    '''

print(start_story)
food = input("Type 'buy' to buy food or type 'steal' to steal it" )

done = False
while not done:
    if food == 'buy':
        print(buy_food)
        police = input("Type 'run' to run from the police or 'convince' to convince the police that you are innocent")
        done = True
    elif food == 'steal':
        print(steal_food)
        police = input("Type 'escape' to run from the police or 'confess' to confess to having stolen food")
        done = True
    else:
        food = input("Type 'buy' or 'steal'")
        done = False




run_police = '''
    You end up running into the forest to get away from the police and encounter the Big Bad Wolf.
    You don't know how to get to grandmother's house, so you ask him for directions.
    He tells you to take a right at the next fork in the path.
    '''
convince_police = '''
    You try to convince the police that you are innocent and that you didn't know that your currency was counterfeit.
    Though you try to do this in a civil manner, when you reach into your pocket to pull out more bills,
    the police shoot you 13 times, believing that you had malicious intent. Your grandmother starves to death.
    '''
escape_police = '''
    You end up running into the forest to get away from the police and encounter the Big Bad Wolf.
    You don't know how to get to grandmother's house, so you ask him for directions.
    He tells you to take a right at the next fork in the path.
    '''
confess_police = '''
    You decide to confess to the police that you were stealing food in order to save your starving grandmother.
    Unfortunately, you end up going to jail and your grandmother starves to death.
    You get into a brawl with your cellmate and die.
    '''
game_over = '''
    Yikes! You're done. GAME OVER.
    '''

done = False
while not done:
    if police == 'run':
        print(run_police)
        done = True
    elif police == 'convince':
        print(convince_police)
        print(game_over)
        quit()
        done = True
    elif police == 'escape':
        print(escape_police)
        done = True
    elif police == 'confess':
        print(confess_police)
        print(game_over)
        quit()
        done = True

turn_right = '''
    You take at the fork as per the wolf's instructions. You end up getting lured into a bear trap.
    The wolf rips you apart and eats you. You are DEAD. Grandmother starves to death.
    '''

turn_left = '''
    You end up getting to grandmother's house safely, but hear odd noises from inside.
    '''
direction = input("Type 'right' to turn right or type 'left' to turn left")

done = False
while not done:
    if direction == 'right':
        print(turn_right)
        print(game_over)
        quit()
        done = True
    if direction == 'left':
        print(turn_left)
        done = True
    else:
        direction = input("Type 'right' or 'left'")
        done = False

go_inside = '''
    You go inside the house, disregarding the noises. The wolf and grandma are inside and savagely roast you for
    having horrible grades. Then they roast you over a fire and eat you. You are DEAD.
    '''

call_hunter = '''
    Grandmother's hunky next-door neighbor happens to be a hunter.
    You call him for backup before entering the house. You find the wolf inside the house and the hunter kills him
    with an ax. The hunter turns out to be a serial killer and murders you and your grandmother. You are DEAD.
    '''

action = input("Type 'go inside' to go inside anyway or type 'call hunter' to ask the hunter for help")

done = False
while not done:
    if action == 'go inside':
        print(go_inside)
        print(game_over)
        quit()
        done = True
    if action == 'call hunter':
        print(call_hunter)
        print(game_over)
        quit()
        done = True
    else:
        action = input("Type 'go inside' or 'call hunter'")
        done = False
