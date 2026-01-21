import curses
import time
from curses import wrapper
import random

def Targetting_Text():
    try:
        with open("text.txt","r") as f:
            lines=f.readlines()
            print(lines)
        return random.choice(lines).strip()
    except FileNotFoundError:
        return "No text to type does not have text.txt file"

def start_scr(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0,"Welcome to the Typing speed test!\n{Hit escape to leave any moment you like.}\n")
    stdscr.addstr("Press Enter to begin!")
    stdscr.getkey()

def display_text(stdscr,Target_text,current_text,wpm=0):
    stdscr.addstr(Target_text)
    stdscr.addstr(1,0,f"WPM={wpm}")
    for i,char in enumerate(current_text):
        correct_char=Target_text[i]
        if char==correct_char:
            color=curses.color_pair(1)
        else:
            color=curses.color_pair(2)
        #adjusting the index of the color pair.
        stdscr.addstr(0,i,char,color)

def wpm_test(stdscr,Target_text):
    current_text=[]
    wpm=0
    stdscr.clear()
    stdscr.addstr(Target_text) 
    start=time.time()
    stdscr.nodelay(True)
    while True:
        time_elapsed=max(time.time()-start,1)
        cpm=len(current_text)/(time_elapsed/60)         #Characters Per minute
        wpm=round(cpm/5)           #Words per minute = Characters per minute/5
        stdscr.clear()
        display_text(stdscr,Target_text,current_text,wpm)
        if "".join(current_text) == Target_text:
            stdscr.nodelay(False)
            break
        try:
            key=stdscr.getkey()
        except:
            continue
        if ord(key)==27:
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text)>0:
                current_text.pop() 
        elif ord(key)==10:
            continue
        elif len(current_text)<len(Target_text):
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)  
    curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_BLACK)         #Defining all the color pairs
    Target_text=Targetting_Text()
    print(Target_text)
    start_scr(stdscr)
    while True:
        wpm_test(stdscr,Target_text)
        stdscr.addstr(3,0,"You completed the text! Press any key to move on to try again...\nor move press esc to quit .......",curses.color_pair(3))
        key=stdscr.getkey()
        if ord(key)==27:
            break

if __name__=="__main__":
    wrapper(main)