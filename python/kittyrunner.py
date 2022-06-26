import vim
import os
import json
import time

# returns the name the kittyrunner is expected to have
def window_name(pid: int) -> str:
    return f'{pid}-kittyrunner'

# creates a kitty window with the given name
def create_window(win_name:str):
    cmdstr = f'kitty @ launch --title {win_name}'
    if vim.eval('g:kittyrunner_keep_focus') == "1":
        cmdstr += ' --keep-focus'
    os.popen(cmdstr)

# sends text to the kittyrunner, creates it if it doesn't exist
def send_text(text: str = ''):
    if text == '':
        text = vim.eval('a:text')
    win_exists, win_name = window_exists()

    if not win_exists:
        create_window(win_name)

    os.popen(f'kitty @ send-text --match title:{win_name} "{text}"')

# returns whether or not the window exists, as well as the name the window has or should have
def window_exists():
    stream = os.popen('kitty @ ls')
    window_list = json.loads(stream.read())
    pid = 0

    windowtitles = []
    for os_window in window_list:
        for tab in os_window['tabs']:
            for window in tab['windows']:
                if window['is_focused']:
                    pid = window['pid']
                windowtitles.append(window['title'])
    win_name = window_name(pid)

    win_exists = False
    for title in windowtitles:
        if title == win_name:
            win_exists = True
            break

    if win_exists:
        return True, win_name
    return False, win_name

# creates the runner if it does not already exist
def open_runner() -> str:
    win_exists, win_name = window_exists()

    if not win_exists:
        create_window(win_name)
    
    return win_name

# closes the runner if it exists
def close_runner():
    win_exists, win_name = window_exists()

    if win_exists:
        os.popen(f'kitty @ close-window --match title:{win_name}')

# runs a command in the existing kittyrunner or a new window
def run_command(cmd: str = ''):
    extra_opts = vim.eval("g:kittyrunner_extra_opts")
    if cmd == '':
        cmd = vim.eval('a:cmd')
    win_name = open_runner()
    os.popen(f'kitty @ send-text --match title:{win_name} {extra_opts} "{cmd}\\\\n"')

# runs a command in a guaranteed new window
def run_oneoff_command():
    cmd = vim.eval('a:cmd')
    os.popen(f'kitty @ launch --keep-focus --copy-env {extra_opts} $SHELL -c "{cmd}"')

# interrupts the runner if it exists
def interrupt_runner():
    win_exists, win_name = window_exists()
    if win_exists:
        os.popen(f'kitty @ signal-child --match title:{win_name} SIGTERM')
