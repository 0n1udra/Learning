
#!/usr/bin/python
# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.

# print grid of all colors and brightnesses
# uses stdout.write to write chars with no newline nor spaces between them
# This should run more-or-less identically on Windows and Unix.
from __future__ import print_function
import sys

from random import *
from string import *

# Add parent dir to sys path, so the following 'import colorama' always finds
# the local source in preference to any installed version of colorama.

from colorama import *
import colorama
# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.

# Add demo dir's parent to sys path, so that 'import colorama' always finds
# the local source in preference to any installed version of colorama.
from os.path import normpath, dirname, join
local_colorama_module = normpath(join(dirname(__file__), '..'))
sys.path.insert(0, local_colorama_module)





class demo1:

    # Fore, Back and Style are convenience classes for the constant ANSI strings that set
    #     the foreground, background and style. The don't have any magic of their own.
    FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
    BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
    STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

    NAMES = {
        Fore.BLACK: 'black', Fore.RED: 'red', Fore.GREEN: 'green', Fore.YELLOW: 'yellow', Fore.BLUE: 'blue', Fore.MAGENTA: 'magenta', Fore.CYAN: 'cyan', Fore.WHITE: 'white'
        , Fore.RESET: 'reset',
        Back.BLACK: 'black', Back.RED: 'red', Back.GREEN: 'green', Back.YELLOW: 'yellow', Back.BLUE: 'blue', Back.MAGENTA: 'magenta', Back.CYAN: 'cyan', Back.WHITE: 'white',
        Back.RESET: 'reset'
    }

    # show the color names
    sys.stdout.write('        ')
    for foreground in FORES:
        sys.stdout.write('%s%-7s' % (foreground, NAMES[foreground]))
    print()

    # make a row for each background color
    for background in BACKS:
        sys.stdout.write('%s%-7s%s %s' % (background, NAMES[background], Back.RESET, background))
        # make a column for each foreground color
        for foreground in FORES:
            sys.stdout.write(foreground)
            # show dim, normal bright
            for brightness in STYLES:
                sys.stdout.write('%sX ' % brightness)
            sys.stdout.write(Style.RESET_ALL + ' ' + background)
        print(Style.RESET_ALL)

    print()

class demo2:
    # !/usr/bin/python
    # Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.

    # Simple demo of changing foreground, background and brightness.

    print(Fore.GREEN + 'green, '
          + Fore.RED + 'red, '
          + Fore.RESET + 'normal, '
          , end='')
    print(Back.GREEN + 'green, '
          + Back.RED + 'red, '
          + Back.RESET + 'normal, '
          , end='')
    print(Style.DIM + 'dim, '
          + Style.BRIGHT + 'bright, '
          + Style.NORMAL + 'normal'
          , end=' ')
    print()

class demo3:
    # !/usr/bin/python
    # Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.

    # Demonstrate the different behavior when autoreset is True and False.

    print(Fore.CYAN + Back.MAGENTA + Style.BRIGHT + 'Line 1: colored, with autoreset=True')
    print('Line 2: When auto reset is True, the color settings need to be set with every print.')

    print(Fore.YELLOW + Back.BLUE + Style.BRIGHT + 'Line 3: colored, with autoreset=False')
    print('Line 4: When autoreset=False, the prior color settings linger (this is the default behavior).')

class demo4:
    # !/usr/bin/python
    # Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.

    # check that stripped ANSI in redirected stderr does not affect stdout


    print(Fore.GREEN + 'GREEN set on stdout. ', end='')
    print(Fore.RED + 'RED redirected stderr', file=sys.stderr)
    print('Further stdout should be GREEN, i.e., the stderr redirection should not affect stdout.')

class demo5:
    # !/usr/bin/python
    # Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.

    # Demonstrate the difference between colorama intialized with wrapping on and off.
    # The point of the demonstration is to show how the ANSI wrapping on Windows can be disabled.
    # The unwrapped cases will be interpreted with ANSI on Unix, but not on Windows.


    print('%sWrapped yellow going to stdout, via the default print function.' % Fore.YELLOW)

    print('%sUnwrapped CYAN going to stdout, via the default print function.' % Fore.CYAN)
    print('%sUnwrapped CYAN, using the file parameter to write via colorama the AnsiToWin32 function.' % Fore.CYAN,
          file=AnsiToWin32(sys.stdout))
    print('%sUnwrapped RED going to stdout, via the default print function.' % Fore.RED)

    print('%sWrapped RED going to stdout, via the default print function.' % Fore.RED)

class demo6:
    # Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.

    # Demonstrate printing colored, random characters at random positions on the screen

    # Fore, Back and Style are convenience classes for the constant ANSI strings that set
    #     the foreground, background and style. The don't have any magic of their own.
    FORES = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
    STYLES = [Style.DIM, Style.NORMAL, Style.BRIGHT]

    # This assumes your terminal is 80x24. Ansi minimum coordinate is (1,1).
    MINY, MAXY = 1, 24
    MINX, MAXX = 1, 80

    # set of printable ASCII characters, including a space.
    CHARS = ' ' + printable.strip()

    PASSES = 1000

    def main():
        # gratuitous use of lambda.
        pos = lambda y, x: '\x1b[%d;%dH' % (y, x)
        # draw a white border.
        print(Back.WHITE)
        print('%s%s' % (pos(MINY, MINX), ' ' * MAXX))
        for y in range(MINY, 1 + MAXY):
            print('%s %s ' % (pos(y, MINX), pos(y, MAXX)))
        print('%s%s' % (pos(MAXY, MINX), ' ' * MAXX))
        # draw some blinky lights for a while.
        for i in range(PASSES):
            print('%s%s%s%s%s' % (
            pos(randint(1 + MINY, MAXY - 1), randint(1 + MINX, MAXX - 1)), choice(FORES), choice(BACKS), choice(STYLES),
            choice(CHARS)))
        # put cursor to top, left, and set color to white-on-black with normal brightness.
        print('%s%s%s%s' % (pos(MINY, MINX), Fore.WHITE, Back.BLACK, Style.NORMAL))

    main()

class demo7:

    # Demonstrate cursor relative movement: UP, DOWN, FORWARD, and BACK in colorama.CURSOR

    up = colorama.Cursor.UP
    down = colorama.Cursor.DOWN
    forward = colorama.Cursor.FORWARD
    back = colorama.Cursor.BACK

    def main():
        """
        expected output:
        1a2
        aba
        3a4
        """
        print("aaa")
        print("aaa")
        print("aaa")
        print(forward() + up(2) + "b" + up() + back(2) + "1" + forward() + "2" + back(3) + down(
            2) + "3" + forward() + "4")

    main()

class demo8:

    def main():
        """automatically reset stdout"""
        with colorama_text():
            print(Fore.GREEN + 'text is green')
            print(Fore.RESET + 'text is back to normal')

        print('text is back to stdout')

    if __name__ == '__main__':
        main()























