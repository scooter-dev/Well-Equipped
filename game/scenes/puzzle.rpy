# Modular Pressure Plate Puzzle System
# Reusable components for dungeon puzzles

# Armor stats - set these based on player's armor choice in earlier scenes
default armor_weight = 0      # -2 to +2 scale
default armor_flexibility = 0 # -2 to +2 scale  
default armor_durability = 0  # -2 to +2 scale
default armor_craftsmanship = 0 # -2 to +2 scale

# Puzzle state
default puzzle_plates = {
    "red": {"solved": False, "requirement": "light", "threshold": -1},
    "blue": {"solved": False, "requirement": "medium", "threshold": 0}, 
    "green": {"solved": False, "requirement": "heavy", "threshold": 1},
    "yellow": {"solved": False, "requirement": "balance", "threshold": 1},
    "purple": {"solved": False, "requirement": "endurance", "threshold": 1}
}

# Helper function to check if player can activate a plate
init python:
    def can_activate_plate(plate_color):
        plate = puzzle_plates[plate_color]
        req = plate["requirement"]
        threshold = plate["threshold"]
        
        if req == "light":
            return armor_weight <= threshold
        elif req == "medium":
            return abs(armor_weight) <= 1
        elif req == "heavy":
            return armor_weight >= threshold
        elif req == "balance":
            return armor_flexibility >= threshold
        elif req == "endurance":
            return armor_durability >= threshold
        return False
    
    def get_plates_solved():
        return sum(1 for plate in puzzle_plates.values() if plate["solved"])
    
    def puzzle_complete():
        return get_plates_solved() >= 3  # Need 3 out of 5 plates

# Reusable label for examining any dungeon puzzle
label examine_puzzle_room:
    "You study the chamber carefully, looking for clues and mechanisms."
    
    menu:
        "Examine the floor patterns":
            call examine_floor_details
        "Check the walls for inscriptions":
            call examine_wall_inscriptions  
        "Look at the exit mechanism":
            call examine_exit_door
        "Continue with the puzzle":
            return

label examine_floor_details:
    "The stone tiles show centuries of wear, with different patterns around each plate."
    "Some areas seem more worn than others, suggesting preferred paths."
    return

label examine_wall_inscriptions:
    "Ancient text covers portions of the walls:"
    "You can make out fragments about 'burden and grace' and 'the measured step.'"
    if armor_craftsmanship >= 1:
        "Your quality gear helps you notice additional, faded text about 'tools shaping the wielder.'"
    return

label examine_exit_door:
    "The door has five gem sockets, each corresponding to a pressure plate color."
    "Currently [get_plates_solved()] of 5 gems are glowing."
    if puzzle_complete():
        "Enough gems are active - the door should open!"
    return

# Reusable pressure testing system
label test_pressure_plate(plate_color):
    $ plate_name = plate_color.capitalize()
    
    if puzzle_plates[plate_color]["solved"]:
        "The [plate_color] plate is already activated."
        return
    
    "You approach the [plate_color] plate..."
    
    if can_activate_plate(plate_color):
        call activate_plate_success(plate_color)
    else:
        call activate_plate_failure(plate_color)
    
    return

label activate_plate_success(plate_color):
    $ puzzle_plates[plate_color]["solved"] = True
    "The [plate_color] plate glows brightly as it activates!"
    
    # Subtle feedback based on how well it worked
    $ req = puzzle_plates[plate_color]["requirement"]
    if req == "light" and armor_weight <= -1:
        "It responds easily to your light step."
    elif req == "heavy" and armor_weight >= 2:
        "The solid weight activates it firmly."
    elif req == "balance" and armor_flexibility >= 2:
        "You find the perfect center point instinctively."
    elif req == "endurance" and armor_durability >= 2:
        "You can maintain the pressure comfortably."
    else:
        "It takes some effort, but you manage to activate it."
    
    return

