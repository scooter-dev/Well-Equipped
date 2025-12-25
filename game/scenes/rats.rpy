label rats:

    scene sewer

    "You encounter enemies! Fight these rats!"
    
    "The rats scurry through the murky water, their eyes gleaming in the dim light."
    "Though numerous, they're no match for a prepared adventurer."

    # Combat encounter with rats
    call combat("rats")

    if combat_result == "defeat":
        jump defeat
    else:
        "The path forward is now clear. You can hear the distant echoes of something much larger ahead."
    
    # Return to main dungeon flow
    jump dungeon_main