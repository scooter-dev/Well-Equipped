# Basic Combat System

label combat(enemy_type="rats"):
    # Set enemy stats from data
    $ enemy_stats = enemy_data[enemy_type]
    $ enemy_hp = enemy_stats["hp"]
    $ enemy_atk = enemy_stats["atk"]
    $ enemy_def = enemy_stats["def"]
    $ enemy_name = enemy_stats["name"]
    $ enemy_max_hp = enemy_hp
    $ defending = False  # Flag for defend command

    "[enemy_name] appears! Combat begins!"

    show screen combat_status

    while enemy_hp > 0 and player_hp > 0:
        # Player turn
        $ _items = [("Attack with Sword", Return("attack")), ("Defend", Return("defend"))]
        call screen combat_menu(_items)
        $ choice = _return

        if choice == "attack":
            $ damage = max(0, player_atk - enemy_def)
            $ enemy_hp -= damage
            "You slash the [enemy_name] with your sword for [damage] damage! Enemy HP: [enemy_hp]/[enemy_max_hp]"
        elif choice == "defend":
            $ defending = True
            "You brace yourself for the next attack."

        # Enemy turn
        if enemy_hp > 0:
            if renpy.random.random() < 0.7:  # 70% chance basic attack
                $ damage = max(0, enemy_atk - (player_def if not defending else player_def // 2))
                $ player_hp -= damage
                "The [enemy_name] attacks! You take [damage] damage. Your HP: [player_hp]/[player_max_hp]"
            else:
                # Environmental effect
                if enemy_type == "rats":
                    $ damage = 5
                    $ player_hp -= damage
                    "The rats swarm in the murky sewer water, splashing you for [damage] damage!"
                else:
                    $ damage = 10
                    $ player_hp -= damage
                    "Toxic sewer fumes overwhelm you, dealing [damage] damage!"
            $ defending = False

    if player_hp <= 0:
        "You have been defeated!"
        $ combat_result = "defeat"
    else:
        "You defeated the [enemy_name]!"
        $ combat_result = "victory"
    hide screen combat_status
    return