@echo off
python "maconfig.py" -i "%~dp0\data_colors.csv" -t "%~dp0\template_colors.xml"
pause