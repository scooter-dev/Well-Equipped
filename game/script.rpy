define e = Character("Eileen")
define g = Character("Guild Leader")
define s = Character("Shopkeeper")
define b = Character("Bada Boom")
define a = Character("Armorer")

default new_adventurer = True
default available_armors = []


label start:

    scene bg room

    show eileen

    e "Well met! So, you want to be an adventurer? Go to the Guild for your first quest."

    jump guild

label guild:

    scene bg tavern

    show guild leader calm

    if new_adventurer:
        g "Welcome to the Adventurer's Guild! I see you're new here. Are you ready to embark on your first quest?"
        $ new_adventurer = False

    g "Welcome back, adventurer! I see you've been busy. Are you prepared to veture forth?"
    $ available_armors = [name for name, data in armor_data.items() if data["available"]]

    menu:
        "Yes" if len(available_armors) > 0:
            "You feel ready to take on the challenge ahead."
            jump choose_armor
        "No":  
            "You decide to take a moment to prepare yourself before embarking on your first quest."
            jump town_square

label choose_armor:
    scene bg guild

    "Before you leave, you need to choose your armor. Each type of armor has its own advantages and disadvantages."

    menu:
        "Slime Armor" if armor_data["slime_armor"]["available"]:
            g "Slime armor, huh? It's cheap and readily available, but don't expect it to last long."
            "Confirm your choice of slime armor?"
            menu:
                "Yes":
                    $ equipment = "slime_armor"
                    jump sewer_entrance
                "No": 
                    jump choose_armor
        "Finely Crafted Armor" if armor_data["finely_crafted_armor"]["available"]:
            g "Ah, the armorer's finest work. A wise choice!"
            "Confirm your choice of finely crafted armor?"
            menu:
                "Yes":
                    $ equipment = "finely_crafted_armor"
                    jump sewer_entrance
                "No":
                    jump choose_armor
        "Upcycled Armor" if armor_data["upcycled_armor"]["available"]:
            g "Ah, the upcycled armor. A unique choice, but it has its merits."
            "Confirm your choice of upcycled armor?"
            menu:
                "Yes":
                    $ equipment = "upcycled_armor"
                    jump sewer_entrance
                "No":
                    jump choose_armor

                "No":
                    jump choose_armor
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

label repeat_guild:

    "You find yourself back at the adventurer's guild at the beginning of your path."

    jump guild
