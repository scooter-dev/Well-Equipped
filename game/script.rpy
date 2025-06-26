define e = Character("Eileen")
define g = Character("Guild Leader")
define s = Character("Shopkeeper")
define b = Character("Bada Boom")
define a = Character("Armorer")

default new_adventurer = True
default armor_list = []
default selected_armor = "none"

label start:

    scene bg room

    show eileen happy

    e "Well met! So, you want to be an adventurer? Go to the Guild for your first quest."

    jump guild

label guild:

    scene bg tavern

    show guild leader calm

    if new_adventurer:
        g "Welcome to the Adventurer's Guild! I see you're new here. Are you ready to embark on your first quest?"

    if(armor_list is empty):
        g "So you want to go on your first quest? You'll need some good armor."

        menu:
            "Leave":
                jump town_square
    else:
        g "Welcome back, adventurer! I see you've been busy. Are you prepared for your first quest?"

        menu:
            "Yes":
                "You feel ready to take on the challenge ahead."
                jump choose_armor
            "No":  
                "You decide to take a moment to prepare yourself before embarking on your first quest."
                jump town_square

label choose_armor:
    scene bg guild

    "Before you leave, you need to choose your armor. Each type of armor has its own advantages and disadvantages."

    menu:
        "Slime Armor":
            g "Ah, I see you've chosen the slime armor. An... interesting choice. I hope you're ready for a slippery challenge!"
            "Confirm your choice of slime armor?"
            menu:
                "Yes":
                    $ selected_armor = "Slime Armor"
                "No": 
                    return
        "Finely Crafted Armor":
            g "Ah, the armorer's finest work. A wise choice!"
            "Confirm your choice of finely crafted armor?"
            menu:
                "Yes":
                    $ selected_armor = "Finely Crafted Armor"
                "No":
                    return
        "Upcycled Armor":
            g "Ah, the upcycled armor. A unique choice, but it has its merits."
            "Confirm your choice of upcycled armor?"
            menu:
                "Yes":
                    $ selected_armor = "Upcycled Armor"
                "No":
                    return
        "Come Back Later":
            "You decide to come back later when you have more information or resources."
            jump town_square

label town_square:
    scene bg town_square

    "Welcome to the town square! Here, you can find various shops and people who might help you on your journey."

    menu:
        "Adventurer's Guild":
            jump guild
        "Armor Shop":
            jump armorer
        "Bright Shiny Store":
            jump slime_store
        "...Alleyway?":
            jump garbage
        "Pie Stand":
            "You decide to take a break and enjoy a delicious pie from the pie stand. It's a nice way to relax before your adventure."

label sewer_entrance:

    scene alleyway

    "With you armor selected, you make your way to the sewer entrance. The air is damp and the smell is... well, it's a sewer."

    jump rats

label repeat_guild:

    "You find yourself back at the adventurer's guild at the beginning of your path."

    jump guild
