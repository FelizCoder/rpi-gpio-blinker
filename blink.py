from gpiozero import LED
from time import sleep
import signal
import sys

led = LED(21)
running = True

def signal_handler(sig, frame):
    global running
    print("Signal received, preparing to shut down...")
    running = False

# Register the signal handler
signal.signal(signal.SIGTERM, signal_handler)

try:
    while running:
        led.on()
        print("LED on")
        sleep(1)
        led.off()
        print("LED off")
        sleep(1)

except KeyboardInterrupt:
    print("Program interrupted by user")
finally:
    led.off()
    led.close()
    print("Cleanup done. Exiting.")
    sys.exit(0)
