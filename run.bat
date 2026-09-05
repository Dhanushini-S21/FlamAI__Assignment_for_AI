@echo off
cd /d "%~dp0"
echo Installing requirements...
python -m pip install -r requirements.txt
echo.
echo Running curve parameter estimation...
python src\solve.py
pause
