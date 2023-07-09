def on_logo_long_pressed():
    basic.show_leds("""
        . # # # .
        # . . . #
        # # . # #
        # . . . #
        . # # # .
        """)
    basic.pause(100)
    basic.show_string("hi im microbit your digital assistant")
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    basic.show_leds("""
        # . . . #
        # . . . .
        # # # . #
        # . # . #
        # . # . #
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_screen_down():
    music.play(music.builtin_playable_sound_effect(soundExpression.sad),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_ab():
    basic.show_string("Hello world my name is microbit")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(step)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global step
    step += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    basic.show_icon(IconNames.HAPPY)
    soundExpression.giggle.play_until_done()
    basic.show_icon(IconNames.ASLEEP)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

step = 0
basic.show_string("Hello!")
