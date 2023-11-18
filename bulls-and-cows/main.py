import logic
import curses

MAX_GAME_COUNT = 10

stdscr = curses.initscr()
curses.resize_term(100, 200)


true_number = logic.generateNumber()

game_count = 0
while game_count < MAX_GAME_COUNT:
    stdscr.addstr(0, 0, "please enter the number:")
    user_answer = stdscr.getstr(1, 0, 3).decode('utf-8')
    if logic.validateInput(user_answer):
        game_count += 1
        strike_count, ball_count, out_count = logic.compareAnswer(true_number, user_answer)


        result = logic.getResult(strike_count, ball_count, out_count, game_count)
        stdscr.addstr(2, 0, result)
        stdscr.getkey()
        if strike_count == 3:
            break

    stdscr.clear()