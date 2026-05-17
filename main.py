# main.py
# AI-Based Smart Navigation for Visually Impaired Using LIDAR, Raspberry Pi and Haptic Feedback
# Raspberry Pi + LIDAR + Haptic Motor

import time
import random

# GPIO setup (for Raspberry Pi)
# Uncomment these lines when using Raspberry Pi hardware

# import RPi.GPIO as GPIO
#
# HAPTIC_PIN = 18
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(HAPTIC_PIN, GPIO.OUT)

# ---------------------------------------------------
# Simulated LIDAR Distance Function
# Replace this with real LIDAR sensor code later
# ---------------------------------------------------

def get_distance():
    """
    Simulate obstacle distance in centimeters
    """
    distance = random.randint(10, 150)
    return distance

# ---------------------------------------------------
# Haptic Feedback Function
# ---------------------------------------------------

def vibrate_motor(duration):
    """
    Vibrate haptic motor for alert
    """

    print("VIBRATION ALERT")

    # Uncomment for real Raspberry Pi hardware
    #
    # GPIO.output(HAPTIC_PIN, GPIO.HIGH)
    # time.sleep(duration)
    # GPIO.output(HAPTIC_PIN, GPIO.LOW)

    time.sleep(duration)

# ---------------------------------------------------
# Main Program
# ---------------------------------------------------

print("Safe Navigation System Started")
print("Monitoring obstacles...\n")

try:

    while True:

        distance = get_distance()

        print(f"Obstacle Distance: {distance} cm")

        # Very close obstacle
        if distance < 30:
            print("WARNING: Obstacle very close")
            vibrate_motor(1)

        # Medium distance obstacle
        elif distance < 70:
            print("Obstacle detected nearby")
            vibrate_motor(0.5)

        # Safe distance
        else:
            print("Path is clear")

        print("--------------------------")

        time.sleep(2)

except KeyboardInterrupt:

    print("\nSystem Stopped")

    # Uncomment for Raspberry Pi
    # GPIO.cleanup()
