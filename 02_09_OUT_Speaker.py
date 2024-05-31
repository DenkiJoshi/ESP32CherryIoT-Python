from machine import Pin, PWM
import time

InputPin = 25
BEAT = 230
DO = 261.6
_DO = 277.18
RE = 293.665
_RE = 311.127
MI = 329.63
FA = 349.228
_FA = 369.994
SO = 391.995
_SO = 415.305
RA = 440
_RA = 466.164
TI = 493.883
octDO = 523.251

# Initialize PWM object
pwm = PWM(Pin(InputPin))

def doremi():
    pwm.freq(int(DO))
    time.sleep_ms(BEAT * 2)
    pwm.freq(int(RE))
    time.sleep_ms(BEAT * 2)
    pwm.freq(int(MI))
    time.sleep_ms(BEAT * 2)
    pwm.freq(int(FA))
    time.sleep_ms(BEAT * 2)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT * 2)
    pwm.freq(int(RA))
    time.sleep_ms(BEAT * 2)
    pwm.freq(int(TI))
    time.sleep_ms(BEAT * 2)
    pwm.freq(int(octDO))
    time.sleep_ms(BEAT)
    pwm.deinit()
    time.sleep_ms(BEAT)
    pwm.init(freq=1) 

def melodychime():
    pwm.freq(int(RA))
    time.sleep_ms(BEAT)
    pwm.freq(int(FA))
    time.sleep_ms(BEAT)
    pwm.freq(int(DO))
    time.sleep_ms(BEAT)
    pwm.freq(int(FA))
    time.sleep_ms(BEAT)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.freq(int(octDO))
    time.sleep_ms(BEAT * 2)
    pwm.freq(int(DO))
    time.sleep_ms(BEAT)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.freq(int(RA))
    time.sleep_ms(BEAT)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.freq(int(DO))
    time.sleep_ms(BEAT)
    pwm.freq(int(FA))
    time.sleep_ms(BEAT * 3)
    pwm.deinit()
    time.sleep_ms(BEAT)
    pwm.init(freq=1)

def fryer():
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.freq(int(FA))
    time.sleep_ms(BEAT)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.deinit()
    time.sleep_ms(BEAT)
    pwm.init(freq=1)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.freq(int(FA))
    time.sleep_ms(BEAT)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.deinit()
    time.sleep_ms(BEAT)
    pwm.init(freq=1)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.freq(int(FA))
    time.sleep_ms(BEAT)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.deinit()
    time.sleep_ms(BEAT)
    pwm.init(freq=1)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.freq(int(FA))
    time.sleep_ms(BEAT)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.deinit()
    time.sleep_ms(BEAT)
    pwm.init(freq=1)

def setup():
    pass

def loop():
    while True:
        doremi()
        melodychime()
        fryer()

setup()
loop()
