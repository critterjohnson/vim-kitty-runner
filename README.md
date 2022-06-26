# vim-kitty-runner
Easily interact with kitty from vim

KittyRunner is inspired by [vimux](https://github.com/preservim/vimux),
a plugin that facilitates easy interaction between tmux and vim. The kitty
terminal remotes the need for a terminal multiplexer like tmux, and in fact
does not play well with them, but there was no good vim plugin for running
commands in a vimux-style runner from within kitty.

By default, when you call `KittyRunner` it will create a new kitty window
(note that this is the kitty definition of window - like a pane in tmux, _not_
an OS window). All further commands run with `KittyRunner` will run in this
same kitty window.

## Installation

With **[vim-bundle](https://github.com/preservim/vim-bundle)**: `vim-bundle install critterjohnson/vim-kitty-runner`

With **[Vundle](https://github.com/gmarik/Vundle.vim)**: `Plugin 'critterjohnson/vim-kitty-runner'` in your .vimrc

With Vim8 plugin support:

```
git submodule add https://github.com/critterjohnson/vim-kitty-runner.git ~/.vim/pack/plugins/start/vim-kitty-runner
```
