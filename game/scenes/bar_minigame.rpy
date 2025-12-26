# Bartending Minigame - Gold Grinding
# Minimal Testable Version: Single customer, fixed sequence

init python:
    # Reusable sequence input system
    class SequenceInput:
        def __init__(self, sequence, timeout=10.0):
            self.sequence = sequence  # List of keys: 'up', 'down', 'left', 'right'
            self.timeout = timeout
            self.current_index = 0
            self.start_time = 0
            self.completed = False
            self.failed = False

        def start(self):
            self.start_time = renpy.get_game_runtime()
            self.current_index = 0
            self.completed = False
            self.failed = False

        def input_key(self, key):
            if self.completed or self.failed:
                return False

            if self.current_index < len(self.sequence):
                if key == self.sequence[self.current_index]:
                    self.current_index += 1
                    if self.current_index >= len(self.sequence):
                        self.completed = True
                        return True
                else:
                    self.failed = True
                    return False
            return False

        def is_timeout(self):
            return (renpy.get_game_runtime() - self.start_time) > self.timeout

        def reset(self):
            self.current_index = 0
            self.completed = False
            self.failed = False



# Arrow key mappings
define ARROW_KEYS = {
    'up': 'uparrow',
    'down': 'downarrow',
    'left': 'leftarrow',
    'right': 'rightarrow'
}

# Shift length in seconds
default shift_length = 30.0

# Last customer result
default last_result = ""
default last_color = "#FFFFFF"

# Function to generate random sequence
init python:
    import random
    def generate_sequence(length=4):
        arrows = ['up', 'down', 'left', 'right']
        return [random.choice(arrows) for _ in range(length)]

label bar_minigame:
    scene bar  # Placeholder scene

    "Welcome to the tavern! Your shift starts now. Serve as many customers as you can!"

    $ shift_start = renpy.get_game_runtime()
    $ customers_served = 0
    $ last_result = ""
    $ last_color = "#FFFFFF"

    # Shift loop
    while (renpy.get_game_runtime() - shift_start) < shift_length:
        # Generate new sequence for customer
        $ current_sequence = generate_sequence(random.randint(3, 5))
        $ seq_input = SequenceInput(current_sequence, timeout=10.0)
        $ seq_input.start()

        # Customer service loop
        $ served = False
        while not seq_input.completed and not seq_input.failed and not seq_input.is_timeout():
            call screen sequence_input_screen(seq_input)

        if seq_input.completed:
            $ customers_served += 1
            $ last_result = "Served!"
            $ last_color = "#00FF00"  # Green
        else:
            $ last_result = "Unhappy customer"
            $ last_color = "#FF0000"  # Red

    # End of shift
    $ gold_earned = customers_served * 5
    $ player_gold += gold_earned
    "Shift over! You served [customers_served] customers and earned [gold_earned] gold. Total gold: [player_gold]"

    menu:
        "What do you want to do next?"
        "Return to Guild":
            jump guild
        "Play another shift":
            jump bar_minigame

default bar_value = 1.0

screen sequence_input_screen(seq_input):
    # Update bar value
    $ bar_value = max(0, (seq_input.timeout - (renpy.get_game_runtime() - seq_input.start_time)) / seq_input.timeout)
    $ bar_val = ExtraAnimatedValue(value=bar_value, range=1.0, delay=0.1)
    $ shift_remaining = max(0, shift_length - (renpy.get_game_runtime() - shift_start))

    # Display current sequence progress
    vbox:
        xalign 0.5
        yalign 0.2
        spacing 10

        text "Customer Order:" size 30

        # Show sequence arrows
        hbox:
            spacing 20
            for i, key in enumerate(seq_input.sequence):
                if i < seq_input.current_index:
                    # Completed part - green
                    text "[key]" color "#00FF00" size 40
                elif i == seq_input.current_index:
                    # Current - yellow
                    text "[key]" color "#FFFF00" size 40
                else:
                    # Upcoming - gray
                    text "[key]" color "#888888" size 40

    # Customer timer bar
    bar:
        xalign 0.5
        yalign 0.5
        xsize 400
        value bar_val
        left_bar Solid("#FFFF00")  # Yellow shrinking bar
        right_bar Solid("#000000")  # Dark background

    # Customer time remaining
    text "Customer time: [int(seq_input.timeout - (renpy.get_game_runtime() - seq_input.start_time))]s" xalign 0.5 yalign 0.55

    # Shift timer
    text "Shift remaining: [int(shift_remaining)]s" xalign 0.5 yalign 0.7 size 25

    # Customers served and last result
    text "Served: [customers_served]" xalign 0.5 yalign 0.75 size 25
    text "Last: [last_result]" xalign 0.5 yalign 0.8 size 25 color last_color

    # Timer for live updates
    timer 0.1 repeat True action Return()

    # Input handling - return to update the screen
    key "K_UP" action [Function(seq_input.input_key, 'up'), Return()]
    key "K_DOWN" action [Function(seq_input.input_key, 'down'), Return()]
    key "K_LEFT" action [Function(seq_input.input_key, 'left'), Return()]
    key "K_RIGHT" action [Function(seq_input.input_key, 'right'), Return()]