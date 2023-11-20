import logic
import curses
import view

MAX_GAME_COUNT = 10
COLS = 100
LINES = 20

stdscr = curses.initscr()
curses.resize_term(LINES, COLS)

while True:
    # game scene
    is_playing = view.playTitleScene(stdscr)

    if not is_playing:
        break

    player_name = view.getPlayerName(stdscr)
    true_number = logic.generateNumber()
    game_count = 0
    view.initGame(stdscr)

    while game_count < MAX_GAME_COUNT:
        user_input = view.getUserInput(stdscr)
        if user_input == 'q':
            break

        game_count += 1
        game_result = logic.getGameResult(true_number, user_input)

        view.printGameProgress(stdscr, game_count, user_input, game_result)
        if game_result.strike_count == 3:
            break