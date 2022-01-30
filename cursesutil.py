def getinp(win, placeholder='', ispass=False):
    txt = ''
    y, x = win.getyx()
    win.addstr(placeholder)
    while 1:
        currx, curry = win.getyx()
        key = win.getch()
        if key == 8 and len(list(txt)) != 0:
            txt = list(txt)
            txt.pop()
            txt = ''.join(txt)
            win.addstr(y, len(placeholder)+len(txt), " ")

        if chr(key)=='\n':
            return txt
            break
        if key != 8 and chr(key) != '\n':
            txt += str(chr(key))
        if ispass != True:
            win.addstr(y, len(placeholder), ''.join(txt))

def incy(a):y,x=a.getyx();a.move(y+1,0)
def decy(a):y,x=a.getyx();a.move(y-1,0)
def incx(a):y,x=a.getyx();a.move(y,x+1)
def decx(a):y,x=a.getyx();a.move(y,x-1)
