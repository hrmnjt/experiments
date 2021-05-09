# ~/.bashrc

# Start starship prompt
eval "$(starship init bash)"

# Enable color in shell
export CLICOLOR=1

# Alias
## Directory
alias l="ls -alh"
alias ..="cd .."
alias ...="cd ../.."
## Git
alias gaa="git add --all"
alias gst="git status"
alias gcmsg="git commit -m"
alias glo="git log --oneline --decorate"
## General
alias loadbash="source ~/.bashrc"

# Sourcing path for rustc
export PATH="$HOME/.cargo/bin:$PATH"
. "$HOME/.cargo/env"
