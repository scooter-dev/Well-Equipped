# Three-Path Sewer Maze Implementation
# Each path designed for specific armor type only



label sewer_maze:
    scene sewer
    
    "After defeating the rats, you descend deeper into the sewer system. The tunnels open into a vast junction where three passages converge, each with an unsettling presence."
    
    "The air hangs thick with the weight of forgotten depths. Something ancient and powerful slumbers ahead - you can feel it in your bones."
    
    menu:
        "Left Tunnel":
            jump slime_path
        "Center Tunnel":
            jump crafted_path
        "Right Tunnel":
            jump upcycled_path
        "Return to Surface":
            "You decide to return to the town square to prepare better."
            jump repeat_guild

label slime_path:
    "You enter the narrow passage. The walls are impossibly close, with sharp protrusions that seem to shift and move."
    
    menu:
        "Proceed through the passage":
            if equipment == "slime_armor":
                # The slime allows for sliding through the narrow, spiked passage
                jump boss
            else:
                #The narrow, spiked passage is impassible
                jump sewer_maze
        "Inspect the walls more closely":
            # The walls are narrow and covered in sharp, shifting spikes
            jump slime_path
        "Return to junction":
            jump sewer_maze

label crafted_path:
    "You enter the wide corridor. Ancient mechanisms stir to life, their purpose unclear but unmistakably hostile."
    
    menu:
        "Proceed through the corridor":
            if equipment == "finely_crafted_armor":
                # The finely crafted armor withstands the mechanical onslaught
                jump boss
            else:
                # The mechanical traps prove too much to handle
                jump sewer_maze
        "Inspect the mechanisms":
            # Assess the threat
            jump crafted_path
        "Return to junction":
            jump sewer_maze

label upcycled_path:
    #There trash and debris everywhere
    
    menu:
        "Navigate the debris maze":
            if equipment == "upcycled_armor":
                # Challenge 1: Bridge building
                # Theres stuff that can be combined to make a bridge
                
                # Challenge 2: Gas leak
                # Pipe puzzle? Or fashion a gas mask?
                
                # Challenge 3: Light source
                # A single pin prick of light from the outside world. Navigate or redirect the light to find your way.
                
                # Success culmination
                # Make your way through, a large stone door looms ahead
                
                jump boss
            else:
                "Oh no."
                "The unstable terrain proves too much to handle. You retreat to the junction to reconsider."
                "This passage seems to require creativity and resourcefulness to navigate."
                jump sewer_maze
        "Inspect the debris and terrain":
            #There trash and debris everywhere
            jump upcycled_path
        "Return to junction":
            jump sewer_maze