@echo off
@rem powershell -Command "Start-Process -NoNewWindow 'npm' -ArgumentList 'run sakata+batch'"
@rem start pwsh -NoExit -Command "node ./nodejs/main-batch.js > ./result/output1.log"
@rem start powershell.exe -Command "python chatbot-rich.py"
start pwsh -Command "Set-Location ..; python chatbot-deepseek.py"