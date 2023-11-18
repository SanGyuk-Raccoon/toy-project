import logic
import curses
import view

MAX_GAME_COUNT = 10
COLS = 200
LINES = 100

stdscr = curses.initscr()
curses.resize_term(LINES, COLS)

while True:
    # game scene
    view.showTitle(stdscr)

    true_number = logic.generateNumber()

    game_count = 0
    while game_count < MAX_GAME_COUNT:
        user_input = view.getUserInput(stdscr)

        game_count += 1
        game_result = logic.getGameResult(true_number, user_input)

        view.printGameResult(stdscr, game_count, user_input, game_result)

        if game_result.strike_count==3:
            break