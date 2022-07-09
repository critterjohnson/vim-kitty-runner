" kittyrunner.vim

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
import kittyrunner
EOF

let g:kittyrunner_cwd = getcwd()

if !exists("g:kittyrunner_extra_opts")
    let g:kittyrunner_extra_opts = ''
endif

if !exists("g:kittyrunner_keep_focus")
    let g:kittyrunner_keep_focus = 1
endif

if !exists("g:kittyrunner_prompt_string")
    let g:kittyrunner_prompt_string = "Enter command: "
endif

function! KittyRunner(cmd)
    python3 kittyrunner.run_command()
endfunction

function! KittyRunnerOneoff(cmd)
    python3 kittyrunner.run_oneoff_command()
endfunction

function! KittyRunnerSendText(text)
    python3 kittyrunner.send_text()
endfunction

function! KittyRunnerOpen()
    python3 kittyrunner.open_runner()
endfunction

function! KittyRunnerAssign(win_id)
    python3 kittyrunner.assign_runner()
endfunction

function! KittyRunnerClose()
    python3 kittyrunner.close_runner()
endfunction

function! KittyRunnerInterrupt()
    python3 kittyrunner.interrupt_runner()
endfunction

function! KittyRunnerPrompt(...)
    let command = a:0 ==# 1 ? a:1 : ''
    let cmd = input(g:kittyrunner_prompt_string, command)
    call KittyRunner(l:cmd)
endfunction

command! -nargs=1 KittyRunner call KittyRunner(<args>)
command! -nargs=1 KittyRunnerOneoff call KittyRunnerOneoff(<args>)
command! -nargs=1 KittyRunnerSendText call KittyRunnerSendText(<args>)
command! -nargs=0 KittyRunnerOpen call KittyRunnerOpen()
command! -nargs=* KittyRunnerAssign call KittyRunnerAssign(<args>)
command! -nargs=0 KittyRunnerClose call KittyRunnerClose()
command! -nargs=0 KittyRunnerInterrupt call KittyRunnerInterrupt()
command! -nargs=* KittyRunnerPrompt call KittyRunnerPrompt(<args>)
