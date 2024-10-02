import logging
from gpiozero import LED
from time import sleep
import signal
import sys

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

led = LED(21)
running = True

def signal_handler(sig, frame):
    global running
    logging.info("Signal received, preparing to shut down...")
    running = False

# Register the signal handler
signal.signal(signal.SIGTERM, signal_handler)

try:
    logging.info("Starting LED blinking")
    while running:
        led.on()
        logging.debug("LED on")
        sleep(1)
        led.off()
        logging.debug("LED off")
        sleep(1)

except KeyboardInterrupt:
    logging.info("Program interrupted by user")
finally:
    led.off()
    led.close()
    logging.info("Cleanup done. Exiting.")
    sys.exit(0)
