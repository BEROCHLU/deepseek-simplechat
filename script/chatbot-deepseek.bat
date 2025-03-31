@echo off
@rem start pwsh -Command "Set-Location ..; python chatbot-deepseek.py"
start "chatbot-deepseek" "C:\Program Files\Git\bin\bash.exe" -c "cd ..; python chatbot-openai.py; exec bash"