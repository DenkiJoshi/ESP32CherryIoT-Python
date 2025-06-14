from machine import Pin, time_pulse_us
import time

SOUND_SPEED = 340  # Speed of sound in air
TRIG_PULSE_DURATION_US = 10

trigPin = Pin(3, Pin.OUT)  # 3:ConnectorA 4:ConnectorB
echoPin = Pin(1, Pin.IN)  # 1:ConnectorA 5:ConnectorB

while True:
    # Prepare the signal
    trigPin.value(0)
    time.sleep_us(5)
    # Create a 10 µs pulse
    trigPin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trigPin.value(0)

    # Get the duration of the ultrasonic wave propagation (in µs)
    ultrason_duration = time_pulse_us(echoPin, 1, 30000)
    # Calculate distance in centimeters using the speed of sound
    distance_cm = SOUND_SPEED * ultrason_duration / 20000

    print(f"Distance: {distance_cm} cm")
    time.sleep_ms(500)
