# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define g = Character("Guild Leader")
define s = Character("Shopkeeper")

label start:

    scene bg room

    show eileen happy

    e "You've created a new Ren'Py game."

    return

label guild:

    scene bg tavern

    show guild leader calm

    g "So you want to go on your first quest? You'll need some good armor."

label slime:

    scene slime armor store

    show store clerk

    s "Are you here to see the most fashionable and affordable armor in the land?"

    "Slime armor gaine in popularity because I mimicked noble's glass armor. Its transparent quality also
    allows for vain adventurers to show off their outfits."

label garbage:

    scene alleyway

    show strange person

    "The strange person you met earlier leads you down backstreets. They promised to show you where old armor pieces are getting
    thrown out."

label armorer:

    scene armor shop

    show craftsman

    "The shop has rebuffs offers from the Slime Armor producers for a while. They want to buy out the competition. It may be more expensive
    but the shopkeep offers repairs in perpetuity. It may be worth it to save up at a lest exciting job."