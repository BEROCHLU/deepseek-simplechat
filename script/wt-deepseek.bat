@echo off
set PWSH_CMD=cd ..; python chatbot-deepseek.py
wt -d . --title "chatbot-deepseek" pwsh -NoExit -Command "Invoke-Expression $env:PWSH_CMD"