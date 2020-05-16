from gpiozero import Button
from gpiozero import LED

# pinNum_btn = [3,6,9,12]
# pinNum_ledL = [2,5,8,11]
# pinNum_ledR = [4,7,10,13]
#
# btn = ButtonBoard(pinNum_btn(0),pinNum_btn(1),pinNum_btn(2),pinNum_btn(3))
# led_L = LEDBoard(pinNum_ledL(0),pinNum_ledL(1),pinNum_ledL(2),pinNum_ledL(3))
# led_R = LEDBoard(pinNum_ledR(0),pinNum_ledL(1),pinNum_ledL(2),pinNum_ledL(3))

# btn = [Button(3),Button(6),Button(9),Button(12)]
# led_L = [LED(2),LED(5),LED(8),LED(11)]
# led_R = [LED(4),LED(7),LED(10),LED(13)]

btn_1 = Button(3); btn_2 = Button(6); btn_3 = Button(9); btn_4 = Button(12)

def btn_L:
    if b >= l:
        return b - l
    else :
        return l - b

def btn_R:
    if b >= r:
        return b - r
    else :
        return r - b

b, r, l = 1
# led_L_1 = LED(2); led_L_2 = LED(5); led_L_3 = LED(8); led_L_4 = LED(11)
# led_R_1 = LED(4); led_R_2 = LED(7); led_R_3 = LED(10); led_R_4 = LED(13)
led_L_1.on()
led_R_1.on()
led_now_L = LED(3 * l - 1)
led_now_R = LED(3 * r + 1)
led_now_L.on()
led_now_R.on()
while True:
    if btn_1.is_pressed:
        b = 1
        if btn_L == 0 or btn_R == 0:
            continue
        else:
            if btn_L >= btn_R:
                led_now_R.off()
                r = 1
                led_now_R.on()
            else:
                led_now_L.off()
                l = 1
                led_now_L.on()
    if btn_2.is_pressed:
        b = 2
        if btn_L == 0 or btn_R == 0:
            continue
        else:
            if btn_L >= btn_R:
                led_now_R.off()
                r = 2
                led_now_R.on()
            else:
                led_now_L.off()
                l = 2
                led_now_L.on()
    if btn_3.is_pressed:
        b = 3
        if btn_L == 0 or btn_R == 0:
            continue
        else:
            if btn_L >= btn_R:
                led_now_R.off()
                r = 3
                led_now_R.on()
            else:
                led_now_L.off()
                l = 3
                led_now_L.on()
    if btn_4.is_pressed:
        b = 4
        if btn_L == 0 or btn_R == 0:
            continue
        else:
            if btn_L >= btn_R:
                led_now_R.off()
                r = 4
                led_now_R.on()
            else:
                led_now_L.off()
                l = 4
                led_now_L.on()
