label armorer:

    scene armor shop

    show craftsman

    "The shop has rebuffed offers from the Slime Armor producers for a while. They want to buy out the competition."
    "It may be more expensive than slime but the shopkeeper offers repairs in perpetuity. It may be worth grinding for."

    a "Ey? A customer! Welcome to me shop. I see you're an adventurer. A bit green you are. HEH HEH HOO! I only craft the finest armor."
    
    a "I have a limited stock because I put care into each piece."

    "The armor that you inspect are finely crafted indeed. However, they are pricey. Don't be discouraged! It is time for the legendary tradition of all adventurers."

    "It's time to grind for gold! Also know as farming for gold by some."
    
    jump farming_gold

# What money making paths are there? Is this the same as the pie thing?
label farming_gold:

    "It's time to get your hands dirty with some menial tasks. This might not be your passion, but it will be worth it. And hey, maybe you'll enjoy the work."

    "But stand firm! Do not be lost in the grind and believe this is all you are. It may take time to supply the gold for your the daily expenses and your passion."

    "It's time for work!"

    jump bar_minigame

label mini_game:

    "Instructions for the mini game: Press blah for blah"

    jump success_fine_armor

label success_fine_armor:
    
    "Great work! You persisted through some menial tasks and earned for the finely crafted armor. "
    $ armor_data["finely_crafted_armor"]["available"] = True
    jump guild