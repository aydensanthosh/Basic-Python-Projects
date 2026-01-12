import curses
from curses import wrapper
import random
TARGET=["The quick brown fox jumps over the lazy dog","Pack my box with five dozen liquor jugs" , "Sphinx of black quartz, judge my vow","Jackdaws love my big sphinx of quartz.","The five boxing wizards jump quickly."]
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Speed test! Enter anywhere to start")
    stdscr.addstr("\n Press any key to begin")
    stdscr.refresh()
    stdscr.getkey()

def wpm(stdscr):

    target_text=random.choice(TARGET)
    current_text=[]
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    
    while True:
        stdscr.clear()
        stdscr.addstr(target_text)

        for char in current_text:
                stdscr.addstr(char,curses.color_pair(1))
        stdscr.refresh()
        k=stdscr.getkey()
        if ord(k)==27:
            break
        if k in ("KEY_BACKSPACE",'\b',"\x7f"):
             if len(current_text)>0:
                  current_text.pop()
        else:
            current_text.append(k)
def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm(stdscr)

wrapper(main)
