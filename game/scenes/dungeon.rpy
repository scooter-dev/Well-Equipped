# Main Dungeon Scene - Coordinates all dungeon-related encounters
# This is the central hub that manages the dungeon flow

label sewer_entrance:
    scene alleyway
    "With your armor selected, you make your way to the sewer entrance. The air is damp and the smell is... well, it's a sewer."
    jump rats

label dungeon_main:
    "You descend into the sewer system. The dark tunnels echo with dripping water and distant sounds of movement."
    jump sewer_maze