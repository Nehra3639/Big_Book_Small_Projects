import sys
import time

print('Forty-Nine Bottles')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(1)

bottles = 49  # This is the starting number of bottles.
PAUSE = 1  # (!) Try changing this to 0 to see the full song at once.

try:
    while bottles > 2:  # Keep looping and display the lyrics.
        print(bottles, 'bottles of milk on the wall,')
        time.sleep(PAUSE)  # Pause for PAUSE number of seconds.
        print(bottles, 'bottles of milk,')
        time.sleep(PAUSE)
        print('Take two down, pass it around,')
        time.sleep(PAUSE)
        bottles = bottles - 2  # Decrease the number of bottles by one.
        print(bottles, 'bottles on the wall!')
        time.sleep(PAUSE)
        print()  # Print a newline.

# Display the last stanza:
    print('1 bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of milk,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles on the wall!')
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
