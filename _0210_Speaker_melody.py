from machine import Pin, PWM
import time

speakerPin = 3  # 3:ConnectorA 4:ConnectorB

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
pwm = PWM(Pin(speakerPin))
pwm.duty_u16(32768)  # 50% duty cycle

def doremi():
    pwm.init()
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

def melodychime():
    pwm.init()
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

def fryer():
    pwm.init()
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.freq(int(FA))
    time.sleep_ms(BEAT)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.deinit()
    time.sleep_ms(BEAT)
    pwm.init()
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.freq(int(FA))
    time.sleep_ms(BEAT)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.deinit()
    time.sleep_ms(BEAT)
    pwm.init()
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.freq(int(FA))
    time.sleep_ms(BEAT)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.deinit()
    time.sleep_ms(BEAT)
    pwm.init()
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.freq(int(FA))
    time.sleep_ms(BEAT)
    pwm.freq(int(SO))
    time.sleep_ms(BEAT)
    pwm.deinit()
    time.sleep_ms(BEAT)

while True:
    doremi()
    melodychime()
    fryer()