from util import GameResult
from logic import validateInput

INPUT_WARNING = "INPUT_ERROR!"
INPUT_SIZE = 3
def playTitleScene(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "THIS IS TITLE")
    stdscr.addstr(1, 0, "PRESS ANY KEY")
    stdscr.addstr(0, 60, "quit : q")

    key = stdscr.getkey()
    if key=='q':
        if quitScene(stdscr):
            return False

    stdscr.clear()
    return True

def initGame(stdscr):
    stdscr.addstr(0, 60, "quit : q")

def getUserInput(stdscr):
    while True:
        stdscr.addstr(0, 0, "please enter the number:")
        stdscr.addstr(1, 0, " " * INPUT_SIZE)
        user_input = stdscr.getstr(1, 0, INPUT_SIZE).decode('utf-8')

        if user_input=='q' or validateInput(user_input):
            return user_input

        stdscr.addstr(2, 0, INPUT_WARNING)
        stdscr.getkey()
        stdscr.addstr(2, 0, " "*(len(INPUT_WARNING)+1)) # getKey에 의해 생기는 문자 1개

def printGameProgress(stdscr, game_count, user_input, game_result:GameResult):
    result = ""
    if game_result.strike_count == 3:
        if game_count==1:
            result = "HOME RUN!"
        else:
            result = "HITS!"
    elif game_result.out_count == 3:
        result = "strike out!"
    else:
        result = f"{game_result.strike_count}S, {game_result.ball_count}B, {game_result.out_count}O"

    stdscr.addstr(2, 0, result)
    stdscr.getkey()

    stdscr.addstr(2, 0, " " * 20)
    stdscr.addstr(game_count, 40, f"#{game_count} You: {user_input} | {result}")

def printFinalResult(stdscr, game_count, result, true_number):
    game_score = 1000
    score_multiple = 100
    if result == "HOME RUN!":
        game_score += 1000
        final_result = "YOU WIN!"
    elif result == "HITS":
        game_score -= game_count * score_multiple
        final_result = "YOU WIN!"
    else:
        game_score -= game_count * score_multiple
        final_result = "you lose..."

    stdscr.addstr(1, 0, final_result)
    stdscr.addstr(f"answer : {true_number}")
    stdscr.addstr(f"answer : {game_score}")

def quitScene(stdscr):
    stdscr.clear()
    stdscr.addstr("real?? (y/n)")

    key = ''

    while True:
        key = stdscr.getkey()
        if key=='y':
            return True
        elif key=='n':
            return False

def getUserName(stdscr):
    stdscr.addstr("enter your name :")
    user_name = stdscr.getstr(1, 0, 3)
    return user_name