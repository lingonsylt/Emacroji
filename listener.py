from pynput import keyboard


def on_press(key):
    global pressed
    try:
        pressed = key.char
    except AttributeError:
        pressed = str(key)[4:]
    return False


def listen():
    global repeat
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    return pressed
