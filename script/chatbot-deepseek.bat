@echo off
@rem start pwsh -Command "Set-Location ..; python chatbot-deepseek.py"
start "" "C:\Program Files\Git\bin\bash.exe" -c "cd ..; python chatbot-deepseek.py; exec bash"