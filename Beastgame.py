import random

# Game loop
while True:

    ##game title##
    print("🌴 WELCOME TO THE JUNGLE OF DOOM 🌴")
    print("\nYou wake up in a dark jungle.")
    print("You have three items to choose from... choose wisely\n")

    # Randomize the 3 foods
    foods = ["Honey", "Trash", "Zebra Meat"]
    random.shuffle(foods)

    box1 = foods[0]
    box2 = foods[1]
    box3 = foods[2]

    print("A 🧌 shaman appears with 3 mystery boxes...")
    print("1. Mystery Box 1")
    print("2. Mystery Box 2")
    print("3. Mystery Box 3")
    print("\nChoose your boxes (type numbers like: 1 2 3):")
    choices = input("Your choices: ")

    # Initialize what player has
    has_Honey = False
    has_Trash = False
    has_Zebra_meat = False

    ##Choice selected##
    if "1" in choices:
        if box1 == "Honey":
            has_Honey = True
        elif box1 == "Trash":
            has_Trash = True
        else:
            has_Zebra_meat = True
    if "2" in choices:
        if box2 == "Honey":
            has_Honey = True
        elif box2 == "Trash":
            has_Trash = True
        else: 
            has_Zebra_meat = True
    if "3" in choices:
        if box3 == "Honey":
            has_Honey = True
        elif box3 == "Trash":
            has_Trash = True
        else:
            has_Zebra_meat = True

    print("\n📦 You are carrying:")
    if has_Honey == True:
        print("   - Honey 🍯")
    if has_Trash == True:
        print("   - Trash 🗑️")
    if has_Zebra_meat == True:
        print("   - Zebra Meat 🦓")

    # Randomize which beast is on which path
    beasts = ["Tiger", "Lion", "Bear", "Raccoon"]
    random.shuffle(beasts)

    path1_beast = beasts[0]
    path2_beast = beasts[1]
    path3_beast = beasts[2]
    path4_beast = beasts[3]

    ##Choice path##
    print("\nFour paths lie before you:")
    print("1. Path to Chicago ❄️ - Cold, dark, damp. A beast roams this realm")
    print("2. Path to Helsinki 🌤️ - Sunny, warm, calm. A beast roams this realm")
    print("3. Path to Sydney 🔥 - Hot, dry, cracked. A beast roams this realm")
    print("4. Path to Cairo 🌵 - Scorching, dead, sandy. A beast roams this realm")
    path_choice = input("Which path do you take? (1, 2, 3, or 4): ")

    # PATH 1
    if path_choice == "1":
        if path1_beast == "Tiger":
            print("\n🐯 A Ferocious TIGER emerges!")
            print("Danger: 9/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")
            
            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Tiger's favorite food is... HUMAN MEAT!")
                print("It doesn't want your food!")
                print("💀 DEATH PERCENTAGE: 99%")
                print("💀 YOU DIE!")
            else:
                print("\nYou try to run away...")
                survival_roll = random.randint(1, 100)
                if survival_roll <= 99:
                    print("💀 DEATH PERCENTAGE: 99%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ MIRACLE! You barely escaped!")
        
        elif path1_beast == "Lion":
            print("\n🦁 A Massive LION emerges!")
            print("Danger: 7/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")
            
            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Lion's favorite food is... Zebra Meat!")
                
                if food_choice == "Zebra Meat" and has_Zebra_meat == True:
                    print("✅ YOU WIN! The lion is satisfied and lets you pass!")
                else:
                    print("Wrong food!")
                    print("💀 DEATH PERCENTAGE: 89%")
                    print("💀 YOU DIE!")
            else:
                print("\nYou try to sneak past...")
                survival_roll = random.randint(1, 100)
                if survival_roll <= 89:
                    print("💀 DEATH PERCENTAGE: 89%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ You managed to escape!")
        
        elif path1_beast == "Bear":
            print("\n🐻 A Giant BEAR jumps out!")
            print("Danger: 10/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")

            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Bear's favorite food is... Honey!")

                if food_choice == "Honey" and has_Honey == True:
                    print("The Bear puts his head inside the jar")
                    print("✅ YOU WIN! The Bear lets you pass")
                else:
                    print("Wrong food!")
                    print("💀 DEATH PERCENTAGE: 94%")
                    print("💀 YOU DIE!")
            else:
                print("\nYou try to sneak past...")
                survival_roll = random.randint(1, 100)
                if survival_roll <= 94:
                    print("💀 DEATH PERCENTAGE: 94%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ You managed to escape!")
        
        elif path1_beast == "Raccoon":
            raccoon_died = False
            print("\n🦝 A cute RACCOON waddles out!")
            print("Danger: 2/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")
            
            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Raccoon's favorite food is... Trash!")
                
                if food_choice == "Trash" and has_Trash == True:
                    print("The raccoon happily munches the trash!")
                    print("But it scratches you while grabbing it!")
                else:
                    print("Wrong food! The raccoon gets angry!")
                    print("💀 DEATH PERCENTAGE: 10%")
                    print("💀 YOU DIE!")
                    raccoon_died = True
            else:
                print("\nThe raccoon sniffs you curiously...")
                print("It scratches you playfully!")
            
            if not raccoon_died:
                print("\n🩸 You're bleeding from the scratches...")
                print("What do you do?")
                continue_choice = input("Continue down the path or Go back? (continue/back): ")
                
                if continue_choice == "continue":
                    print("\nYou continue walking down the path...")
                    print("You hear a rustling in the bushes...")
                else:
                    print("\nYou turn around to go back...")
                    print("But something is blocking your way...")
                
                print("\n🐯 THE TIGER APPEARS!")
                print("It smells your blood from the scratches!")
                
                survival_roll = random.randint(1, 100)
                if survival_roll <= 99:
                    print("💀 DEATH PERCENTAGE: 99%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ MIRACLE! You somehow escaped!")

    # PATH 2
    elif path_choice == "2":
        if path2_beast == "Tiger":
            print("\n🐯 A Ferocious TIGER emerges!")
            print("Danger: 9/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")
            
            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Tiger's favorite food is... HUMAN MEAT!")
                print("It doesn't want your food!")
                print("💀 DEATH PERCENTAGE: 99%")
                print("💀 YOU DIE!")
            else:
                print("\nYou try to run away...")
                survival_roll = random.randint(1, 100)
                if survival_roll <= 99:
                    print("💀 DEATH PERCENTAGE: 99%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ MIRACLE! You barely escaped!")
        
        elif path2_beast == "Lion":
            print("\n🦁 A Massive LION emerges!")
            print("Danger: 7/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")
            
            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Lion's favorite food is... Zebra Meat!")
                
                if food_choice == "Zebra Meat" and has_Zebra_meat == True:
                    print("✅ YOU WIN! The lion is satisfied and lets you pass!")
                else:
                    print("Wrong food!")
                    print("💀 DEATH PERCENTAGE: 89%")
                    print("💀 YOU DIE!")
            else:
                print("\nYou try to sneak past...")
                survival_roll = random.randint(1, 100)
                if survival_roll <= 89:
                    print("💀 DEATH PERCENTAGE: 89%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ You managed to escape!")
        
        elif path2_beast == "Bear":
            print("\n🐻 A Giant BEAR jumps out!")
            print("Danger: 10/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")

            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Bear's favorite food is... Honey!")

                if food_choice == "Honey" and has_Honey == True:
                    print("The Bear puts his head inside the jar")
                    print("✅ YOU WIN! The Bear lets you pass")
                else:
                    print("Wrong food!")
                    print("💀 DEATH PERCENTAGE: 94%")
                    print("💀 YOU DIE!")
            else:
                print("\nYou try to sneak past...")
                survival_roll = random.randint(1, 100)
                if survival_roll <= 94:
                    print("💀 DEATH PERCENTAGE: 94%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ You managed to escape!")
        
        elif path2_beast == "Raccoon":
            raccoon_died = False
            print("\n🦝 A cute RACCOON waddles out!")
            print("Danger: 2/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")
            
            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Raccoon's favorite food is... Trash!")
                
                if food_choice == "Trash" and has_Trash == True:
                    print("The raccoon happily munches the trash!")
                    print("But it scratches you while grabbing it!")
                else:
                    print("Wrong food! The raccoon gets angry!")
                    print("💀 DEATH PERCENTAGE: 10%")
                    print("💀 YOU DIE!")
                    raccoon_died = True
            else:
                print("\nThe raccoon sniffs you curiously...")
                print("It scratches you playfully!")
            
            if not raccoon_died:
                print("\n🩸 You're bleeding from the scratches...")
                print("What do you do?")
                continue_choice = input("Continue down the path or Go back? (continue/back): ")
                
                if continue_choice == "continue":
                    print("\nYou continue walking down the path...")
                    print("You hear a rustling in the bushes...")
                else:
                    print("\nYou turn around to go back...")
                    print("But something is blocking your way...")
                
                print("\n🐯 THE TIGER APPEARS!")
                print("It smells your blood from the scratches!")
                
                survival_roll = random.randint(1, 100)
                if survival_roll <= 99:
                    print("💀 DEATH PERCENTAGE: 99%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ MIRACLE! You somehow escaped!")

    # PATH 3
    elif path_choice == "3":
        if path3_beast == "Tiger":
            print("\n🐯 A Ferocious TIGER emerges!")
            print("Danger: 9/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")
            
            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Tiger's favorite food is... HUMAN MEAT!")
                print("It doesn't want your food!")
                print("💀 DEATH PERCENTAGE: 99%")
                print("💀 YOU DIE!")
            else:
                print("\nYou try to run away...")
                survival_roll = random.randint(1, 100)
                if survival_roll <= 99:
                    print("💀 DEATH PERCENTAGE: 99%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ MIRACLE! You barely escaped!")
        
        elif path3_beast == "Lion":
            print("\n🦁 A Massive LION emerges!")
            print("Danger: 7/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")
            
            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Lion's favorite food is... Zebra Meat!")
                
                if food_choice == "Zebra Meat" and has_Zebra_meat == True:
                    print("✅ YOU WIN! The lion is satisfied and lets you pass!")
                else:
                    print("Wrong food!")
                    print("💀 DEATH PERCENTAGE: 89%")
                    print("💀 YOU DIE!")
            else:
                print("\nYou try to sneak past...")
                survival_roll = random.randint(1, 100)
                if survival_roll <= 89:
                    print("💀 DEATH PERCENTAGE: 89%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ You managed to escape!")
        
        elif path3_beast == "Bear":
            print("\n🐻 A Giant BEAR jumps out!")
            print("Danger: 10/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")

            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Bear's favorite food is... Honey!")

                if food_choice == "Honey" and has_Honey == True:
                    print("The Bear puts his head inside the jar")
                    print("✅ YOU WIN! The Bear lets you pass")
                else:
                    print("Wrong food!")
                    print("💀 DEATH PERCENTAGE: 94%")
                    print("💀 YOU DIE!")
            else:
                print("\nYou try to sneak past...")
                survival_roll = random.randint(1, 100)
                if survival_roll <= 94:
                    print("💀 DEATH PERCENTAGE: 94%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ You managed to escape!")
        
        elif path3_beast == "Raccoon":
            raccoon_died = False
            print("\n🦝 A cute RACCOON waddles out!")
            print("Danger: 2/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")
            
            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Raccoon's favorite food is... Trash!")
                
                if food_choice == "Trash" and has_Trash == True:
                    print("The raccoon happily munches the trash!")
                    print("But it scratches you while grabbing it!")
                else:
                    print("Wrong food! The raccoon gets angry!")
                    print("💀 DEATH PERCENTAGE: 10%")
                    print("💀 YOU DIE!")
                    raccoon_died = True
            else:
                print("\nThe raccoon sniffs you curiously...")
                print("It scratches you playfully!")
            
            if not raccoon_died:
                print("\n🩸 You're bleeding from the scratches...")
                print("What do you do?")
                continue_choice = input("Continue down the path or Go back? (continue/back): ")
                
                if continue_choice == "continue":
                    print("\nYou continue walking down the path...")
                    print("You hear a rustling in the bushes...")
                else:
                    print("\nYou turn around to go back...")
                    print("But something is blocking your way...")
                
                print("\n🐯 THE TIGER APPEARS!")
                print("It smells your blood from the scratches!")
                
                survival_roll = random.randint(1, 100)
                if survival_roll <= 99:
                    print("💀 DEATH PERCENTAGE: 99%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ MIRACLE! You somehow escaped!")

    # PATH 4
    elif path_choice == "4":
        if path4_beast == "Tiger":
            print("\n🐯 A Ferocious TIGER emerges!")
            print("Danger: 9/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")
            
            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Tiger's favorite food is... HUMAN MEAT!")
                print("It doesn't want your food!")
                print("💀 DEATH PERCENTAGE: 99%")
                print("💀 YOU DIE!")
            else:
                print("\nYou try to run away...")
                survival_roll = random.randint(1, 100)
                if survival_roll <= 99:
                    print("💀 DEATH PERCENTAGE: 99%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ MIRACLE! You barely escaped!")
        
        elif path4_beast == "Lion":
            print("\n🦁 A Massive LION emerges!")
            print("Danger: 7/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")
            
            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Lion's favorite food is... Zebra Meat!")
                
                if food_choice == "Zebra Meat" and has_Zebra_meat == True:
                    print("✅ YOU WIN! The lion is satisfied and lets you pass!")
                else:
                    print("Wrong food!")
                    print("💀 DEATH PERCENTAGE: 89%")
                    print("💀 YOU DIE!")
            else:
                print("\nYou try to sneak past...")
                survival_roll = random.randint(1, 100)
                if survival_roll <= 89:
                    print("💀 DEATH PERCENTAGE: 89%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ You managed to escape!")
        
        elif path4_beast == "Bear":
            print("\n🐻 A Giant BEAR jumps out!")
            print("Danger: 10/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")

            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Bear's favorite food is... Honey!")

                if food_choice == "Honey" and has_Honey == True:
                    print("The Bear puts his head inside the jar")
                    print("✅ YOU WIN! The Bear lets you pass")
                else:
                    print("Wrong food!")
                    print("💀 DEATH PERCENTAGE: 94%")
                    print("💀 YOU DIE!")
            else:
                print("\nYou try to sneak past...")
                survival_roll = random.randint(1, 100)
                if survival_roll <= 94:
                    print("💀 DEATH PERCENTAGE: 94%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ You managed to escape!")
        
        elif path4_beast == "Raccoon":
            raccoon_died = False
            print("\n🦝 A cute RACCOON waddles out!")
            print("Danger: 2/10")
            print("\nWould you like to offer food?")
            offer = input("(yes or no): ")
            
            if offer == "yes":
                print("\nYou check your bag. You have:")
                if has_Honey:
                    print("- Honey")
                if has_Trash:
                    print("- Trash")
                if has_Zebra_meat:
                    print("- Zebra Meat")
                print("\nWhich one do you throw?")
                food_choice = input("Your choice: ")
                print("\nThe Raccoon's favorite food is... Trash!")
                
                if food_choice == "Trash" and has_Trash == True:
                    print("The raccoon happily munches the trash!")
                    print("But it scratches you while grabbing it!")
                else:
                    print("Wrong food! The raccoon gets angry!")
                    print("💀 DEATH PERCENTAGE: 10%")
                    print("💀 YOU DIE!")
                    raccoon_died = True
            else:
                print("\nThe raccoon sniffs you curiously...")
                print("It scratches you playfully!")
            
            if not raccoon_died:
                print("\n🩸 You're bleeding from the scratches...")
                print("What do you do?")
                continue_choice = input("Continue down the path or Go back? (continue/back): ")
                
                if continue_choice == "continue":
                    print("\nYou continue walking down the path...")
                    print("You hear a rustling in the bushes...")
                else:
                    print("\nYou turn around to go back...")
                    print("But something is blocking your way...")
                
                print("\n🐯 THE TIGER APPEARS!")
                print("It smells your blood from the scratches!")
                
                survival_roll = random.randint(1, 100)
                if survival_roll <= 99:
                    print("💀 DEATH PERCENTAGE: 99%")
                    print("💀 YOU DIE!")
                else:
                    print("✅ MIRACLE! You somehow escaped!")

    else:
        print("\n❌ Invalid path choice!")
        print("You stood there confused and got lost in the jungle...")
        print("💀 YOU DIE!")

    # PLAY AGAIN PROMPT
    print("\n" + "="*50)
    print("🪦 GAME OVER 🪦")
    print("="*50)
    play_again = input("\nPlay again? (yes/no): ")
    
    if play_again.lower() != "yes":
        print("\nThanks for playing! 🌴")
        break