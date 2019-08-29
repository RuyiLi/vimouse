from textwrap import dedent
import mouse

x = y = 0

HELP_MESSAGE = dedent('''
    Commands:
    :q - Terminates the program.
    :help - Displays this help message.
    :left <px> - Moves the mouse left by the specified amount of pixels.
    :right <px> - Moves the mouse right by the specified amount of pixels.
    :up <px> - Moves the mouse up by the specified amount of pixels.
    :down <px> - Moves the mouse down by the specified amount of pixels.
''')

WELCOME_MESSAGE = dedent('''
    ViMouse (Created by Ruyi Li for the 2019 ProgrammerHumor Hackathon)
    This program will nullify any attempts to move your cursor with normal mouse input devices, forcing you to use keyboard input to move the cursor instead.
    For a list of valid commands, type :help.
''')


def freezeMouse(evt):
    global x, y
    if isinstance(evt, mouse.MoveEvent):
        mouse.move(x, y)


def do_command(command, *args):
    if not command.startswith(':'):
        print('ERR: Command must be prefixed with a colon (:).')
        return

    command = command[1:]

    if command == 'q':
        return -1

    if command == 'help':
        print(HELP_MESSAGE)
        return

    if command not in ['left', 'right', 'up', 'down']:
        print(f'ERR: {command} is not a valid command.')
        return

    if len(args) == 0:
        print(
            f'ERR: The distance argument was not provided for command {command}.')
        return

    if args[0].lstrip('+-').isdigit():
        dist = int(args[0])

    if command == 'left':
        mouse.move(-dist, 0, False)
    elif command == 'right':
        mouse.move(dist, 0, False)
    elif command == 'up':
        mouse.move(0, -dist, False)
    elif command == 'down':
        mouse.move(0, dist, False)

    if len(args) > 1:
        do_command(*args[1:])


def main():
    global x, y
    while True:
        x, y = mouse.get_position()
        command = input()
        if do_command(*command.split()) == -1:
            break


if __name__ == '__main__':
    mouse.hook(freezeMouse)
    print(WELCOME_MESSAGE)
    main()
    print('Program terminated.')
