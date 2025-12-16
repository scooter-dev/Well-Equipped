# Sewer Maze Puzzle Enhancement Plan

## Overview
Replace the current pressure plate puzzle system with a three-path sewer maze that explores themes of consumption and equipment choices through gameplay.

## Design Philosophy
- **No "ideal" paths** - all paths are exploration of consumption themes
- **Learning through experience** - players discover armor strengths through trial and error
- **Thematic consistency** - each path reflects its armor type's philosophy
- **Player agency** - all paths technically accessible, but with different challenges

## Core Structure

### Scene Flow
```
sewer_entrance → rats → sewer_junction → [path_choice] → boss
                                    ↓
                              [failure] → return_to_junction
```

### Path Designs

#### Slime Path (Spiked Corridor)
- **Layout**: Narrow corridor with wall-mounted spikes
- **Mechanic**: 
  - **Regular slime armor**: Can slip through gaps but gets damaged by spikes
  - **Enhanced slime armor**: Can slip through unharmed
  - **Other armors**: Too bulky to fit through gaps
- **Player Learning**: "I can almost make it through, but my armor isn't protective enough"
- **Theme**: Fast fashion's fragility and need for enhancement

#### Crafted Path (Guardian Gauntlet)
- **Layout**: Series of mechanical guardians and reinforced barriers
- **Mechanic**:
  - **Crafted armor**: Ideal for breaking barriers and fighting guardians
  - **Other armors**: Can attempt but take more damage/struggle more
- **Player Learning**: "Quality equipment makes challenges manageable"
- **Theme**: Value of craftsmanship and quality

#### Upcycled Path (Debris Maze)
- **Layout**: Maze of broken pipes, collapsed tunnels, and debris
- **Mechanic**:
  - **Upcycled armor**: Can patch broken sections and use debris creatively
  - **Other armors**: Can navigate but miss creative solutions
- **Player Learning**: "Resourcefulness matters as much as equipment"
- **Theme**: Sustainability and creative problem-solving

## Implementation Plan

### Phase 1: Core Structure Replacement

#### 1.1 Remove Current Puzzle System
- [ ] Delete `puzzle.rpy` entirely (pressure plate system)
- [ ] Replace `jump dungeon_pressure_puzzle` in `dungeon.rpy:25` with `jump sewer_junction`
- [ ] Remove all pressure plate variable references

#### 1.2 Create New Scene Structure
- [ ] Implement `sewer_junction` label
- [ ] Create path selection menu
- [ ] Add return-to-junction mechanics

### Phase 2: Individual Path Implementation

#### 2.1 Sewer Junction Scene
```python
label sewer_junction:
    "After defeating the rats, you reach a junction where three sewer tunnels converge. Each tunnel has distinct characteristics:
    
    - **Left Tunnel**: Narrow passage with glinting metal spikes visible in the walls
    - **Center Tunnel**: Wide corridor with mechanical sounds and flickering lights  
    - **Right Tunnel**: Debris-filled passage with makeshift bridges and broken pipes
    
    All three tunnels seem to lead toward the boss's lair, but each presents different challenges."
    
    menu:
        "Take the Left Tunnel (Spiked Corridor)":
            jump slime_path
        "Take the Center Tunnel (Guardian Gauntlet)":
            jump crafted_path
        "Take the Right Tunnel (Debris Maze)":
            jump upcycled_path
        "Return to Guild":
            jump repeat_guild
```

#### 2.2 Slime Path Implementation
```python
label slime_path:
    "You enter the narrow corridor. The walls are lined with sharp metal spikes, but there are small gaps between them."
    
    if armor_data["Slime Armor"]["equipped"]:
        if slime_armor_enhanced:
            "Your enhanced slime armor glides effortlessly through the spiked corridor."
            jump boss
        else:
            "You slip through the gaps between spikes, but your fragile armor gets ripped and torn by the sharp edges."
            "You make it through, but your armor is heavily damaged. You'll need to return to the guild for repairs."
            $ slime_armor_damaged = True
            jump sewer_junction
    else:
        "Your armor is too bulky to fit through the narrow gaps between the spikes. You're forced to turn back."
        jump sewer_junction
```

#### 2.3 Crafted Path Implementation
```python
label crafted_path:
    "You enter the wide corridor. Mechanical guardians patrol the area, and reinforced barriers block your path."
    
    if armor_data["Finely Crafted Armor"]["equipped"]:
        "Your finely crafted armor provides excellent protection against the guardians' attacks."
        "You break through the reinforced barriers with confidence."
        jump boss
    else:
        "The guardians' attacks damage your armor, and the barriers are difficult to break through."
        "You manage to progress but your equipment takes heavy damage. You should return to prepare better."
        jump sewer_junction
```

