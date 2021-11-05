from microbit import *
import random

while True:
    
    if button_a.is_pressed():
        sleep(60)
        display.show(Image(
        "90000:"
        "00000:"
        "00000:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "99000:"
        "00000:"
        "00000:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "99900:"
        "00000:"
        "00000:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "99990:"
        "00000:"
        "00000:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "99999:"
        "00000:"
        "00000:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "09999:"
        "00009:"
        "00000:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00999:"
        "00009:"
        "00009:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00099:"
        "00009:"
        "00099:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00009:"
        "00009:"
        "00999:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00000:"
        "00009:"
        "09999:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00000:"
        "09000:"
        "09999:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00000:"
        "09900:"
        "09990:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00000:"
        "09900:"
        "09900:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00000:"
        "09900:"
        "00900:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00000:"
        "00900:"
        "09900:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00000:"
        "00000:"
        "99900:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00000:"
        "00000:"
        "99000:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00000:"
        "00000:"
        "90000:"
        "00000:"
        "00000"))
        sleep(60)
        display.show(Image(
        "00000:"
        "00000:"
        "00000:"
        "00000:"
        "00000"))
        sleep(180)
        
        
    if button_b.is_pressed():
        display.show(random.randint(1, 6))
    
    if accelerometer.was_gesture('shake'):
        tool = random.randint(0,2)
        if tool == 0:
            display.show(Image.SQUARE_SMALL)
        elif tool == 1:
            display.show(Image.SQUARE)
        else:
            display.show(Image.SWORD)
