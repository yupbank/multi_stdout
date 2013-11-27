#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2013-11-26
'''

import curses
from curses import panel
import time
 
stdscr = curses.initscr()
stdscr.refresh()
h, w = stdscr.getmaxyx()
curses.start_color()

def wGetchar(win = None):
    if win is None: win = stdscr
    return win.getch()

def Getchar():
    wGetchar()

nap_msec = 10
def wait_a_while():
    if nap_msec == 1:
        Getchar()
    else:
        curses.napms(nap_msec)


def mkpanel(color, rows, cols, tly, tlx):
    win = curses.newwin(rows, cols, tly, tlx)
    pan = panel.new_panel(win)
    if curses.has_colors():
        if color == curses.COLOR_BLUE:
            fg = curses.COLOR_WHITE
        else:
            fg = curses.COLOR_BLACK
        bg = color
        curses.init_pair(color, fg, bg)
        #win.bkgdset(ord('b'), curses.color_pair(color))
    else:
        win.bkgdset(ord('a'), curses.A_BOLD)

    return pan

def pflush():
    panel.update_panels()
    curses.doupdate()

import random
def generate(limit=-1):
    while 1:
        if limit<0:
            for i in xrange(1000000000):
                yield 'the champion %s\n'%i
        elif limit == 0:
            return 
        else:
            limit = limit - 1

a = generate(10)
b = generate()
c = generate(100)

def fill_panel(pan, g=b):
    win = pan.window()
    num = pan.userptr()[1]

    win.move(1, 1)
    win.addstr("-pan%c-" % num)
    win.clrtoeol()
    win.box()

    maxy, maxx = win.getmaxyx()
    buf = []
        #for x in range(1, maxx - 1):
            #win.move(y, x)
    for y in range(2, maxy - 2):
        try:
            a = g.next()
        except:
            return
        win.move(y, 1)
        a = a.strip().split()
        win.addstr(a)
        win.clrtoeol()
        win.box()
        pan.show()
        pflush()
x = h/3
y = w/3

p1 = mkpanel(curses.COLOR_MAGENTA, h, y, 0, 0)
p2 = mkpanel(curses.COLOR_MAGENTA, h, y, 0, y)
p3 = mkpanel(curses.COLOR_MAGENTA, h, y, 0, 2*y)
p1.set_userptr("p1")
p2.set_userptr("p2")
p3.set_userptr("p3")
while b.next():
    fill_panel(p1, b)
    fill_panel(p2, b)
    fill_panel(p3, c)
    p1.show()
    p2.show()
    p3.show()
    pflush()
    #wait_a_while()
#pad.refresh(0,0, 5,5, 20,75)

#while True:
#    try:
#        stdscr.addch(h-1, w-1, '*')
#        time.sleep(3)
#        stdscr.refresh()
#    except curses.error:
#        pass
# 
#curses.endwin()
