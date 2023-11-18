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
        strike_count, ball_count, out_count = logic.compareAnswer(true_number, user_input)

        result = logic.getResult(strike_count, ball_count, out_count, game_count)
        stdscr.addstr(2, 0, result)
        stdscr.getkey()
        if strike_count == 3:
            break

        stdscr.addstr(2, 0, " "*20)
        stdscr.addstr(game_count, 40, f"#{game_count} You: {user_input} | {result}")