label activate_plate_failure(plate_color):
    $ req = puzzle_plates[plate_color]["requirement"]
    
    if req == "light":
        "You step as lightly as possible, but the plate remains dark. Your footstep is still too heavy."
    elif req == "heavy":
        "You press down with all your weight, but the plate barely responds. It needs more pressure."
    elif req == "balance":
        "You shift your weight trying to find the sweet spot, but the plate's glow wavers and fades."
    elif req == "endurance":
        "You maintain pressure on the plate, but after a few moments you shift uncomfortably and it deactivates."
    else:
        "The plate flickers briefly but doesn't fully activate."
    
    # Offer subtle hints based on armor stats
    if armor_craftsmanship >= 1:
        "Your experience with quality equipment gives you insight into what might work better."
    
    return

# Main puzzle scene
label dungeon_pressure_puzzle:
    scene bg dungeon_room
    with fade
    
    "You enter a chamber with five colored pressure plates arranged in a circle."
    "Each plate has subtle markings indicating different activation requirements."
    
    call examine_puzzle_room
    
    label pressure_puzzle_loop:
        call display_puzzle_status
        
        if puzzle_complete():
            jump puzzle_solved
        
        menu:
            "Test red plate" if not puzzle_plates["red"]["solved"]:
                call test_pressure_plate("red")
            "Test blue plate" if not puzzle_plates["blue"]["solved"]:
                call test_pressure_plate("blue")
            "Test green plate" if not puzzle_plates["green"]["solved"]:
                call test_pressure_plate("green")
            "Test yellow plate" if not puzzle_plates["yellow"]["solved"]:
                call test_pressure_plate("yellow")
            "Test purple plate" if not puzzle_plates["purple"]["solved"]:
                call test_pressure_plate("purple")
            "Re-examine the room":
                call examine_puzzle_room
            "Try alternative approach" if get_plates_solved() >= 1:
                call alternative_puzzle_approach
        
        jump pressure_puzzle_loop

label display_puzzle_status:
    "Progress: [get_plates_solved()]/5 plates activated (need 3 to proceed)"
    return

label alternative_puzzle_approach:
    "You look for creative solutions..."
    
    # Different options based on armor stats
    if armor_flexibility >= 1:
        menu:
            "Use agility to quickly move between plates":
                "Your flexible gear lets you maintain multiple plates briefly!"
                $ puzzle_plates["red"]["solved"] = True
                $ puzzle_plates["blue"]["solved"] = True
                "Two plates activate from your quick movements!"
                return
            "Stick with standard approach":
                return
    
    if armor_craftsmanship >= 2:
        menu:
            "Use gear's special features":
                "Your well-made equipment has hidden capabilities you can leverage."
                call craft_based_solution
                return
            "Continue normally":
                return
    
    "You don't see any alternatives that work with your current capabilities."
    return

label craft_based_solution:
    "Your quality gear reveals additional options others might miss."
    menu:
        "Activate weight-shifting mechanism":
            $ puzzle_plates["green"]["solved"] = True
            "A hidden feature in your armor adds temporary weight!"
        "Use precision balance aids":
            $ puzzle_plates["yellow"]["solved"] = True  
            "Built-in balance assistance helps you nail the precision plate!"
        "Engage comfort enhancement":
            $ puzzle_plates["purple"]["solved"] = True
            "Superior ergonomics let you maintain pressure longer!"
    jump boss

label puzzle_solved:
    "The door mechanism clicks as enough plates are activated."
    "The ancient portal grinds open, revealing the path ahead."
    
    # Subtle acknowledgment of approach without being preachy
    if get_plates_solved() == 5:
        "Your thorough approach opened every pathway."
    elif armor_craftsmanship >= 2:
        "Quality equipment provided options others might not have."
    elif armor_flexibility >= 1:
        "Adaptability proved valuable in finding solutions."
    
    scene bg dungeon_corridor
    with fade
    jump boss