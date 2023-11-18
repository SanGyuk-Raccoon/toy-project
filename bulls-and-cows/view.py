from logic import validateInput

INPUT_WARNING = "INPUT_ERROR!"
INPUT_SIZE = 3
def showTitle(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "THIS IS TITLE")
    stdscr.addstr(1, 0, "PRESS ANY KEY")

    stdscr.getkey()
    stdscr.clear()

def getUserInput(stdscr):
    while True:
        stdscr.addstr(0, 0, "please enter the number:")
        stdscr.addstr(1, 0, " " * INPUT_SIZE)
        user_input = stdscr.getstr(1, 0, INPUT_SIZE).decode('utf-8')
        if validateInput(user_input):
            return user_input

        stdscr.addstr(2, 0, INPUT_WARNING)
        stdscr.getkey()
        stdscr.addstr(2, 0, " "*(len(INPUT_WARNING)+1)) # getKey에 의해 생기는 문자 1개
