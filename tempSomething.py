import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
while 1:
    c = stdscr.getch()
    if c == ord('p'): print("I pressed p")
    elif c == ord('q'): break

curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()
