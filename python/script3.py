# Imports
import webiopi

# Enable debug output
webiopi.setDebug()

# Retrieve GPIO lib
GPIO = webiopi.GPIO
SWITCH = 21
SERVO  = 23
LED0   = 17
LED1   = 17

# Called by WebIOPi at script loading
def setup():
    webiopi.debug("Blink script - Setup")
    # Setup GPIOs
    GPIO.setFunction(LED0, GPIO.PWM)
    # GPIO.setFunction(LED1, GPIO.OUT)

    GPIO.pwmWrite(LED0, 0.5)      # set to 50% ratio
    # GPIO.pwmWriteAngle(SERVO, 0)    # set to 0 (neutral)
    # GPIO.digitalWrite(LED1, GPIO.HIGH)

# Looped by WebIOPi
def loop():
    # Toggle LED each 5 seconds
    # value = not GPIO.digitalRead(LED1)
    # GPIO.digitalWrite(LED1, value)
    webiopi.sleep(5)

# Called by WebIOPi at server shutdown
def destroy():
    webiopi.debug("Blink script - Destroy")
    # Reset GPIO functions
    # GPIO.setFunction(SWITCH, GPIO.IN)
    # GPIO.setFunction(SERVO, GPIO.IN)
    GPIO.setFunction(LED0, GPIO.IN)
    # GPIO.setFunction(LED1, GPIO.IN)
