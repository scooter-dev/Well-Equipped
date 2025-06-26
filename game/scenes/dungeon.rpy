label rats:

    scene sewer

    "You encounter enemies! Fight these rats!"

    jump puzzle

label puzzle:

    "Ther is one more challenge in between you and the horrible creature. A classic puzzle for an aspiring adventurer. Not a phiscal one like the rats."

    "This is a test of the mind! Arguably this is more important than your choice of armor. Even one who dons (spelling?) less fortified armor can face great challenges."

    # puzzle here

    jump boss

label boss:
    
    scene boss shadowed

    "You've finally reached your bounty! The powerful enemy that has felled a dozen unprepared adventurers. Will you share their fate?"

# jump based on choice of armor

label fight_slime_armor:
    "You boldly enter the cavern equipped with slime armor. You feel a little silly in this armor as you see all the destroyed slime armor around the room."
    "The armor's slippery surface makes it harder for the boss to land a direct hit, but it offers little protection."
    jump fight_boss_slime

label finely_crafted_armor:
    "You boldly enter the cavern equipped with the armor that was lovingly crafted by a local armorer. You feel pride because you saved up for this fine piece."
    "The armor absorbs the first few hits from the boss, giving you an advantage in the fight."
    jump fight_boss_finely_crafted

label upcycled_armor:
    "You boldly enter the cavern equipped with your trash armor. You rescued this armor and made it your own. It no longer stinks. It is no longer scarred and ripped."
    "The armor's patchwork design surprises the boss, giving you a chance to strike first."
    jump fight_boss_upcycled

label fight_boss_finely_crafted:
    "The fight is intense, but your finely crafted armor holds up well against the boss's attacks."
    "You manage to land a decisive blow, defeating the boss!"
    jump success

label fight_boss_upcycled:
    "The fight is challenging, but your upcycled armor's unique design gives you an edge."
    "You cleverly use the armor's quirks to outmaneuver the boss and claim victory!"
    jump success

label fight_boss_slime:
    "The fight is chaotic, and your slime armor struggles to keep up with the boss's powerful attacks."
    "Despite your best efforts, the armor fails to protect you, and the boss overpowers you."
    jump defeat

label defeat:
    "You have failed."
    "Do you want to try again or return to the adventurer's guild to prepare better?"
    menu:
        "Try Again":
            jump fight_boss
        "Return to Guild":
            jump repeat_guild

label success:
    "You did it!"
    "The boss is defeated, and you emerge victorious. The guild will surely recognize your achievement."
    "Do you want to return to the guild or explore other paths?"
    menu:
        "Return to Guild":
            jump repeat_guild
        "Explore Other Paths":
            jump guild