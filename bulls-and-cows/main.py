import logic
import curses

MAX_GAME_COUNT = 10

stdscr = curses.initscr()
curses.resize_term(100, 200)





true_number = logic.generateNumber()

while MAX_GAME_COUNT > 0:
    stdscr.addstr(0, 0, "please enter the number:")
    user_answer = stdscr.getstr(1, 0, 3).decode('utf-8')

    if logic.validateInput(user_answer):
        MAX_GAME_COUNT -= 1
        strike_count, ball_count, out_count = logic.compareAnswer(true_number, user_answer)
        result = logic.printResult(strike_count, ball_count, out_count)
        if strike_count == 3:
            break