#### 2.4 Upcycled Path Implementation
```python
label upcycled_path:
    "You enter the debris-filled passage. Broken pipes, collapsed tunnels, and makeshift obstacles block your way."
    
    if armor_data["Upcycled Armor"]["equipped"]:
        "Your resourceful nature helps you navigate the debris field. You patch broken sections and use debris creatively."
        "You find clever solutions that others might miss."
        jump boss
    else:
        "The unstable terrain is difficult to navigate. You struggle to find safe passage through the debris."
        "You make some progress but the journey is treacherous. You should prepare better before continuing."
        jump sewer_junction
```

### Phase 3: Slime Armor Enhancement System

#### 3.1 State Management Variables
```python
# Add to game initialization
default slime_armor_damaged = False
default slime_armor_enhanced = False
default slime_enhancement_available = False
default slime_essence_collected = False
```

#### 3.2 Guild Master Interaction
```python
# Add to guild label after slime armor damage
if slime_armor_damaged:
    g "I see your slime armor was damaged in the spiked corridor. That path requires special preparation."
    g "If you bring me slime essence from defeated slimes, I can teach you to craft enhanced slime armor that can withstand those spikes."
    $ slime_enhancement_available = True
```

#### 3.3 Slime Essence Collection
```python
label slime_hunting:
    "You venture into the sewers to hunt slimes for their essence."
    # Mini-game implementation here
    $ slime_essence_collected = True
    jump guild
```

#### 3.4 Enhancement Crafting
```python
# Add to guild label
if slime_essence_collected and slime_enhancement_available:
    g "Perfect! With this slime essence, I can enhance your armor. Let me teach you the technique."
    "The Guild Master teaches you to reinforce your slime armor with collected essence."
    $ slime_armor_enhanced = True
    $ slime_armor_damaged = False
```

### Phase 4: Integration and Polish

#### 4.1 Environmental Storytelling
- [ ] Add remains of failed slime armor adventurers in spiked corridor
- [ ] Include broken mechanical guardians and successful tracks in crafted path
- [ ] Place previous adventurers' failed attempts vs. successful solutions in upcycled path
- [ ] Add clues about monster's origin (corrupted slime armor) throughout

#### 4.2 Dialogue Updates
- [ ] Update Guild Master dialogue to reference slime path failures
- [ ] Add path-specific observations from player character
- [ ] Update boss battle dialogue to reference path taken

#### 4.3 Victory Conditions
- [ ] All three paths lead to boss when successfully completed
- [ ] Enhanced slime armor provides same success as other armors
- [ ] Maintain current boss battle mechanics

## Key Design Decisions

### Confirmed Choices
- No "ideal" paths - all paths are exploration of consumption themes
- Slime path sends player back when armor is damaged (no damage system initially)
- Free path switching when not in combat
- Guild master teaches enhancement after slime path failure
- All paths lead to boss when successfully navigated

### Open Questions
1. **Slime Essence Hunting**: Mini-game or simple narrative progression?
2. **Visual Indicators**: Should enhanced slime armor have GUI indicators?
3. **Failure Consequences**: Permanent consequences or infinite retries?
4. **Path Difficulty**: Should non-ideal paths be progressively harder or just different?

## Implementation Priority

### High Priority
1. Replace puzzle system with junction and basic paths
2. Implement slime armor damage and enhancement system
3. Add state management variables

### Medium Priority
1. Environmental storytelling and dialogue updates
2. Slime essence collection mini-game
3. Path-specific descriptions and feedback

### Low Priority
1. Visual polish and GUI enhancements
2. Advanced failure mechanics
3. Secret content and easter eggs

## Files to Modify

### New Files
- `game/scenes/sewer_maze.rpy` - New maze implementation

### Modified Files
- `game/script.rpy` - Update jump targets
- `game/scenes/dungeon.rpy` - Replace puzzle system
- `game/data/armor.rpy` - Add new state variables
- `PROJECT_STATUS.md` - Update implementation status

## Testing Checklist

### Core Functionality
- [ ] All three paths accessible from junction
- [ ] Slime path damages regular armor, passes enhanced armor
- [ ] Crafted path works best with crafted armor
- [ ] Upcycled path works best with upcycled armor
- [ ] All successful paths lead to boss

### Enhancement System
- [ ] Slime armor damage triggers guild dialogue
- [ ] Slime essence collection works
- [ ] Enhancement crafting functions
- [ ] Enhanced armor passes spiked corridor

### State Management
- [ ] Variables track correctly between scenes
- [ ] Armor status persists through path attempts
- [ ] Return to junction maintains game state

## Theme Integration

### Consumption Commentary
- **Slime Path**: Fast fashion's fragility and need for constant replacement/enhancement
- **Crafted Path**: Value of investing in quality over quantity
- **Upcycled Path**: Resourcefulness and sustainable alternatives

### Player Learning
- Experience teaches armor strengths rather than explicit instruction
- Failure provides narrative motivation for improvement
- Multiple successful approaches reinforce theme of choice

### Environmental Storytelling
- Previous adventurers' attempts show consequences of choices
- Monster's origin as corrupted slime armor ties themes together
- Each path's environment reflects its philosophical approach