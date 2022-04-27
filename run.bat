@echo off

call %~dp0venv\Scripts\activate

set TOKEN=XXXX

python bot_telegram.py

pause