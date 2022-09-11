num1 = 0
num2 = 0
op = 0
in_num = 0

def on_button_pressed_a():
    global op, in_num
    if not (num1 == 0 and num2 == 0):
        op += 1
        if op == 1:
            basic.show_leds("""
                . . # . .
                                . . # . .
                                # # # # #
                                . . # . .
                                . . # . .
            """)
        elif op == 2:
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . # # # .
                                . . . . .
                                . . . . .
            """)
        elif op == 3:
            basic.show_leds("""
                # . . . #
                                . # . # .
                                . . # . .
                                . # . # .
                                # . . . #
            """)
        elif op == 4:
            basic.show_leds("""
                . . # . .
                                . . . . .
                                # # # # #
                                . . . . .
                                . . # . .
            """)
        elif op == 0:
            pass
        else:
            op = 4
    else:
        in_num += 1
        basic.show_string("" + str((in_num)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global num1, num2
    if num1 == 0:
        num1 = in_num
        basic.clear_screen()
    elif not (num1 == 0):
        num2 = in_num
        basic.clear_screen()
    else:
        if not (num1 == 0 and num2 == 0 and op == 0):
            if op == 1:
                basic.show_string("" + str((num1 + num2)))
        else:
            pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global op, in_num
    if not (num1 == 0 and num2 == 0):
        op += -1
        if op == 1:
            basic.show_leds("""
                . . # . .
                                . . # . .
                                # # # # #
                                . . # . .
                                . . # . .
            """)
        elif op == 2:
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . # # # .
                                . . . . .
                                . . . . .
            """)
        elif op == 3:
            basic.show_leds("""
                # . . . #
                                . # . # .
                                . . # . .
                                . # . # .
                                # . . . #
            """)
        elif op == 4:
            basic.show_leds("""
                . . # . .
                                . . . . .
                                # # # # #
                                . . . . .
                                . . # . .
            """)
        elif op == 0:
            pass
        else:
            op = 4
    else:
        in_num += -1
        basic.show_string("" + str((in_num)))
input.on_button_pressed(Button.B, on_button_pressed_b)
