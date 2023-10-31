import curses

def writeString(scr, r, c, s):
    print(f"Write {s} on ({r}, {c})")
    scr.addstr(r, c, s)
    scr.getkey()

def getString(scr, r, c, cnt):
    string = scr.getstr(r, c, cnt)
    print(f"Get {string}(cnt={cnt}) on ({r}, {c})")

if __name__=="__main__":
    stdscr = curses.initscr()

    curses.resize_term(100, 200)
    stdscr.getkey()

    curses.resize_term(50, 100)
    stdscr.getkey()

    writeString(stdscr, 0, 0, "TEST")

    curses.noecho()
    writeString(stdscr, 1, 0, "TEST")

    curses.echo()
    getString(stdscr, 2, 0, 3)

    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    stdscr.addstr(0, 0, "COLOR TEST", curses.color_pair(1) | curses.A_BOLD)
    stdscr.getkey()

    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLUE)
    stdscr.addstr(2, 0, "COLOR TEST", curses.color_pair(2) | curses.A_BOLD)
    stdscr.getkey()

    curses.endwin()