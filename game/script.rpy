# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define g = Character("Guild Leader")
define s = Character("Shopkeeper")
define b = Character("Bada Boom")
define a = Character("Armorer")

label start:

    scene bg room

    show eileen happy

    e "Well met! So, you want to be an adventurer? Go to the Guild for your first quest."

    jump guild

label guild:

    scene bg tavern

    show guild leader calm

    g "So you want to go on your first quest? You'll need some good armor."

# choice to jump to different routes.


label slime:

    scene slime armor store

    show store clerk

    s "Are you here to see the most fashionable and affordable armor in the land?"

    "Slime armor gained popularity because I mimicked noble's glass armor. Its transparent quality also
    allows for vain adventurers to show off their outfits."

    "As you inspect the armor, you percieve that it has a couple advantages. However, it seems a bit flimsy."

# jump to a scene or just before going on to the sewer

label garbage:

    scene alleyway

    show strange person

    "The strange person you met earlier leads you down backstreets. They promised to show you where old armor pieces are getting
    thrown out."

    "After a long hunt in the garbage of many shops, you come across a well-used set of armor. It is soaked in the waste of this particular shop. It moderately damaged."
    
    b "Wow, kid! Great find. If you repair that, you'll be set for a while. You can wash it and patch it up- It'll be good as new! If you like, you can use my workshop."

    b "I've repaired plenty of weapons and other junk. If you help me out with some other repairs, I'll even give you a special weapon!"

# jump to bada boom's workshop


label armorer:

    scene armor shop

    show craftsman

    "The shop has rebuffs offers from the Slime Armor producers for a while. They want to buy out the competition. It may be more expensive
    but the shopkeep offers repairs in perpetuity. It may be worth it to save up at a lest exciting job."

    a "Ey? A customer! Welcome to me shop. I see you're an adventurer. A bit green you are. HEH HEH HOO! I only craft the finest armor."
    
    a "I have a limited stock because I put care into each piece."

    "The armor that you inspect are finely crafted indeed. However, they are a pricey. Don't be discouraged! It is time for the legendary tradition of all adventurers."

    "It's time to grind for gold! Also know as farming for gold by some."

# jump to a scene or just before going on to the sewer

label farming_gold:

    "It's time to get your hands dirty with some menial tasks. This might not be your passion, but it will be worth it. And hey, maybe you'll enjoy the work."

    "But stand firm! Do not be lost in the grind and believe this is all you are. It may take time to supply the gold for your the daily expenses and your passion."

    "It's time for work!"

    jump mini_game

label mini_game:

    "Instructions for the mini game: Press blah for blah"

    jump success_fine_armor

label success_fine_armor:
    
    "Great work! You persisted through some menial tasks and earned for the finely crafted armor. "

label guild_equipped:

    "I see that you are well equipped. Very well! Your first quest with be a bit difficult, but I think you are up to the task! This will be a test and an initiation."

# different reactions based on choices.

    jump sewer_entrance


label sewer_entrance:

    scene alleyway

    "Are you prepared to face the threat? This is your last chance to acquire armor."

    jump rats

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

label finely_crafted_armor:
    "You boldly enter the cavern equipped with the armor that was lovingly crafted by a local armorer. You feel pride because you saved up for this fine piece."

label upcycled_armor:
    "You boldly enter the cavern equipped with your trash armor. You rescued this armor and made it your own. It no longer stinks. It is no longer scarred and ripped."

label fight_boss:
    "Fight, Defend, Evade"

#bonuses based on choice of armor and choice of solution to armor 
# combat game jump based on result


label defeat:
    "You have failed."

#option to go back to adventurers guild just before the choice to aquire armor

label success:
    "You did it!"

# go to main screen or go back and try a different route

label repeat_guild:

    "You find your self back at the adventurers guild at the beginning of your path."

    jump guild

