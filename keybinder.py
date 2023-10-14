from jsonloader import read, write, display
from listener import listen

done = False

json_path = 'keybinds.json'

print('Welcome to the keybind configurator!')

while not done:
    keybinds = read(json_path)
    print(f'\nCurrent Keybinds:\n{display(keybinds)}\n')

    print('Choose Hotkey')
    pressed = listen()

    if pressed == keybinds['stopper']:
        print('You have chosen to change the Stopper Key, please press the new one')
        stopper = listen()
        if stopper not in keybinds:
            print(f'Setting Stopper to {stopper}')
            keybinds['stopper'] = stopper
        else:
            print(f'{stopper} is already in use for {keybinds[stopper]}')
    else:
        print(f'You pressed: {pressed}\n')

        emoji = input('Choose Emoji (del -> Delete): ')

        if emoji == 'del':
            print(f'Deleting {keybinds[pressed]}')
            del keybinds[pressed]
        else:
            print(f'\nSetting {pressed} to {emoji}')
            keybinds[pressed] = emoji

    write(keybinds, json_path)

    if input('\nAre you done? (Y/*) ').upper() == 'Y':
        done = True
