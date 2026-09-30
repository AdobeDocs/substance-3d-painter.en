@echo off
cd /d "%~dp0"
python sbs_param_gui.py
if errorlevel 1 pause
