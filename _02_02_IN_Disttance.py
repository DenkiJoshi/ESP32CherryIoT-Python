from machine import Pin, time_pulse_us
import time

SOUND_SPEED = 340  # Speed of sound in air
TRIG_PULSE_DURATION_US = 10

trig_pin = Pin(32, Pin.OUT)
echo_pin = Pin(33, Pin.IN)

while True:
    # Prepare the signal
    trig_pin.value(0)
    time.sleep_us(5)
    # Create a 10 µs pulse
    trig_pin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.value(0)

    # Get the duration of the ultrasonic wave propagation (in µs)
    ultrason_duration = time_pulse_us(echo_pin, 1, 30000)
    # Calculate distance in centimeters using the speed of sound
    distance_cm = SOUND_SPEED * ultrason_duration / 20000

    print(f"Distance: {distance_cm} cm")
    time.sleep_ms(500)
