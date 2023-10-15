import pyautogui
import pyperclip3 as clip
from jsonloader import read, display
from pynput import keyboard


def enter(emoji: str):
    clip.copy(emoji)
    pyautogui.hotkey('ctrl', 'v')


json_path = 'keybinds.json'
keybinds = read(json_path)
stopper = keybinds['stopper']
print(
    f'Welcome to Emacroji, press {stopper} to stop\n\nCurrent Keybinds:\n{display(keybinds)}\n'
)


def on_press(key):
    try:
        pressed = key.char
    except AttributeError:
        pressed = str(key)[4:]
    if pressed in keybinds:
        enter(keybinds[pressed])
        print(f'Key {pressed}, entering {keybinds[pressed]}')
    elif pressed == stopper:
        print('\nStopping...')
        return False


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
