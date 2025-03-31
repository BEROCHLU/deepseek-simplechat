@echo off
start "" "C:\Program Files\Git\bin\bash.exe" -c "cd ..; python chatbot-openai.py; exec bash"