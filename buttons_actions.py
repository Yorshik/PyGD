from main_game import run_game

running = True


def button1_action():
    global running
    running = True
    run_game(running)


def button2_action():
    global running
    running = False
