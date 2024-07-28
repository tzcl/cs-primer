# We can use the bell character to make the terminal beep
# print("\a")

# To know how many times to beep, we can read from stdin
# We need to change the terminal control mode to read straight away
# (by default, the terminal is in canonical mode which processes input by lines)
import sys
import tty
import time

tty.setcbreak(sys.stdin)

while True:
    ch = sys.stdin.read(1)
    if ch.isdigit():
        for _ in range(int(ch)):
            # Only seems to beep a maximum of 5 times without sleeping
            sys.stdout.write("\a")
            time.sleep(0.5)
            sys.stdout.flush()
