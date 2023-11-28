from util import GameResult
from logic import validateAnswer
from logic import validatePlayerName
import curses

COLS = 100
LINES = 20

stdscr = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.resize_term(LINES, COLS)

NAME_WARNING = "please enter 3-digits-English letter"
ANSWER_WARNING = "please enter 3-digits-unique number"
QUIT_RESTART_WARNING = "Please enter Y or N."
INPUT_SIZE = 3


def playTitleScene():
    while True:
        stdscr.clear()
        curses.flash()
        TITLE = '''
        .:. .:::... .:                                             _--_     dMb
        .-..=++++*-.::                                          __(._  )   d0P
        .::.---=+*++*=:--:.                                        <  (D)  .MP
      .-*###**+--==*#%##*=                                        .~ \ /~```M-.
       ......=+-:-=***.                                         .~    V    Mo_ \\
         .:-:-=-+=*+-                                         (   (___. {:)-./
             :=******+-.                                         ~._____.(:}
             :*#%%%%+                                             /     .M\\
           .=*#+*#%%#+.                                          /      "" \\
          .-*#%%#%%%%#.                                          |    /\\   |
           .+#*#%%%%##%:                                         /   /  \\   \\
            .=+#++++*#+:                                        /   /    \\   \\
                                                                \\__/      \\__/
                                                                / /        | |
                                                              .^V^.      .^V^.
                                                               +-+        +-+"
        '''
        stdscr.addstr(0, 0, TITLE)
        stdscr.addstr(4, 32, "BUllS AND COWS", curses.A_STANDOUT)
        stdscr.addstr(6, 28, "PRESS ANY KEY TO START...", curses.A_BLINK)
        stdscr.addstr(0, 83, "QUIT THE GAME : Q", curses.color_pair(1))

        key = stdscr.getkey()
        if key == 'q':
            quitScene()
        else:
            stdscr.clear()
            return


def showGameScreen():
    curses.flash()
    contour = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ☀︎ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    stdscr.addstr(11, 0, contour, curses.color_pair(2))

    game_rule = ('''
                 중복 없는 세자리 숫자를 맞춰보세요!
                 S(Strike) : 위치와 숫자가 동일한 경우
                 B(Ball): 위치는 다르지만, 해당 숫자가 있는 경우
                 O(Out) : 제출한 숫자가 포함되어 있지 않은 경우
                 ''')
    stdscr.addstr(12, 0, game_rule)
    stdscr.addstr(0, 73, "RESTART THE GAME : input R", curses.color_pair(1))


def inputUserAnswer():
    while True:
        stdscr.addstr(0, 0, "please enter the number:")
        stdscr.addstr(1, 0, " " * INPUT_SIZE)
        try:
            user_input = stdscr.getstr(1, 0, INPUT_SIZE).decode('utf-8')
        except UnicodeDecodeError:
            stdscr.addstr(2, 0, ANSWER_WARNING, curses.color_pair(1))
            stdscr.getch()
            stdscr.addstr(2, 0, " " * (len(ANSWER_WARNING) + 1))
            continue

        if user_input == 'R' or validateAnswer(user_input):
            return user_input
        stdscr.addstr(2, 0, ANSWER_WARNING, curses.color_pair(1))
        stdscr.getkey()
        stdscr.addstr(2, 0, " " * (len(ANSWER_WARNING) + 1))  # getKey에 의해 생기는 문자 1개


def printGameProgress(game_count, user_input, game_result: GameResult):
    if game_result.strike_count == 3:
        curses.flash()
        if game_count == 1:
            result = "HOME RUN!"
        else:
            result = "HITS!"
    elif game_result.out_count == 3:
        result = "strike out!"
        curses.flash()
    else:
        result = f"{game_result.strike_count}S, {game_result.ball_count}B, {game_result.out_count}O"

    stdscr.addstr(2, 0, result, curses.color_pair(3))
    stdscr.getkey()
    stdscr.addstr(2, 0, " " * 20)
    stdscr.addstr(game_count, 74, f"#{game_count} You: {user_input} | {result}", curses.color_pair(3))


def printFinalResult(true_number, player_score, game_count, game_result: GameResult):
    curses.flash()
    stdscr.clear()
    if game_result.strike_count == 3:
        if game_count == 1:
            stdscr.addstr(0, 0, "HOMERUN!", curses.color_pair(2))
            stdscr.addstr(1, 0, f"answer : {true_number}")
            stdscr.addstr(2, 0, f"score : {player_score}")
        elif game_count > 1:
            stdscr.addstr(0, 0, "YOU WIN!", curses.color_pair(2))
            stdscr.addstr(1, 0, f"answer : {true_number} | retry : {game_count}/10")  # MAX_GAME_COUNT = 10
            stdscr.addstr(2, 0, f"score : {player_score}")
    else:
        stdscr.addstr(0, 0, "YOU LOSE...", curses.color_pair(1))
        stdscr.addstr(1, 0, f"answer : {true_number}")
    stdscr.getkey()


def quitScene():
    while True:
        stdscr.clear()
        stdscr.addstr("Are you sure you want to QUIT? ---> press Y/N")
        try:
            quit_answer = stdscr.getstr(1, 0, 1).decode('utf-8')
        except UnicodeDecodeError:
            stdscr.addstr(2, 0, QUIT_RESTART_WARNING, curses.color_pair(1))
            stdscr.refresh()
            stdscr.getch()
            continue

        if quit_answer.lower() == 'y':
            exit(0)
        elif quit_answer.lower() == 'n':
            return
        else:
            stdscr.addstr(2, 0, QUIT_RESTART_WARNING, curses.color_pair(1))
            stdscr.refresh()
            stdscr.getch()


def getPlayerName():
    while True:
        stdscr.addstr(0, 0, "enter your name :")
        init_player_name = stdscr.getstr(1, 0, 3).upper()
        try:
            player_name = init_player_name.decode('utf-8')
        except UnicodeDecodeError:
            stdscr.addstr(1, 0, NAME_WARNING, curses.color_pair(1))
            stdscr.refresh()
            stdscr.getch()
            stdscr.clear()
            continue
        if validatePlayerName(player_name):
            return player_name
        else:
            stdscr.addstr(1, 0, NAME_WARNING, curses.color_pair(1))
            stdscr.getkey()
            stdscr.addstr(1, 0, " " * (len(NAME_WARNING) + 1))  # getKey에 의해 생기는 문자 1개


def printRank(player_ranking):
    curses.flash()
    stdscr.clear()
    rank = 1
    for player, score in player_ranking:
        if rank == 1:
            stdscr.addstr(f'{rank} place | {player} : {score}\n', curses.color_pair(2))
        else:
            stdscr.addstr(f'{rank} place | {player} : {score}\n')
        rank += 1
    stdscr.getkey()